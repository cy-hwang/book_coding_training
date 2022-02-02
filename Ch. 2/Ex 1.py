"""
목표: 사용자의 이름을 입력 받아 이름을 이용한 인사말 출력
제약조건: 입력부분, 문자열 연결(String Concatenation) 부분, 출력 부분을 별도로 작성
출력 예시
  - what is your name? Brian
  - Hello, Brian, nice to meet you!

# 도전과제
 - 변수를 사용하지 않는 새로운 버전을 작성
 - 사람들마다 서로 다른 인사말이 나타나도록 프로그램 작성
"""


import random


if __name__ == "__main__":
    """
    # 기본과제
    name = input("What is your name? ")
    print(f'Hello, {name}, nice to meet you!')
    """

    # 도전과제
    def greet1(name):
        return f'Hello, {name}, nice to meet you!'

    def greet2(name):
        return f'Hi {name}, it\'s happy to meeting you'

    def greet3(name):
        return f'Get off'

    greetingList = [greet1, greet2, greet3]
    print(greetingList[random.randrange(0,3)](input("What is your name? ")))
