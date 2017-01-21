sudo unlink /etc/nginx/sites-enabled/default
sudo ﻿cp nginx.conf /etc/nginx/sites-enabled/nginx.conf
sudo /etc/init.d/nginx restart
mkdir ~/web
cp myapp.py ~/web/hello.py
cd ~/web
gunicorn -b 0.0.0.0:8080 hello:app