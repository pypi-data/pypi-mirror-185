# Development

Applied principles are:
- Test driven development (TDD)
- Open source, community contributions are welcome

## Tools

We use [hatch](https://hatch.pypa.io) as project management tool.
Environments and scripts are in the file `pyproject.toml`.

Some usefull commands:
- `hatch run cov` or `hatch run pytest` to run tests
- `hatch lint:fmt` to apply black and isort
- `hatch lint:all` to check linting, typing, style and security
- `hatch jupyter:lab` to open a jupyter lab instance

## Release Process

See https://packaging.python.org/en/latest/tutorials/packaging-projects/,
https://hatch.pypa.io/latest/build/ and https://hatch.pypa.io/latest/publish/.

- Set the `version` in `__about__.py`.
- Run `hatch build`.
-
