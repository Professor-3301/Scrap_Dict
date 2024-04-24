from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from Tool.scrape_functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/webscrap")
def webscrap():
    return render_template('webscrap.html')

# @app.route("/scrapetest")
# def scrape():
#     return render_template('scrape.html')

@app.route("/result")
def result():
    return render_template('result.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/contacttest")
def contacttest():
    return render_template('contacttest.html')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/directory")
def directory():
    return render_template('directory.html')

@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    # try:
    #     url_to_scrape = request.form.get('url')
    #     scraping_option = request.form.get('scraping-options')  # Get the selected scraping option

    #     # Send an HTTP request to the URL
    #     response = requests.get(url_to_scrape)

    #     # Check if the request was successful (status code 200)
    #     if response.status_code == 200:
    #         # Parse the HTML content of the page
    #         soup = BeautifulSoup(response.text, 'html.parser')

    #         # Extract information based on the selected scraping option
    #         if scraping_option == 'image-scraping':
    #             # Scraping logic for images
    #             images = soup.find_all('img')
    #             scraped_data = {'images': [img['src'] for img in images]}

    #         elif scraping_option == 'link-scraping':
    #             # Scraping logic for links
    #             links = soup.find_all('a')
    #             scraped_data = {'links': [link['href'] for link in links]}

    #         return render_template('result.html', data=scraped_data)

    #     else:
    #         return render_template('result.html', error='Failed to retrieve the webpage. Status code: ' + str(response.status_code))

    # except Exception as e:
    #     return render_template('result.html', error='An unexpected error occurred: ' + str(e))
    return render_template('scrape.html')

if __name__ == '__main__':
    app.run(debug=True)
