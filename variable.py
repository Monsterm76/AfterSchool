#문제 1번
r =int(input("원의 반지름"))

s = r**2 * 3.14
l = 2 * 3.14 * r

print("원의 둘레:" ,l,"원의 넓이:",s)

#문제 2번

price = int(input("책 값"))
disc = int(input("할인율"))
dilvc = int(input("배송비"))

total = price * (100-disc)/100 + dilvc
print("가격:",total)

#문제 3번
from datetime import datetime
name = int(input("이름"))
age = datetime.today().year - yourbirth + 1
yourbirth = int(input("출생년"))
print(age,"살",name)

#문제 4번

print(datetime.today("Y%,M2%,D2%)) 
