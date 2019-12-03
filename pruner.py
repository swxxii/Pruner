#! /usr/bin/python3
##########################################################################
# pruner.py - https://github.com/swxxii/Pruner
# A Python script to remove completed torrents from qBittorrent
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

# Remove torrents once completed for this many minutes
prune_after = 10

# Change to the IP and Port of your qBittorrent server
server = "10.0.0.2:8081"

#
#   MAIN SCRIPT EXECUTION
#

# calculate the time prune_after mins ago
threshold = datetime.now() - timedelta(minutes=prune_after)
# make readable version so we can print later
thre_str = threshold.strftime('%Y-%m-%d %H:%M:%S')

# make GET request to qBittorrent API for list of finished torrents
# returns JSON array


def get_torrents():
    api_url = "http://{0}/query/torrents?filter=completed".format(server)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_url, headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


# call the above function
torrents = get_torrents()

# if we got something, loop over torrents
if torrents is not None:
    for t in torrents:
        # convert torrent's finished time into datetime
        finished = datetime.fromtimestamp(int(t['completion_on']))
        # make readable version
        fin_str = finished.strftime('%Y-%m-%d %H:%M:%S')

        # boolean to decide to prune or not?
        prune = finished < threshold

        # print some info
        print("\nTorrent: {0}".format(t['name']))
        print("Hash: {0}".format(t['hash']))
        print("Finished on {0} (threshold={1})".format(fin_str, thre_str))
        print("Prune: {0}".format(prune))

        # send the prune request to qBittorrent
        if (prune):
            api_url = "http://{0}/command/delete".format(server)
            body = {'hashes': t['hash']}
            response = requests.post(api_url, data=body)
