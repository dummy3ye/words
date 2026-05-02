# Makefile for Words Harvester
run:
	python src/main.py

test:
	pytest

setup:
	pip install -r requirements.txt
	mkdir -p logs internal dist
