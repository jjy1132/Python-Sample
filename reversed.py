list_a= [1,2,3,4,5]
list_reversed = reversed(list_a)

print("# reversed() 함수")
print("reversed([1,2,3,4,5]):",list_reversed)
print("list(reversed([1,2,3,4,5])):", list(list_reversed))
print()

print("# reversed()함수와 반복문")
print("for i in reversed([1,2,3,4,5]):")
for i in reversed(list_a):
    print("-",i)

numbers = [1,2,3,4,5,6]

for i in reversed(numbers):
    print("첫번째 반복문: {}".format(i))

for i in reversed(numbers):
    print("두번째 반복문: {}".format(i))
