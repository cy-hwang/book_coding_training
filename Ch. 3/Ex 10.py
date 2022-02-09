"""
# 목표: 간단한 셀프계산대 시스템을 만들어보자. 세 가지 물건의 가격과 수량을 각각 입력 받은 다음 소계를 구하고 소계에 대한 5.5%의 세금을 계산하자.
       그리고 물건 종류별 수량과 전체 수량을 출력한 후 가격 소계, 세금, 합계 금액을 출력하자.

# 출력 예시
  Price of item 1: 25
  Quantity of item 1: 2
  Price of item 2: 10
  Quantity of item 2: 1
  Price of item 3: 4
  Quantity of item 3: 1
  Subtotal: $64.00
  Tax: $3.52
  Total: $67.52

# 제약 조건
  - 입력 부분, 계산 부분, 출력 부분을 프로그램에서 모두 구분되게 작성할 것.
    즉, 입력 값을 모두 받은 다음 계산을 하고, 출력할 문자열을 생성한 후 최종 결과를 출력하자.
  - 계산을 시작하기 전에 반드시 입력 값을 숫자 데이터로 변환시킬 것

# 도전과제
  1. 입력 값으로 숫자만 받을 수 있도록 프로그램을 수정해보자. 숫자가 입력될 때까지 진행되지 않도록 하라.
  2. 제한되지 않은 개수의 물건을 입력 받을 수 있도록 프로그램을 수정해보자. 즉, 물건에 대한 내용이 입력되지 않을 때까지 입력을 받고 세금과 합계 금액을 계산하자.
"""
TAX = 5.5


def valueValidator1(statement1, statement2):
    condition = True
    while condition:
        val = input(statement1)
        if val.isdigit():
            condition = False
            return int(val)
        else:
            print(f"{statement2} must be positive integer.")


def valueValidator2(statement1, statement2):
    condition = True
    while condition:
        val = input(statement1)
        if val.isdigit():
            condition = False
            return int(val)
        elif val == "":
            condition = False
            return val
        else:
            print(f"{statement2} must be positive integer.")


if __name__ == "__main__":
    idx = 1
    totalPrice = []
    condition = True
    while condition:
        price = valueValidator2(f"Price of item {idx}: ", "Item price")
        if price == "":
            condition = False
        else:
            quantity = valueValidator1(f"Quantity of item {idx}: ", "Quantity of item")
            totalPrice.append(price * quantity)
            idx += 1

    subtotal = 0
    for price in totalPrice:
        subtotal += price

    tax = subtotal * TAX / 100
    total = subtotal + tax

    print(f"Subtotal: ${subtotal}")
    print(f"Tax: ${tax}")
    print(f"Total: ${total}")

"""
for문
    for price in totalPrice:
        subtotal += price

String 비교
    if price == "": 
"""
