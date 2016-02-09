
.PHONY: help install clean delpyc assets scss syncf5 tar_data import_db reload react react-watch

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install -- to proceed to a new install of this project. Use clean command before if you want to reset a current install"
	@echo "  clean  -- to clean your local repository from all stuff created by buildout and instance usage"
	@echo "  delpyc  -- to remove all *.pyc files, this is recursive from the current directory"
	@echo
	@echo "  assets -- to minify all assets and collect static files"
	@echo "  scss -- to compile all SCSS stuffs with compass"
	@echo "  react -- to build reactjs form controllers"
	@echo "  react-watch -- to watch for changes on react sources to automatically re-build reactjs form controllers"
	@echo
	@echo "  tar_data             -- to dump applications datas to json files then put them in a tarball"
	@echo "  import_db            -- to import dumped datas, you should empty the database before"
	@echo
	@echo "  reload               -- to reload uwsgi instance (for integration and production only)"
	@echo

delpyc:
	@find . -name "*\.pyc"|xargs rm -f

clean: delpyc
	@rm -Rf bin include eggs lib parts django-apps-src develop-eggs local .installed.cfg

install:
	virtualenv --no-site-packages --setuptools --python python2.7 .
	bin/pip install 'setuptools==19.1'
	bin/pip install 'pip==7.1.2'
	mkdir -p eggs
	bin/python bootstrap.py
	bin/buildout -v

test: delpyc
	@bin/test
