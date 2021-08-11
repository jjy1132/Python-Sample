output = [array for array in range(1,101) if "{:b}".format(array).count('0') == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:",sum(output))
