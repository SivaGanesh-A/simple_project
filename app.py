from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb+srv://netaasree:Doreamon%40143@cluster1.gtow5.mongodb.net/DailyDiary?retryWrites=true&w=majority")
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
