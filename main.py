from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
all_books = []

class Login(db.Model):
    email = db.Column(db.String(1000), nullable=False, primary_key=True)
    username = db.Column(db.String(1000), nullable=False)
    password = db.Column(db.String(1000), unique=True, nullable=False)


db.create_all()


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new_user = Login(username=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return "new user added"
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = Login.query.filter_by(username=name, password=password).first()
        if user:
            return name
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
