"""Run unitconv tests, print the fixture nonce, then serve it on port 8080."""

from __future__ import annotations

import os
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

NONCE = os.environ["FIXTURE_NONCE"]


def main() -> None:
    print(f"fixture-nonce={NONCE}", flush=True)
    suite = unittest.defaultTestLoader.discover("unitconv/tests")
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)

    body = f"fixture-nonce={NONCE}\n".encode()

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, fmt: str, *args: object) -> None:
            print(fmt % args, flush=True)

    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()


if __name__ == "__main__":
    main()
