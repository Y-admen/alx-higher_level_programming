#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter
"""
from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    dict = {'email': email}
    "converts it into a URL-encoded string"
    data = parse.urlencode(dict)
    "URL-encoded string converted into bytes"
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as req:
        mail = req.read()
        "convert the bytes back into a human-readable string."
        print(mail.decode('utf-8'))
