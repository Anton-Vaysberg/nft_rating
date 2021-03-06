#!/bin/bash

#export GOOGLE_APPLICATION_CREDENTIALS=/fullpath/serviceaccount.json
pip install google-cloud
pip install --upgrade google-api-python-client
pip install beautifulsoup4
pip install selenium
pip install twython
pip install requests
pip install uuid
pip install datetime

# Install Chrome browser
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
sudo yum -y localinstall google-chrome-stable_current_x86_64.rpm

#remove previous version of nftRating python project
rm -rf nft_rating/

yum -y install git
git clone https://Anton-Vaysberg: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@github.com/Anton-Vaysberg/nft_rating

# Navigate to python project and install chromedriver
pip install --target=nft_rating/nftRating/ chromedriver-py
