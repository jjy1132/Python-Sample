numbers = [1, 2, 3, 4, 5, 6]

#print("::".join(str(number) for number in numbers))
print("::".join(map(str,numbers)))

print()

numbers1 = list(range(1,10+1))

print("#홀수만 추출하기")
print(list(filter(lambda x: x%2 == 1,numbers1)))
print()

print("#3 이상, 7 미만 추출하기")
print(list(filter(lambda x: 3<=x<7,numbers1)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda x: x**2<50,numbers1)))
