#coding:utf-8
#�α�
guests = ['nainai','yeye','zj'];
print(len(guests));
for guest in guests:
	print("my invited guest is " +  guest +"\n");
	
#ѭ����ȡ�б�����Ԫ��ֱ��ֻ��������Ȼ�������������
for guest in guests:
	sorry_guest = guests.pop();
	print("sorry " + sorry_guest + " can't arrive" + "\n");
	if len(guests) == 2:
		break;

for guest in guests:
	print("only two people can be invited,there are " + guest + "\n");
