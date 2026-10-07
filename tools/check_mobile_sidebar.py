#!/usr/bin/env python3
"""Exercise the built mobile sidebar in a real 390px Chrome viewport."""

import json
import shutil
import sys
import threading
from contextlib import contextmanager
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, _format, *_args):
        pass


@contextmanager
def serve(directory):
    handler = lambda *args, **kwargs: QuietHandler(
        *args, directory=str(directory), **kwargs
    )
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server.server_port
    finally:
        server.shutdown()
        thread.join()


def read_state(driver):
    return driver.execute_script(
        r"""
        const trigger = document.getElementById('sidebar-trigger');
        const sidebar = document.getElementById('sidebar');
        const primary = [...document.querySelectorAll(
          '#sidebar .nv-sidebar-primary .nav-link'
        )];
        const utilities = [...document.querySelectorAll(
          '#sidebar .nv-sidebar-utilities .nav-link'
        )];
        const rect = trigger.getBoundingClientRect();
        return {
          innerWidth: window.innerWidth,
          innerHeight: window.innerHeight,
          bodyClientWidth: document.body.clientWidth,
          bodyScrollWidth: document.body.scrollWidth,
          bodyOverflowX: getComputedStyle(document.body).overflowX,
          rootOverflowX: getComputedStyle(document.documentElement).overflowX,
          triggerWidth: rect.width,
          triggerHeight: rect.height,
          triggerVisible: getComputedStyle(trigger).display !== 'none',
          expanded: trigger.getAttribute('aria-expanded'),
          controls: trigger.getAttribute('aria-controls'),
          open: document.body.hasAttribute('sidebar-display'),
          focusInSidebar: sidebar.contains(document.activeElement),
          focusIsTrigger: document.activeElement === trigger,
          primaryVisible: primary.filter(
            (item) => item.getBoundingClientRect().height > 0
          ).length,
          primaryLabels: primary.map(
            (item) => (
              item.querySelector('.nv-sidebar-copy strong')?.textContent ||
              item.textContent
            ).trim().split(/\s+/)[0]
          ),
          utilitiesVisible: utilities.filter(
            (item) => item.getBoundingClientRect().height > 0
          ).length,
          mode: document.documentElement.getAttribute('data-mode'),
          background: getComputedStyle(document.body).backgroundColor
        };
        """
    )


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    require((site / "think" / "index.html").exists(), f"missing built THINK page: {site}")

    chrome = next(
        (
            path
            for name in ("google-chrome", "google-chrome-stable", "chromium")
            if (path := shutil.which(name))
        ),
        None,
    )
    require(chrome, "Chrome/Chromium executable not found")

    options = webdriver.ChromeOptions()
    options.binary_location = chrome
    for argument in (
        "--headless=new",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--force-device-scale-factor=1",
        "--window-size=390,844",
    ):
        options.add_argument(argument)

    with serve(site) as port, webdriver.Chrome(options=options) as driver:
        driver.set_window_size(390, 844)
        driver.get(f"http://127.0.0.1:{port}/think/")
        wait = WebDriverWait(driver, 10)
        wait.until(lambda current: current.execute_script("return document.readyState") == "complete")

        initial = read_state(driver)
        require(380 <= initial["innerWidth"] <= 400, f"unexpected viewport: {initial}")
        require(initial["bodyScrollWidth"] <= initial["bodyClientWidth"], f"horizontal overflow: {initial}")
        require(initial["triggerVisible"], f"mobile trigger hidden: {initial}")
        require(initial["triggerWidth"] >= 44 and initial["triggerHeight"] >= 44, f"undersized trigger: {initial}")
        require(initial["primaryVisible"] == 5, f"HOME + four primary links unavailable: {initial}")
        require(
            initial["primaryLabels"] == ["HOME", "THINK", "BUILD", "OBSERVE", "ABOUT"],
            f"primary link order changed: {initial}",
        )
        require(initial["utilitiesVisible"] == 3, f"utility links unavailable: {initial}")
        require(initial["controls"] == "sidebar" and initial["expanded"] == "false", f"trigger semantics wrong: {initial}")

        trigger = driver.find_element(By.ID, "sidebar-trigger")
        trigger.click()
        wait.until(lambda current: read_state(current)["open"])
        opened = read_state(driver)
        require(opened["expanded"] == "true" and opened["focusInSidebar"], f"open focus contract failed: {opened}")
        require(
            opened["bodyOverflowX"] == "hidden" or opened["rootOverflowX"] == "hidden",
            f"open drawer allows horizontal scrolling: {opened}",
        )

        driver.switch_to.active_element.send_keys(Keys.ESCAPE)
        wait.until(lambda current: not read_state(current)["open"])
        escaped = read_state(driver)
        require(escaped["expanded"] == "false" and escaped["focusIsTrigger"], f"Escape close contract failed: {escaped}")

        trigger.click()
        wait.until(lambda current: read_state(current)["open"])
        driver.find_element(By.ID, "mask").click()
        wait.until(lambda current: not read_state(current)["open"])
        masked = read_state(driver)
        require(masked["focusIsTrigger"], f"mask did not restore trigger focus: {masked}")

        trigger.click()
        wait.until(lambda current: read_state(current)["open"])
        before_theme = read_state(driver)
        mode_toggle = driver.find_element(By.ID, "mode-toggle")
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'})", mode_toggle
        )
        wait.until(lambda _current: mode_toggle.is_displayed() and mode_toggle.is_enabled())
        mode_toggle.click()
        wait.until(lambda current: read_state(current)["background"] != before_theme["background"])
        themed = read_state(driver)
        require(
            themed["bodyOverflowX"] == "hidden" or themed["rootOverflowX"] == "hidden",
            f"theme allows horizontal scrolling: {themed}",
        )
        require(themed["primaryVisible"] == 5 and themed["utilitiesVisible"] == 3, f"theme hid navigation: {themed}")

        first_navigation = driver.find_element(
            By.CSS_SELECTOR, "#sidebar .nv-sidebar-primary .nav-link"
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'})", first_navigation
        )
        first_navigation.click()
        wait.until(lambda current: not read_state(current)["open"])
        navigated = read_state(driver)
        require(navigated["expanded"] == "false", f"navigation did not close menu: {navigated}")

        print(json.dumps({
            "initial": initial,
            "opened": opened,
            "escaped": escaped,
            "masked": masked,
            "themed": themed,
            "navigated": navigated,
        }, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
