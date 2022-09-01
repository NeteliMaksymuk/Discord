import requests
import json
import random

headers = {
    'user-agent': 'Mozilla/5.0'
}

payload = {
    "fingerprint": "fingerprint",
    "email": "email",
    "username": "username",
    "password": "password",
    "invite": None,
    "consent": True,
    "date_of_birth": "2000-01-01",
    "gift_code_sku_id": None,
    "captcha_key": None
}

email = input('Enter email: ')
username = input('Username: ')
password = ''

for x in range(9):
    password = password + random.choice(list(
        '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'
    ))

print('Your password is: ', password)

payload['email'] = email
payload['username'] = username
payload['password'] = password
payload = json.dumps(payload)

session = requests.Session()

responce_fingerprint = session.post('https://discord.com/api/v8/auth/fingerprint', headers=headers, data=payload)
payload = json.loads(payload)

payload['fingerprint'] = str(responce_fingerprint.json()['fingerprint'])

payload = json.dumps(payload)
session = requests.Session()
responce_register = session.post('https://discord.com/api/v9/auth/register', headers=headers, data=payload)

if responce_register.status_code == 201:
    print(responce_register.status_code, '\n', responce_register.text)
elif responce_register.status_code == 429:
    print('Take it easy')
else:
    print('Check your email or username')
    print(responce_register.text)
