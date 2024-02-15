#!/bin/bash

# Set your username and password here
username="terryAlx"
password="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"

# Git commands
git add .
git commit -m "web_scraping"

# Providing credentials to git using environment variables
# Note: This method isn't secure as it leaves the password visible in process listings
GIT_ASKPASS=echo GIT_USERNAME="$username" GIT_PASSWORD="$password" git push

