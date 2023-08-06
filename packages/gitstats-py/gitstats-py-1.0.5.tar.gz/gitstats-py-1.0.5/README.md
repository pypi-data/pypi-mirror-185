# Gitstats

Gitstats is a project that calculates some user metrics for a set of Github projects. This project aims to be as configurable and easy to update as possible, so other users could add their own metrics or output formats, contributing to the project.

## Installation

You can install gitstats with pip:

```
pip install gitstats-py
```

or locally install the source code:

```
git clone https://github.com/diverso-lab/gitstats
cd gitstats
pip install .
```

## Usage

Once installed, you can run the tool just by typing the command `gitstats` in shell.

For this to work, you need a config.txt file in your current working directory. There is an [example config](https://github.com/diverso-lab/gitstats/blob/main/config.txt) file in the project. Do not copy the config above as it does not support comments:

```
[global]
# Starting date (YYYY-MM-DD)
date = 2022-9-30
# Here you must introduce a personal access token from your Github developer settings
token = token
# Introduce which metrics you want to get
metrics = CommitCount,LinesOfCode,Issues,Tests
# Introduce the expected values for each metric in the same order
expected_values = 12,240,6,6

[repos]
# List of repos to be analized. URLs below first must be indented.
urls = https://github.com/...
    https://github.com/...
    https://github.com/...
```

Then, you should get a **metrics** directory with the results, and an **alerts** directory telling which users have not reached the expected values.