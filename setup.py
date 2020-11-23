from clint.textui import colored, puts, indent
from PyInquirer import prompt
import time
import os
import platform

op = platform.system()


questions = [
    {
        "type": "input",
        "name": "admin_page_username",
        "message": "Name of user for logging and logging out"
    },
    {
        "type": "password",
        "name": "admin_page_password",
        "message": "* Password for user logging in and out"
    },
    {
        "type": "email",
        "name": "admin_page_email",
        "message": "Email for admin user",
    }
]

puts(colored.blue("Welcome to the setup for the Password Saver Django Project\n"))

if op == "Windows":
    os.system(
        'cd src && python manage.py makemigrations && python manage.py migrate')
elif op == "Linux" or op == "Darwin":
    os.system(
        'cd src && python3 manage.py makemigrations && python manage.py migrate')
else:
    puts(colored.red('Fatal error has happened'))

time.sleep(10)

puts(colored.blue('Nearly done with the setup, it is about 95\\% done'))

puts(colored.yellow(
    "Please if you don't mind fill in this prompts so as to finish the setup"))

anwsers = prompt(questions)

email = anwsers['admin_page_email']
password = anwsers['admin_page_password']
username = anwsers['admin_page_username']

if email == "":
    email = "{}.secret-password-saver-development.localhost".format(username)

os.system(
    'python manage.py createsuperuser --email={} --username={}'.format(email, username))
