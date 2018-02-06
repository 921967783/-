#coding:utf-8

rivers = ['henhe','changjiang','huanghe','beijiaerhu','niluohe'];
print(len(rivers));
print(rivers);
print(sorted(rivers));

print(rivers);
#sorted是函数，返回新的列表；sort，reverse都是方法，直接对列表进行操作，这就是区别
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
