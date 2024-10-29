SERVICES_DIR := services

install:
	@for f in $(shell ls ${SERVICES_DIR}); do pip install ${SERVICES_DIR}/$${f}; done

install-dev:
	@for f in $(shell ls ${SERVICES_DIR}); do pip install -e ${SERVICES_DIR}/$${f};poetry install -C ${SERVICES_DIR}/$${f} --only dev --no-root; done

test:
	@for f in $(shell ls ${SERVICES_DIR}); do  set -e; cd ${SERVICES_DIR}/$${f}; sh -c 'pytest || ([ $$? = 5 ] && exit 0 || exit $$?)'; cd ../..; done

lint:
	# lint examples
	flake8 --toml-config $(word 1, $(wildcard $(SERVICES_DIR)/*))/pyproject.toml --black-config $(word 1, $(wildcard $(SERVICES_DIR)/*))/pyproject.toml examples; 
	# lint services
	@for f in $(shell ls ${SERVICES_DIR}); do set -e; cd ${SERVICES_DIR}/$${f};flake8 .; cd ../..; done