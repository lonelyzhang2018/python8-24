#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
'''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
#创建自己的模块
#import mymodule
#mymodule.sayhi()
#print('Version',mymodule.__versions__)

from mymodule import sayhi, __versions__
sayhi()
print('Version',__versions__)

print(os.getcwd())

#for循环遍历
l = [1,2,3,4,5,6,7]
for i in range(len(l)):
    print(i,  l[i])

print ('--------------------')
#while循环遍历
index = 0
while index < len(l):
    print(index, l[index])
    index+=1
print ('--------------------')
#index结合for循环遍历
index = 0
for i in l:
    print(index,  i)
    index += 1

print ('--------------------')
#拉链(zip)方法遍历
for i ,v in zip(range(len(l)), l):
    print (i, v)

print ('--------------------')
#enumerate遍历方法
for i, v in enumerate(l):
    print (i , v)

def fib(max):
    index = 0 
    a, b = 0, 1
    while index < max:
        yield index, a
        a, b= b, a+b
        index +=1

print ('--------------------')
for i , v in fib(10):
    print (i , v)


number  = 23
while True:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.') # New block start
        print('(but you do not win any prizes!)') # New block ends here
        break     #this causes the while loop to stop
    elif guess < number:
        print('No, it is a little higher than that') # Another block
        # You can do whatever you want in a block ...
    else:
        print('No, it is a little lower than that')
        # you must have guess > number to reach here
    for i in range (guess):
        print (i)
    else :
        print ( 'The for loop is over' )
print('Done')
# This last statement is always executed, after the if statement is

def printMax(a,b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to',b)
    else:
        print(b, 'is maximum')

printMax(100,200)

#局部变量/全局语句
x = 50
def func():
    global x     #global 语句被用来声明x 是全局的
    print('x is', x)
    x = 2
    print('Changed local x to', x)
func()
print('x is still', x)

#非局部语句
def make_counter(): 
    y = 0 
    print('y is',y)
    def counter(): 
        nonlocal y   #将非局部变量y 变成全局变量y
        y += 1 
        print('Changed local y to',y)
        return y 
    return counter

def make_counter_test(): 
  mc = make_counter() 
  print(mc())
  print(mc())
  print(mc())

make_counter_test()

#关键参数
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)

def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        print ('number::'+ str(number))
        count += number
        print ('count::'+ str(count))
    for key in keywords:
        print ('keywords:'+str(keywords[key]))
        count += keywords[key]
    return count

print(total(10, 1, 2, 3, vegetables=50, fruits=100))

#文档字符
def printMax(x, y):
    '''Prints the maximum of two numbers.
    The two values must be integers.'''
    x = int(x) # convert to integers, if possible
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

printMax(3, 5)
print(printMax.__doc__)
print ('--------------------')
print(printMax.__str__)
print ('--------------------')
print(printMax.__hash__)

print('The command line argumnts are:')
for i in sys.argv:   #字符串的列表
    print (i)

print('\nThe pythonpath is ',sys.path,'\n')

age = 25
name = 'Swaroop'
print('{0} is {1} years old'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of '
    'Python'))
print('{0:_^11}'.format('hello'))

# 首先，我们来看一下在输入的sys 模块上使用dir。我们看到它包含一个庞大的属
# 性列表。
# 接下来，我们不给dir 函数传递参数而使用它，默认地，它返回当前模块的属性
# 列表。注意，输入的模块同样是列表的一部分。
print (dir(sys))
del make_counter_test
print (dir())


if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')




