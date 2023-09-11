#guess the number name
import random
num = random.randint(1,100)
while True:
	numa = input('猜猜数字是什么：')
	numa = int(numa)
	if numa == num:
		print('你猜对啦！')
		break
	elif numa > num:
		print('猜大了一些哟，继续猜')
	elif numa < num:
		print('猜小了一些哟，继续猜')