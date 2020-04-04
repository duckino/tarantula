clean:
	rm -rf ./out/*
	rm -rf ./logs/*

pipenv:
	pip3 install pipenv
	pipenv install -dev