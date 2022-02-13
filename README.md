# Twitter Bot CLI

- [Twitter Bot CLI](#twitter-bot-cli)
  - [Overview](#overview)
  - [Installation](#installation)
    - [1. Install from github](#1-install-from-github)
    - [2. PyPI](#2-pypi)
  - [Getting started](#getting-started)
    - [1. Setting Config file](#1-setting-config-file)
    - [2. Send tweet](#2-send-tweet)
  - [ROADMAP](#roadmap)


## Overview

`tbc` is developer friendly twitter bot runner.


## Installation

### 1. Install from github

install latest pip package from github

**ssh mode**

```bash
# ssh
pip install git+ssh://git@github.com/sota0121/twitter-bot-cli
```

**https mode**

```bash
# https
pip install git+https://github.com/sota0121/twitter-bot-cli
```

if want to install specific version (See: [Releases](https://github.com/sota0121/twitter-bot-cli/releases))

```bash
pip install git+ssh://git@github.com/sota0121/twitter-bot-cli@v0.4.0
```

**check if successfully installed**

```bash
tbc --help
```

### 2. PyPI

(Comming soon ...)


## Getting started

### 1. Setting Config file

Create `.tbcconfig.yml`

See: [Twitter Authentication for Developer](https://developer.twitter.com/ja/docs/basics/authentication/overview)

```yaml
version: "1"

twitter:
  consumer_key: "Twitter api consumer key"
  consumer_secret: "Twitter api consumer secret"
  access_token: "Twitter api access token"
  access_secret: "Twitter api access secret"

source:
  # local, gcs, gspread
  type: "local"

  # for local
  local_path: "src/data/tweets-tbl.csv"

  # for gcs (future support)
  gcs_path: "path/to/cloud/storage/table.csv"

  # for gspread (future support)
  gspread_path: "path/to/spreadsheet/table"

```


### 2. Send tweet

```bash
tbc bot send -m "Hello Twitter!"

# output
Welcome to tbc !!!
bot sub command !!!
load : .tbcconfig.yml
successfully tweeted
```


## ROADMAP

See: [ROADMAP.md](docs/ROADMAP.md)
