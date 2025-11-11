'''
Python Operators
'''
#1.Arithematic Operators
a=20
b=10
print("a+b:",a+b) #a+b: 30
print("a-b:",a-b) #a-b: 10
print("a*b:",a*b) #a*b:200
print("a/b:",a/b) #a/b:2.0
print("a//b:",a//b) #a//b:2
print("a%b:",a%b) #a%b:0
print("a*b:",a*b) #a*b:10240000000000

#2.Comparison Operators
c=30
d=40
print('c<d:',c<d) #c<d: True
print('c>d:',c>d) #c>d: False
print('c<=d:',c<=d) #c<=d: True
print('c>=d:',c>=d) #c>=d: False
print('c==d:',c==d) #c==d: False
print('c!=d:',c!=d) #c!=d: True

#3.Assignment Operators
'''
var = var op val
var op= val
'''

e=100
e+=100
print('e+=100:',e) #e+=100: 200
e-=100
print('e-=100:',e) #e-=100: 100
e*=100
print('e*=100:',e) #e*=100: 10000
e//=100
print('e//=100:',e) #e//=100: 100
e**=10
print('e*=10:',e) #e*=100: 100000000000000000000
e%=3
print('e%=3:',e) #e%=100: 1
e/=5
print('e/=5:',e) #e/=100: 0.2

#4.Logical Operators
'''
F and F = F
F and T = F
T and F = F
T and T = T

F or F = F
F or T = T
T or F = T
T or T = T

not F = T
not T = F
'''

x=100
y=50

print("x%20==0 and y%20==0:",x%20==0 and y%20==0) #x%20==0 and y%20==0: False
print("x%20==0 or y%20==0:",x%20==0 or y%20==0) #x%20==0 or y%20==0: True
print("not x%20==0:",not x%20==0) #not x%20==0: False
print("not y%20==0:",not y%20==0) #not y%20==0: True

#5.Membership Operators
s='python programming'

print("'i in s:",'i' in s) #'i in s: True
print("'x not in s:",'x' not in s) #'x not in s: True

l=[1,2,3,4,5]
print("3 in l:",3 in l) #3 in l: True
print("10 not in l:",10 not in l) #10 not in l: True

t=(102,103,104,105)
print("108 in t:",108 in t) #108 in t: False
print("104 not in t:",104 not in t) #104 not in t: False

s={10,20,30,40}
print("40 in s:",40 in s) #40 in s: True
print("50 not in s:",50 not in s) #50 not in s: True

d={1:2,2:4,3:9,4:16,5:25}
print("1 in d:",1 in d) #1 in d: True
print("4 not in d:",4 not in d) #4 not in d: False


#6.Identity Operators
a=[1,2,3,4]
b=[1,2,3,4]
print('a is b:',a is b) #a is b: False
c=a
print('a is c:',a is c) #a is c: True
print('id(a):',id(a)) #id(a): 1616504692224
print('id(b):',id(b)) #id(b): 1616505860224
print('id(c):',id(c)) #id(c): 1616504692224


print('a is not b:',a is not b) #a is not b: True
print('a is not c:',a is not c) #a is not c: False