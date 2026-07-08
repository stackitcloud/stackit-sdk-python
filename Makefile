SERVICES_DIR := services
SERVICES := $(shell ls $(SERVICES_DIR))

INSTALL_TARGETS := $(addprefix install-,$(SERVICES))
INSTALL_DEV_TARGETS := $(addprefix install-dev-,$(SERVICES))
TEST_TARGETS := $(addprefix test-,$(SERVICES))
LINT_TARGETS := $(addprefix lint-,$(SERVICES))
UPDATE_TARGETS := $(addprefix update-dependencies-,$(SERVICES))

.PHONY: install install-core $(INSTALL_TARGETS)
install: install-core $(INSTALL_TARGETS)

install-core:
	uv sync --no-dev --directory core/

$(INSTALL_TARGETS): install-%:
	# install service $*
	uv sync --no-dev --directory $(SERVICES_DIR)/$*

.PHONY: install-dev $(INSTALL_DEV_TARGETS)
install-dev: $(INSTALL_DEV_TARGETS)
	# install core. This needs to be done last or it will get overriden by the dependency installation of the services
	uv sync --frozen --directory core

$(INSTALL_DEV_TARGETS): install-dev-%:
	# install service $*
	uv sync --frozen --directory $(SERVICES_DIR)/$*

.PHONY: test-services test-core $(TEST_TARGETS)
test-services: test-core $(TEST_TARGETS)

test-core:
	cd core && uv run pytest

$(TEST_TARGETS): test-%:
	# test service $*
	cd $(SERVICES_DIR)/$* && sh -c 'uv run pytest || ([ $$? = 5 ] && exit 0 || exit $$?)'

.PHONY: lint-services lint-core lint-examples lint-versions $(LINT_TARGETS)
lint-services: lint-core lint-examples $(LINT_TARGETS) lint-versions

lint-core:
	cd core && uv run flake8 .

lint-examples:
	# lint examples. Use configuration from core
	cd core && uv run flake8 --toml-config pyproject.toml --black-config pyproject.toml ../examples

$(LINT_TARGETS): lint-%:
	# lint service $*
	cd $(SERVICES_DIR)/$* && uv run flake8 .

lint-versions:
	# lint versions
	./scripts/lint-versions.sh

# Old parameterized targets for single service, aliased to pattern rules
test:
	$(MAKE) test-$(service)

lint:
	$(MAKE) lint-$(service)

.PHONY: update-dependencies update-dependencies-core $(UPDATE_TARGETS)
update-dependencies: update-dependencies-core $(UPDATE_TARGETS)

update-dependencies-core:
	cd core && uv lock

$(UPDATE_TARGETS): update-dependencies-%:
	# lock service $*
	cd $(SERVICES_DIR)/$* && uv lock
