SERVICES_DIR := services

install:
	# install core
	uv sync --no-dev --directory core/
	# install services
	@for f in $(shell ls ${SERVICES_DIR}); do uv sync --no-dev --directory ${SERVICES_DIR}/$${f}; done

install-dev:	
	# install services
	@for f in $(shell ls ${SERVICES_DIR}); do set -e;uv sync --directory ${SERVICES_DIR}/$${f}; done
	# install core. This needs to be done last or it will get overriden by the dependency installation of the services
	uv sync --directory core

test-services:
	# test core
	cd core && uv run pytest
	# test services
	@for f in $(shell ls ${SERVICES_DIR}); do  set -e; cd ${SERVICES_DIR}/$${f}; sh -c ' uv run pytest || ([ $$? = 5 ] && exit 0 || exit $$?)'; cd ../..; done

lint-services:
	# lint core
	cd core && uv run flake8 .
	# lint examples. Use configuration from core
	uv run flake8 --toml-config core/pyproject.toml --black-config core/pyproject.toml examples;
	# lint services
	@for f in $(shell ls ${SERVICES_DIR}); do set -e; cd ${SERVICES_DIR}/$${f};uv run flake8 .; cd ../..; done
	# lint versions
	@./scripts/lint-versions.sh

test:
	echo "Testing service ${service}"
	cd ${SERVICES_DIR}/${service}; sh -c ' uv run pytest || ([ $$? = 5 ] && exit 0 || exit $$?)'; cd ../..;

lint:
	echo "Linting service ${service}"
	cd ${SERVICES_DIR}/${service};uv run flake8 .; cd ../..;

update-dependencies:
	# lock core
	cd core && uv lock
	# lock services
	@for f in $(shell ls ${SERVICES_DIR}); do set -e; cd ${SERVICES_DIR}/$${f};uv lock; cd ../..; done
