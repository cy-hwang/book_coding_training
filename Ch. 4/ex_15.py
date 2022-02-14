"""
# 목표: 사용자 로그인 증명을 검증하는 간단한 프로그램을 작성하라.
       프로그램은 사용자 이름과 암호를 입력 받은 다음, 미리 저장된 사용자 이름에 대한 암호를 비교하여 암호가 일치하면 "Welcome!"을,
       그렇지 않으면 "That password is incorrect"를 출력한다.

# 출력 예시
  What is the password: 12345
  That password is incorrect.
  ---
  What is the password: abc123
  Welcome!

# 제약 조건
  - 이 문제를 해결하기 위해 if/else 문을 사용할 것
  - 사용자 이름과 암호는 대소문자를 구별하도록 할 것

# 도전과제
  1. 암호를 입력할 때 화면에 아무것도 나타나지 않도록 하기 위해서는 어떻게 해야 할 지 고민해보자
  2. 사용자 이름과 암호로 구성된 map을 만들어 사용자 이름과 암호 조합을 찾도록 하라
  3. 암호를 평문으로 저장하는 대신 Bcrypt를 이용하여 암호화한 다음 저장하자. 그리고는 사용자로부터 입력 받은 암호를 비크립트로 동일하게 암호화한 후
     map에 저장된 암호와 비교하도록 프로그램을 수정해보자
"""
from getpass import getpass
import bcrypt

USER = {
    "user1": b"$2b$12$45CTd9tzWllRKMizJMVSt.qCCafIuY4vg7aPXBKTtY3godFh2kug2",  # 123
    "user2": b"$2b$12$kvk9GY6pVCQQbjVOuW6YvefoctNs5FOw36onWNS1qbF7WC1CSMOV2",  # 345
}

if __name__ == "__main__":
    user_id = input("What is the ID: ")
    password = getpass("What is the password: ")

    # print(bcrypt.hashpw(bytes(password, "utf-8"), bcrypt.gensalt())) # get password hash

    if (user_id in USER) and bcrypt.checkpw(bytes(password, "utf-8"), USER[user_id]):
        print("Welcome!")
    else:
        print("That password is incorrect.")


"""
# getpass.getpass: 암호를 입력할 때 화면에 아무것도 나타나지 않도록 
    getpass.getpass(prompt='Password: ', stream=None)
    Prompt the user for a password without echoing. The user is prompted using the string prompt, which defaults to 'Password: '.

# string -> byte
    bytes(str, "utf-8")
    
# bcrypt hashing
    import bcrypt
    bcrypt.hashpw(bytes(password, "utf-8"), bcrypt.gensalt()) # str -> hash
    bcrypt.checkpw(bytes(password, "utf-8") # value comparison
"""
