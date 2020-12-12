# splash-tor-proxy
Proxy Infrastructure to pass local splash rendering requests through the TOR network. The goal with this setup is to obfuscate the source of requests. It is not yet configured for proxy rotation by rebuilding TOR circuits.

## Requirements
Docker, Docker-Compose

## Installation
Just run `docker-compose -f splash-proxy-infrastructure.yml up -d` to initialize the containers.

## Usage
If you utilize the Python package Scrapy for your web-scraping projects, you can configure this splash service as your rendering engine for your spider requests. No additional changes are required, the spider only  has to be  able to  make requests to `localhost:8050`.
Please be mindful that routing via TOR is slower than non onion routing, so adjust your requests limits accordingly. Dont flood the TOR network with scraping requests.
