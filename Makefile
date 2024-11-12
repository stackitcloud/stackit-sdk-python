SERVICES_DIR := services

install:
	# install core
	pip install core/
	# install services
	@for f in $(shell ls ${SERVICES_DIR}); do pip install ${SERVICES_DIR}/$${f}; done

install-dev:	
	# install services
	@for f in $(shell ls ${SERVICES_DIR}); do set -e;poetry install -C ${SERVICES_DIR}/$${f} --no-root;pip install -e ${SERVICES_DIR}/$${f}; done
	# install core. This needs to be done last or it will get overriden by the dependency installation of the services
	poetry install -C core --no-root; pip install -e core

test:
	# test core
	cd core && poetry install --with dev && pytest
	# test services
	@for f in $(shell ls ${SERVICES_DIR}); do  set -e; cd ${SERVICES_DIR}/$${f}; poetry install --with dev;sh -c 'pytest || ([ $$? = 5 ] && exit 0 || exit $$?)'; cd ../..; done

lint:	
	# lint core
	cd core && poetry install --no-root --only dev &&flake8 . 
	# lint examples. Use configuration from core
	flake8 --toml-config core/pyproject.toml --black-config core/pyproject.toml examples; 
	# lint services
	@for f in $(shell ls ${SERVICES_DIR}); do set -e; cd ${SERVICES_DIR}/$${f};poetry install --no-root --only dev; flake8 .; cd ../..; done

update-dependencies:
	# lock core
	cd core && poetry lock
	# lock services
	@for f in $(shell ls ${SERVICES_DIR}); do set -e; cd ${SERVICES_DIR}/$${f};poetry lock; cd ../..; done