# Jupyterhub-SQLAuthenticator
> Authenticate Jupyterhub with a MySQL user database

## Installation

Run this command to install:

```
pip install sqlauthenticator
```

In your `jupyter_config.py` file, add or modify the following line to set the authentication method:

```
c.JupyterHub.authenticator_class = 'sqlauthenticator.SQLAuthenticator'
```

Additionally, set the following environment variables to point to your MySQL users database:

- `MYSQL_HOST` - MySQL Server hostname
- `MYSQL_PORT` - MySQL Server port
- `MYSQL_DB` - MySQL Database name
- `MYSQL_USER` - MySQL Username
- `MYSQL_PASS` - MySQL Password

## Usage

The database defined in `MYSQL_DB` should have a table called `users` which has columns `username` and `password`.

- `username` should contain the plaintext username to be used by Jupyterhub
- `password` should contain the user password hashed with the [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) hashing scheme.
	