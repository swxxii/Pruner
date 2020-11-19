# Pruner

A simple Python script to remove completed torrents from qBittorrent. (No longer maintaining PowerShell version.)

- Configurable delay (only remove torrents once completed for X minutes)
- Skip torrents in certain category (useful for Sonarr)

## Requirements

- qBittorrent 4.1 or later
- Python 3

## Basic Install

- Run `pip install requests`
- Update the config section of the script for your qBittorrent setup: `server` address, `username` and `password`.

## Synology NAS Install

### Prerequisites
1. Enable home folders via DSM<br> (Control Panel > User > Advanced > Enable user home service).
1. Enable SSH access via DSM and log in as `admin`
1. Install Python 3 package via DSM. (3.8.2 used)

### Setup

1. Invoke pip using this command to install the `requests` module

    ```
    admin@server:~$ /volume1/\@appstore/py3k/usr/local/bin/pip3 install requests
    ```

1. Put the configured `pruner.py` script somewhere on your NAS.

1. Test it manually from the shell to make sure it works.
    ```
    admin@server:~$ python3 /volume1/configs/scripts/pruner.py
    ```
1. Create a cron job (scheduled task) in Synology DSM with the above command to run as `admin` user. 

## Version history

- **0.4** - Added option to exclude by category.
- **0.3** - Added authentication support, fix delete API call to use GET method.
- **0.2** - Updated to work with qBittorrent API v2.
- **0.1** - Convert to Python. Fix bug with prune age detection.
