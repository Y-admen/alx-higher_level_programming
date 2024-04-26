#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the value of theX-Request-Id variable found in the header of the response."""
from sys import argv
from urllib import request

if __name__ == "__main__":
    url = argv[1]
    file = request.Request(url)
    with request.urlopen(file) as res:
        print(res.headers.get('X-Request-Id'))
