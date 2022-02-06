"""
따옴표 출력

# 목표: 큰 따옴표는 문자열의 시작과 끝을 나타내는 용도로 자주 사용되지만, 가끔은 확장문자(escape character)를 사용하여 따옴표 자체를 출력할 일도 생긴다.
인용구와 그 말을 한 사람을 입력받는 프로그램을 작성하라. 인용구와 사람 이름은 다음의 출력 예와 같이 나타내보자

# 출력 예시
  What is the quote? These aren't the droids you're looking for
  Who said it? Obei-wan Kenobi
  Obi-Wan Kenobi says, "These aren'tthe droids you're looking for"

# 제약조건
  - 한 개의 출력문만 사용하여 결과를 출력할 것. 이때 따옴표를 출력하기 위해 적절한 확장문자를 사용해야 한다,.
  - 만일 사용하는 프로그래밍 언어가 문자열 보간(String Interpolation)이나 문자열 대체(String Substitution)를 
  지원하는 경우라도 이 기능들을 사용하지 말고 그냥 문자열 연결(String Concatenation)을 사용할 것

# 도전과제
  1. 7장에서 데이터리스트에 대해서도 연습하게 될 것이다. 앞의 프로그램을 수정하여 사용자로부터 입력을 받는 대신 인용구와 이와 관련된 내용(사람 이름)을 
  담는 자료 구조를 만들어 모든 내용을 앞의 출력 예와 같이 나타내보자. 맵 협태의 배열을 사용하면 좋을 것 이다.
"""

if __name__ == "__main__":
    quote = input("What is the quote? ")
    name = input("Who said it? ")
    # print(f'{name} says, "{quote}"')
    print(name + ' says, "' + quote + '"')
