# 재귀함수를 통해 중첩리스트 제거

def flatten(data):
    output = []

    for item in data:
        if type(item) == list:
            output += flatten(item)

        else:
            output.append(item)

    return output

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본:", example)
print("변환:", flatten(example))
            
print()

person_min = 2      # 앉힐수있는 최소사람수
person_max = 10     # 앉힐수있는 최대사람수
person_all = 100    # 전체사람의 수

memo = {}

def group_sit(person_remain,person_sit): #남은사람의 수 , 앉힌사람의 수
    key = str([person_remain, person_sit])

    if key in memo:
        return memo[key]
    if person_remain < 0:
        return 0
    if person_remain == 0:
        return 1

    count = 0
    for i in range(person_sit, person_max + 1):
        count += group_sit(person_remain - i, i)

    memo[key] = count

    return count

print(group_sit(person_all, person_min))
