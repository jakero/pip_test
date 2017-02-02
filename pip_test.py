"""
requests를 테스트 해본다

/home/<username>/.pyenv/versions/3.4.3/env/<envname>
"""
import requests

r = requests.get('http://google.co.kr')
print(r.text)