#conftest.py is a special Pytest configuration file.

import pytest  #imports the Pytest library.
from playwright.sync_api import sync_playwright
from pathlib import Path

from config import BASE_URL

#fixture is a pytest mechanism used to provide the setup or resources required by test cases.
@pytest.fixture(scope="session")
def pw_browser():
    # start Playwright and browser once per test session
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    yield {"p": p, "browser": browser}
    try:
        browser.close()
    except Exception:
        pass
    try:
        p.stop()
    except Exception:
        pass


@pytest.fixture(scope="function")
def page(request, pw_browser):
    # create a new context per test to record per-test video while reusing the same browser
    browser = pw_browser["browser"]
    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)

    context = browser.new_context(ignore_https_errors=True, record_video_dir=str(videos_dir))
    page = context.new_page()

    page.goto(BASE_URL)
    page.wait_for_load_state("load")

    yield page

    # teardown: close context (this finalizes and writes the video file)
    try:
        page.close()
    except Exception:
        pass
    try:
        context.close()
    except Exception:
        pass

    # rename the most recent video file produced in videos_dir to a stable name for this test
    try:
        vids = list(videos_dir.glob("*.webm"))
        if vids:
            latest = max(vids, key=lambda p: p.stat().st_mtime)
            stable = videos_dir / f"{request.node.name}.webm"
            try:
                latest.replace(stable)
            except Exception:
                # fallback to rename
                try:
                    latest.rename(stable)
                except Exception:
                    pass
    except Exception:
        pass


def pytest_configure(config):
    # make the html plugin available to hooks via global variable `pytest_html`
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    # run this logic during the teardown phase so context teardown has completed and video file exists
    if report.when == "teardown":
        page = item.funcargs.get("page") if "page" in item.funcargs else None

        # if test failed, capture screenshot
        if report.failed and page:
            try:
                screenshots_dir = Path("screenshots")
                screenshots_dir.mkdir(exist_ok=True)
                file_name = screenshots_dir / f"{item.name}.png"
                page.screenshot(path=str(file_name))
                if 'pytest_html' in globals() and pytest_html:
                    try:
                        extras.append(pytest_html.extras.image(str(file_name)))
                    except Exception:
                        pass
            except Exception:
                pass

        # attach video if available (we rename videos in fixture teardown to {testname}.webm)
        try:
            videos_dir = Path("videos")
            vid_file = videos_dir / f"{item.name}.webm"
            if vid_file.exists():
                if 'pytest_html' in globals() and pytest_html:
                    try:
                        rel_path = vid_file.as_posix()
                        extras.append(pytest_html.extras.html(f'<video controls width="640" src="{rel_path}"></video>'))
                    except Exception:
                        pass
        except Exception:
            pass

        report.extras = extras
