"""
# 목표: 복리를 통해 투자 수익을 계산하는 프로그램을 작성하라. 프로그램은 원금, 투자 기간, 연이율, 연간 수익이 지급되는 횟수를 입력받는다.
       복리 공식은 다음과 같다

       원리금 = 원금(1 + 연이율/연간 이자 지급 횧수) ^ (연간 이자 지급 횟수 * 연단위 투자 기간)

# 출력 예시
  What is the principal amount? 1500
  What is the rate: 4.3
  What is the number of years: 6
  What is the number of times the interest is compounded per year:4
  $1500 invested at 4.3% for 6 years compounded 4 times per year is $1938.84

# 제약 조건
  - 연이율은 반드시 퍼센트 단위로 입력받은 후(예: .15가 아닌 15) 프로그램에서 입력 값을 100으로 나누어 계산할 것
  - 센트를 기준으로 하는 소숫점 다음에 숫자가 있을 때는 센트를 기준으로 올림 처리할 것
  - 출력되는 원리금은 화폐단위로 출력할 것

# 도전과제
  1. 입력 값으로 숫자만 받을 수 있도록 프로그램을 수정해보자. 숫자가 입력될 때까지 진행되지 않도록 하라.
  2. 목표 원리금을 입력하면 필요한 초기 투자 원금을 계산하도록 프로그램을 수정해보자.
  3. 이 프로그램을 GUI 버전으로 구현하여 입력 값이 변겨오디는 즉시 바로 결과가 업데이트되도록 하라.
"""


import math


def is_float(num):
    """[해당 값의 실수여부 판단 함수]

    Args:
        num ([any]): [실수여부 판단 대상]

    Returns:
        [bool]: [True if 실수 else False]
    """
    try:
        float(num)
        return True
    except ValueError:
        return False


def value_validator(statement1, statement2):
    """[input으로 입력받은 값이 양의 정수인지 확인하는 함수]

    Args:
        statement1 ([str]): input 입력시 표출 문구
        statement2 ([str]): 양의 정수 대상

    Returns:
        [int]: 입력받은 값
    """
    while True:
        val = input(statement1)
        if val.isdigit():
            return int(val)
        print(f"{statement2} must be positive integer.")


if __name__ == "__main__":

    principal = value_validator("What is the principal amount: ", "Principal")
    rate = 0.0
    while True:
        rate = input("What is the rate: ")
        if is_float(rate):
            rate = float(rate)
            break
    year = value_validator("What is the number of years: ", "Years")
    compound_count = value_validator(
        "What is the number of times the interest is compounded per year: ", "Counts"
    )

    worth = principal * pow(1 + rate / 100 / compound_count, compound_count * year)
    worth = math.ceil(worth * 100) / 100

    print(
        f"${principal} invested at {rate}% for {year} years compounded {compound_count} times per year is ${worth}"
    )
