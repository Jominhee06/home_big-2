# name = "KIm"
# email = "yun@naver.com"
# addr = "Seoul"

# def print_business_card(name, email, addr):
#     print("-"*25)
#     print("Name: %s" % name)
#     print("E-mail: %s" % email)
#     print("Office Address: %s" % addr)
#     print("-"*25)

# print_business_card(name,email,addr)

print("start")

#빈 클래스 정의
# class BusinessCard:
#     def set_info(self,name,email,addr):
#         self.name = name
#         self.email = email
#         self.addr = addr
        
#     def print_business_car(self):
#         print("-"*25)
#         print("Name: %s" % self.name)
#         print("E-mail: %s" % self.email)
#         print("Office Address: %s" % self.addr)
#         print("-"*25)

# member1 = BusinessCard()
# member1.set_info("Yuna Kim", "yunaki@naver.com", "Seoul")
# print(member1.print_business_car())


#시작부터 변수를 입력해줘야하는 클래스
# class BusinessCard:
#     def __init__(self,name,email,addr):
#         self.name = name
#         self.email = email
#         self.addr = addr
        
#     def print_business_car(self):
#         print("-"*25)
#         print("Name: %s" % self.name)
#         print("E-mail: %s" % self.email)
#         print("Office Address: %s" % self.addr)
#         print("-"*25)

# member1 = BusinessCard("Kangsan Lee", "kangsan.lee", "USA")
# print(member1.print_business_car())

#생성자는 클래스를 생성하자마자 실행된다.
# print("medium")
# class MYCLASS:
#     def __init__(self):
#         print("객채가 생성되었습니다.")

# inst1 = MYCLASS()

class FOO:
    def fun1():
        print("function1")
    def fun2(self):
        print(id(self))
        print("function2")
f = FOO()
print(id(f))
f.fun2()


