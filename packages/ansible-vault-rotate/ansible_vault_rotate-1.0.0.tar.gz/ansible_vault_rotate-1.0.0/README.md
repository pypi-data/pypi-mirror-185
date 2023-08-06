python-ansible-vault-rotate
===
[![GitHub License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](https://github.com/trustedshops-public/spring-boot-starter-keycloak-path-based-resolver/blob/main/LICENSE)
[![pre-commit](https://img.shields.io/badge/%E2%9A%93%20%20pre--commit-enabled-success)](https://pre-commit.com/)
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/trustedshops-public/python-ansible-vault-rotate/tree/main.svg?style=shield&circle-token=9c1ea1cc46c804b46f457772637c8481717b511a)](https://dl.circleci.com/status-badge/redirect/gh/trustedshops-public/python-ansible-vault-rotate/tree/main)
[![codecov](https://codecov.io/gh/trustedshops-public/python-ansible-vault-rotate/branch/main/graph/badge.svg?token=6PJ1GJzIcB)](https://codecov.io/gh/trustedshops-public/python-ansible-vault-rotate)

Advanced Python CLI to rotate the secret used for ansible vault inline secrets and files in a project

## Features

- Reencrypt vault files
- Reencrypt inline vaulted secrets

## Installation

It is strongly recommended to use pipx instead of pip if possible:

```sh
pipx install ansible-vault-rotate
```

Otherwise you can also use plain pip, but be warned that this might
collide with your ansible installation globally!

```sh
pip install ansible-vault-rotate
```

## Usage

### Rekey given vault secret with new secret specified on CLI

```sh
ansible-vault-rotate --old-vault-secret-source file://my-vault-password --new-vault-secret-source my-new-secret
```

## Rekey only specific files (e.g. when using multiple keys per stage)

```sh
ansible-vault-rotate --old-vault-secret-source file://my-vault-password-<stage> --new-vault-secret-source my-new-secret --file-glob-pattern group_vars/<stage>/*.yml
```

## Getting help about all args

```sh
ansible-vault-rotate --help
```

## Development

For development, you will need:

- Python 3.9 or greater
- Poetry

### Install

```
poetry install
```

### Run tests

```
poetry run pytest
```
