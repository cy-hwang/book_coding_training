"""
# 목표: 정년까지 몇 년 남았는지, 퇴직하는 해는 몇 년이 되는지를 계산하는 프로그램을 작성하라.
  이 프로그램은 현재 나이와 퇴직하고자 하는 나이를 입력 받아 다음의 출력 예와 같이 나타낸다.

# 출력 예
  What is your current age? 25
  At what age would you like to retire? 65
  You have 40 years left until you can retire.
  It's 2015, so you can retire in 2055.

# 제약조건
  - 수학 계산에 사용하기 전에 입력 값을 꼭 숫자로 변환시킬 것
  - 올해 년도를 프로그램에 직접 넣지 말 것. 대신 프로그래밍 언어를 통해 시스템 날짜를 구해서 사용할 것

# 도전 과제
  - 이미 퇴직했을 나이를 입력하면 음수 값이 출력되는 상황이 발생하는데, 이 상황을 해결하도록 프로그램을 수정해보자
"""

from datetime import datetime


def setValue(statement):
    condition = True

    while condition:
        val = input(statement)
        if val.isdigit():
            return int(val)
        else:
            print("Please input positive integer")


if __name__ == "__main__":
    currentAge = setValue("What is your current age? ")
    retireAge = setValue("At what age would you like to retire? ")
    remainingYear = retireAge - currentAge
    while remainingYear < 0:
        print("Inserted inappropriate retireAge.")
        retireAge = setValue("At what age would you like to retire? ")
        remainingYear = retireAge - currentAge

    print(f"You have {remainingYear} years left until you can retire.")

    currentYear = int(datetime.today().strftime("%Y"))
    print(f"It's {currentYear}, so you can retire in {currentYear + remainingYear}")

"""
datetime.today().strftime("%Y") : 현재 시스템 상의 locale 반영
"""
