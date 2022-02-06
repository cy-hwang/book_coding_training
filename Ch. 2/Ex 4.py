"""
# 목적: 명사, 동사, 형용사, 부사에 해당되는 단어를 입력 받은 후 여러분이 만든 이야기에 넣어 완성된 이야기를 출력해보자

# 출력 예시
  Enter a noun: dog
  Enter a verb: walk
  Enter an adjective: blue
  Enter an adverb: quickly
  Do you walk your blue dog quickly? That's hilarious

# 제약조건
  - 이 프로그램에서는 한 개의 출력문만 사용할 것
  - 만일 사용하는 프로그래밍 언어가 문자열 보간이나 문자열 대체를 지원하는 경우, 출력문을 만드는데 활용할 것

# 도전과제
  - 입력할 수 있는 단어를 더 늘려 이야기를 확장시켜 보자
  - 대답에 따라 이야기가 만들어지는 브랜칭 스토리를 구현해보자. 브랜칭 스토리 개념은 4장 '의사 결정'에서 확인할 수 있다.
"""

if __name__ == "__main__":
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious")
