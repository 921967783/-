#coding:utf-8

rivers = ['henhe','changjiang','huanghe','beijiaerhu','niluohe'];
print(len(rivers));
print(rivers);
print(sorted(rivers));

print(rivers);
#sorted�Ǻ����������µ��б�sort��reverse���Ƿ�����ֱ�Ӷ��б���в��������������
print(sorted(rivers,reverse=True));

print(rivers);

rivers.reverse();
print(rivers);
rivers.reverse();
print(rivers);

rivers.sort();
print(rivers);
rivers.sort(reverse=True);
print(rivers);
