# Flask MongoDB Rental Listings

Flask MongoDB Rental Listings is a web application that aggregates rental property listings from a popular classifieds website and presents them in a user-friendly format. This project provides a practical example of building a web application using Flask for the backend server, MongoDB for database storage, and BeautifulSoup for web scraping.

## Features

- **Web Scraping**: The `scraper.py` script utilizes BeautifulSoup to scrape rental property listings from a specific webpage. It extracts information such as property titles, prices, locations, and image URLs.

- **Database Integration**: Retrieved rental property data is stored in a MongoDB database using the PyMongo library. Each property listing is represented as a document in the MongoDB collection.

- **Dynamic Website**: The Flask application dynamically renders HTML templates to display rental property listings retrieved from the MongoDB database. Users can browse through listings, view property details, and images.

## Usage

### Installation

1. Clone the Repository:
    ```bash
    git clone https://github.com/jg-script/flask-mongodb-rental-listings
    ```

2. Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Scrape Website for Rental Listings

1. Update URL:
    - Open the `scraper.py` script.
    - Replace the URL in the `page_to_scrape` variable with the URL of the website containing rental property listings.

2. Run Scraper:
    ```bash
    python scraper.py
    ```

### Configure MongoDB Connection

1. Update Connection String:
    - Open the `scraper.py` script.
    - Replace `"mongodb://localhost:27017"` with your MongoDB connection string.

### Run the Application

1. Start Flask Server:
    ```bash
    python app.py
    ```

2. Access Website:
    - Open a web browser and navigate to `http://localhost:5000` to view the rental property listings.
