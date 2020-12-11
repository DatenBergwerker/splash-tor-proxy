import requests
import json

external_ip = requests.get('http://localhost:8050/render.html?url=http://ip.jsontest.com/&proxy=default')
external_ip = json.loads(external_ip.text)
print(external_ip)

# import requests
#
#
# proxies = {
#     'http': 'socks5://127.0.0.1:9050',
#     'https': 'socks5://127.0.0.1:9050'
# }
#
#
# def main():
#     url = 'http://ifconfig.me/ip'
#
#     response = requests.get(url)
#     print('ip: {}'.format(response.text.strip()))
#
#     response = requests.get(url, proxies=proxies)
#     print('tor ip: {}'.format(response.text.strip()))
#
#
# if __name__ == '__main__':
#     main()