"""
# 목표: 두 개의 숫자를 입력 받은 후, 두 숫자를 이용하 ㄴ사칙연산 결과를 다음의 출력 예와 같이 나타내보자

# 출력 예시
  What is the first number? 10
  What is the second number? 5
  10 + 5 = 15
  10 - 5 = 5
  10 * 5 = 50
  10 / 5 = 2

# 제약 조건
  - 문자열로 입력 도록 할 것. 이렇게 받은 문자열 값은 사칙연산을 하기 전에 숫자값으로 변환
  - 입력 값과 출력 값 모두 숫자 변환 및 기타 프로세스에 영향을 받지 않도록 할 것
  - 한 개의 출력문만 사용하여 적당한 위치에 줄바꿈 글자를 넣을 것

#  도전 과제
  - 숫자만 입력되도록 프로그램을 수정해보자. 숫자가 아닌 값이 입력된 경우 진행되면 안 된다
  - 음수를 넣을 수 없도록 하라
  - 계산 부분을 함수로 구현해보자. 함수에 대해서는 5장 '함수'에서 확인할 수 있다
  - 앞의 프로그램을 GUI로 구현하여 숫자를 넣는 즉시 자동으로 계산 결과가 업데이트 되도록 하라
"""


def sumFunc(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"


def minusFunc(num1, num2):
    return f"{num1} - {num2} = {num1 - num2}"


def multipleFunc(num1, num2):
    return f"{num1} * {num2} = {num1 * num2}"


def divisionFunc(num1, num2):
    return f"{num1} / {num2} = {round(num1 / num2, 1)}"


if __name__ == "__main__":
    condition = True

    while condition:
        num1 = input("What is the first number? ")
        if num1.isdigit():
            num1 = int(num1)
            condition = False
        else:
            print("Insert interger only")

    condition = True

    while condition:
        num2 = input("What is the second number? ")
        if num2.isdigit():
            num2 = int(num2)
            condition = False
        else:
            print("Insert integer only")

    print(
        f"{sumFunc(num1, num2)}\n{minusFunc(num1, num2)}\n{multipleFunc(num1, num2)}\n{divisionFunc(num1, num2)}"
    )
"""
round(num1 / num2, 0)
str.isdigit()
"""
