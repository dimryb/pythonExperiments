import requests
import sys

url = sys.argv[1]

try:
    response = requests.get(url, timeout=30)
except requests.Timeout:
    print("ошибка timeout, url:", url)
except requests.HTTPError as err:
    code = err.response.status_code
    print("ошибка url: {0}, code: {1}".format(url, code))
except requests.RequestException:
    print("ошибка скачивания url: ", url)
else:
    print(response.content)

print("end")
