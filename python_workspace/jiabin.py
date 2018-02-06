#coding:utf-8
#嘉宾
guests = ['nainai','yeye','zj'];
for guest in guests:
	print("my invited guest is " +  guest +"\n");
	
no_guest = "nainai";
new_guest = "baba";
guests.remove(no_guest);
guests.insert(0,new_guest);
print("so " + no_guest + " can't arrive , but " + new_guest + " come");
for guest in guests:
		print("new invited list is " + guest + "\n");
del guests[0];
#pop去除末尾的元素，也可以指定pop(0)
pop_guest = guests.pop();

#替换元素只要直接指定替换就行了
guests[0] = "xinlaid";
for guest in guests:
		print("new invited list is " + guest + "\n");


