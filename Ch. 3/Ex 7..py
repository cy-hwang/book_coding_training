"""
# 목표: 방의 면적을 계산하는 프로그램을 작성하라. 방의 길이와 폭을 피트 단위로 입력 받은 다음 제곱피트와 제곱미터로 변적을 나타내보자

# 출력 예
  What is the length of the room in feet? 15
  What is the width of the room in feet? 20
  The area is 
  300 square feet
  27.871 square meters

=> 제곱피트에서 제곱미터 변환식: m2 = f2 * 0.09290304

# 제약조건
  - 출력문과 계산부분을 분리할 것
  - 상수를 사용하여 변환 상수를 저장할 것

# 도전 과제
  - 입력 값으로 숫자만 받을 수 있도록 프로그램을 수정해보자. 숫자가 입력될 때까지 진행되지 않도록 하라
  - 입력 값이 피트 단위인지 미터 단위인지 선택하는 새로운 버전을 만들어보자
  - 이 프로그램을 GUI 버전으로 구현하여 입력 값이 변겨오디는 즉시 바로 결과가 업데이트 되도록 하라
"""

from decimal import Decimal, getcontext

PARAM = 0.09290304


def setValue(statement):
    condition = True

    while condition:
        val = input(statement)
        if isFloat(val) and float(val) >= 0:
            return val
        else:
            print("Please input positive float value")


def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if __name__ == "__main__":

    getcontext().prec = 7
    length = setValue("What is the length of the room in feet? ")
    width = setValue("What is the width of the room in feet? ")

    print("The area is")
    print(f"{Decimal(length) * Decimal(width)} square feet")
    print(f"{Decimal(length) * Decimal(width) * Decimal(PARAM)} square meters")

"""
# 실수여부 체크
def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# 부동소숫점의 정확한 계산
: string을 활용한 계산

from decimal import Decimal, getcontext
getcontext().prec = 7
print(f"{Decimal(length) * Decimal(width)} square feet")
"""
