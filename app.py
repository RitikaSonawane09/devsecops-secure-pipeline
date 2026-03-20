from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def home():
    return "Welcome to DevSecOps Demo"

#Vulnerability endpoint(for testing)
@app.route("/user")
def user():
    name = request.args.get("name")
    query = "SELECT * FROM users WHERE name = '%s' "%name
    return f"Query: {query}"

#Harcoded Secret
API_KEY = "12345-SECRET-KEY"

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=5000)