from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://unexpectedgaming1:e8Zj1Bdn31TcJBkw@cluster0.h33hn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = MongoClient(MONGO_URI)
db = client['simpledb']  # Database Name
collection = db['simplecollection']  # Collection Name

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_data():
    try:
        # Get data from the form
        name = request.form.get("name")
        email = request.form.get("email")
        if not name or not email:
            return jsonify({"error": "Name and email are required"}), 400
        
        # Save to MongoDB
        collection.insert_one({"name": name, "email": email})
        return jsonify({"message": "Data saved successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/test-db')
def test_db():
    try:
        client.server_info()  # This will raise an exception if the connection fails
        return "Database connected successfully!"
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    # Turn off debug mode for production
    app.run(debug=False)
