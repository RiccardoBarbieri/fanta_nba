import requests
from proxy_checker import ProxyChecker

def download_proxies():
    # url = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt'

    # proxies = requests.get(url).text.split('\n')

    proxies = ["192.168.1.20:8890"]

    checker = ProxyChecker()

    for i in proxies:
        print(i)
        check = checker.check_proxy(i)
        if check:
            print(f'Proxy {i} is working')
        else:
            print(f'Proxy {i} is not working')
            proxies.remove(i)

    return proxies


download_proxies()
