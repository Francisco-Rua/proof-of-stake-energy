# Proof of stake energy consumption.

![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

## Description

- This repository contains the code to process and plot the measures taken for the Proof of Work discussion paper. There is a group of CSV files that contain the measures taken for the Proof of Stake discussion paper.

## Development

### Clone this repository

```bash
git clone https://github.com/francisco-rua/proof-of-stake-energy.git
```

Navigate to the directory of the cloned repo

```bash
cd proof-of-stake-energy
```

### Set up of the repository

Give execute permission to your script and then run `setup_repo.sh`

- If you are in Mac:

```bash
chmod +x setup_repo.sh
```

Run the set-up.

```bash
./setup_repo.sh
```
- If you are in windows, install and activate the virtual environment:

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

Set up the venv

```bash
pip install -e ".[dev]"
```

## Running scripts locally:

Goes to the file "process_and_plotting.ipynb" on the root of this repository and press on run_all.

- Make sure you have the data folder in the root of this 
repository.

- Make sure you have the virtual environment activated.

- Make sure you have the requirements installed.

- Make sure you have the data folder in the root of this repository.

- Make sure your python is from the virtual environment: You can check this by running `which python` in the terminal. It should be something like `.../venv/bin/python`. If venv is already activated, in the right top corner of your terminal you should see `(venv)`.

## Git Large File Storage (Git LFS)

All files in [`data/`](data/) are stored with `lfs`.

To initialize Git LFS:

```bash
git lfs install
```

```bash
git lfs track data/**/*
```

To pull data files, use

```bash
git lfs pull
```

## Synchronize with the repository

- Always pull the latest code first:

```bash
git pull
```

- Make changes locally, save. And then add, commit and push:

```bash
git add [file-to-add]
git commit -m "update message"
git push
```

## Best practice

### Coding Style

We follow [PEP8](https://www.python.org/dev/peps/pep-0008/) coding format.
The most important rules above all:

1. Keep code lines length below 80 characters. Maximum 120. Long code lines are NOT readable.
1. We use snake_case to name function, variables. CamelCase for classes.
1. We make our code as DRY (Don't repeat yourself) as possible.
1. We give a description to classes, methods and functions.
1. Variables should be self explaining and just right long:
   - `implied_volatility` is preferred over `impl_v`
   - `implied_volatility` is preferred over `implied_volatility_from_broker_name`

### Do not

1. Do not place .py files at root level (besides setup.py)!
1. Do not upload big files > 100 MB.
1. Do not upload log files.
1. Do not declare constant variables in the MIDDLE of a function.
