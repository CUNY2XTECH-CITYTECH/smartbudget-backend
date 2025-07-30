from db_setup import db
from datetime import datetime

# 1. Users Table
class User(db.Model):
    __tablename__ = 'users'
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100), nullable=False)

# 2. Transactions Table
class Transaction(db.Model):
    __tablename__ = 'transactions'
    transactionID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'))
    type = db.Column(db.String(10))  # 'income' or 'expense'
    category = db.Column(db.String(50))
    amount = db.Column(db.Float)
    date = db.Column(db.Date)

# 3. Budgets Table
class Budget(db.Model):
    __tablename__ = 'budgets'
    budgetID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'))
    category = db.Column(db.String(50))
    limitAmount = db.Column(db.Float)

# 4. Stocks Table
class Stock(db.Model):
    __tablename__ = 'stocks'
    stockID = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10))
    companyName = db.Column(db.String(100))
    currentPrice = db.Column(db.Float)
    lastUpdated = db.Column(db.Date)

# 5. Threads Table
class Thread(db.Model):
    __tablename__ = 'threads'
    threadID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'))
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# 6. Comments Table
class Comment(db.Model):
    __tablename__ = 'comments'
    commentID = db.Column(db.Integer, primary_key=True)
    threadID = db.Column(db.Integer, db.ForeignKey('threads.threadID'))
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# 7. Expenses Table
class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    amount = db.Column(db.Float)
    category = db.Column(db.String(100))
    date = db.Column(db.Date)