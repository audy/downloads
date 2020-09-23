import downloads
import os


def test_downloads(run_in_tmp_path):
    out_path = downloads.download("http://i.imgur.com/ij2h06p.png")
    assert os.path.exists(out_path) == True


def test_downloads_with_out_path(run_in_tmp_path):
    out_path = downloads.download(
        "http://i.imgur.com/i5pJRxX.jpg", out_path="cheezburger.jpg"
    )

    assert os.path.exists("cheezburger.jpg")


def test_downloads_https(run_in_tmp_path):
    out_path = downloads.download(
        "https://i.imgur.com/ij2h06p.png", out_path="http-test.png"
    )
    assert os.path.exists(out_path)


def test_downloads_with_progress(run_in_tmp_path):
    out_path = downloads.download(
        "https://i.imgur.com/ij2h06p.png", progress=True
    )
    assert os.path.exists(out_path)


def test_strips_parameters(run_in_tmp_path):
    out_path = downloads.download(
        "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif?a=b&c=d"
    )
    assert os.path.exists("giphy.gif")
