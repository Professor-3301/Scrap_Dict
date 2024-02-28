# main.py
from Switch import *
from scrape_functions import *
from Logo import *



print_colorful_logo()
url_to_scrape = 'http://www.cek.ac.in'


result = select_scraping_option(url_to_scrape)


