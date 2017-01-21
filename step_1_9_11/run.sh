#!/bin/bash

sudo unlink /etc/nginx/sites-enabled/default
sudo ﻿ln -s nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
gunicorn -b 0.0.0.0:8080 myapp:app