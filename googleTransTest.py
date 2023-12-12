# 구글 번역기로 보내서 번역, 일반 개발자가 만들어 둔 모듈이 가져다가 사용

import googletrans
import pprint  # 내장함수 -> 보기좋게 반환

trans = googletrans.Translator()  # 구글 번역 객체

str =  input("번역하라 문장을 입력하세요:")

# pprint.pprint(googletrans.LANGUAGES)  # 번역가능한 언어의 ticker

result1 = trans.translate(str, dest='en')  # 영어로 번역
result2 = trans.translate(str, dest='ja')  # 일어로 번역
result3 = trans.translate(str, dest='zh-cn')  # 중어로 번역

print(result1.text)
print(result2.text)
print(result3.text)