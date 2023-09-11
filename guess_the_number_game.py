#guess the number name
import random
start = input('请决定随机数字范围开始值：')
end = input('请决定随机数字范围结束值：')
start = int(start)
end = int(end)
num = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count +1
	numa = input('猜猜数字是什么：')
	numa = int(numa)
	if numa == num:
		print('你猜对啦！')
		print('这是你猜的第', count, '次')
		break
	elif numa > num:
		print('猜大了一些哟，继续猜')
	elif numa < num:
		print('猜小了一些哟，继续猜')
	print('这是你猜的第', count, '次')