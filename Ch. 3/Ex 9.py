"""
# 목표: 천장을 칠하는 데 필요한 페인트 양을 구하는 프로그램을 작성하라.
       길이와 폭을 입력 받은 다음, 1리터에 9m2를 칠한다고 가정하여 계산하자. 그리고 천장을 칠하는 데 필요한 페인트 양을 정수로 표현해보자.

# 출력 예시
  You will need to purchase 2 liters of paint to cover 10 square meters.

  반드시 1리터짜리 통 단위로 페인트를 구매해야 한다.
  그렇기 때문에 이 문제를 해결하기 위해서는 반드시 올림을 해야 한다.

# 도전과제
  1. 입력 값으로 숫자만 받을 수 있도록 프로그램을 수정해보자. 숫자가 입력될 때까지 진행되지 않도록 하라.
  2. 원 모양의 방도 계산할 수 있도록 하라.
  3. ㄴ자 모양의 방도 계싼할 수 있도록 하라.
  4. 모바일 버전으로 프로그램을 작성하여 철물점에서 사용할 수 있도록 하라.
"""
import math


PAINT = 9


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
    length = valueValidator("What is the length of the ceiling in feet? ", "Length")
    width = valueValidator("What is the width of the ceiling in feet? ", "Width")

    roomSize = length * width
    print(
        f"You will need to purchase {math.ceil(roomSize/PAINT)} liters of paint to cover {roomSize} square meters"
    )
