# python enviroment
virtualenv env
pip install -r requirements.txt

# database migration
flask db init
flask db migrate
flask db upgrade

# run app
flask run
