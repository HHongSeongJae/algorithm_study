text = input().upper()

check = {}
for i in text:
    if i in check:
        check[i] += 1
    else:
        check[i] = 1

max_val = 0
error = 0
for key, value in check.items():
    if max_val < value:
        max_val = value
        result = key
        error = 0
    elif max_val == value: # 최대값이 동일한 것 체크
        error += 1

if error == 0:
    print(result)
else:
    print("?")


# 메모리 33076 KB
# 시간 208 ms