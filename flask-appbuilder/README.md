# Flask App with Flask-AppBuilder (FAB)

## Contents
- [Flask App with Flask-AppBuilder (FAB)](#flask-app-with-flask-appbuilder-fab)
  - [Contents](#contents)
  - [Run](#run)
  - [Login](#login)
  - [Code](#code)
    - [Setup](#setup)
    - [Create Admin User](#create-admin-user)

## Run

```bash
flask run
```

## Login

Username: `admin` | Password: `p`

## Code

### Setup

- PowerShell: [setup.ps1](dev/setup.ps1):

```powershell
# PowerShell

# create directory
mkdir .\flask-appbuilder
Set-Location .\flask-appbuilder

# initialize virtualenv
python -m venv venv
.\venv\Scripts\activate.ps1

# pip installs
pip install --upgrade pip
pip install Flask Flask-AppBuilder
pip freeze > requirements.txt
Get-Content .\requirements.txt

# create app (name: flaskapp; DB Engine: SQLAlchemy):
flask fab create-app --name flaskapp --engine SQLAlchemy
```

- Bash: [setup.sh](dev/setup.sh):

```bash
mkdir ./flask-appbuilder && cd flask-appbuilder
python3 -m venv venv
source ./venv/bin/activate
pip3 install --upgrade pip
pip3 install Flask Flask-AppBuilder
pip3 freeze > requirements.txt
flask fab create-app --name flaskapp --engine SQLAlchemy
```

### Create Admin User

- PowerShell: [create-admin.ps1](dev/create-admin.ps1):

```powershell
# powershell
$env:FLASK_APP = "app"
flask fab create-admin
```

- Bash: [create-admin.sh](dev/create-admin.sh):

```bash
export FLASK_APP=app/__init__.py
flask fab create-admin
```