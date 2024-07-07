# ScrapDict

ScrapDict is a powerful web scraping and directory enumeration tool designed to simplify web data extraction. Built with Flask, it utilizes BeautifulSoup for web scraping and Dirb for directory enumeration, providing users with a comprehensive and efficient solution.

## Features

- **Web Scraping**: Extract data from websites efficiently.
- **Directory Enumeration**: Discover hidden directories on web servers.
- **User-Friendly Interface**: Simple and intuitive web interface for easy interaction.

## Installation

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Setup

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/scrapdict.git
    cd scrapdict
    ```

2. **Create a virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application**

    ```bash
    python app.py
    ```

5. **Access the application**

    Open your web browser and navigate to `http://127.0.0.1:5000`

## Usage

1. **Enter the URL**: Provide the URL of the website you want to scrape or enumerate.
2. **Select Scraping Option**: Choose between image scraping and hyperlink scraping.
3. **Start Scraping**: Click the button to start the scraping process.
4. **View Results**: Download the scraped images or view the extracted links on the result page.

## Project Structure

```plaintext
scrapdict/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── result.html
│   │   └── scrape.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   ├── scrape/
│   │   ├── __init__.py
│   │   ├── scraper.py
│   │   └── utils.py
│   ├── forms.py
│   └── models.py
├── images/
├── tests/
│   ├── __init__.py
│   ├── test_scraper.py
│   └── test_routes.py
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
