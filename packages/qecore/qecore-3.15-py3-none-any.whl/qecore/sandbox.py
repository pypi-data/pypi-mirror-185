#!/usr/bin/env python3
import os
import re
import sys
import base64
import traceback
import signal
import atexit
import time
import xml.etree.ElementTree as ET
from time import sleep
from subprocess import Popen
from mimetypes import MimeTypes
import behave
import pkg_resources
from dogtail.utils import config, isA11yEnabled, enableA11y
from dogtail.rawinput import keyCombo
from qecore.utility import run, overview_action

from qecore.logger import QELogger, Logging
from qecore.application import Application
from qecore.flatpak import Flatpak
from qecore.icons import qecore_icons, QECoreIcon

# First check: dogtail utility for accessibility check and enabling.
if not isA11yEnabled():
    print("Accessibility not detected running. Enabling via dogtail...")
    enableA11y()
    sleep(2)

# Second check: gsettings command to get the state and enable if set to false.
GET_ACCESSIBILITY = "gsettings get org.gnome.desktop.interface toolkit-accessibility"
SET_ACCESSIBILITY = (
    "gsettings set org.gnome.desktop.interface toolkit-accessibility true"
)
if "true" not in run(GET_ACCESSIBILITY):
    print("Accessibility not detected running. Enabling via gsettings command...")
    run(SET_ACCESSIBILITY)


log = QELogger()
generic_log = Logging()

NO_VALUES = ["", "n", "no", "f", "false", "0"]


