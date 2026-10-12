Title: Add an inch length unit

Add the length unit `in` (inch) to unitconv. One inch is 0.0254 meters. `python -m unitconv 1 in m` prints `0.0254`. Unknown units still raise `UnknownUnit`. Temperature and length still cannot be mixed.

Acceptance criterion: `make container-check` passes in the sandbox. That target builds this repo on the task Docker daemon (no workspace bind mounts), starts the web and beacon containers with label `curie.fixture.nonce` set to `FIXTURE_NONCE`, prints that nonce, and reads it back from the web port at `DOCKER_PUBLISHED_HOST` (default `localhost`).

Suggested check: `FIXTURE_NONCE=$$(python3 -c 'import uuid; print(uuid.uuid4().hex)') FIXTURE_PUBLISH=127.0.0.1:18080 make container-check`
