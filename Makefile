SERVICES_DIR := services

install:
	@for f in $(shell ls ${SERVICES_DIR}); do pip install ${SERVICES_DIR}/$${f}; done

install-dev:
	@for f in $(shell ls ${SERVICES_DIR}); do pip install -e ${SERVICES_DIR}/$${f}[dev]; done

test:
	@for f in $(shell ls ${SERVICES_DIR}); do cd ${SERVICES_DIR}/$${f}; pytest; cd ../..; done

lint:
	# lint examples
	flake8 --toml-config $(word 1, $(wildcard $(SERVICES_DIR)/*))/pyproject.toml --black-config $(word 1, $(wildcard $(SERVICES_DIR)/*))/pyproject.toml examples; 
	# lint services
	@for f in $(shell ls ${SERVICES_DIR}); do cd ${SERVICES_DIR}/$${f}; flake8 .; cd ../..; done

