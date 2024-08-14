# PetDatabaseQR
Application for creating pet pages so that if they are lost you can contact the owner

## Tech stack
1. Python 3.12.4
2. FastAPI 0.112.0
3. SQLAlchemy 2.0.32
4. python-dotenv 1.0.1
5. MySql

## Run tutorial
1. Create python venv use `python -m venv venv`
2. Activate venv `.\backend\venv\Scripts\activate.bat`
3. Install all requirements `pip install -r .\backend\requirements.txt`
4. Edit .env file in "backend" (inputyour values)
5. run main.py (backend) `uvicorn backend.main:app`
