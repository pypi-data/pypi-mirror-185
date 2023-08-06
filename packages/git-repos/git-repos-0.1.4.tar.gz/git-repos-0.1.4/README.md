# Git repos

[![PyPI version](https://badge.fury.io/py/git-repos.svg)](https://badge.fury.io/py/git-repos)
[![Unstable package](https://img.shields.io/badge/_Unstable_package_-_This_code_is_a_work_in_progress_-red)](https://semver.org)


Manages git repos inside a directory.


## Install

    pip install git-repos


## Usage

Inside a directory with several git repos run:

    repos

To check all available commands:

```
$ repos help
NAME
    repos —  Manages your git repos

USAGE
    repos                       # Lists all repos in text format
    repos export --json         # Exports all repos as json
    repos export --yaml         # Exports all repos as yaml
    repos show REPO             # Saves configured repos
    repos save                  # Saves configured repos
    repos push                  # Pushes to upstream
    repos pull                  # Pulls from upstream
    repos sync                  # Pull from upstream and save
    repos help                  # Shows this help
    repos version               # Prints the current version
```
