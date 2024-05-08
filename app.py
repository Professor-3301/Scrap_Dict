from flask import Flask, render_template, request, jsonify ,send_file
import requests
from bs4 import BeautifulSoup
from Tool.Directory_Enumeration.dirb import dirb_enum
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

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/contacttest")
def contacttest():
    return render_template('contacttest.html')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route('/directory' , methods=['GET','POST']) 
def directory():
    if request.method == 'POST':
        url = request.form['url']
        directories_list = dirb_enum(url,200)
        return render_template('result_dirb.html', data=directories_list)
    elif request.method == 'GET':
        return render_template('directory.html')



@app.route('/scrape', methods=['GET','POST'])
def scrape():
    if request.method == 'POST':
        if request.method == 'POST':
        # Get the form data
            url = request.form['url']
            scraping_option = request.form['scraping-option']

        # Perform scraping logic based on the selected option
            if scraping_option == 'image-scraping':
                scrape_images(url)
                return send_file('./images.zip', as_attachment=True)
            elif scraping_option == 'link-scraping':
                scraped_data = scrape_hyperlinks(url)
                return render_template('result.html', data=scraped_data)
        # Render the result template with scraped data
            
    elif request.method == 'GET':
        return render_template('scrape.html')
    


if __name__ == '__main__':
    app.run(debug=True)

