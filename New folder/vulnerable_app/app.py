from flask import Flask, request
import os
import sqlite3

app = Flask(__name__)

API_KEY = "sk_test_123456789_secret_key"

@app.route("/user")
def get_user():
    username = request.args.get("name")
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cursor.execute(query)
    return str(cursor.fetchall())

@app.route("/")
def home():
    name = request.args.get("name", "World")
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
