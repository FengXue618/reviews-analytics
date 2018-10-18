# 54 [程式练习] 留言分析程式

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 500000 == 0:
			print(len(data)) 
print('每50万印出一次进度，data总长为', len(data))
#print(len(data)) #加上这一行就能知道读取进度了
