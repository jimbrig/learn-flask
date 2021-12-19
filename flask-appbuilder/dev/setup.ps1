mkdir .\flask-appbuilder
Set-Location .\flask-appbuilder
python -m venv venv
.\venv\Scripts\activate.ps1
pip install --upgrade pip
pip install Flask Flask-AppBuilder
pip freeze > requirements.txt
Get-Content .\requirements.txt

flask fab create-app --name flaskapp --engine SQLAlchemy