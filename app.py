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

@app.route("/scrapetest", methods=['GET'])
def scraptest():
    url_to_scrape = request.form.get('url')
    print(url_to_scrape)

    # try:
    #     global scraped_data = scrape_hyperlinks(url_to_scrape)
        
    #     return scraped_data
    # except Exception as e:
    #     return jsonify({'success': False, 'error': str(e)})
    return render_template('scrapetest.html')




@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/contacttest")
def contacttest():
    return render_template('contacttest.html')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route('/scrape', methods=['POST'])
def scrape_url():
    try:
        url_to_scrape = request.form.get('url')

        # Send an HTTP request to the URL
        response = requests.get(url_to_scrape)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract information based on the website's HTML structure
            # For example: titles = soup.find_all('h2')
            
            # Process and store the extracted data
            scraped_data = {'data': soup.prettify()}

            return render_template('scrape.html', data=scraped_data)

        else:
            return render_template('result.html', error='Failed to retrieve the webpage. Status code: ' + str(response.status_code))

    except Exception as e:
        return render_template('result.html', error='An unexpected error occurred: ' + str(e))

if __name__ == '__main__':
    app.run(debug=True)
