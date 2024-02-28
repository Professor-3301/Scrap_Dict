# scrape_functions.py
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor

def scrape_html(url):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract information based on the website's HTML structure
            # For example: titles = soup.find_all('h2')

            # Process and print or store the extracted data
            return soup.prettify()

        else:
            return f'Failed to retrieve the webpage. Status code: {response.status_code}'

    except Exception as e:
        return f'An error occurred: {str(e)}'




def download_image(url, folder='images'):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Create a folder if it doesn't exist
            if not os.path.exists(folder):
                os.makedirs(folder)

            # Get the file name from the URL
            file_name = os.path.join(folder, os.path.basename(urlparse(url).path))

            # Save the image file
            with open(file_name, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)

            print(f"Image downloaded: {file_name}")

        else:
            print(f"Failed to download image from {url}. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred while downloading image from {url}: {str(e)}")

def scrape_images(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all image tags
            img_tags = soup.find_all('img')

            # Create a ThreadPoolExecutor with a specified number of threads
            with ThreadPoolExecutor(max_workers=5) as executor:
                # Use threads to download images concurrently
                executor.map(download_image, [urljoin(url, img['src']) for img in img_tags])

        else:
            print('Failed to retrieve the webpage. Status code:', response.status_code)

    except Exception as e:
        print('An error occurred:', str(e))



def scrape_metadata(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extracting metadata
            title = soup.find('title').text if soup.find('title') else "Title not found"
            
            description_tag = soup.find('meta', attrs={'name': 'description'})
            description = description_tag['content'] if description_tag else "Description not found"

            keywords_tag = soup.find('meta', attrs={'name': 'keywords'})
            keywords = keywords_tag['content'] if keywords_tag else "Keywords not found"

            # Print or process the extracted metadata
            print("Title:", title)
            print("Description:", description)
            print("Keywords:", keywords)

        else:
            print('Failed to retrieve the webpage. Status code:', response.status_code)

    except Exception as e:
        print('An error occurred:', str(e))



def scrape_hyperlinks(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all anchor tags (a) containing href attribute
            a_tags = soup.find_all('a', href=True)

            # Extract and print the hyperlinks
            result = ''
            for a_tag in a_tags:
                hyperlink = urljoin(url, a_tag['href'])
                print(hyperlink)
                result += hyperlink + '\n'
            return result

        else:
            print('Failed to retrieve the webpage. Status code:', response.status_code)

    except Exception as e:
        print('An error occurred:', str(e))
