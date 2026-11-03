from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright
import pytest_html
from config import BASE_URL


@pytest.fixture(scope="function")
def page(request):
    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)

    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(videos_dir),
    )
    page = context.new_page()

    page.goto(BASE_URL)
    page.wait_for_load_state("load")

    request.node._video_path = None
    yield page

    try:
        if page.video:
            request.node._video_path = page.video.path()
    except Exception:
        request.node._video_path = None
    finally:
        context.close()
        browser.close()
        p.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = list(getattr(report, "extras", getattr(report, "extra", [])))

    video_path = getattr(item, "_video_path", None)
    if video_path and Path(video_path).exists():
        relative_video_path = Path(video_path).relative_to(Path.cwd())
        video_src = relative_video_path.as_posix()
        extra.append(
            pytest_html.extras.html(
                f"""
                <div style="margin-top: 12px;">
                    <h3>Recorded Session</h3>
                    <video width="640" controls>
                        <source src="{video_src}" type="video/webm">
                    </video>
                </div>
                """
            )
        )

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_name = screenshots_dir / f"{item.name}.png"
            page.screenshot(path=str(file_name))
            extra.append(pytest_html.extras.image(str(file_name)))

    report.extras = extra
    if hasattr(report, "extra"):
        report.extra = extra