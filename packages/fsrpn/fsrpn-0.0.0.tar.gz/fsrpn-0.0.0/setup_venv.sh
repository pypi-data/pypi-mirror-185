#!/usr/bin/env bash
set -e

if [ ! -d venv ]; then
	python -m venv venv
fi
. venv/Scripts/activate
pip install -r requirements.txt
