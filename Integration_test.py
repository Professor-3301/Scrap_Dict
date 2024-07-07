import unittest,os,contextlib
from flask import Flask
from app import app

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    def test_scrape_hyperlinks(self):
        response = self.app.post('/scrape', data=dict(url='https://cek.ac.in/', scraping_option='link-scraping'))
        print(response.headers)


    def test_directory_enumeration(self):
        response = self.app.post('/directory', data=dict(url='https://cek.ac.in/', enumerate='on'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'directory', response.data)

if __name__ == '__main__':
    with open(os.devnull, 'w') as f:
        with contextlib.redirect_stdout(f):
            unittest.main(argv=[''], exit=False)
