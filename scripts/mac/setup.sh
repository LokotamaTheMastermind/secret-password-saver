username = id -un

cd ../../ && python3 src/manage.py makemigrations contacts && python3 src/manage.py migrate
python3 src/manage.py createsuperuser --username $username --email $username@discord-friends.localhost
cd scripts/mac && startup.sh
