setup:
	echo setup
install:
	pip install git+https://github.com/moaible/python-pip-library-boilerplate
uninstall:
	pip uninstall library-boilerplate -y
reinstall: uninstall install
lint:
	mypy boilerplate
autocorrect:
	echo test
