#! /usr/bin/python3
##########################################################################
# pruner.py - https://github.com/swxxii/Pruner
# A Python script to remove completed torrents from qBittorrent
# Version 0.3
# ########################################################################
import json
import requests
import datetime
import time
from time import mktime
from datetime import datetime, timedelta

#
#   CONFIGURATION
#

# Change to the details of your qBittorrent server.
server = 'http://10.0.0.2:8081'
username = 'admin'
password = 'bittorrent'

# Remove torrents only if completed this many minutes ago.
# Set to zero (0) to prune immediately.
prune_after = 10

# Don't prune torrents in this category - useful for Sonarr
exclude = 'TV'

#
#   FUNCTIONS
#


def authenticate():
    api_url = "{0}/api/v2/auth/login".format(server)
    headers = {'Accept': 'application/json', 'Host': server,
               'Origin': server, 'Referer': server}
    data = {'username': username, 'password': password}
    response = requests.get(api_url, headers=headers, data=data)
    print("Request: {0}".format(api_url))
    print("Response: {0}".format(response.status_code))
    if (response.status_code == 200):
        return response.cookies['SID']
    else:
        return None


def get_torrents():
    api_url = "{0}/api/v2/torrents/info?filter=completed".format(server)
    headers = {'Accept': 'application/json', 'Host': server,
               'Origin': server, 'Referer': server}
    response = requests.get(api_url, headers)
    print("Request: {0}".format(api_url))
    print("Response: {0}".format(response.status_code))
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


def delete_torrent(hash):
    api_url = "{0}/api/v2/torrents/delete?hashes={1}&deleteFiles=false".format(
        server, hash)
    headers = {'Accept': 'application/json', 'Host': server,
               'Origin': server, 'Referer': server}
    cookies = {'SID': sid_cookie}
    response = requests.get(api_url, headers=headers, cookies=cookies)
    print("Request: {0}".format(api_url))
    print("Response: {0}".format(response.status_code))

#
#   MAIN SCRIPT EXECUTION
#


# calculate the time prune_after mins ago
threshold = datetime.now() - timedelta(minutes=prune_after)
# make readable version so we can print later
thre_str = threshold.strftime('%Y-%m-%d %H:%M:%S')


print('Authenticating...')
sid_cookie = authenticate()
if (sid_cookie == None):
    print('Could not login. Terminating.')
    exit(1)
print('Logged in OK. SID={0}'.format(sid_cookie))

print("Getting torrents...")
torrents = get_torrents()

# if we got something, loop over torrents
if torrents is not None:
    if len(torrents) < 1:
        print("No torrents to prune.")
    for t in torrents:
        # convert torrent's finished time into datetime
        finished = datetime.fromtimestamp(int(t['completion_on']))
        # make readable version
        fin_str = finished.strftime('%Y-%m-%d %H:%M:%S')

        # boolean to decide to prune or not?
        prune = finished < threshold and t['category'].lower() != exclude.lower()

        # print some info
        print("\nTorrent: {0}".format(t['name']))
        print("Hash: {0}".format(t['hash']))
        print("Finished on {0} (threshold={1})".format(fin_str, thre_str))
        print("Prune: {0}".format(prune))

        # send the prune request to qBittorrent
        if (prune):
            delete_torrent(t['hash'])

else:
    print("Request error.")
