##python-httptracker

A Bittorrent Http Tracking protocol client


##Usage

```python

from httptrack import HTTPTracker

client = HTTPTracker(announce_url, info_hash='7BC238FD69F5A43C1CD5566870420D63F074BAD8',
                                   piece_length=1098160)
client.get_peers()

print client.peers

```


##License

<b>MIT</b>
