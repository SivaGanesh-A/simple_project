from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb+srv://unexpectedgaming1:e8Zj1Bdn31TcJBkw@cluster0.h33hn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
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

@app.route('/test-db')
def test_db():
    from pymongo import MongoClient
    try:
        client = MongoClient("<your-connection-string>")
        client.server_info()  # This will raise an exception if the connection fails
        return "Database connected successfully!"
    except Exception as e:
        return f"Error: {str(e)}", 500
