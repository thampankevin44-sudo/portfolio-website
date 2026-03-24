from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # write your mysql password here
    database="portfolio_db"
)

cursor = db.cursor()

# Home page
@app.route('/')
def home():
    return render_template("index.html")

# About page
@app.route('/about')
def about():
    return render_template("about.html")

# Projects page
@app.route('/projects')
def projects():
    return render_template("projects.html")

# Contact page
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        sql = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
        val = (name, email, message)

        cursor.execute(sql, val)
        db.commit()

        return "Message Sent Successfully!"

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)

    