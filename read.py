# 54讲 流言分析程式

data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print(len(data))
#执行结果：1000000
#FengdeMBP:reviews-analytics fengxue$ 
# 引出第一笔来看看
print(data[0])
print('~~~~~~~~~~~')
#1000000
#These are very comfortable but I took one star away because they took a little time to break in, unlike my Clarks Wave sandals which were immediately comfortable.  I was looking for a dressier alternative to the Waves which feel wonderful but look very utilitarian. The Leisa looks prettier but you are giving up some comfort.  The straps are a bit thin and stiff so they dug in and chafed a little until I figured out how to adjust them (for me they work best when I keep the front strap snug but the back strap as loose as possible).  Now that they are broken in I look forward to wearing them on my upcoming vacation - they'll be great for walking around and exploring while also looking cute with my summer dresses.
#FengdeMBP:reviews-analytics fengxue$ 
print(data[1])
#These are very comfortable but I took one star away because they took a little time to break in, unlike my Clarks Wave sandals which were immediately comfortable.  I was looking for a dressier alternative to the Waves which feel wonderful but look very utilitarian. The Leisa looks prettier but you are giving up some comfort.  The straps are a bit thin and stiff so they dug in and chafed a little until I figured out how to adjust them (for me they work best when I keep the front strap snug but the back strap as loose as possible).  Now that they are broken in I look forward to wearing them on my upcoming vacation - they'll be great for walking around and exploring while also looking cute with my summer dresses.

#~~~~~~~~~~~
#I love these boots. I have a wide foot and needed comfortable boots that I can wear all day without getting tired and still look classy.These boots were perfect and oh so comfortable. Everyone made a comment about how great they look.


