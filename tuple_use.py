[a,b] = [10,20]
(c,d) = (10,20)

print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)

print()

tuple_test = 10,20,30,40
print("#괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:",tuple_test)
print("type(tuple_test):", type(tuple_test))

print()

a1, b1, c1 = 10,20,30
print("#괄호가 없는 튜플을 활용한 할당")

print("a1:",a1)
print("b1:",b1)
print("c1:",c1)

print()

a2, b2 = 10,20

print("#교환 전 값")
print("a2:",a2)
print("b2:",b2)
print()

a2,b2 = b2,a2

print("#교환 후 값")
print("a2:",a2)
print("b2:",b2)
print()
