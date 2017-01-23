#!/usr/bin/env bash
sudo unlink /etc/nginx/sites-enabled/default
sudo cp nginx.conf /etc/nginx/sites-enabled/nginx.conf
sudo /etc/init.d/nginx restart
mkdir ~/web
cp -r ask ~/web/
cd ~/web/ask
gunicorn -b 0.0.0.0:8000 ask.wsgi