cd ../../ && python src/manage.py makemigrations contacts && python src/manage.py migrate
python src/manage.py createsuperuser --username %username% --email %username%@discord-friends.localhost
cd scripts/windows && startup.bat