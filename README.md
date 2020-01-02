# Pruner

A simple Python script to remove completed torrents from qBittorrent. (No longer maintaining PowerShell version.)

Configurable delay (only remove torrents once they have been completed for certain number of minutes).

## Requirements

- qBittorrent version 4.1 or later
- Python 3 recommended

## Basic Setup

- Run `pip install requests`
- Edit the configuration section of the script to reflect your qBittorrent setup: `server` address, `username` and `password`.

## Synology NAS Setup

- Log into NAS as admin
- Run `pip install virtualenv` -- installs the Python `virtualenv` package.
- Run `virtualenv env` -- creates a Python environment (in your home dir) called `env`.
- Run `. env/bin/activate` -- start Python in the virtual environment.
- Run `pip install requests` -- install the requests package into your virtual environment.
- Copy `run-pruner.sh` to your Synology scripts folder
- Update `run-pruner.sh` to point to wherever you put `pruner.py`.
- in Synology scheduler call the `run-pruner.sh` script.

## Docker Setup

- COMING SOON!

## Version history

- **0.3** - Added authentication support, fix delete API call to use GET method
- **0.2** - Updated to work with qBittorrent API v2.
- **0.1** - Convert to Python. Fix bug with prune age detection.
