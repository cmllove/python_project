# #name = input("what's your name:")
# #print ('hello,',name)
# #bir = int(input("when your birthday:"))
# #if bir >=15:
# #    print('hello,brother!')
# #else:
# #    print('GOOD TIME:',bir)
# #a=123
# #B=a
# #a='ABCX'
# #print (a)
# #a=2
# #a=a+2
# #print(a)
# #a='abc'
# #b=a
# #a='asdf'
# #print(b)
# #a='liu jiaqi'
# #print (a.upper())
# #print (a.lower())
# #print (a)
# #first_name='liu'
# #last_name='jiaqi'
# #full_name=first_name+" " + last_name
# #print(full_name.title())
# #print ('hello,' , full_name.title() ,'!')
# #a = "name:  a"
# #b = "JACK"
# #c = "MARY"
# #print (a,'\n\t',b,'\n',c,'\n\t',b)
# #print (a.rstrip().title())
# #print ('余额：')
# #print (2222-88-104-58+43-37-40-30-300-69+100-23-40-1190-30+719+250,'￥')
# #print ('''hello,\nWorld''')
# #age =int(input())
# #if age >= 18:
# #    print ('adult')
# #else:
# #    print ('teenager')
# #name = input("what's your name:")
# #print ('hello,',name)
# #a=123
# #a="ABC"
# #print (a)
# #name = 'Eric'
# #print('Hello!',name.upper()+"!")
# #print ('HELLO!',name+'!','Would u like sunny?')
# #name = 'A Bbbbbb \nccccc'
# #print (name.title())
# #print (name.lower())
# #print ('wife said'+','+':'+'No')
# #a='wife'
# #b=a+' said,:NO!'
# #print
# #print ('\u4\e2d')
# #print ('\u4e2d')
# #print ('中文'.encode('utf-8'))
# #print('zhongwen '.encode('ascii'))
# #print('中文English'.encode('utf-8'))
# #print('中文English'.encode('ascii'))
# #print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# #print('中'.encode('utf-8'))
# #print(b'\xe4\xb8\xad'.decode('utf-8'))
# #print(len(b'English'.decode('utf-8')))
# #print('中文'.encode('utf-8'))
# # print('\'%.3f = %010x\'' % (3,17))
# #print('%d = %010d%%' % (3,1))
# #print('%.8f' % 3.1415926535)
# #s1=100
# #s2=200
# #print( 'XIAOMING\'s score increased by:%.1f%%' % ((int(s2)-int(s1))/int(s1)*100))
# #r = (s2-s1)/s1*100
# #print('成绩提高了%.1f%%' % r)
# #print((int(s2)-int(s1))/int(s1))
# #print(r)
# # s1=input('first grade:');
# # s2=input('second grade:');
# # r=(int(s2)-int(s1))/int(s1)*100
# # name=input('请输入考生姓名：')
# # if int(s2)>int(s1):
# #     print('HELLO',name,'\nYour score increased by:%.5f%%'%r)
# # else:
# #      print('成绩没有增长')
# # classmates=['first','second','third']
# #
# # print(classmates[0])
# # print(len(classmates))
# # # classmates=[]
# # classmates.append('fourth')
# # classmates.insert(4,'fifth')
# # print(classmates)
# # print(classmates[1])
# # T_emp=('a','b',['c','d'])
# # print(T_emp)
# # T_emp[2][0]=['X']
# # T_emp[2][1]=['Y']
# # T_emp[2][0].append('e')
# # T_emp[2][1].insert(1,'f')
# # print(T_emp)
# # -*- coding: UTF-8 -*-
# # s=int(input('age:'))
# # if s<18:
# #     print('teenager')
# # else:
# #     print('adult','年龄：%.5f'%s)
# # a=0
# # b=100
# # # while b>0:
# # #     a=a+b
# # #     b=b-2
# # # print(a)
# # while a<=10:
# #     if a>5:
# #         break
# #     print(a)
# # #     a=a+1
# # a = {'Michael': 95, 'Bob': 75, 'Tracy':98}
# # b=('t',)
# # c=['y',]
# # # print(a['Tracy'])
# # # print('Tom' in a)
# # # c=input('NAME:')
# # # b=(a.get(c))
# # # if b == None:
# # #     a[c]=5
# # # else:
# # #     a[c] = 5
# # # # print(a)
# # # print(a['Bob'])
# # # print(b)
# # # print(c)
# # s1=set([1,2,3,4])
# # s2=set([2,3,5,6])
# # s3=['1',1,'a',3,7,'n']
# # s4=s3.sort()
# # # print(s1&s2)
# # # print([s1|s2])
# # s1.remove(1)
# # s1.add(9)
# # print(s4)
# # print(sorted(s3))
# #!/usr/bin/python
# # # -*- coding: UTF-8 -*-
# # aList = [123, 'Google', 'Runoob', 'Taobao', 'Facebook']
# # aList.sort()
# # print("List : ", aList)
# t1=(1,2,3)
# t2=(4,5,6)
# d1={t1:t2}
# print(d1[(1,2,3)])
# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x
# x=int(input('x:'))
# print(my_abs(x))
#-*-求解一元二次方程2x2 + 3x + 1 = 0 的解-*-
# -*- coding:UTF-8 -*-
# import math
# def quadratic(a,b,c):
#     dt=b*b-4*a*c
#     x1=-b+math.sqrt(dt)
#     x2=-b-math.sqrt(dt)
#     return (x1/2/a,x2/2/a)
# print(quadratic(2,3,1))
# def power(x):
#     return x*x
# print(power(2))
# def power(x,n):
#     s=1
#     while n>0:
#         n=n-1
#         s=s*x
#     return s
# print(power(5,0))
# print(power(5,n=2))
# def power(x,n):
#     s=1
#     if n==0:
#          return s
#     if n<0:
#         while n<0:
#             n=n+1
#             s=1/(s*x)
#             return s
#     else:
#         while n>0:
#             n=n-1
#             s=s*x
#             return s
# print(power(2,0))
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
# print(add_end())
# print(add_end(['2']))
# def person(name,age):
#     return 'name:',name
#
#
# print(person('jiaqi','18'))
# def enroll(name, gender):
#     print('name:', name)
#     print('gender:', gender)
#     return
# print(enroll('Sarah','F'))
# def calc(*number):
#     s=0
#     for n in number:
#         s=s+n*n
#     return s
#
# print(calc(1,2,3))
# print(calc(3,5))
# print(calc())
# def person(name,age,**other):
#     print('name:',name,'age:',age,'other:',other)
# print(person('jiaqi',12,a='b'))
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
print(person('liu',12,city='Beijing', addr='Chaoyang', zipcode=123456))
def per(name,age,*,city='BJ',job):
    print('name:',name,'age:',age,'city:',city,'job:',job)
print('jia',24,'TIANJIN','Engineer')
def product(*x):
    s=1
    for n in x:
        if not isinstance(n,(int,float)):
            raise TypeError('NUBMBERS ONLY')
        s=s*n
        return s
# a=(1,2,3)
print(product(6))
def res(n):
    if n==1:
        return 1
    s=n*res(n-1)
    return s
print(res(3))
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
print(fact(3))
L=[]
r=10
for n in range(0,r,2):
    L.append([n])
print(L)
print(L[0:5])
def range_even(x):
       n=[0,]
       s=0
       while s <= x:
           s=s+2
           n.append(s)
       return n
# print(range_even(10))
def trim(s):
    









