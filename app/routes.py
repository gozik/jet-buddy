import os
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from app import app
from app.models import Transaction

def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt', 'csv', 'xlsx'])
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=filename))
    return render_template('index.html')

@app.route('/transactions')
def transactions():
    return render_template('transactions.html', transactions=Transaction.query.all())