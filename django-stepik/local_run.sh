#!/usr/bin/env bash
cd ask
gunicorn -b 0.0.0.0:8000 ask.wsgi