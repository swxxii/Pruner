# Pruner

A simple Python script to remove completed torrents from qBittorrent. (No longer maintaining PowerShell version.)

Configurable delay (only remove torrents once they have been completed for certain number of minutes).

## Requirements

- qBittorrent version 4.1 or later
- Python 3 recommended
- `pip install requests`

## Setup

Edit the configuration section of the script to reflect your qBittorrent setup: `server` address, `username` and `password`.

## Version history

- **0.3** - Added authentication support, fix delete API call to use GET method
- **0.2** - Updated to work with qBittorrent API v2.
- **0.1** - Convert to Python. Fix bug with prune age detection.
