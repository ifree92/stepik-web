#!/usr/bin/env bash
sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE SCHEMA `test_db`"
sudo unlink /etc/nginx/sites-enabled/default
sudo cp nginx.conf /etc/nginx/sites-enabled/nginx.conf
sudo /etc/init.d/nginx restart
mkdir ~/web
cp -r ask ~/web/