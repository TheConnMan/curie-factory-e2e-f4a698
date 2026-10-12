# Remote-daemon contract: no workspace bind mounts; dial published ports at
# DOCKER_PUBLISHED_HOST (default localhost). Every container gets
# curie.fixture.nonce=$(FIXTURE_NONCE).

COMPOSE ?= docker compose
PROJECT ?= unitconv-docker-fixture
PUBLISH_HOST ?= $(if $(DOCKER_PUBLISHED_HOST),$(DOCKER_PUBLISHED_HOST),localhost)
export FIXTURE_PUBLISH ?= 127.0.0.1:18080

.PHONY: container-check

container-check:
	@if ! docker info >/dev/null 2>&1; then \
	  echo "container-check: no Docker daemon reachable (docker info failed). Start a daemon or set DOCKER_HOST." >&2; \
	  exit 1; \
	fi
	@if [ -z "$(FIXTURE_NONCE)" ]; then \
	  echo "container-check: FIXTURE_NONCE is required so containers can be labeled curie.fixture.nonce." >&2; \
	  exit 1; \
	fi
	@$(COMPOSE) -p $(PROJECT) -f compose.yaml down --remove-orphans >/dev/null 2>&1 || true
	$(COMPOSE) -p $(PROJECT) -f compose.yaml build
	$(COMPOSE) -p $(PROJECT) -f compose.yaml up -d web
	$(COMPOSE) -p $(PROJECT) -f compose.yaml run --rm --no-deps beacon
	@port=$$($(COMPOSE) -p $(PROJECT) -f compose.yaml port web 8080 | awk -F: '{print $$NF}'); \
	if [ -z "$$port" ]; then \
	  echo "container-check: web published no port" >&2; exit 1; \
	fi; \
	echo "container-check: dialing http://$(PUBLISH_HOST):$$port"; \
	ok=; \
	for _ in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do \
	  if body=$$(curl -fsS "http://$(PUBLISH_HOST):$$port"); then \
	    printf '%s\n' "$$body"; \
	    printf '%s\n' "$$body" | grep -F "fixture-nonce=$(FIXTURE_NONCE)" >/dev/null; \
	    ok=1; break; \
	  fi; \
	  sleep 0.5; \
	done; \
	if [ "$$ok" != 1 ]; then \
	  echo "container-check: nonce was not served at http://$(PUBLISH_HOST):$$port" >&2; \
	  $(COMPOSE) -p $(PROJECT) -f compose.yaml logs web >&2 || true; \
	  exit 1; \
	fi
	$(COMPOSE) -p $(PROJECT) -f compose.yaml down --remove-orphans
