import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0'
}

payload = {
      "fingerprint": "",
      "email": "",
      "username": "",
      "password": "",
      "invite": None,
      "consent": True,
      "date_of_birth": "2000-01-01",
      "gift_code_sku_id": None,
      "captcha_key": None
}
payload=json.dumps(payload)

session = requests.Session()

k=session.post('https://discord.com/api/v8/auth/fingerprint', headers=headers,data=payload)

payload = {
          "fingerprint": "",
          "email": "djasllsllgggggflfest@gmail.com",
          "username": "netelalalaltest",
          "password": "lglglitestproject",
          "invite": None,
          "consent": True,
          "date_of_birth": "2000-01-01",
          "gift_code_sku_id": None,
          "captcha_key": None
}
payload['fingerprint']=str(k.json()['fingerprint'])


payload=json.dumps(payload)

session = requests.Session()
p = session.post('https://discord.com/api/v9/auth/register', headers=headers,data=payload)
print(p.status_code)
print(p.text)
print(p.cookies)







