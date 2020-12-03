setup:
	pipenv install
	pipenv install -d
install:
	pip install git+https://github.com/moaible/python-pip-library-boilerplate
uninstall:
	pip uninstall library-boilerplate -y
reinstall: uninstall install
lint:
	pipenv run vet
autocorrect:
	pipenv run fmt
test:
	pipenv run test
