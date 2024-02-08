from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["Scraper"]  # Assuming the database is named "Scraper"
collection = db["rent"]  # Assuming the collection is named "rent"


@app.route("/")
def index():
    try:
        # Retrieve data from MongoDB collection
        data = list(collection.find({}))  # Fetch all documents from the collection
        print("Data retrieved successfully:", data)  # Debug print to check retrieved data

        # Render HTML template and pass the data to it
        return render_template("frontend_webscrapper.html", data=data)
    except Exception as e:
        print("Error retrieving data from MongoDB:", e)  # Debug print for any errors
        return "Error retrieving data from MongoDB"


if __name__ == "__main__":
    app.run(debug=True)
