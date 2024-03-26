# text = input().upper()

# check = {}
# for i in text:
#     if i in check:
#         check[i] += 1
#     else:
#         check[i] = 1

# max_val = 0
# error = 0
# for key, value in check.items():
#     if max_val < value:
#         max_val = value
#         result = key
#         error = 0
#     elif max_val == value: # 최대값이 동일한 것 체크
#         error += 1

# if error == 0:
#     print(result)
# else:
#     print("?")


# 메모리 33076 KB
# 시간 208 ms

### set 튜플을 활용한 풀이
word = input().upper()
word_list = list(set(word))  # 파이썬 집합 자료형을 통해서 중복을 한다.

'''
중복을 허용하지 않는다.
순서가 없다(Unordered)
'''

check = []

for i in word_list:
    #문자가 몇 개있는지 확인
    cnt = word.count(i)
    # print(i ,cnt) # S 4 P 1 I 4 M 1 ... 로 출력

    # word_list의 순서에 맞게 개수를 유지하는 list인 check에 개수 유지
    check.append(cnt)

#최대값이 여러개 있으면 ? 출력
if check.count(max(check)) >= 2:
    print("?")
else:
    print(word_list[check.index(max(check))]) # check리스트에서 가장 큰값의 index를 통해서 word_list를 출력

# 메모리 33076 KB
# 시간 80 ms