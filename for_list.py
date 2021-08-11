array = [273, 32, 103, 57, 52]

for i in array :
    print(i)

for character in "안녕하세요" :
    print("-", character)

print()

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers :
    if number >= 100 :
        print("- 100이상의 수 :",number)
        
print()

numbers_a = [273,103,5,32,65,9,72,800,99]


for number_1 in numbers_a :
    if number_1 % 2 == 0 :
        print(number_1,"는 짝수입니다.")
    else :
        print(number_1,"는 홀수입니다.")

print()
 
for number_2 in numbers_a :
    number_str = str(number_2)
    print(number_2, "는",len(number_str),"자릿수입니다.")

print()
    
list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
    ]

for list_a in list_of_list :
    for list_b in list_a :
        print(list_b)

print()

numbers_5 = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers_5 :
    output[(number+2) %3].append(number)

print(output)
