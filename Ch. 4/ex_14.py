"""
# 목표: 입력한 가격에 대한 세금을 계산하는 간단한 프로그램을 작성하라.
       프로그램은 주문 가격과 함께 주(state) 이름을 입력받는데, 주 이름이 "WI"인 경우 세율은 5.5%가 된다.
       프로그램은 위스콘신 주 거주자에 해당하는 소계, 세율, 합계 금액을 출력하지만 다른주에 거주하는 경우에는 합계 금액만을 출력한다.

# 출력 예시
  What is the order amount? 10
  What is the state? WI
  The subtotal is $10.00
  The tax is $0.55
  The total is $10.55
  
  ---
  What is the order amount? 10
  What is the state? MN
  The total is $10.55

# 제약 조건
  - 오직 if문만 사용하여 작성할 것(else문을 절대 사용해서는 안됨)
  - 모든 금액은 가장 가까운 센트로 반올림할 것
  - 프로그램의 마지막에 한 개의 추력문만 사용하여 결과를 출력할 것

# 도전과제
  1. 주 이름의 약어를 대소문자가 섞인 상태로 입력해도 되도록 프로그램을 수정해보자
  2. 주 이름 전체를 대소문자가 섞인 상태로 입력해도 되도록 프로그램을 수정해보자
"""


import math

TAX = 5.5


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


def make_cent(value):
    """센트 단위로 변환. 이하 금액은 올림하여 센트로 표기

    Args:
        value ([float]): [금액]

    Returns:
        [float]: [소숫점 둘째자리까지 표기된 그맹ㄱ]
    """
    return math.ceil(value * 100) / 100


if __name__ == "__main__":
    order = value_validator("What is the order amount? ", "Order amount")
    state = input("What is the state? ")
    tax = make_cent(order * TAX / 100)

    state = state.replace(" ", "")  # 공백 제거
    if state.upper() == "WI" or state.upper() == "WISCONSIN":
        print(f"The subtotal is ${order}")
        print(f"The tax is ${tax}")
    print(f"The total is ${order +tax}")
