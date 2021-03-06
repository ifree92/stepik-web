#!/usr/bin/env bash
sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE SCHEMA test_db"
sudo unlink /etc/nginx/sites-enabled/default
sudo cp nginx.conf /etc/nginx/sites-enabled/nginx.conf
sudo /etc/init.d/nginx restart
mkdir ~/web
cp -r ask ~/web/
#sed -i "s/'PASSWORD': '123'/'PASSWORD': ''/g" ~/web/ask/ask/settings.py
echo "" > ~/web/ask/ask/__init__.py
python ~/web/ask/manage.py syncdb
nano ~/web/ask/ask/settings.py