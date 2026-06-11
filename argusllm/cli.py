import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        prog="argusllm",
        description="ArgusLLM — LLM API security layer",
    )
    subparsers = parser.add_subparsers(dest="command")

    # ── serve ──────────────────────────────────────────────────────────────
    serve_parser = subparsers.add_parser("serve", help="Start the ArgusLLM API server")
    serve_parser.add_argument("--host", default="127.0.0.1", help="Bind host (default: 127.0.0.1)")
    serve_parser.add_argument("--port", type=int, default=8000, help="Bind port (default: 8000)")
    serve_parser.add_argument("--reload", action="store_true", help="Enable auto-reload (dev mode)")

    args = parser.parse_args()

    if args.command == "serve":
        _serve(args.host, args.port, args.reload)
    else:
        parser.print_help()
        sys.exit(1)


def _serve(host: str, port: int, reload: bool):
    try:
        import uvicorn
    except ImportError:
        print("uvicorn is required to run the server. Install it with: pip install uvicorn")
        sys.exit(1)

    print(f"ArgusLLM API starting on http://{host}:{port}")
    print(f"Docs available at http://{host}:{port}/docs")
    uvicorn.run(
        "argusllm.server:app",
        host=host,
        port=port,
        reload=reload,
    )


if __name__ == "__main__":
    main()
