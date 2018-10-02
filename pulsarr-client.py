#!/usr/bin/python3

import urllib.request, json

class PulsarrClient:
    def __init__(self, server, api_key):
        self._server = server
        self._api_key = api_key

    def _get_json(self, loc):
        with urllib.request.urlopen(loc) as url:
            data = json.loads(url.read().decode())
            return data

    def list_books(self):
        req_url = '{}/api/library?apikey={}'.format(self._server, self._api_key)
        raw = self._get_json(req_url)
        books = [book for book in raw if book['Status'] == 'Complete']
        return books

    def download_book(self, book_id, download_location):
        req_url = '{}/api/library/{}?apikey={}'.format(self._server, book_id, self._api_key)
        urllib.request.urlretrieve(req_url, download_location)

client = PulsarrClient('http://<hostname>', '<api key>')
client.list_books()
