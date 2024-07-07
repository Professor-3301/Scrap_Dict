from flask import Flask, render_template, request, jsonify ,send_file
import requests
from bs4 import BeautifulSoup
from Tool.Directory_Enumeration.dirb import dirb_enum
from Tool.scrape_functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route('/directory' , methods=['GET','POST']) 
def directory():
    
    if request.method == 'POST':
        url = request.form['url']
        enumerate_directories_flag = 'enumerate' in request.form

        if enumerate_directories_flag:
            directories = dirb_enum(url)
            all_scraped_data = []

            for directory in directories:

                scraped_data = scrape_hyperlinks(directory)
                all_scraped_data.append(directory)

                all_scraped_data.append(scraped_data)
                all_scraped_data.append('\n')
            
            
            return render_template('result.html', data=all_scraped_data)
        
        else:
            directories = dirb_enum(url)
            return render_template('result_dirb.html', data=directories)
    
    return render_template('directory.html')


@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    if request.method == 'POST':
        url = request.form['url']
        scraping_option = request.form['scraping-option']
        if scraping_option == 'image-scraping':
            scrape_images(url)
            return send_file('./images.zip', as_attachment=True)
        elif scraping_option == 'link-scraping':
            scraped_data = scrape_hyperlinks(url)
            return render_template('result.html', data=scraped_data)
    
    return render_template('scrape.html')


if __name__ == '__main__':
    app.run(debug=True)