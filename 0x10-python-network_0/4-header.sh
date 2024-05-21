#!/bin/bash
#sends a GET request to the URL, header variable X-School-User-Id: 98
curl -sH "X-School-User-Id: 98" "$1"
