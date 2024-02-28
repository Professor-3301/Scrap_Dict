from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

            return render_template('result.html', data=scraped_data)

        else:
            return render_template('result.html', error='Failed to retrieve the webpage. Status code: ' + str(response.status_code))

    except Exception as e:
        return render_template('result.html', error='An unexpected error occurred: ' + str(e))

if __name__ == '__main__':
    app.run(debug=True)
