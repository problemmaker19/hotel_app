# Deploy instructions

Clone repo:
```
git clone https://github.com/problemmaker19/hotel_app.git
cd hotel_app
```
Create and activate virtual enviroment:
```
python -m venv venv
source venv/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Make .env configs:
```
vi .env
```
Migrate:
```
python manage.py migrate
```
Run application:
```
python manage.py runserver
```
### .env variables
```
#Base
SECRET_KEY=<YOUR_SECRET_KEY>
DEBUG=<BOOL>

#Postgres connection
dbname=<DB_NAME>
user=<DB_USERNAME>
password=<PASSWORD>
host=<HOST>
port=<PORT>
```
### For admin panel access create superuser:
```
python manage.py createsuperuser
```
## API Docs (swagger)
http://localhost/swagger
