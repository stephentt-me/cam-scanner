# api-python

A REST API interface interact with user.

## Development

* Dependency Manager: Poetry

```bash
poetry install  # install dependency
poetry shell  # active venv
```

* Secret manager: Make sure your have correction `.env`, from `.env.sample`
* Containerize: Dockerfile supported.
* Protobuf: fetch from monorepo and `make gen-proto`

## Usage

Using `make <command>`

* `run`: Start project (using wsgi)
* `run-dev`: Start project in dev mode (simple Python run)
* `test`: Run test
* `gen-proto`: copy and gen protoc
* `gen-doc`: using `aglio` for render APIDoc into HTML

## API Doc

Using API Blueprint, checkout `documentation/apis`.

Recommend using `aglio` for HTML render.