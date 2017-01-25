#!/usr/bin/env bash
cd ~/web/ask
gunicorn -b 0.0.0.0:8000 ask.wsgi