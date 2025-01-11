from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb+srv://unexpectedgaming1:e8Zj1Bdn31TcJBkw@cluster0.h33hn.mongodb.net/")
db = client['simpledb']  # Database Name
collection = db['simplecollection']  # Collection Name

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_data():
    # Get data from the form
    name = request.form.get("name")
    email = request.form.get("email")
    
    # Save to MongoDB
    collection.insert_one({"name": name, "email": email})
    
    return jsonify({"message": "Data saved successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
