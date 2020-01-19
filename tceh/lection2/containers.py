import collections 
listWithDuplicates = ["red", "green", "blue", "yellow", "blue", "blue", "blue", "yellow", "yellow"]

# counter tool 

cnt = collections.Counter()

for elem in listWithDuplicates:
	cnt[elem] += 1

print(cnt)