import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract all links from the page
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            # Make links absolute using urljoin
            absolute_links = [urljoin(url, link) for link in links]
            return absolute_links
        else:
            print(f"Failed to retrieve webpage. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

def scrape_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract and process content as needed
            content = soup.get_text()
            # print(content)

            # Get links on the current page
            links_on_page = get_links(url)
            #[ print(element) for element in links_on_page ]
            # Crawl each link on the page
            for link in links_on_page:
                # Ensure it's from the same domain
                if urlparse(link).netloc == urlparse(url).netloc:
                    
                    crawl(link, 1)
        else:
            print(f"Failed to retrieve webpage. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def crawl(seed_url, max_depth=1):
    visited_urls = set()

    def _crawl(url, depth):
        if depth > max_depth or url in visited_urls:
            return
        visited_urls.add(url)

        print(f"Scraping: {url}")
        scrape_content(url)

    _crawl(seed_url, 0)

# Example usage
start_url = 'http://www.cek.ac.in'
crawl(start_url)
