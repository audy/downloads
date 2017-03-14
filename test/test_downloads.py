import unittest
import downloads
import os

class DownloadsTest(unittest.TestCase):

    def test_downloads(self):
        out_path = downloads.download('http://i.imgur.com/ij2h06p.png')
        self.assertEqual(os.path.exists(out_path), True)


    def test_downloads_with_out_path(self):
        out_path = downloads.download(
            'http://i.imgur.com/i5pJRxX.jpg',
            out_path='cheezburger.jpg'
        )

        self.assertEqual(os.path.exists('cheezburger.jpg'), True)


    def test_downloads_https(self):
        out_path = downloads.download('https://i.imgur.com/ij2h06p.png', out_path='http-test.png')
        self.assertEqual(os.path.exists(out_path), True)


    def test_downloads_with_progress(self):
        out_path = downloads.download('https://i.imgur.com/ij2h06p.png', progress=True)
        self.assertEqual(os.path.exists(out_path), True)


    def test_strips_parameters(self):
        out_path = downloads.download('https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif?a=b&c=d')
        self.assertEqual(os.path.exists('giphy.gif'), True)
