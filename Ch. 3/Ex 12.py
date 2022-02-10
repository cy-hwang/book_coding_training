"""
# 목표: 단리를 계산하는 프로그램을 작성하라.
       원금을 입력 받은 다음 이자를 퍼센트 단위로 입력받고, 기간을 연단위로 입력 받은 후 원리금(원금 +이자)을 출력해보자

       => 단리 공식은 다음과 같다.

       원리금 = 원금 * (1 + 연이율*기간(연단위))

# 출력 예시
  Enter the principal: 1500
  Enter the rate of interest: 4.3
  Enter the number of years: 4
  After 4 years at 4.3%, the investment will be worth $1758

# 제약 조건
  - 연이율은 받으시 퍼센트 단위로 입력 받은 후(예:.15가 아니라 15) 프로그램에서 입력 값을 100으로 나누어 계산할 것
  - 센트를 기준으로 하는 소숫점 다음에 숫자가 있을 때는 센트를 기준으로 올림 처리할 것
  - 출력되는 원리금은 화폐 단위로 출력할 것

# 도전과제
  1. 입력 값 원금, 이율, 기간은 모두 숫자로만 받을 수 있도록 프로그램을 수정해보자. 숫자가 입력될 때까지 진행되지 않도록 하라.
"""


import math


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


if __name__ == "__main__":
    principal = value_validator("Enter the principal: ", "Principal")

    while True:
        interest = input("Enter the rate of interest: ")
        if is_float(interest):
            interest = float(interest)
            break
        print("Interest must be float type")

    year = value_validator("Enter the number of years: ", "Years")
    totalWorth = principal * (1 + interest / 100 * year)
    totalWorth = math.ceil(totalWorth * 100) / 100  # 실링 단위에서 올림

    print(
        f"After {year} years at {interest}%, the investment will be worth ${totalWorth}"
    )

"""
# Code Formatter 적용: black

# linter 적용: pylint
"""
