import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import concurrent.futures

def get_links(url, domain_links):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract all links from the page
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            # Make links absolute using urljoin
            absolute_links = [urljoin(url, link) for link in links]
            # Filter out only the links belonging to the same domain
            parsed_url = urlparse(url)
            same_domain_links = [link for link in absolute_links if urlparse(link).netloc == parsed_url.netloc]
            # Remove duplicate links
            same_domain_links = list(set(same_domain_links))
            # Append the filtered links to the domain_links list
            domain_links.extend(same_domain_links)
        else:
            print(f"Failed to retrieve webpage. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
domain_links = []
url_to_scrape = 'https://www.ceconline.edu'
get_links(url_to_scrape, domain_links)

def download_image(url, folder):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            if not os.path.exists(folder):
                os.makedirs(folder)

            file_name = os.path.basename(urlparse(url).path)
            file_path = os.path.join(folder, file_name)
            if not os.path.exists(file_path):  # Check if file already exists
                with open(file_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                print(f"Image downloaded: {file_path}")
            else:
                print(f"Image already exists: {file_path}")
        else:
            print(f"Failed to download image from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while downloading image from {url}: {str(e)}")


def scrape_images_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tags = soup.find_all('img')
            for img_tag in img_tags:
                img_url = urljoin(url, img_tag['src'])
                folder = os.path.join('images', urlparse(url).netloc)
                download_image(img_url, folder)
        else:
            print(f"Failed to retrieve webpage {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while scraping images from {url}: {str(e)}")

def scrape_images_from_domain(domain_links):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(scrape_images_from_url, domain_links)

# Example usage: Scraping images from all sites in the domain_links array
scrape_images_from_domain(domain_links)
