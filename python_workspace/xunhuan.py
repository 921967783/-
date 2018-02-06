#coding:utf-8
#嘉宾
guests = ['nainai','yeye','zj'];
print(len(guests));
for guest in guests:
	print("my invited guest is " +  guest +"\n");
	
#循环截取列表最后的元素直到只有两个，然后输出邀请名单
for guest in guests:
	sorry_guest = guests.pop();
	print("sorry " + sorry_guest + " can't arrive" + "\n");
	if len(guests) == 2:
		break;

for guest in guests:
	print("only two people can be invited,there are " + guest + "\n");
