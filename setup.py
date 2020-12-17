from clint.textui import colored, puts
from PyInquirer import prompt
import time
import os
import platform
import webbrowser

op = platform.system()

questions = [
    {
        "type": "input",
        "name": "admin_page_username",
        "message": "Name of user for logging and logging out"
    },
    {
        "type": "input",
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

print()

puts(colored.blue('Nearly done with the setup, it is about 95% done'))

puts(colored.yellow(
    "Please if you don't mind fill in this prompts so as to finish the setup"))

print()

anwsers = prompt(questions)

email = anwsers['admin_page_email']
username = anwsers['admin_page_username']

if email == "":
    email = "{}.secret-password-saver-development@localhost".format(username)

print()

puts(colored.blue('To finish the setup add your password'))
time.sleep(2)

os.system(
    'cd src && python manage.py createsuperuser --email={} --username={}'.format(email, username))

print()

os.system('cls')

puts(colored.green('Done starting server and opening browser'))

webbrowser.open('http://localhost:5000')

os.system('cd src && python manage.py runserver 5000')
