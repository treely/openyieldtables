# Contributing

Thanks for you interest in contributing to `openyieldtables`.

This document is a guideline. Don't worry about getting everything perfect. We
are happy to work with you on your contribution.

[Upvoting existing issues](#upvoting-issues), [reporting new issues](#reporting-issues),
or [giving feedback](#tell-us-about-your-experience) about your experience are
the easiest ways to contribute.

We also accept pull requests for changes to the code and to the documentation.
For more information on how to do this, read our
[developer guide](#development).

If you have any questions, please reach out via any of our support channels on
our [website](https://tree.ly).

## Upvoting Issues

An easy way to contribute is to upvote existing issues that are relevant to
you. This will give us a better idea what is important for you and other users.

Please avoid content-less +1 comments but instead use the emoji reaction to
upvote with a 👍. This allows people to sort issues by reaction and doesn't
spam the maintainers.

## Reporting Issues

Before you report an issue, please search the existing issues to make sure
someone hasn't already reported it. When reporting a new issue, include as much
detail as possible. Please include:

- What you did, what happened, and what you expected to happen
- Steps to reproduce the issue
- Which version of `openyieldtables` you are using
- Logs or stacktraces

## Tell us about your experience

You don't have to create a detailed bug report or request a new feature to make
a valuable contribution. Giving us feedback about your experience with
`openyieldtables` is incredibly valuable as well.
Please get in touch with us to tell us what you like and don't like about it
via our websites: [Tree.ly](https://tree.ly), [FMM](https://www.fmm.at/).

## Development

### Prerequisites

- [Poetry](https://python-poetry.org/docs/#installation)
- Python 3.9+

### Installation

#### Clone the Repository

```bash
git clone git@github.com:treely/openyieldtables.git
cd path/to/openyieldtables
```

#### Install the dependencies

```bash
poetry install
```

### Environment setup

For development, we recommend using an IDE with Poetry support. For managing
different python versions, we recommend using `pyenv`.

Poetry can pick up the local python version from `pyenv` automatically:

```bash
pyenv local 3.9
poetry env use python
```

For activating the virtual environment, use:

```bash
poetry shell
```

### Code quality

To ensure code quality, we use `pytest` for testing. To run the tests, use the
following command:

```bash
poetry run pytest
```

We also use `black` for code formatting, `flake8` for linting and `isort` for
import sorting. You can run these tools separately with:

```bash
poetry run black .
poetry run flake8 .
poetry run isort .
```

However, we recommend using `pre-commit` to run these tools automatically
before each commit. To install the pre-commit hooks, use:

```bash
poetry run pre-commit install
```

To run the pre-commit checks manually, use:

```bash
poetry run pre-commit run --all-files
```

### API

We use `fastapi` for the API. To run the API locally at
[http://127.0.0.1:8000](http://127.0.0.1:8000), use:

```bash
poetry run uvicorn api.main:app --reload
```

#### Run the API using Docker

To run the API using Docker, use:

```bash
docker build . -t openyieldtables
docker run -p 8000:8000 openyieldtables
```

### Documentation

We use `mkdocs` for the documentation. To run the documenation locally at
[http://127.0.0.1:8000](http://127.0.0.1:8000), use:

```bash
poetry run mkdocs serve
```

To build the documentation, use:

```bash
poetry run mkdocs build
```

### Releases (Commit message format)

The repository uses [python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/)
to make automated releases in workflows. `python-semantic-release` uses the
commit messages to determine the consumer impact of changes in the codebase.
Following formalized conventions for commit messages, semantic-release
automatically determines the next semantic version number, generates a
changelog and publishes the release.

The table below shows which commit message gets you which release type when
`python-semantic-release` runs:

| Commit message                                                                                                                                                                                                                    | Release type                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `fix: Handle case when yield_class is a float`                                                                                                                                                                                    | ~~Patch~~ Fix Release                                                                                           |
| `feat: Add a 'title' parameter to the get_yield_table_data function`                                                                                                                                                              | ~~Minor~~ Feature Release                                                                                       |
| `fix: Rename 'diameter' to 'dbh' in the YieldTable model`<br><br>`BREAKING CHANGE: The 'diameter' field has been replaced with 'dbh'.`<br>`It's not possible anymore to reference the 'diameter' field in a YieldTable instance.` | ~~Major~~ Breaking Release <br /> (Note that the `BREAKING CHANGE: ` token must be in the footer of the commit) |

For more information on the commit message format, see this guideline: https://gist.github.com/brianclements/841ea7bffdb01346392c#file-commit-formatting-md
