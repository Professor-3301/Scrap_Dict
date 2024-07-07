import unittest
import os,contextlib
from Tool.scrape_functions import scrape_hyperlinks,scrape_images

class TestScrapeFunctions(unittest.TestCase):

    def test_scrape_images(self):
        url = 'https://cek.ac.in/'
        result = scrape_images(url)
        self.assertTrue(os.path.exists('images.zip'))

    def test_scrape_hyperlinks(self):
        url = 'https://cek.ac.in/'
        result = scrape_hyperlinks(url)

if __name__ == '__main__':
    with open(os.devnull, 'w') as f:
        with contextlib.redirect_stdout(f):
            unittest.main(argv=[''], exit=False)
