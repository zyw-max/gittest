#!/usr/bin/python
#-*-cod:utf-8-*-

# for i in range(-3, 4):
#     # 空格
#     for j in range(3 - abs(i)):
#         print(' ', end='')
#     # *
#     for k in range(2 * abs(i) + 1):
#         print('*', end='')
#     print()


# n=input().split()
# i=1
# while True:
#     if ((1+i)*(i+1)//2-1)<=int(n[0])<((3+i)*(i+3)//2-1):
#         k=i
#         a=int(n[0])-((1+i)*(i+1)//2-1)
#         break
#     i+=2
# add=-2
# x=k
# while True:
#     print(" "*((k-x)//2)+n[1]*x)
#     x+=add
#     if x==1:
#         add=2
#     if x>k or x<=0:
#         break
# print(a)

import pytest
d = [(1,2),(1,3)]
@pytest.fixture(params=d)
def f(request):
    return request.param
def test_1(f):
    print(f[0])
    print(f[1])