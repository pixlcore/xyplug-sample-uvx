import json
import sys


def main(argv: list[str] | None = None) -> int:
    """Reads one JSON line from STDIN, pretty-prints it, then emits a final JSON message."""
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
        # No input provided; remain silent per spec aside from final JSON
        pass

    # Always print final JSON before exit
    print('{ "xy":1, "code":0 }')
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
