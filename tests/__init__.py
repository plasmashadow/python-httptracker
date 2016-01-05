import unittest
import mock
from httptrack import HTTPTracker
from bencode import bencode
import hashlib
import requests


def trim_hash(info_hash):
    """cleans up info hash"""
    if len(info_hash) == 40:
        return info_hash.decode("hex")
    if len(info_hash) != 20:
        raise TypeError("Infohash not equal to 20 digits", info_hash)
    return info_hash


class TestHttpTracker(unittest.TestCase):

    def setUp(self):
        self.parsed_dict = {'comment': 'Torrent downloaded from http://thepiratebay.org',
                            'announce': 'http://tracker.openbittorrent.com:80/announce',
                            'info': {'files': [{'path': ['An Introduction to Neural Networks.zip'],
                                                'length': 1098160},
                                               {'path': ['Torrent downloaded from thepiratebay.org.txt'],
                                                'length': 49}],
                                     'piece length': 262144,
                                     'name': 'An Introduction to Neural Networks',
                                     'pieces': "\x04\x15\x12\xf6\xaa\xba*\x85\x87\xe4\x1eGK#\xd0\xd5\x82+\xb9\xb3\xef6 Ul\x8f\xa4\xe5\x03\xca\xb0ck\\\xba=z'\xe8\xb0\xf2\xc22;\x04m\x99\x00\xd4m\xf7\x8d\xc7\x8d\xc9\xfe$a\xc8\x07B\xcc\xd9\x90\x91\xd5?b\x93\x8b\xc1<\xbdEs:F\xac)6\x02\x93\xbdOP*i\x1a\xc9.\x15\xf5\x7f5\t\x8e\xafv\xc8\xf3"},
                            'creation date': 1264385305,
                            'announce-list': {'11': 'http://tracker.publicbt.com:80/announce',
                                              '10': 'http://tracker.openbittorrent.com:80/announce',
                                              '15': 'udp://tracker.istole.it:80/announce',
                                              '14': 'udp://fr33domtracker.h33t.com:3310/announce'}}

        info_hash = hashlib.sha1(bencode(self.parsed_dict.get('info'))).hexdigest()
        info_hash = trim_hash(info_hash)
        self.tracker = HTTPTracker(self.parsed_dict.get('announce'),
                                   info_hash=info_hash,
                                   piece_length=self.parsed_dict.get('info').get('piece length'))

    @mock.patch('requests.get')
    def test_tracker_request(self, mock_request):
        self.tracker.get_peers()
        args, kwargs = mock_request.call_args
        announce = args[0]
        self.assertEqual(announce, self.tracker.announce_url)