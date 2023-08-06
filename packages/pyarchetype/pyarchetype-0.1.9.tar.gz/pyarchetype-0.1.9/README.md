# PyArchetype

This project is used to simplify the skeleton creation of python projects

## Installation

pip install pyarchetype

## Syntax

Tool to create the skeleton of a python project

```sh
usage: pyarchetype [-h] [-v] [--create] [--wizard] [--path PATH]
                   [--module MODULE] [--name NAME] [--email EMAIL]
                   [--initial_version INITIAL_VERSION]
                   [--license {MIT,Apache-2.0,GPL-3.0-only,Propietary}]
                   [--force_overwrite] [--create_venv]

Tool to create the skeleton of a python project. Version 0.1.0

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --create              Create skeleton structure of your python project
  --wizard              Define all parameters in wizard mode
  --path PATH           basedir. Default current dir
  --module MODULE       Module name . Default value is app
  --name NAME           Owner. Default value is jordiredondo
  --email EMAIL         Email address. Default value is user@email.com
  --initial_version INITIAL_VERSION
                        Initial Version. Default value is 0.0.1
  --license {MIT,Apache-2.0,GPL-3.0-only,Propietary}
                        license. Default value is MIT
  --force_overwrite     Force overwrite. Default value is false
  --create_venv         Create project virtualenv. Default value is false
```

## Example of execution

At below example we are creating an app under path "myapp". This bootstrapping also creates python .venv

```sh
pyarchetype --create --path myapp --create_venv --name user1 --email user1@email.com --create_venv
INFO:pyarchetype.pyarchetype:all_flags={
    "create": true,
    "wizard": false,
    "path": "myapp",
    "module": "app",
    "name": "user1",
    "email": "user1@email.com",
    "initial_version": "0.0.1",
    "license": "MIT",
    "force_overwrite": false,
    "create_venv": true
}
INFO:pyarchetype.pyarchetype:Creating basedir myapp
INFO:pyarchetype.pyarchetype:Updating file myapp/.vscode/tasks.json
INFO:pyarchetype.pyarchetype:Updating file myapp/.vscode/launch.json
INFO:pyarchetype.pyarchetype:Updating file myapp/.gitignore
INFO:pyarchetype.pyarchetype:Updating file myapp/pyproject.toml
INFO:pyarchetype.pyarchetype:Updating file myapp/LICENSE
INFO:pyarchetype.pyarchetype:Updating file myapp/README.md
INFO:pyarchetype.pyarchetype:Updating file myapp/requests.txt
INFO:pyarchetype.pyarchetype:Updating file myapp/scripts/compile_and_upload.sh
INFO:pyarchetype.pyarchetype:Force filename=myapp/scripts/compile_and_upload.sh chmod=0755 . Only relevant for Unix-like platforms
INFO:pyarchetype.pyarchetype:Updating file myapp/scripts/compile_only.sh
INFO:pyarchetype.pyarchetype:Force filename=myapp/scripts/compile_only.sh chmod=0755 . Only relevant for Unix-like platforms
INFO:pyarchetype.pyarchetype:Updating file myapp/scripts/upload_pypi.sh
INFO:pyarchetype.pyarchetype:Force filename=myapp/scripts/upload_pypi.sh chmod=0755 . Only relevant for Unix-like platforms
INFO:pyarchetype.pyarchetype:Updating file myapp/.pypirc
INFO:pyarchetype.pyarchetype:Force filename=myapp/.pypirc chmod=0600 . Only relevant for Unix-like platforms
INFO:pyarchetype.pyarchetype:Creating folder myapp/tmp
INFO:pyarchetype.pyarchetype:Creating folder myapp/tests
INFO:pyarchetype.pyarchetype:Updating file myapp/src/app/app.py
INFO:pyarchetype.pyarchetype:Updating file myapp/src/app/__init__.py
INFO:pyarchetype.pyarchetype:Updating file myapp/tests/app/test_app.py
```

## Source Code

https://github.com/redcorjo/pyarchetype.git

Version: 2023010702