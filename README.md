# Portfolio CV website
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)

This the template for my cv website <a href="https://salehmzh.ir">salehmzh.ir</a>

Its a simple django project and works fine for me on cpanel

It has captcha for admin login page and another captcha for submiting contact form.

It use python 3.8.x and django==3.2.x

Make sure you have python in your machine before installation.

1. To install first you need to clone the repo:

	```sh
	git clone https://github.com/smz6990/Portfolio.git
	```
	or you can download it <a href="https://github.com/smz6990/Portfolio">here</a>
	
2. Next you must change your directory to the project directory:
	```sh
	cd portfolio
	```
3. Now create a virtual environment, for e.g:
	```sh
	python -m venv venv
	```
4. Activate the virtual environment (for windows):
	```sh
	\venv\Scripts\activate
	```
5. Activate the virtual environment (for Unix/MacOs):
	```sh
	/venv/bin/activate
	```
6. Install the requirements packages:
	```sh
	pip install -r requirements.txt
	```
	Note: you need to be in the same directory as requirements.txt
7. Now run makemigratins:
	```sh
	python manage.py makemigrations
	```
8. Now run migrate:
	```sh
	python manage.py migrate
	```
9. Now run the inrenal server in Django:
	```sh
	python manage.py runserver
	```
10. Open your browser and enter 127.0.0.1:8000
and that is it.

Feel free to ask me question

saleh.mohammadzadeh@gmail.com
