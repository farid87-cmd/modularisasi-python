import requests

url = 'https://deti k.com'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Succsess Response = {response.status_code}')
        #print(f'Content {response.text}')
    else:
        print(f'WOOPS, ada kesalahan request {response.status_code}')
except Exception as e:
    print(f'ADA ERROR!!, {e}')
print('Program Ended')