class TestSandbox:
    def __init__(self, component, logging=False, context=None, kiosk=False):
        """
        :type component: str
        :param component: Name of the component that is being tested.

        :type logging: bool
        :param logging: Turn on or off logging of this submodule.

        :type context: <behave.runner.Context>
        :param context: Behave context

        .. note::

            You are able to use logging via debug variable:
            QECORE_DEBUG=yes behave -kt <test_name>

            You are able to use general logging via variable:
            LOGGING=yes behave -kt <test_name>

            You can enforce embedding for testing purposes via debug variable:
            QECORE_EMBED_ALL=yes
        """

        assert isinstance(logging, bool), "".join(
            ("Unexpected argument, logging should be bool")
        )

        if context is not None:
            assert isinstance(context, behave.runner.Context), "".join(
                "Unexpected argument, context should be <behave.runner.Context>"
            )

        self.logging = logging
        self._embed_all = (
            os.environ.get("QECORE_EMBED_ALL", "").lower() not in NO_VALUES
        )
        self._logging_env = os.environ.get("QECORE_DEBUG", "").lower() not in NO_VALUES
        self._logging_generic = os.environ.get("LOGGING", "").lower() not in NO_VALUES

        log.logger.disabled = not (self.logging or self._logging_env)
        generic_log.logger.disabled = True

        if context is not None:
            generic_log.logger.disabled = not (self.logging or self._logging_generic)
            for formatter in context._runner.formatters:
                if (
                    "pretty" in formatter.name
                    and getattr(formatter, "monochrome", None) is not None
                ):
                    formatter.monochrome = self.logging or self._logging_generic

        log.info(
            f"__init__(self, component={component}, \
                logging={str(self.logging)}, context={repr(context)})"
        )

        log.info("Accessibility is somehow turning off, making another check.")
        # First check: dogtail utility for accessibility check and enabling.
        if not isA11yEnabled():
            print("Accessibility not detected running. Enabling via dogtail.")
            enableA11y()
            sleep(2)

        # Second check: gsettings command to get the state and enable if set to false.
        if "true" not in run(GET_ACCESSIBILITY):
            print(
                "Accessibility not detected running. Enabling via gsettings command..."
            )
            run(SET_ACCESSIBILITY)

        self.context = context
        self.kiosk = kiosk
        self.component = component
        self.current_scenario = None
        self.background_color = None
        self.background_image_revert = False
        self.background_image_location = None

        self.disable_welcome_tour = True

        self.enable_animations = None

        self.enable_close_yelp = True

        self.logging_start = None
        self.screenshot_run_result = None

        self.record_video = True
        self.record_video_pid = None

        self.attach_video = True
        self.attach_video_on_pass = False

        self.attach_journal = True
        self.attach_journal_on_pass = False

        self.attach_coredump = False
        self.attach_coredump_on_pass = True
        self.attach_coredump_file_check = False

        self.attach_screenshot = True
        self.failed_test = False

        self.attach_faf = True
        self.attach_faf_on_pass = True

        self.status_report = True

        self.logging_cursor = None
        self.test_execution_start = None

        self.workspace_return = False

        self.set_keyring = True
        self.keyring_process_pid = None

        self.wait_for_stable_video = True

        self.production = True

        self.timeout_handling = True

        self._after_scenario_hooks = []
        self.reverse_after_scenario_hooks = False

        self.html_report_links = True

        self.embed_separate = False
        self.change_title = True
        self.session_icon_to_title = True
        self.default_application_icon_to_title = False

        self.applications = []
        self.package_list = ["gnome-shell", "mutter"]
        self.default_application = None

        self._new_log_indicator = True

        self._set_up_scenario_skip_check()
        self._retrieve_session_data()
        self._check_for_coredump_fetching()
        self._set_g_debug_environment_variable()
        self._wait_until_shell_becomes_responsive()

    def before_scenario(self, context, scenario):
        """
        Actions that are to be executed before every scenario.

        :type context: <behave.runner.Context>
        :param context: Pass this object from environment file.

        :type scenario: <Scenario>
        :param scenario: Pass this object from environment file.

        .. note::

            You can enforce embedding for testing purposes via debug variable:
            QECORE_EMBED_ALL=yes
        """

        log.info(f"before_scenario(self, context, scenario) test: {scenario.tags[-1]}")

        self._scenario_skipped = False

        self.failed_test = False

        # If QECORE_EMBED_ALL is set, set production to True.
        self.production = self.production or self._embed_all

        self._set_welcome_tour()

        self._set_animations()

        self.current_scenario = scenario.tags[-1]
        self._set_journal_log_start_time()
        self._set_coredump_log_start_time()

        if not self.kiosk:
            overview_action(action="hide")

        self.set_typing_delay(0.2)
        self.set_debug_to_stdout_as(False)
        self._close_yelp()
        self._close_initial_setup()
        self._copy_data_folder()
        self.set_blank_screen_to_never()

        self._set_up_embedding(context)

        if self.change_title:
            self._set_title(context)

        if self.timeout_handling:
            self._set_timeout_handling()

        if self.record_video and self.production:
            self._start_recording()

        self._detect_keyring()
        self._return_to_home_workspace()

    def after_scenario(self, context, scenario):
        """
        Actions that are to be executed after every scenario.

        :type context: <behave.runner.Context>
        :param context: Pass this object from environment file.

        :type scenario: <Scenario>
        :param scenario: Pass this object from environment file.
        """

        log.info(f"after_scenario(self, context, scenario) test: {scenario.tags[-1]}")

        if scenario.status == "failed":
            self.failed_test = True

        self._capture_image()

        if self.background_image_revert:
            self._revert_background_image()

        if self.record_video:
            self._stop_recording()

        if not self.kiosk:
            overview_action(action="hide")

        for application in self.applications:
            application.kill_application()

        self._attach_screenshot_to_report(context)

        self._attach_journal_to_report(context)

        self._attach_coredump_log_to_report(context)

        self._attach_video_to_report(context)

        self._attach_abrt_link_to_report(context)

        self._attach_version_status_to_report(context)

        self._process_after_scenario_hooks(context)

        self._process_embeds(context)

        if self.html_report_links:
            self._html_report_links(context)

        self._new_log_indicator = False

    def _after_all(self, context):
        """
        This is executed as behave after_all hook,
        if context is proved in :func:`__init__`.

        :type context: <behave.runner.Context>
        :param context: Object is passed from the function that is calling it.

        .. note::
            Do **NOT** call this, if you provided context to :func:`__init__`.
        """

        log.info("_after_all(self, context)")

        self._scenario_skip_check_cb(do_assert=True)

    def _scenario_skip_check_cb(self, do_assert=False):
        """
        Callback function. Checks if any scenario was executed.

        .. note::

            Do **NOT** call this by yourself. This method is called when test ends.
        """

        log.info(f"_scenario_skip_check_cb(self, do_assert={do_assert})")

        if do_assert:
            assert not self._scenario_skipped, "No scenario matched tags"
        else:
            if self._scenario_skipped:
                print("No scenario matched tags, exiting with error code 1.")
                # sys.exit, raise, assert do not work in an atexit hook.
                os._exit(1)

    def _set_up_scenario_skip_check(self):
        """
        Remember in sandbox if any scenario (:func:`before_scenario`) was executed.

        If context provided, set after_all behave hook, otherwise set atexit hook.

        .. note::

            Do **NOT** call this by yourself. This method is called at :func:`__init__`.
        """

        log.info("_set_up_scenario_skip_check(self)")

        self._scenario_skipped = True

        if self.context is not None:
            log.info(" context is set, setting after_all behave hook")

            def get_hook(old_hook):
                def hook_runner(*args, **kwargs):
                    if old_hook is not None:
                        log.info("execute environment after_all HOOK")
                        old_hook(*args, **kwargs)
                    else:
                        log.info("after_all not defined in environment")
                    log.info("execute QECore after_all HOOK")
                    self._after_all(*args, **kwargs)

                return hook_runner

            hooks = self.context._runner.hooks
            hooks["after_all"] = get_hook(hooks.get("after_all", None))
            self.context._runner.hooks = hooks
        else:
            log.info(" context is None, setting atexit hook")
            atexit.register(self._scenario_skip_check_cb)

    def _gracefull_exit(self, signum, frame):
        """
        If killed externally, run user defined hooks not to break tests that will be
        executed next.

        .. note::

            Do **NOT** call this by yourself. This method is called when killed
            externally (timeout).
        """

        log.info(f"_graceful_exit(self, signum={signum}, frame)")

        assert False, f"Timeout: received signal: '{signum}'"

    def _start_recording(self):
        """
        Start recording the video.

        .. note::

            Do **NOT** call this by yourself.
            This method is called by :func:`before_scenario`.
        """

        log.info("_start_recording(self)")

        self.display_clock_seconds()
        self.set_max_video_length_to(600)

        active_script_recordings = run("pgrep -fla qecore_start_recording").strip("\n")
        log.info(
            f"_start_recording: removing active recordings: \
                '{active_script_recordings}'"
        )
        leftover_recording_processes_pids = run(
            "pgrep -f qecore_start_recording"
        ).strip("\n")
        if leftover_recording_processes_pids:
            leftover_recording_process_pid_list = (
                leftover_recording_processes_pids.split("\n")
            )
            for script_pid in leftover_recording_process_pid_list:
                run(f"sudo kill -9 {script_pid}")

        active_screen_casts = run("pgrep -fla Screencast").strip("\n")
        log.info(
            f"_start_recording: removing active Screencasts: '{active_screen_casts}'"
        )
        leftover_screencast_processes_pids = run("pgrep -f Screencast").strip("\n")
        if leftover_screencast_processes_pids:
            leftover_screencast_process_pid_list = (
                leftover_screencast_processes_pids.split("\n")
            )
            for screen_cast_pid in leftover_screencast_process_pid_list:
                run(f"sudo kill -9 {screen_cast_pid}")

        absolute_path_to_video = os.path.expanduser("~/Videos")
        run(f"sudo rm -rf {absolute_path_to_video}/Screencast*")

        record_video_process = Popen("qecore_start_recording", shell=True)
        self.record_video_pid = record_video_process.pid

    def _stop_recording(self):
        """
        Stop recording the video.

        .. note::

            Do **NOT** call this by yourself.
            This method is called by :func:`after_scenario`.
        """

        log.info("_stop_recording(self)")

        # Stop screencasting started by qecore.
        if self.record_video_pid is not None:
            run(f"sudo kill -9 {self.record_video_pid} > /dev/null")

        # Giving the org.gnome.Shell.Screencast chance to end
        # on its own - before killing it.
        for timer in range(30):
            screencast_process = run("pgrep -f Screencast").strip("\n")
            if screencast_process:
                sleep(0.1)
            else:
                log.info(
                    f"_stop_recording: Screencast process ended on its own in '{str(timer/10)}' seconds."
                )
                break

        # Failsafe.
        leftover_recording_processes_pids = run(
            "pgrep -f 'qecore_start_recording|Screencast'"
        ).strip("\n")
        if leftover_recording_processes_pids:
            # Purely for logging purposes.
            leftover_recording_processes = run(
                "pgrep -fla 'qecore_start_recording|Screencast'"
            ).strip("\n")
            log.info(
                f"_stop_recording: leftover processes: '{leftover_recording_processes}'"
            )

            # Kill any leftover process.
            leftover_recording_processes_pid_list = (
                leftover_recording_processes_pids.split("\n")
            )
            for leftover_process_pid in leftover_recording_processes_pid_list:
                log.info(
                    f"_stop_recording: failsafe needed, killing active recording '{leftover_process_pid}'"
                )
                run(f"sudo kill -9 {leftover_process_pid}")

            sleep(1)

        self.record_video_pid = None

    def get_app(
        self,
        name,
        a11yAppName=None,
        desktopFileExists=True,
        desktopFileName="",
        desktopFilePath="",
        appProcessName="",
    ):
        """
        This function is a wrapper over :func:`get_application` to preserve the old api name.
        This is defined as an extra function because even the method parameters were renamed to
        comply with the snake_case naming style.
        """

        log.info(
            " ".join(
                (
                    f"get_app(self, name={name}, a11yAppName={a11yAppName},",
                    f"desktopFileExists={desktopFileExists}, desktopFileName={desktopFileName},",
                    f"desktopFilePath={desktopFilePath}, appProcessName={appProcessName})",
                )
            )
        )

        return self.get_application(
            name,
            a11y_app_name=a11yAppName,
            desktop_file_exists=desktopFileExists,
            desktop_file_name=desktopFileName,
            desktop_file_path=desktopFilePath,
            app_process_name=appProcessName,
        )

    def get_application(
        self,
        name,
        a11y_app_name=None,
        desktop_file_exists=True,
        desktop_file_name="",
        desktop_file_path="",
        app_process_name="",
    ):
        """
        Return application to be used in test.

        :type name: str
        :param name: Name of the package that provides the application.

        :type a11y_app_name: str
        :param a11y_app_name: Application's name as it appears in the a11y tree.

        :type desktop_file_exists: bool
        :param desktop_file_exists: Does desktop file of the application exist?

        :type desktop_file_name: str
        :param desktop_file_name: Application's desktop file name.

        :type app_process_name: str
        :param app_process_name: Application's name as it appears in a running process.

        :return: Application class instance
        :rtype: <qecore.application.Application>

        This function is wrapped by :func:`get_app`.
        """

        log.info(
            " ".join(
                (
                    f"get_application(self, name={name},",
                    f"a11y_app_name={a11y_app_name},",
                    f"desktop_file_exists={desktop_file_exists},",
                    f"desktop_file_name={desktop_file_name},",
                    f"desktop_file_path={desktop_file_path},",
                    f"app_process_name={app_process_name})",
                )
            )
        )

        new_application = Application(
            name,
            a11y_app_name=a11y_app_name,
            desktop_file_exists=desktop_file_exists,
            desktop_file_name=desktop_file_name,
            desktop_file_path=desktop_file_path,
            app_process_name=app_process_name,
            shell=self.shell,
            session_type=self.session_type,
            session_desktop=self.session_desktop,
            kiosk=self.kiosk,
        )

        self.package_list.append(name)
        self.applications.append(new_application)
        self.default_application = (
            new_application
            if self.default_application is None
            else self.default_application
        )

        return new_application

    def get_flatpak(self, flatpak_id, **kwargs):
        """
        Return flatpak to be used in test.

        :type flatpak_id: str
        :param flatpak_id: Unique name of flatpak, mandatory format: org.flathub.app

        :return: Flatpak class instance
        :rtype: <qecore.flatpak.Flatpak>
        """

        log.info(f"get_flatpak(self, flatpak_id={flatpak_id}")

        flatpak = Flatpak(flatpak_id=flatpak_id, **kwargs)
        flatpak.shell = self.shell
        self.applications.append(flatpak)
        self.default_application = self.default_application or flatpak
        return flatpak

    def add_package(self, package_input) -> None:
        """
        Add package for a Status embed to the html log.

        :type package_input: str or list
        :param package_input: Package string or Package list .
        """

        log.info(f"add_package(self, package_input='{package_input}')")

        packages = []

        if isinstance(package_input, str):
            packages = [package_input]

        elif isinstance(package_input, list):
            packages = package_input

        else:
            packages = ["You did not provide a string or a list."]

        self.package_list.extend(packages)

    def _wait_until_shell_becomes_responsive(self):
        """
        Give some time if shell is not yet loaded fully.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`sandbox.TestSandbox.__init__`.
        """

        log.info(
            f"_wait_until_shell_becomes_responsive: waiting for '{self.session_type}'."
        )

        if self.kiosk:
            self.shell = None
            return

        error_message = ""
        for _ in range(60):
            try:
                from dogtail.tree import root

                if "gnome-shell" not in [x.name for x in root.applications()]:
                    log.info(
                        "_wait_until_shell_becomes_responsive: gnome-shell not detected in a11y root yet."
                    )
                    sleep(0.5)
                else:
                    self.shell = root.application("gnome-shell")
                    return
            except Exception as error:
                error_message = error
                log.info(
                    f"_wait_until_shell_becomes_responsive: session is not usable yet: '{error}'."
                )

        raise Exception(f"A11y root not found: unable to continue: '{error_message}'")

    def _retrieve_session_data(self):
        """
        Get session/system data.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`__init__`.
        """

        log.info("_retrieve_session_data(self)")

        self.architecture = run("uname -m").strip("\n")
        log.info(
            f"_retrieve_session_data: architecture detected: '{self.architecture}'"
        )

        # Distributions expected for now: self.distribution = ["Red Hat Enterprise Linux", "Fedora"]
        self.distribution = run("cat /etc/os-release | grep ^NAME=")
        self.distribution = self.distribution.split("=")[-1].strip("\n").strip('"')
        log.info(
            f"_retrieve_session_data: distribution detected: '{self.distribution}'"
        )

        self.session_display = run("echo $DISPLAY").strip("\n")
        if not self.session_display:
            log.info(
                "_retrieve_session_data: session display is not set - retrieve from qecore_get_active_display"
            )

            self.session_display = run("qecore_get_active_display").strip("\n")
            os.environ["DISPLAY"] = self.session_display

        log.info(
            f"_retrieve_session_data: session_display detected: '{self.session_display}'"
        )

        try:
            self.resolution = [
                int(x)
                for x in re.findall(r"\d+x\d+", run("xrandr | grep '*'"))[0].split("x")
            ]
        except Exception as error:
            self.resolution = f"The resolution retrieval failed for: {error}"

        log.info(f"_retrieve_session_data: resolution detected: '{self.resolution}'")

        self.session_desktop = run("echo $XDG_SESSION_DESKTOP").strip("\n")
        log.info(
            f"_retrieve_session_data: session_desktop detected: '{self.session_desktop}'"
        )

        self.session_type = "x11"
        if (
            "XDG_SESSION_TYPE" in os.environ
            and "wayland" in os.environ["XDG_SESSION_TYPE"]
        ):
            self.session_type = "wayland"
        log.info(
            f"_retrieve_session_data: session_type detected: '{self.session_type}'"
        )

    def _set_up_embedding(self, context):
        """
        Set up embeding to the behave html formatter.

        :type context: <behave.runner.Context>
        :param context: Passed object.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`before_scenario`.
        """

        log.info("_set_up_embedding(self)")

        def embed_data(
            mime_type, data, caption, html_el=None, fail_only=False, separate=None
        ):
            log.info(
                " ".join(
                    (
                        f"embed(mime_type={mime_type},",
                        f"data=..., caption={caption},",
                        f"html_el={repr(html_el)},",
                        f"fail_only={fail_only},",
                        f"separate={separate})",
                    )
                )
            )

            if context.html_formatter is None:
                log.info("  skipping embed as no html formatter detected")
                return

            formatter = context.html_formatter

            if separate is None:
                separate = self.embed_separate

            # If data is empty we want to finish html tag by at least one character
            non_empty_data = " " if not data else data

            if html_el is None:
                html_el = formatter.actual["act_step_embed_span"]

            if mime_type == "call" or fail_only:
                context._to_embed.append(
                    {
                        "html_el": html_el,
                        "mime_type": mime_type,
                        "data": non_empty_data,
                        "caption": caption,
                        "fail_only": fail_only,
                        "separate": separate,
                    }
                )
            else:
                formatter._doEmbed(html_el, mime_type, non_empty_data, caption)
                if separate:
                    ET.SubElement(html_el, "br")

        def set_title(title, append=False, tag="span", **kwargs):
            for formatter in context._runner.formatters:
                if (
                    formatter.name == "html"
                    and getattr(formatter, "set_title", None) is not None
                ):
                    formatter.set_title(title=title, append=append, tag=tag, **kwargs)

                elif (
                    formatter.name == "html-pretty"
                    and getattr(formatter, "set_title", None) is not None
                ):
                    formatter.set_title(title=title)

        # Set up a variable that we can check against if there is a formatter in use.
        context.html_formatter = None

        # Main reason for this is backwards compatibility.
        # There always used to be context.embed defined and was ignored if called.
        # We define the same to not break the legacy usage while checking html_formatter to save time.
        def _dummy_embed(*args, **kwargs):
            pass

        context.embed = _dummy_embed

        for formatter in context._runner.formatters:

            # Formatter setup for html.
            if formatter.name == "html":
                formatter.embedding = embed_data
                context.html_formatter = formatter
                context.embed = embed_data
                break

            # Formatter setup for html-pretty.
            if formatter.name == "html-pretty":
                context.html_formatter = formatter
                context.embed = formatter.embed
                break

        context._to_embed = []
        context.set_title = set_title

    def add_after_scenario_hook(self, callback, *args, **kwargs):
        """
        Creates hook from callback function and its arguments.
        Hook will be called during :func:`sandbox.after_scenario`.

        :type callback: <function>
        :param callback: function to be called

        .. note::
            Hooks are called in :func:`sandbox.after_scenario` in the order they were added. To reverse
            the order of execution set `sandbox.reverse_after_scenario_hooks` (default `False`).

        **Examples**::

            # already defined function
            def something():
                ...

            sandbox.add_after_scenario_hook(something)

            # generic function call
            sandbox.add_after_scenario_hook(function_name, arg1, arg2, kwarg1=val1, ...)

            # call command
            sandbox.add_after_scenario_hook(subprocess.call, "command to be called", shell=True)

            # embed data - if you want them embeded in the last step
            sandbox.add_after_scenario_hook(context.embed, "text/plain", data, caption="DATA")

            # embed data computed later (read log file)
            sandbox.add_after_scenario_hook(lambda context:
                context.embed("text/plain", open(log_file).read(), caption="LOG"), context)
        """

        log.info("add_after_scenario_hook()")

        self._after_scenario_hooks += [(callback, args, kwargs)]

    def _set_timeout_handling(self):
        """
        Set up signal handling.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`before_scenario`.
        """

        log.info("_set_timeout_handling(self)")

        signal.signal(signal.SIGTERM, self._gracefull_exit)
        run("touch /tmp/qecore_timeout_handler")

    def _set_welcome_tour(self):
        """
        Disable gnome-welcome-tour via gsettings command if allowed.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`before_scenario`.
        """

        log.info("_set_welcome_tour(self)")

        if self.disable_welcome_tour:
            run(
                " ".join(
                    (
                        "gsettings",
                        "set",
                        "org.gnome.shell",
                        "welcome-dialog-last-shown-version",
                        "100.0",  # larger number than the current 40
                    )
                )
            )

    def _set_animations(self):
        """
        Set animations via gsettings command.
        Default value is None so the settings is not set unless user specifies otherwise.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`before_scenario`.
        """

        log.info("_set_animations(self)")

        if self.enable_animations is not None:
            run(
                " ".join(
                    (
                        "gsettings",
                        "set",
                        "org.gnome.desktop.interface",
                        "enable-animations",
                        "true" if self.enable_animations else "false",
                    )
                )
            )

    def _set_journal_log_start_time(self):
        """
        Save time.
        Will be used to retrieve logs from journal.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`before_scenario`.
        """

        log.info("_set_journal_log_start_time(self)")

        initial_cursor_output = run("sudo journalctl --lines=0 --show-cursor").strip()
        cursor_target = initial_cursor_output.split("cursor: ", 1)[-1]
        self.logging_cursor = f'"--after-cursor={cursor_target}"'

    def _set_coredump_log_start_time(self):
        """
        Save time.
        Will be used to retrieve coredumpctl list.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`before_scenario`.
        """

        log.info("_set_coredump_log_start_time(self)")

        self.test_execution_start = run("date +%s").strip("\n")

    def _close_yelp(self):
        """
        Close yelp application that is opened after fresh system installation.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`before_scenario`.
        """

        log.info("_close_yelp(self)")

        # Attribute switch to allow not closing yelp in before_scenario.
        # Corner case was found in which we test yelp and do not close between scenarios.
        if not self.enable_close_yelp:
            return

        help_process_id = run("pgrep yelp").strip("\n")
        if help_process_id.isdigit():
            run(f"kill -9 {help_process_id}")

    def _close_initial_setup(self):
        """
        Close initial setup window that is opened after the first login to the system.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`before_scenario`.
        """

        log.info("_close_initial_setup(self)")

        run("echo yes > ~/.config/gnome-initial-setup-done")

    def set_blank_screen_to_never(self):
        """
        Set blank screen to never. For longer tests it is undesirable for screen to lock.

        .. note::

            This method is called by :func:`before_scenario`.
            There was never need to have other options,
            we do not want the system to sleep during the test.
        """

        log.info("set_blank_screen_to_never(self)")

        run("gsettings set org.gnome.desktop.session idle-delay 0")

    def set_max_video_length_to(self, number=600):
        """
        Set maximum allowed video length. With default value for 10 minutes.

        :type number: int
        :param number: Maximum video length.

        .. note::

            This method is called by :func:`before_scenario`. You can overwrite the setting.
        """

        log.info(f"set_max_video_length_to(self, number={number})")

        run(
            " ".join(
                (
                    "gsettings set",
                    "org.gnome.settings-daemon.plugins.media-keys",
                    f"max-screencast-length {number}",
                )
            )
        )

    def display_clock_seconds(self):
        """
        Display clock seconds for better tracking test in video.

        .. note::

            This method is called by :func:`before_scenario`.
            There was never need to have other options,
            as we want to see the seconds ticking during the test.
        """

        log.info("display_clock_seconds(self)")

        run("gsettings set org.gnome.desktop.interface clock-show-seconds true")

    def _return_to_home_workspace(self):
        """
        Return to home workspace.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`before_scenario`.
        """

        log.info("_return_to_home_workspace(self)")

        if not self.workspace_return:
            return

        keyCombo("<Super><Home>")

    def set_typing_delay(self, number):
        """
        Set typing delay so slower machines will not lose characters on type.

        :type number: int
        :param number: Time in between accepted key strokes.

        .. note::

            This method is called by :func:`before_scenario`. You can overwrite the setting.
        """

        log.info(f"set_typing_delay(self, number={number})")

        config.typingDelay = number

    def set_debug_to_stdout_as(self, true_or_false=False):
        """
        Set debugging to stdout.

        :type true_or_false: bool
        :param true_or_false: Decision if debug to stdout or not.

        .. note::

            This method is called by :func:`before_scenario`. You can overwrite the setting.
        """

        log.info(f"set_debug_to_stdout_as(self, true_or_false={true_or_false})")

        config.logDebugToStdOut = true_or_false

    def _copy_data_folder(self):
        """
        Copy data/ directory content to the /tmp/ directory.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`before_scenario`.
        """

        log.info("_copy_data_folder(self)")

        if os.path.isdir("data/"):
            run("rsync -r data/ /tmp/")

    def _detect_keyring(self):
        """
        Detect if keyring was setup. If not, setup the keyring with empty password.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`before_scenario`.
        """

        log.info("_detect_keyring(self)")

        if not self.set_keyring:
            return

        if self.kiosk:
            return

        current_user = os.path.expanduser("~")

        is_keyring_set = os.path.isfile("/tmp/keyring_set")
        log.info(f"_detect_keyring: keyring set by qecore: '{is_keyring_set}'")

        is_keyring_in_place = os.path.isfile(
            f"{current_user}/.local/share/keyrings/default"
        )
        log.info(f"_detect_keyring: default keyring exists: '{is_keyring_in_place}'")

        if not is_keyring_set or not is_keyring_in_place:
            run(f"sudo rm -rf {current_user}/.local/share/keyrings/*")

            # This should always succeed.
            # If not, do not fail here, let behave handle it and generate html log.
            try:
                log.info("_detect_keyring: creating keyring process.")

                create_keyring_process = Popen("qecore_create_keyring", shell=True)
                self.keyring_process_pid = create_keyring_process.pid
                sleep(1)

                log.info(
                    "_detect_keyring: confirming choosing empty password for keyring in session."
                )
                self.shell.child("Continue").click()
                sleep(0.2)

                log.info(
                    "_detect_keyring: confirming to store password unencrypted in session."
                )
                self.shell.child("Continue").click()
                sleep(0.2)
            except Exception as error:
                print(
                    f"_detect_keyring error with keyring creation/confirmation: '{error}'"
                )
                traceback.print_exc(file=sys.stdout)

                log.info("_detect_keyring: failed to create, end the session prompt.")
                create_keyring_process.kill()

            run("touch /tmp/keyring_set")

    def _capture_image(self):
        """
        Capture screenshot after failed step.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`after_scenario`.
        """

        if not self.production:
            return

        if not (self.attach_screenshot or self._embed_all):
            return

        if not (self.failed_test or self._embed_all):
            return

        log.info("_capture_image(self)")

        self.screenshot_run_result = run(
            "gnome-screenshot -f /tmp/screenshot.png", verbose=True
        )

    def _check_for_coredump_fetching(self):
        """
        Set attach_coredump variable if set in Jenkins - tested via file existance.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`__init__`.
        """

        log.info("_check_for_coredump_fetching(self)")

        self.attach_coredump_file_check = os.path.exists("/tmp/qecore_coredump_fetch")

    def _set_g_debug_environment_variable(self):
        """
        Setup environment variable G_DEBUG as 'fatal-criticals'.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`__init__`.
        """

        log.info("_set_g_debug_environment_variable(self)")

        # Environment value set upon checked field in Jenkins.
        if os.path.isfile("/tmp/headless_enable_fatal_critical"):
            log.info("_set_g_debug_environment_variable: set G_DEBUG=fatal-criticals.")
            os.environ["G_DEBUG"] = "fatal-criticals"

        # Fatal_wanings has bigger priority than criticals.
        # Should both options be set in Jenkins the warning will overwrite the variable.
        if os.path.isfile("/tmp/headless_enable_fatal_warnings"):
            log.info("_set_g_debug_environment_variable: set G_DEBUG=fatal-warnings.")
            os.environ["G_DEBUG"] = "fatal-warnings"

    def _set_title(self, context):
        """
        Append component name and session type to HTML title.

        :type context: <behave.runner.Context>
        :param context: Passed object.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`before_scenario`.
            Use :func:`context.set_title` to set HTML title.
        """

        log.info("_set_title(self, context)")

        formatter_instance = getattr(context, "html_formatter", None)
        if formatter_instance is None:
            return

        if formatter_instance.name == "html":
            context.set_title("", tag="br", append=True)

            if self.default_application_icon_to_title:
                icon = self.get_default_application_icon()
                if icon is not None:
                    context.set_title(
                        "",
                        append=True,
                        tag="img",
                        alt=self.session_type[1],
                        src=icon.to_src(),
                        style="height:1.8rem; vertical-align:text-bottom;",
                    )

                context.set_title(f"{self.component} - ", append=True, tag="small")

            if self.session_icon_to_title:
                context.set_title(
                    "",
                    append=True,
                    tag="img",
                    alt=self.session_type[1],
                    src=qecore_icons[self.session_type].to_src(),
                    style="height:1.8rem; vertical-align:text-bottom;",
                )

                context.set_title(
                    self.session_type[1:],
                    append=True,
                    tag="small",
                    style="margin-left:-0.4em;",
                )

            self.change_title = False

        elif formatter_instance.name == "html-pretty":
            formatter_instance.set_icon(icon=qecore_icons[self.session_type].to_src())

    def get_default_application_icon(self):
        """
        Get icon for default application.

        :return: icon or None
        :rtype: <icons.QECoreIcon>
        """

        log.info("get_default_application_icon(self)")

        # Importing here because of sphinx documentation generating issues.
        import gi

        gi.require_version("Gtk", "3.0")
        from gi.repository import Gtk

        if self.default_application and self.default_application.icon:
            icon_theme = Gtk.IconTheme.get_default()
            icon = icon_theme.lookup_icon(self.default_application.icon, 48, 0)
            if icon:
                icon_path = icon.get_filename()
                if icon_path:
                    mime = MimeTypes()
                    mime_type = mime.guess_type(icon_path)[0]
                    data_base64 = base64.b64encode(open(icon_path, "rb").read())
                    data_encoded = data_base64.decode("utf-8").replace("\n", "")
                    return QECoreIcon(mime_type, "base64", data_encoded)
        return None

    def _attach_screenshot_to_report(self, context):
        """
        Attach screenshot to the html report upon failed test.

        :type context: <behave.runner.Context>
        :param context: Passed object.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`after_scenario`.
        """

        log.info("_attach_screenshot_to_report(self, context)")

        # Running this function makes sense only when formatter is defined.
        if context.html_formatter is None:
            log.info("No formatter defined.")
            return

        if not self.production:
            log.info(f"Attribute self.production='{str(self.production)}'.")
            return

        if not (self.attach_screenshot or self._embed_all):
            log.info(
                f"Attribute self.attach_screenshot='{str(self.attach_screenshot)}'."
            )
            return

        if not (self.failed_test or self._embed_all):
            log.info(f"Attribute self.failed_test='{str(self.failed_test)}'.")
            return

        if self.screenshot_run_result[1] != 0:
            log.info("_attach_screenshot_to_report: Screenshot capture failed.")
            context.embed(
                mime_type="text/plain",
                data=f"Screenshot capture failed: \n{self.screenshot_run_result}\n",
                caption="Screenshot",
                fail_only=True,
            )
        else:
            self.attach_image_to_report(
                context, "/tmp/screenshot.png", "Screenshot", fail_only=True
            )

    def attach_image_to_report(
        self, context, image=None, caption="DefaultCaption", fail_only=False
    ):
        """
        Attach image to the html report upon user request.

        :type context: <behave.runner.Context>
        :param context: Passed object.

        :type image: str
        :param image: Location of the image/png file.

        :type caption: str
        :param caption: Caption that is to be displayed in test html report.

        :type fail_only: bool
        :param fail_only: attach only if scenario fails

        .. note::

            Use this to attach any image to report at any time.
        """

        log.info(
            f"attach_image_to_report(self, context, image={image}, caption={caption}, fail_only={fail_only})"
        )

        # Running this function makes sense only when formatter is defined.
        if context.html_formatter is None:
            log.info("No formatter defined.")
            return

        if not self.production:
            log.info(f"Attribute self.production='{str(self.production)}'.")
            return

        log.info(
            " ".join(
                (
                    "attach_image_to_report(self, context,",
                    f"image={image},",
                    f"caption={caption},",
                    f"fail_only={fail_only})",
                )
            )
        )

        if os.path.isfile(image):
            data_base64 = base64.b64encode(open(image, "rb").read())
            data_encoded = data_base64.decode("utf-8").replace("\n", "")
            context.embed(
                mime_type="image/png",
                data=data_encoded,
                caption=caption,
                fail_only=fail_only,
            )

    def _attach_video_to_report(self, context):
        """
        Attach video to the html report upon failed test.

        :type context: <behave.runner.Context>
        :param context: Passed object.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`after_scenario`.
        """

        log.info("_attach_video_to_report(self, context)")

        # Running this function makes sense only when formatter is defined.
        if context.html_formatter is None:
            log.info("No formatter defined.")
            return

        if not (self.production and self.record_video):
            log.info(f"Attribute self.production='{str(self.production)}'.")
            log.info(f"Attribute self.record_video='{str(self.record_video)}'.")
            return

        if not (self.attach_video or self._embed_all):
            log.info(f"Attribute self.attach_video='{str(self.attach_video)}'.")
            return

        if not (self.attach_video_on_pass or self.failed_test or self._embed_all):
            log.info(f"Attribute self.failed_test='{str(self.failed_test)}'.")
            log.info(
                f"Attribute self.attach_video_on_pass='{str(self.attach_video_on_pass)}'."
            )
            return

        absolute_path_to_video = os.path.expanduser("~/Videos")
        screencast_list = [
            f"{absolute_path_to_video}/{file_name}"
            for file_name in os.listdir(absolute_path_to_video)
            if "Screencast" in file_name
        ]
        log.info(f"_attach_video_to_report: screencast list '{screencast_list}'")

        video_name = f"{self.component}_{self.current_scenario}"
        absolute_path_to_new_video = f"{absolute_path_to_video}/{video_name}.webm"
        log.info(
            f"_attach_video_to_report: absolute path to new video '{absolute_path_to_new_video}'"
        )

        if screencast_list == []:
            log.info("_attach_video_to_report: No video file found.")
            context.embed(
                mime_type="text/plain",
                data="No video file found.",
                caption="Video",
                fail_only=not self.attach_video_on_pass,
            )
        else:
            if self.wait_for_stable_video:
                self._wait_for_video_encoding(screencast_list[0])

            data_base64 = base64.b64encode(open(screencast_list[0], "rb").read())
            data_encoded = data_base64.decode("utf-8").replace("\n", "")
            context.embed(
                mime_type="video/webm",
                data=data_encoded,
                caption="Video",
                fail_only=not self.attach_video_on_pass,
            )

            log.info("_attach_video_to_report: renaming screencast.")
            run(f"mv {screencast_list[0]} {absolute_path_to_new_video}")
            log.info("_attach_video_to_report: erasing unsaved videos.")
            run(f"sudo rm -rf {absolute_path_to_video}/Screencast*")

    def _attach_journal_to_report(self, context):
        """
        Attach journal to the html report upon failed test.

        :type context: <behave.runner.Context>
        :param context: Passed object.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`after_scenario`.
        """

        log.info("_attach_journal_to_report(self, context)")

        # Running this function makes sense only when formatter is defined.
        if context.html_formatter is None:
            log.info("No formatter defined.")
            return

        if not self.production:
            log.info(f"Attribute self.production='{str(self.production)}'.")
            return

        if not (self.attach_journal or self._embed_all):
            log.info(f"Attribute self.attach_journal='{str(self.attach_journal)}'.")
            return

        if not (self.attach_journal_on_pass or self.failed_test or self._embed_all):
            log.info(f"Attribute self.failed_test='{str(self.failed_test)}'.")
            log.info(
                f"Attribute self.attach_journal_on_pass='{str(self.attach_journal_on_pass)}'."
            )
            return

        journal_run = run(
            " ".join(
                (
                    "sudo journalctl --all",
                    f"--output=short-precise {self.logging_cursor}",
                    "> /tmp/journalctl_short.log",
                )
            ),
            verbose=True,
        )

        if journal_run[1] != 0:
            log.info("_attach_journal_to_report: creation of journalctl log failed.")
            context.embed(
                mime_type="text/plain",
                data=f"Creation of journalctl file failed: \n{journal_run}\n",
                caption="journalctl",
                fail_only=not self.attach_journal_on_pass,
            )
        else:
            log.info("_attach_journal_to_report: creation of journalctl log succeeded.")
            journal_data = self.file_loader("/tmp/journalctl_short.log")

            context.embed(
                mime_type="text/plain",
                data=journal_data,
                caption="journalctl",
                fail_only=not self.attach_journal_on_pass,
            )

        log.info("_attach_journal_to_report: erase the journalctl log.")
        run("rm /tmp/journalctl_short.log")

    def _attach_coredump_log_to_report(self, context):
        """
        Attach coredump log to the html report upon failed test.

        :type context: <behave.runner.Context>
        :param context: Passed object.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`after_scenario`.
        """

        log.info("_attach_coredump_log_to_report(self, context)")

        # Running this function makes sense only when formatter is defined.
        if context.html_formatter is None:
            log.info("No formatter defined.")
            return

        if not self.production:
            log.info(f"Attribute self.production='{str(self.production)}'.")
            return

        if not (
            self.attach_coredump or self.attach_coredump_file_check or self._embed_all
        ):
            log.info(f"Attribute self.attach_coredump='{str(self.attach_coredump)}'.")
            log.info(
                f"Attribute self.attach_coredump_file_check='{str(self.attach_coredump_file_check)}'."
            )
            return

        if not (self.attach_coredump_on_pass or self.failed_test or self._embed_all):
            log.info(f"Attribute self.failed_test='{str(self.failed_test)}'.")
            log.info(
                f"Attribute self.attach_coredump_on_pass='{str(self.attach_coredump_on_pass)}'."
            )
            return

        # Get coredump list results only from duration of the test.
        coredump_list = run(
            f"sudo coredumpctl list --since=@{self.test_execution_start}"
        )

        # If there are no coredumps end right here.
        if "No coredumps found." in coredump_list:
            log.info("_attach_coredump_log_to_report: No coredumps found.")
            return

        coredump_log = "/tmp/qecore_coredump.log"
        debuginfo_install_log = "/tmp/qecore_debuginfo_install.log"

        # Empty the coredump file logs.
        if os.path.isfile(coredump_log):
            log.info("_attach_coredump_log_to_report: emptying the coredump log.")
            run(f">{coredump_log}")

        # Do not empty debuginfo log - the content is desired in all possible tests.
        if not os.path.isfile(debuginfo_install_log):
            log.info("_attach_coredump_log_to_report: creating debuginfo log file.")
            run(f"touch {debuginfo_install_log}")

        # Get packages to be installed from gdb.
        def get_packages_from_coredump(pid):
            # Get first gdb output and load it to file to parse over.
            run(f"echo 'q' | sudo coredumpctl gdb {pid} 2&> {coredump_log}")

            # Set the base variable to return with all data.
            desired_data = ""

            # Open the file and iterate over its lines.
            with open(coredump_log, "r") as f:
                # Loading one line at a time.
                next_line = f.readline()

                # Loop until there is no next line.
                while next_line:
                    # Parse correct lines to fetch debuginfo packages.
                    if "debug" in next_line and "install" in next_line:
                        _, target = next_line.split("install ", 1)
                        desired_data += target.strip("\n") + " "

                    # If there is no coredump file present there si nothing to fetch.
                    elif "Coredump entry has no core attached." in next_line:
                        log.info(
                            "_attach_coredump_log_to_report: coredump entry has no core attached."
                        )
                        return None

                    # Load the next line.
                    next_line = f.readline()

            return desired_data

        # Install all packages that gdb desires.
        def install_debuginfo_packages(pid):
            # We need gdb to be installed.
            if "not installed" in run("rpm -q gdb"):
                log.info("_attach_coredump_log_to_report: installing gdb.")
                run(f"sudo dnf install -y gdb >> {debuginfo_install_log}")

            # Iterate a few times over the gdb to get packages and install them.
            packages_installed_in_last_attempt = ""
            for _ in range(20):
                packages_to_install = get_packages_from_coredump(pid)

                # Install required packages but break if packages were already attempted to be installed.
                if packages_to_install and (
                    packages_to_install != packages_installed_in_last_attempt
                ):
                    packages_installed_in_last_attempt = packages_to_install
                    run(
                        f"sudo dnf debuginfo-install -y {packages_to_install} >> {debuginfo_install_log}"
                    )
                else:
                    break

        # Load coredump lines as provided.
        list_of_results = coredump_list.rstrip("\n").split("\n")[1:]
        valid_coredump_counter = 0

        for coredump_line in list_of_results:
            starting_time = time.time()

            coredump_line_split = coredump_line.split(" ")
            coredump_line_filtered = [x for x in coredump_line_split if x]
            coredump_pid_to_investigate = coredump_line_filtered[4]

            # Check if coredump file does not exist.
            if coredump_line_filtered[8] == "none":
                # Attach data to html report.
                context.embed(
                    mime_type="text/plain",
                    data="Coredump entry has no core attached.",
                    caption="coredump_log",
                )
                continue

            # Install all debuginfos given by coredump file with found pid.
            install_debuginfo_packages(coredump_pid_to_investigate)

            # All debuginfo packages should be installed now - get the backtrace and attach it to report.
            gdb_command = "thread apply all bt full"
            run(
                f"echo '{gdb_command}' | sudo coredumpctl gdb {coredump_pid_to_investigate} 2&> {coredump_log}"
            )

            # Calculate the total execution time of coredump fetch.
            coredump_fetch_time = time.time() - starting_time

            valid_coredump_counter += 1
            context.embed(
                mime_type="text/plain",
                data=self.file_loader(coredump_log),
                caption=f"coredump_log_{coredump_pid_to_investigate}+{coredump_fetch_time:.1f}s",
            )

        if valid_coredump_counter != 0:
            context.embed(
                mime_type="text/plain",
                data=self.file_loader(debuginfo_install_log),
                caption="debug_info_install_log",
            )

    def _attach_abrt_link_to_report(self, context):
        """
        Attach abrt link to the html report upon detected abrt FAF report.

        :type context: <behave.runner.Context>
        :param context: Passed object.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`after_scenario`.
        """

        log.info("_attach_abrt_link_to_report(self, context)")

        # Running this function makes sense only when formatter is defined.
        if context.html_formatter is None:
            log.info("No formatter defined.")
            return

        if not self.production:
            log.info(f"Attribute self.production='{str(self.production)}'.")
            return

        if not (self.attach_faf or self._embed_all):
            log.info(f"Attribute self.attach_faf='{str(self.attach_faf)}'.")
            return

        if not (self.attach_faf_on_pass or self.failed_test or self._embed_all):
            log.info(f"Attribute self.failed_test='{str(self.failed_test)}'.")
            log.info(
                f"Attribute self.attach_faf_on_pass='{str(self.attach_faf_on_pass)}'."
            )
            return

        faf_reports = set()

        abrt_directories = run("sudo ls /var/spool/abrt/ | grep ccpp-", verbose=True)
        log.info(f" abrt_directories result: '{abrt_directories}'")

        if abrt_directories[1] != 0:
            log.info(
                f" abrt_directories return code was non-zero: '{abrt_directories[1]}'"
            )
            return

        abrt_directories_as_list = abrt_directories[0].strip("\n").split("\n")
        for abrt_directory in abrt_directories_as_list:

            reason_file = f"/var/spool/abrt/{abrt_directory}/reason"
            reported_to_file = f"/var/spool/abrt/{abrt_directory}/reported_to"

            try:
                log.info(f"_attach_abrt_link_to_report: reading file '{reason_file}'")
                abrt_faf_reason_run = run(f"sudo cat '{reason_file}'", verbose=True)

                log.info(
                    f"_attach_abrt_link_to_report: reading file '{reported_to_file}'"
                )
                abrt_faf_hyperlink_run = run(
                    f"sudo cat '{reported_to_file}'", verbose=True
                )

                if abrt_faf_reason_run[1] == 0 and abrt_faf_hyperlink_run[1] == 0:
                    abrt_faf_reason = abrt_faf_reason_run[0].strip("\n")
                    abrt_faf_hyperlink = (
                        abrt_faf_hyperlink_run[0]
                        .split("ABRT Server: URL=")[-1]
                        .split("\n")[0]
                    )

                    faf_reports.add((abrt_faf_hyperlink, f"Reason: {abrt_faf_reason}"))

                else:
                    log.info(
                        "_attach_abrt_link_to_report: non-zero return code while reading file."
                    )
                    log.info(
                        f"_attach_abrt_link_to_report: abrt_faf_reason_run '{abrt_faf_reason_run}'"
                    )
                    log.info(
                        f"_attach_abrt_link_to_report: abrt_faf_hyperlink_run '{abrt_faf_hyperlink_run}'"
                    )

            except Exception as error:
                log.info(f"_attach_abrt_link_to_report: Exception caught: {error}'")

        if faf_reports:
            context.embed(
                "link",
                faf_reports,
                caption="FAF reports",
                fail_only=not self.attach_faf_on_pass,
            )

    def _attach_version_status_to_report(self, context) -> None:
        """
        Process status report - this will attach version of many components needed for correct function.

        :type context: <behave.runner.Context>
        :param context: Passed object.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`after_scenario`.
        """

        log.info("_attach_version_status_to_report(self, context)")

        # Running this function makes sense only when formatter is defined.
        if context.html_formatter is None:
            log.info("No formatter defined.")
            return

        cached_versions_file = "/tmp/qecore_version_status.txt"

        if self.status_report and self._new_log_indicator:
            # If the cached file exitsts attach it.
            if os.path.isfile(cached_versions_file):
                context.embed(
                    "text/plain",
                    data=self.file_loader(cached_versions_file),
                    caption="Status",
                    fail_only=False,
                )
                return

            status_data = "Versions used in testing:\n"

            # Iterate over components and get package version.
            for component in self.package_list:

                # Handling gnome-shell differently to prevent flooding the Status log with extensions.
                if component == "gnome-shell":
                    component_rpm = run(f"rpm -q '{component}'")

                # Get a name for rpm version check, we want other components to list all parts.
                else:
                    component_rpm = run(f"rpm -qa | grep '{component}'")

                status_data += "\n".join(
                    (
                        f"\nComponent: '{component}'",
                        f"{component_rpm}",
                    )
                )

            # Import version from module.
            try:
                qecore_version = pkg_resources.require("qecore")[0].version
            except ImportError as error:
                qecore_version = f"__qecore_version_unavailable__: '{error}'"

            # Import version from module.
            try:
                behave_version = pkg_resources.require("behave")[0].version
            except ImportError as error:
                behave_version = f"__behave_version_unavailable__: '{error}'"

            # Import version from module.
            try:
                behave_html_formatter_version = pkg_resources.require(
                    "behave_html_formatter"
                )[0].version
            except ImportError as error:
                behave_html_formatter_version = (
                    f"__formatter_version_unavailable__: '{error}'"
                )

            # Import version from module.
            try:
                behave_html_pretty_formatter_version = pkg_resources.require(
                    "behave_html_pretty_formatter"
                )[0].version
            except ImportError as error:
                behave_html_pretty_formatter_version = (
                    f"__formatter_version_unavailable__: '{error}'"
                )

            # Get dogtial rpm version.
            dogtail_rpm = run("rpm -qa | grep dogtail")

            # Join the data from modules and dogtail rpm.
            status_data += "\n".join(
                (
                    "\nVersions from modules:",
                    f"qecore: '{qecore_version}'",
                    f"behave: '{behave_version}'",
                    f"behave_html_formatter: '{behave_html_formatter_version}'",
                    f"behave_html_pretty_formatter: '{behave_html_pretty_formatter_version}'",
                    f"dogtail: \n{dogtail_rpm}",
                )
            )

            # Embed the data to the report.
            with open(cached_versions_file, "w+", encoding="utf-8") as _cache_file:
                _cache_file.write(status_data)

            context.embed("text/plain", status_data, caption="Status", fail_only=False)

    def _process_after_scenario_hooks(self, context):
        """
        Process attached after_scenario_hooks.

        :type context: <behave.runner.Context>
        :param context: Passed object.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`after_scenario`.
        """

        log.info("_process_after_scenario_hooks(self, context)")

        hook_errors = ""

        if self.reverse_after_scenario_hooks:
            log.info(" reversing _after_scenario_hooks")
            self._after_scenario_hooks.reverse()

        log.info(f" processing {len(self._after_scenario_hooks)} hooks")

        for callback, args, kwargs in self._after_scenario_hooks:
            try:
                callback(*args, **kwargs)
            except Exception as error:
                error_trace = traceback.format_exc()
                hook_errors += "\n\n" + error_trace
                context.embed(
                    "text/plain",
                    f"Hook Error: {error}\n{error_trace}",
                    caption="Hook Error",
                )

        self._after_scenario_hooks = []

        assert not len(hook_errors), "".join(
            f"Exceptions during after_scenario hook:{hook_errors}"
        )

    def _process_embeds(self, context):
        """
        Process posponed embeds (with myme_type="call" or fail_only=True).

        :type context: <behave.runner.Context>
        :param context: Passed object.

        :type scenario: <behave.model.Scenario>
        :param scenario: Passed object.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`after_scenario`.
        """

        log.info("_process_embeds(self, context)")

        scenario_fail = self.failed_test or self._embed_all

        embeds = getattr(context, "_to_embed", [])
        log.info(f" process {len(embeds)} embeds")

        for kwargs in embeds:
            # Execute postponed "call"s.
            if kwargs["mime_type"] == "call":
                # "data" is function, "caption" is args, function returns triple.
                mime_type, data, caption = kwargs["data"](*kwargs["caption"])
                kwargs["mime_type"], kwargs["data"], kwargs["caption"] = (
                    mime_type,
                    data,
                    caption,
                )
            # skip "fail_only" when scenario passed
            if not scenario_fail and kwargs["fail_only"]:
                continue
            # Reset "fail_only" to prevent loop.
            kwargs["fail_only"] = False
            context.embed(**kwargs)
        context._to_embed = []

    def _html_report_links(self, context):
        """
        Fetch a tag link to the git repository in current commit.

        :type context: <behave.runner.Context>
        :param context: Passed object.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`after_scenario`.
        """

        log.info("_html_report_links(self, context)")

        # Running this function makes sense only when formatter is defined.
        if context.html_formatter is None:
            log.info("No formatter defined.")
            return

        git_url = self.project_git_url
        git_commit = self.project_git_commit
        if not git_url or not git_commit:
            log.info("The git_url or git_commit is not valid.")
            return

        project_url_base = f"{self.project_git_url}/-/tree/{self.project_git_commit}/"
        qecore_url_base = "/".join(
            ("https://gitlab.com", "dogtail/qecore/-/tree/master/qecore/")
        )
        nmci_url_base = "/".join(
            (
                "https://gitlab.freedesktop.org",
                "NetworkManager/NetworkManager-ci/-/tree/master/",
            )
        )

        # This will return an instance of PrettyHTMLFormatter.
        formatter_instance = getattr(context, "html_formatter", None)

        # If no instance was given end the handling.
        if formatter_instance is None:
            log.info("No instance of formatter found.")
            return

        # Formatter html handling.
        if formatter_instance.name == "html":
            log.info("Handling 'html' formatter.")

            # Search for links in scenario HTML element.
            scenario_el = getattr(formatter_instance, "scenario_el", None)
            if scenario_el is None:
                log.info("Formatter instance has no scenario_el attribute.")
                return

            scenario_file = scenario_el.find(".//span[@class='scenario_file']")
            step_files = scenario_el.findall(".//div[@class='step_file']/span")
            tags_el = scenario_el.find(".//span[@class='tag']")

            # Link tags to scenario (.feature file).
            if tags_el is not None:
                tags = tags_el.text.split()
                tags.reverse()
                tags_el.text = ""
                scenario_name = True

                for tag in tags:
                    if tag.startswith("@rhbz"):
                        bug_id = tag.replace("@rhbz", "").rstrip(",")
                        link_el = ET.Element(
                            "a",
                            {
                                "href": "https://bugzilla.redhat.com/" + bug_id,
                                "target": "_blank",
                                "style": "color:inherit",
                            },
                        )
                        link_el.text = tag
                        tags_el.insert(0, link_el)

                    elif scenario_name:
                        scenario_name = False
                        if scenario_file is not None:
                            file_name, line = scenario_file.text.split(":", 2)
                            link_el = ET.Element(
                                "a",
                                {
                                    "href": project_url_base + file_name + "#L" + line,
                                    "target": "_blank",
                                    "style": "color:inherit",
                                },
                            )
                            link_el.text = tag
                            tags_el.insert(0, link_el)

                    else:
                        span_el = ET.Element("span")
                        span_el.text = tag
                        tags_el.insert(0, span_el)

            # Link files.
            for file_el in [scenario_file] + step_files:
                if file_el is not None and ":" in file_el.text:
                    file_name, line = file_el.text.split(":", 2)
                    if file_name.startswith("NMci"):
                        url = nmci_url_base + file_name.replace("NMci/", "", 1)

                    elif "/site-packages/qecore/" in file_name:
                        url = (
                            qecore_url_base
                            + file_name.split("/site-packages/qecore/")[-1]
                        )

                    else:
                        url = project_url_base + file_name

                    link = ET.SubElement(
                        file_el,
                        "a",
                        {
                            "href": url + "#L" + line,
                            "target": "_blank",
                            "style": "color:inherit",
                        },
                    )
                    link.text = file_el.text
                    file_el.text = ""

        # Formatter html-pretty handling.
        if formatter_instance.name == "html-pretty":
            log.info("Handling 'html-pretty' formatter.")

            # Iterate over the data we have and change links where necessary.
            for feature in formatter_instance.features:
                for scenario in feature.scenarios:
                    # Iterate over all tags.
                    for tag in scenario.tags:
                        # Tag class has attributes behave_tag and link
                        # The tag becomes link only after this setup, the default on formatters' side is <span>.

                        # If the tag.link is not None, it was modified already,
                        # skip another attempt to modify it to link.
                        if tag.has_link():
                            break

                        # Either it becomes a link to bugzilla or link to git.
                        if tag.behave_tag.startswith("rhbz"):
                            # Exctract just the number from th @rhbz tag so we can link it to bugzilla.
                            bug_id = tag.behave_tag.replace("rhbz", "").rstrip(",")
                            bug_link = "https://bugzilla.redhat.com/" + bug_id

                            # Tag becomes link to bugzilla.
                            tag.set_link(bug_link)

                        # No reason to not attempt to do link every single time, everything should be on git.
                        else:
                            # Tag becomes link to git project.
                            # If the tag was normalized for Outline as a string, use the scenario location line.
                            if type(tag.behave_tag) is str:
                                tag.set_link(
                                    project_url_base
                                    + scenario.location.filename
                                    + "#L"
                                    + str(scenario.location.line)
                                )
                            else:
                                tag.set_link(
                                    project_url_base
                                    + scenario.location.filename
                                    + "#L"
                                    + str(tag.behave_tag.line)
                                )

                    # Iterate once over all steps to make links to its location.
                    for step in scenario.steps:
                        # Iterate over it only in case it was not set yet and the location exists.
                        if not step.location_link and step.location:
                            # Split the location to file_name and line number so we can shape it.
                            file_name, line = step.location.split(":", 2)
                            # Handling for NMci project.
                            if file_name.startswith("NMci"):
                                url = nmci_url_base + file_name.replace("NMci/", "", 1)
                            # Handling for qecore project.
                            elif "/site-packages/qecore/" in file_name:
                                url = (
                                    qecore_url_base
                                    + file_name.split("/site-packages/qecore/")[-1]
                                )
                            # Handling for all other projects.
                            else:
                                url = project_url_base + file_name

                            # Set the actual link so formatter can use it.
                            step.location_link = url + "#L" + line

    @property
    def project_git_url(self):
        remote = getattr(self, "_project_git_url", None)
        if remote is None:
            remote, return_code, _ = run(
                "sudo git config --get remote.origin.url", verbose=True
            )
            remote = remote.strip("\n")[:-4]

            if return_code != 0:
                remote = False

            elif remote.startswith("git@"):
                remote = remote.replace(":", "/").replace("git@", "https://")

            self._project_git_url = remote

        log.info(f"The project_git_url property is returning '{str(remote)}'")
        return remote

    @property
    def project_git_commit(self):
        commit = getattr(self, "_project_git_commit", None)
        if commit is None:
            commit, return_code, _ = run("sudo git rev-parse HEAD", verbose=True)
            commit = commit.strip("\n")

            if return_code != 0:
                commit = False

            self._project_git_commit = commit

        log.info(f"The project_git_commit property is returning '{str(commit)}'")
        return commit

    def _wait_for_video_encoding(self, file_name):
        """
        Wait until the video is fully encoded.
        This is verified by video's changing size.
        Once the file is encoded the size will not change anymore.

        :type file_name: str
        :param file_name: Video location for size verification.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`attach_video_to_report`.

        This fixes some issues with the video and most of the time the video will
        get passed with all data, in the testing this took between 2-5 seconds.
        But there still are situations when the encoding is not made in the trivial amount of time
        mostly on slower machines. Currently the hard cutoff is 60 seconds after that the wait will
        terminate and the video will get passed as is to the html report.

        This time loss is no issue with few failing tests and has huge advantage of
        having an entire video with all controling elements (sometimes the video cannot be moved
        to the middle, or does not have data abouts its length). With many failing tests this might
        add significant time to the testing time. To prevent waiting for the encoded video
        and therefore not waiting at all use::

            <qecore.sandbox.TestSandbox>.wait_for_stable_video = False
        """

        log.info(f"_wait_for_video_encoding(self, file_name={file_name})")

        current_size = 0
        current_stability = 0

        iteration_cutoff = 0

        while current_stability < 30:
            new_size = os.path.getsize(file_name)
            if current_size == new_size:
                current_stability += 1
            else:
                current_stability = 0

            current_size = new_size
            sleep(0.1)

            iteration_cutoff += 1
            if iteration_cutoff > 600:
                break

        log.info(f"The stability counter: '{current_stability}")
        log.info(f"The iteration cutoff: '{iteration_cutoff}')")

    def set_background(
        self, color=None, background_image=None, background_image_revert=False
    ):
        """
        Change background to a single color or an image.

        :type color: str
        :param color: String black/white to set as background color.

        :type background_image: str
        :param background_image: Image location to be set as background.

        :type background_image_revert: bool
        :param background_image_revert: Upon settings this attribute to True,
            the :func:`after_scenario` will return the background to the original state,
            after the test.

        To get the wanted color you can pass strings as follows::

            color="black"
            color="white"
            color="#FFFFFF" # or any other color represented by hexadecimal
        """

        log.info(
            "".join(
                (
                    f"set_background(self, color={color}, ",
                    f"background_image={background_image}).",
                )
            )
        )

        self.background_image_revert = background_image_revert

        if self.background_image_revert:
            self.background_image_location = run(
                "gsettings get org.gnome.desktop.background picture-uri"
            ).strip("\n")

        if background_image:
            if "file://" in background_image:
                run(
                    f"gsettings set org.gnome.desktop.background picture-uri {background_image}"
                )
            else:
                run(
                    f"gsettings set org.gnome.desktop.background picture-uri file://{background_image}"
                )
        elif color == "white":
            run("gsettings set org.gnome.desktop.background picture-uri file://")
            run('gsettings set org.gnome.desktop.background primary-color "#FFFFFF"')
            run('gsettings set org.gnome.desktop.background secondary-color "#FFFFFF"')
            run('gsettings set org.gnome.desktop.background color-shading-type "solid"')
        elif color == "black":
            run("gsettings set org.gnome.desktop.background picture-uri file://")
            run('gsettings set org.gnome.desktop.background primary-color "#000000"')
            run('gsettings set org.gnome.desktop.background secondary-color "#000000"')
            run('gsettings set org.gnome.desktop.background color-shading-type "solid"')
        elif "#" in color:
            run("gsettings set org.gnome.desktop.background picture-uri file://")
            run(f"gsettings set org.gnome.desktop.background primary-color '{color}'")
            run(f"gsettings set org.gnome.desktop.background secondary-color '{color}'")
            run('gsettings set org.gnome.desktop.background color-shading-type "solid"')
        else:
            log.info(
                " ".join(
                    (
                        f"Color '{color}' is not defined.",
                        "You can define one yourself and submit merge request.",
                    )
                )
            )

    def _revert_background_image(self):
        """
        Revert background image to the before-test state.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`after_scenario`.
        """

        log.info("_revert_background_image(self)")

        run(
            " ".join(
                (
                    "gsettings",
                    "set",
                    "org.gnome.desktop.background",
                    "picture-uri",
                    self.background_image_location,
                )
            )
        )

    def file_loader(self, file_name):
        """
        Load content from file or upon UnicodeDecodeError debug the location of the error and return replaced data.

        :type file_name: str
        :param file_name: String representation of file location.

        :return: File data or some debug data and file content replaced in places that were not readable.
        :rtype: str
        """

        log.info(f"file_loader(self, file_name={file_name})")

        _file_data = ""
        if not os.path.isfile(file_name):
            log.info("file_loader: File does not exist.")

            return "File does not exist."

        log.info("file_loader: File exists, continuing to read.")

        try:
            _file_data = open(file_name, "r").read()
            log.info("file_loader: File read is successful.")

        except UnicodeDecodeError as error:
            log.info("file_loader: File read is NOT successful.")

            # Gather all lines that contain non-ASCII characters.
            _file = open(file_name, "rb")
            non_ascii_lines = [
                line for line in _file if any(_byte > 127 for _byte in line)
            ]
            _file.close()

            # Attempt to load the file and replace all error data.
            file_content = open(
                file_name, "r", encoding="utf-8", errors="replace"
            ).read()

            _file_data = f"\nException detected:\n{error}"
            _file_data += (
                f"\nDetected non-ASCII lines:\n{non_ascii_lines}"
                if any(non_ascii_lines)
                else "None"
            )
            _file_data += f"\nReplaced file content:\n{file_content}"

        log.info("file_loader: return _file_data.")

        return _file_data
