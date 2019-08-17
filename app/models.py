from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username) 


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operation_date = db.Column(db.DateTime) #Дата операции
    payment_date = db.Column(db.DateTime) #Дата платежа
    card_tail = db.Column(db.String(10)) #Номер карты
    status = db.Column(db.String(10)) #Статус
    operation_value = db.Column(db.Float(precision=2)) #Сумма операции
    operation_currency = db.Column(db.String(10)) #Валюта операции
    payment_value = db.Column(db.Float(precision=2)) #Сумма платежа
    payment_currency = db.Column(db.String(10)) #Валюта платежа
    cashback = db.Column(db.Float(precision=2)) #Кэшбэк
    category = db.Column(db.String(30)) #Категория
    MCC = db.Column(db.Integer) #MCC
    description = db.Column(db.String(250)) #Описание
    bonus = db.Column(db.Float(precision=2)) #Бонусы (включая кэшбэк)
