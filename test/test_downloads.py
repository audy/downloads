import downloads
import os

FILE_URL = "https://raw.githubusercontent.com/audy/downloads/master/readme.md"


def test_downloads(run_in_tmp_path):
    out_path = downloads.download(FILE_URL)
    assert os.path.exists(out_path)


def test_downloads_with_out_path(run_in_tmp_path):
    downloads.download(FILE_URL, out_path="readme.md")

    assert os.path.exists("readme.md")


def test_downloads_https(run_in_tmp_path):
    out_path = downloads.download(FILE_URL, out_path="test.md")
    assert os.path.exists(out_path)


def test_downloads_with_progress(run_in_tmp_path):
    out_path = downloads.download(FILE_URL, progress=True)
    assert os.path.exists(out_path)


def test_downloads_no_tmp_dir(run_in_tmp_path):
    out_path = downloads.download(FILE_URL, progress=True, use_tmp_dir=False)
    assert os.path.exists(out_path)


def test_strips_parameters(run_in_tmp_path):
    downloads.download(f"{FILE_URL}?test=true")
    assert os.path.exists("readme.md")
