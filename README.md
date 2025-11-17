xyplug-sample-uvx
=================

A minimal Hello World package designed to be executed via `uvx` directly from a Git repository (no PyPI required).

Quick start
-----------

1) Tag the repo to match the version in `pyproject.toml` (currently `1.0.0`):

   git tag v1.0.0
   git push origin v1.0.0

2) Run it with uvx (pick one):

   - Inferred entry point (script name equals project name):

     uvx git+https://github.com/<user>/<repo>.git@v1.0.0

   - Explicit entry point using `--from` (more flexible):

     uvx --from git+https://github.com/<user>/<repo>.git@v1.0.0 xyplug-sample-uvx

3) Pass an optional name argument:

   This CLI now reads one JSON line from STDIN and pretty-prints it, then emits a final JSON line:

   echo '{"a":1,"b":[2,3]}' | uvx --from git+https://github.com/<user>/<repo>.git@v1.0.0 xyplug-sample-uvx

   Example output:

   Read JSON from STDIN:
   {
     "a": 1,
     "b": [
       2,
       3
     ]
   }
   { "xy":1, "code":0 }

Expected output
---------------

Hello, world! (from xyplug-sample-uvx)

or, with a name:

Hello, Alice! (from xyplug-sample-uvx)

Implementation notes
--------------------

- The console script name is `xyplug-sample-uvx` and maps to `xyplug_sample_uvx.cli:main` via `[project.scripts]` in `pyproject.toml`.
- The importable Python package uses underscores (`xyplug_sample_uvx`) since hyphens are not valid in module names.
- No third-party dependencies are required; JSON parsing uses Python's standard library.
