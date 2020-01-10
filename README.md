# Pruner

A simple Python script to remove completed torrents from qBittorrent. (No longer maintaining PowerShell version.)

Configurable delay (only remove torrents once they have been completed for certain number of minutes).

## Requirements

- qBittorrent 4.1 or later
- Python 3

## Basic Setup

- Run `pip install requests`
- Edit the configuration section of the script to reflect your qBittorrent setup: `server` address, `username` and `password`.

## Synology NAS Setup
**Background:** This method uses a Python virtual environment (venv) to install packages and run the script. This is a recommended step to prevent us having to modify the stock Python installation in the NAS which could break stuff.
- Make sure you have enabled home folders in Synology DiskStation<br> (Control Panel > User > Advanced > Enable user home service).
- SSH into your NAS as admin user.
- Run `python3 -m venv env` -- creates a Python venv (in your home dir) called `env`.
- Run `. env/bin/activate` -- start Python inside the virtual environment.
- Run `pip install requests` -- install the requests package into the venv.
- Copy `run-pruner.sh` to your Synology scripts folder and update to point to wherever you put `pruner.py`.
- In the Synology Task Scheduler create a job to call the `run-pruner.sh` script,<br>e.g. `bash /volume1/configs/scripts/run-pruner.sh`.

## Docker Setup

- COMING SOON!

## Version history

- **0.3** - Added authentication support, fix delete API call to use GET method.
- **0.2** - Updated to work with qBittorrent API v2.
- **0.1** - Convert to Python. Fix bug with prune age detection.
