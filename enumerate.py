example_list = ["요소A","요소B","요소C"]

print("#단순 출력")
print(example_list)
print()

print("#enumerate() 함수 적용출력")
print(enumerate(example_list))
print()

print("#list()함수를 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("#반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i,value))
    
      
