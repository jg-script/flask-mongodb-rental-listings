from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["Scraper"]  # Assuming the database is named "rent_apartment"
collection = db["rent"]  # Assuming the collection is also named "rent_apartment"

page_to_scrape = requests.get("https://www.clasificadosonline.com/UDRentalsListingAdv.asp?RentalsPueblos=%25&Category=%25&Bedrooms=%25&LowPrice=0&HighPrice=9999999999999999&IncPrecio=1&Area=&redirecturl=%2FUDRentalsListingAdvMap%2Easp&BtnSearchListing=Listado&offset=30")
soup = BeautifulSoup(page_to_scrape.content, "html.parser")

titles = soup.find_all("span", class_="link-blue-color")
prices = soup.find_all("span", class_="Tahoma16BrownNound")
locations = soup.find_all("span", style="color: blue !important;")

# Find all tables with the class "tbl-main-photo" and extract the src attribute from the first td tag
image_tables = soup.find_all("table", class_="tbl-main-photo")
images = [table.find("td").find("img")["src"] for table in image_tables]

data = []

for title, price, location, image in zip(titles, prices, locations, images):
    data.append({
        "title": title.text.strip(),
        "price": float(price.text.strip().replace('$', '').replace(',', '')),
        "location": location.text.strip(),
        "image_url": image  # Use the extracted image URL directly
    })

sorted_data = sorted(data, key=lambda x: x["location"])

try:
    # Insert data into MongoDB collection
    result = collection.insert_many(sorted_data)
    print("Data inserted successfully. Inserted IDs:", result.inserted_ids)
except Exception as e:
    print("Error:", e)
