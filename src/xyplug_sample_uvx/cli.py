import json
import sys
import requests
import urllib3


def main(argv: list[str] | None = None) -> int:
    """Reads one JSON line from STDIN, pretty-prints it, then emits a final JSON message."""
    # Demonstrate third-party dependency is installed (print to stdout)
    try:
        print(
            f"Dependency check: requests {requests.__version__} with urllib3 {urllib3.__version__}"
        )
    except Exception:
        # If anything odd happens here, do not impact main behavior
        pass
    # Read a single line from STDIN (no blocking if not piped on many shells)
    line = sys.stdin.readline()
    if line:
        try:
            obj = json.loads(line)
            pretty = json.dumps(obj, indent=2, sort_keys=True)
            print(f"Read JSON from STDIN:\n{pretty}")
        except Exception as err:  # keep behavior simple for demo
            print(f"Error: failed to parse JSON from STDIN: {err}", file=sys.stderr)
    else:
        # No input provided; remain silent on stdout aside from final JSON
        pass

    # Always print final JSON before exit
    print('{ "xy":1, "code":0 }')
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
