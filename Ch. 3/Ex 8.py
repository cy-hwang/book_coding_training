"""
# 목표: 피자를 정확하게 나누는 프로그램을 작성하라. 사람 수, 피자 개수, 조각 개수를 입력 받는데, 이때 조각 개수는 짝수여야 한다.
  일단 한 사람이 받게 되는 피자 조각 개수를 출력해보자. 만일 남는 조각이 있다면 그 개수도 나타내보자.

# 출력 예시
  How many people? 8
  How many pizzas do you have? 2

  How many pieces are in a pizza? 8
  8 people with 2 pizzas
  Each person gets 2 pieces of pizza.
  There are 0 leftover pieces.

# 도전과제
  1. 입력 값으로 숫자만 받을 수 있도록 프로그램을 수정해보자. 숫자가 입력될 때까지 진행되지 않도록 하라
  2. 출력 내용을 변경하여 수일치가 되도록 하라.
  Ex. Each person gets 2 pieces of pizza
  Ex 2. Each person gets 1 pieces of pizza
    남은 피자 조각도 위와 같이 수일치를 하여 출력되도록 하라
  3. 사람 수와 한 사람당 원하는 피자 조각 수를 입력받은 다음, 피자를 몇 판 구매해야 하는지 계산하는 프로그램을 작성하라
"""

# 피자 조각이 양의 정수이며, 짝수여부 체크
def pieceValidator(pieces):
    return pieces.isdigit() and int(pieces) % 2 == 0


def valueValidator(statement1, statement2):
    condition = True
    while condition:
        val = input(statement1)
        if val.isdigit():
            condition = False
            return int(val)
        else:
            print(statement2)


if __name__ == "__main__":
    people = valueValidator("How many people? ", "People must be positive integer.")
    pizzas = valueValidator(
        "How many pizzas do you have? ", "Pizza must be positive integer."
    )

    condition = True
    pieces = 0

    while condition:
        pieces = input("How many pieces are in a pizza? ")
        if pieceValidator(pieces):
            pieces = int(pieces)
            condition = False
        else:
            print("Pizza pieces must be even")

    print(f"{people} people with {pizzas} pizzas")
    distribution = int(pizzas * pieces / people)
    print(f"Each person gets {distribution} pieces of pizza")

    print(f"There are {pizzas * pieces - distribution * people} leftover pieces.")

"""
# 내림: int(pizzas * pieces / people)
"""
