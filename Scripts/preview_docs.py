#!/usr/bin/env python3

import argparse
import functools
import http.server
import pathlib
import socketserver
import subprocess
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "source"
BUILD_DIR = REPO_ROOT / "build"
HTML_DIR = BUILD_DIR / "html"


def build_docs() -> None:
    subprocess.run(
        ["sphinx-build", "-M", "html", str(SOURCE_DIR), str(BUILD_DIR)],
        cwd=REPO_ROOT,
        check=True,
    )


def serve_docs(port: int, bind: str) -> None:
    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler,
        directory=str(HTML_DIR),
    )

    class ReusableTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    with ReusableTCPServer((bind, port), handler) as httpd:
        print(f"Serving documentation at http://{bind}:{port}/")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build and preview the generated Sphinx documentation over HTTP."
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to serve on. Default: 8000",
    )
    parser.add_argument(
        "--bind",
        default="127.0.0.1",
        help="Address to bind the HTTP server to. Default: 127.0.0.1",
    )
    parser.add_argument(
        "--no-build",
        action="store_true",
        help="Serve build/html as-is without rebuilding first.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.no_build:
        build_docs()

    if not HTML_DIR.exists():
        print(f"HTML output directory does not exist: {HTML_DIR}", file=sys.stderr)
        print("Build the docs first or run without --no-build.", file=sys.stderr)
        return 1

    serve_docs(args.port, args.bind)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
