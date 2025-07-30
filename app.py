from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from db_setup import db
from models import User, Transaction, Expense, Thread, Comment  # etc.
import pandas as pd
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budget.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Home page
@app.route("/")
def home_page():
    return render_template('index.html')

# Route to upload a CSV file
@app.route('/upload', methods=['POST'])
def upload_csv():
    file = request.files['file']
    if not file or not file.filename.endswith('.csv'):
        return "Invalid file", 400

    # Convert CSV to pandas DataFrame
    df = pd.read_csv(file)
    records = df.to_dict(orient='records')

    # Loop through rows and save to database
    for _, row in df.iterrows():
        new_expense = Expense(
            description=row.get('description'),
            amount=float(row.get('amount', 0)),
            category=row.get('category'),
            date=pd.to_datetime(row.get('date')).date()  # safe date conversion

        )
        db.session.add(new_expense)

    db.session.commit()
    return render_template('index.html', records=records)

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
