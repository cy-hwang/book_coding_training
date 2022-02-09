"""
# 목표: 환율을 변환하는 프로그램을 작성하라. 여기에서는 유로에서 미국 달러로 변환시킨다.
       먼저 유로 금액을 입력 받은 다음 유로 환율을 입력 받는다. 그리고는 유로에 해당하는 미국 달러 값을 출력한다.
       환율 변환식은 다음과 같다.

       미국달러가격 = 유로가격 * 현재 유로 환율 / 현재 미국 달러 환율

        => 일반적으로 자국 달러 환율은 100이다.

# 출력 예시
  How many Euros are you exchanging? 81
  What is the exchange rate? 137.51
  81 Euros at an exchange rate of 137.51 is
  111.38 dollars

# 제약 조건
  - 센트를 기준으로 하는 소숫점 다음에 숫자가 있을때는 센트를 기준으로 올림 처리를 할 것
  - 한 개의 출력문만 사용할 것

# 도전과제
  1. 환율표를 프로그램에 넣은 다음 환율 대신 국가 이름을 입력 받도록 프로그램을 수정해보자
  2. 애플리케이션에 별도의 API를 적용하여 현재의 업데이트된 환율을 적용하는 프로그램으로 수정해보자.
"""
import math
import requests


def valueValidator(statement1, statement2):
    condition = True
    while condition:
        val = input(statement1)
        if val.isdigit():
            condition = False
            return int(val)
        else:
            print(f"{statement2} must be positive integer.")


if __name__ == "__main__":

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    url = "https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.EURUSD"
    exchange = requests.get(url, headers=headers).json()
    exchangeRate = round(1 / exchange[0]["basePrice"], 5)

    euro = valueValidator("How many Euros are you exchanging? ", "Euros")

    print(
        f"{euro} Euros at an exchange rate of {exchangeRate} is {math.ceil(euro * exchangeRate * 100)/100}"
    )


"""
# venv: pipenv

# requests 모듈
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    url = "https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.EURUSD"
    exchange = requests.get(url, headers=headers).json()

# 환율 API
    url = "https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.EURUSD"
"""
