# Overview

This is an example Python package which can be downloaded and executed by a single `uvx` command.  It is designed to read JSON from STDIN, and output JSON to STDOUT, as part of a bare-bones simple xyOps Event Plugin.  

Here is the Plugin command for this package:

```sh
uvx git+https://github.com/pixlcore/xyplug-sample-uvx.git@v1.0.0
```

Here is an example invocation with some test data piped in:

```sh
echo '{"xy":1,"test":[2,3]}' | uvx git+https://github.com/pixlcore/xyplug-sample-uvx.git@v1.0.0
```

Expected output:

```
Read JSON from STDIN:
{
  "xy": 1,
  "test": [
    2,
    3
  ]
}

{ "xy":1, "code":0 }
```

**Note**: xyOps will ignore and pass through the "pretty-printed" JSON output, and only consume the compact message at the end.

# Instructions

- Make sure you have a properly-formatted `pyproject.toml` file at the root of your repo.
- Create `src/YOUR_PACKAGE_NAME` parent dirs (no dashes allowed).
- Place `__init__.py` and `cli.py` in that directory.
- Tag the repo to match the version in `pyproject.toml` (currently `1.0.0`):

```sh
git tag v1.0.0
git push origin v1.0.0
```

# Implementation notes

- The console script name is `xyplug-sample-uvx` and maps to `xyplug_sample_uvx.cli:main` via `[project.scripts]` in `pyproject.toml`.
- The importable Python package uses underscores (`xyplug_sample_uvx`) since hyphens are not valid in module names.
- No third-party dependencies are required; JSON parsing uses Python's standard library.
