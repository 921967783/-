#coding:utf-8
#�α�
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
#popȥ��ĩβ��Ԫ�أ�Ҳ����ָ��pop(0)
pop_guest = guests.pop();

#�滻Ԫ��ֻҪֱ��ָ���滻������
guests[0] = "xinlaid";
for guest in guests:
		print("new invited list is " + guest + "\n");


