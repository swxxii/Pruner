Pruner
======

A PowerShell script to remove completed torrents from qBittorrent.

## qBittorrent setup

In your qBittorrent settings, enable this setting:

* Bypass authentication for clients in whitelisted IP subnets

Then add the IP range of your LAN in the box e.g. 10.0.0.0/24.

If you are running in Docker bridged mode, you need to enter the IP range of your client network e.g. 172.17.0.0/16.