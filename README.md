<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://st3.depositphotos.com/10376142/32584/v/950/depositphotos_325841400-stock-illustration-grey-translator-icon-isolated-on.jpg?forcejpeg=true"></a>
</p>

<h3 align="center">CSV Transaltor Frontend</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Django Project to upload CSV and download Translated CSV.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Authors](#authors)


## 🧐 About <a name = "about"></a>

This repository contains a Django project which connects to CSV Translation Backend repository => https://github.com/JodhwaniMadhur/Translator
The frontend is hosted currently on http://ec2-43-205-142-160.ap-south-1.compute.amazonaws.com:8000

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

For getting a local copy of this project, just run ```git clone https://github.com/JodhwaniMadhur/CSV-Translator-Frontend.git ``` in your local machine CMD.

### Prerequisites

What things you need to install the software and how to install them.
This project requires Pyhton 3, Django 2.1 or greater, Viewflow.
Python can be installed from www.python.org
Instuctions to install pip => https://pip.pypa.io/en/stable/installation/ 

Steps to follow(after installing pip):

```
pip3 install django django-viewflow
cd simple-file-upload
export EC2_URL='<backend url>' 
export TRANSLATION_API_PORT_NUMBER='server port number'
#URL shouldn't contain '/' at rhe end and 'http://' at the start

```

### Steps to run the server

```
python3 manage.py migrate
python3 manage.py runserver
#This will start the server in development mode

#To start the server in testing mode change the DEBUG flag in settings.py file to False and then repeat the above 2 steps
```


## 🎈 Usage <a name="usage"></a>

There are 4 routes to this frontend.
-/ : Home route from where other routes are accessible.
-/uploads : Upload CSV file you want to translate
-/download-translated-csv : Requires file name and the language, on button press a file get's downloaded
-/download-previously-translated-csv : Requires file name and the language, on button press a file get's downloaded

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [Django](https://www.djangoproject.com/) - Web Framework
- [AWS EC2](https://aws.amazon.com/ec2/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@JodhwaniMadhur](https://github.com/JodhwaniMadhur) - Idea & Initial work

