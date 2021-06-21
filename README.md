# Backend Booster - Django + PostgreSQL

This codebase is a Django + PostgreSQL boilerplate. It is intended to be used as a
[Booster](https://github.com/jared-jewitt/booster-guidelines) for my [Launchpad](https://github.com/jared-jewitt/launchpad).
However, that being said, it can still be used completely on its own.

#### Requirements:

- [Docker](https://www.docker.com/)
- [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) - Only for Windows users

#### Features:

- 🐍 Python 3.9
- 🐍 Django 3
- ⚙️ Django Rest Framework 3
- ⬛ Black for consistent code style
- 👀 Lint your code with Pylint
- 🔃 pre-commit for code quality assurance

#### Developers:

- [Jared Jewitt](https://jared-jewitt.github.io/)

---

### 🏃 Getting Started

Run the backend via the command below, then visit the API at `http://localhost:5000`

```
make up
```

### ⌨️ Commands

###### Make

| Command     | Description                                                                   |
| ----------- | ----------------------------------------------------------------------------- |
| `make up`   | Launches the database + server                                                |
| `make down` | Removes the database + server containers                                      |
| `make nuke` | Purges all database + server containers, images, networks, volumes            |
| `make bash` | Shells into the server to run one-off commands. e.g. `python manage.py test`  |

###### Python (use these after running `make bash`)

| Command                            | Description                               |
| ---------------------------------- | ----------------------------------------- |
| `python manage.py test`            | Runs the suite of Django tests            |
| `python -m pylint **/*.py`         | Runs Pylint to check for linting errors   |
| `python -m black **/*.py`          | Runs Black to fix linting errors          |


### 🚀 Deployment

[Instructions here](google-cloud-console/README.md).

### ⚖️ License

Code released under the [MIT License](LICENSE).
