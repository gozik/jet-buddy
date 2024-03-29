import os
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

from app import app, db
from app.models import Transaction
from app.forms import TransactionForm

def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt', 'csv', 'xlsx'])
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    form = TransactionForm()
    if form.validate_on_submit():
        if Transaction.query.filter_by(payment_value=form.value.data, 
                payment_date=form.date.data, 
                category=form.category.data).first():
            flash('Transaction has been added earlier.')
        else:
            trn = Transaction(payment_value=form.value.data, 
                payment_date=form.date.data, 
                category=form.category.data)
            db.session.add(trn)
            db.session.commit()
        return redirect(url_for('transactions'))
    return render_template('transactions.html', transactions=Transaction.query.all(), form=form)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            Transaction.from_csv_tinkoff(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('transactions'))
    return render_template('upload.html', files=os.listdir('uploads'))
