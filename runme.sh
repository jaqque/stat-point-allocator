#!/bin/sh

export FLASK_APP=thingy.py
exec flask run --host=0.0.0.0
