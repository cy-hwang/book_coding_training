"""
# 목표: 나이를 입력받아 미국법상 운전 가능한 나이인 16세와 비교하여 16세 이상이면 "You are old enough to lagally drive"라고 출력하고,
       16세 미만이면, "You are not old enough to legally drive"라고 출력하는 프로그램을 작성하라

# 출력 예시
  What is your age? 15
  You are not old enough to legally drive.

  ---
  What is your age? 35
  You are old enough to legally drive.

# 제약 조건
  - 한 개의 출력문만 사용할 것
  - 3항 연산자를 사용할 것. 사용하는 프로그래밍 언어가 3항 연산자를 지원하지 않는다면 일반적인 if/else문을 사용할 것.
    하지만 여전히 메세지를 출력하는 출력문은 한 개만 사용할 것

# 도전과제
  1. 0보다 작은 값을 입력하거나 숫자가 아닌 값을 입력하면 올바른 나이를 입력하라는 에러 메시지를 출력해보자.
  2. 프로그램 로직에 운전 가능한 나이를 코드 안에 넣는 대신, 나라별 운전 가능한 연령을 조사하여 테이블로 구성한 다음,
     나이와 국가를 입력 받아 해당 국가에서 운전을 할 수 있는지를 출력하도록 프로그램을 수정해보자.
"""
AGE_LIMITATION = 16

if __name__ == "__main__":
    age = 0
    while True:
        val = input("What is your age? ")
        if val.isdigit():
            age = int(val)
            break
        print("Age must be positive integer.")

    msg = (
        "You are old enough to legally drive."
        if age >= AGE_LIMITATION
        else "You are not old enough to legally drive."
    )

    print(f"{msg}")

"""
# 3항 연산자
    msg = (
        "You are old enough to legally drive."
        if age >= AGE_LIMITATION
        else "You are not old enough to legally drive."
    )
"""
