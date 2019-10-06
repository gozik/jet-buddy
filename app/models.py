from app import db

from datetime import datetime
import csv

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

    @staticmethod
    def from_csv_tinkoff(file):
        try:
            with open(file, 'r', encoding='windows-1251') as f:
                reader = csv.reader(f, delimiter=';')
                headers = next(reader, None)
                for row in reader:
                    csv_dict = dict(zip(headers, row))
                    transaction = Transaction(**{
                        'operation_date': datetime.strptime(csv_dict["Дата операции"], "%d.%m.%Y %H:%M:%S"),
                        'payment_date': datetime.strptime(csv_dict["Дата платежа"], "%d.%m.%Y").date() if csv_dict["Дата платежа"] else None,
                        'card_tail': csv_dict["Номер карты"],
                        'status': csv_dict["Статус"],
                        'operation_value': float(csv_dict["Сумма операции"].replace(',', '.')),
                        'operation_currency': csv_dict["Валюта операции"],
                        'payment_value': float(csv_dict["Сумма платежа"].replace(',', '.')),
                        'payment_currency': csv_dict["Валюта платежа"],
                        'cashback': float(csv_dict["Кэшбэк"].replace(',', '.')) if csv_dict["Кэшбэк"] else None,
                        'category': csv_dict["Категория"],
                        'MCC': int(csv_dict["MCC"]) if csv_dict["MCC"] else None,
                        'description': csv_dict["Описание"],
                        'bonus': float(csv_dict["Бонусы (включая кэшбэк)"].replace(',', '.')) if csv_dict["Бонусы (включая кэшбэк)"] else None,
                    })
                    db.session.add(transaction)
                db.session.commit()
        except Exception as ex:
            db.session.rollback()
            raise ex

