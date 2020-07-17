# import time
from collections import OrderedDict
# with open('C:\\Users\\ADMIN\Desktop\\py-files\\pyproject\\wordlist.txt') as f:
#     line1 = f.read().splitlines()

# with open('C:\\Users\\ADMIN\Desktop\\py-files\\pyproject\\list2.txt') as f:
#     line2 = f.read().splitlines()

# with open('C:\\Users\\ADMIN\Desktop\\py-files\\pyproject\\list3.txt') as f:
#     line3 = f.read().splitlines()

# with open('C:\\Users\\ADMIN\Desktop\\py-files\\pyproject\\list3.txt') as f:
#     line3 = f.read().splitlines()

# list_1 = line1
# list_2 = line2
# list_3 = line3
# # print(list_3)
# # time.sleep(500)
# resultList = list(list_1 + list_2)
# final = list(list_3 + resultList)

# # print(resultList)
# password = []
# password = final

# with open('passwordlist.txt', 'r') as f:
#     res = list(OrderedDict.fromkeys(f)) 
#     print(res)

with open('password.txt', 'r') as f:
    count = 0
    # for listitem in password:
    # filehandle.write('%s\n' % listitem)
    for line in f:
        count += 1
print("Total number of lines is:", count)

with open('passwordlist.txt', 'r') as pl:
    count = 0
    # pl.write('%s\n' % passcode)
    for line in pl:
        count += 1
print("Total number of lines is:", count)
# # print(line2)
