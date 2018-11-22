#青蛙跳：一只青蛙一次可以挑1个台阶，也可以跳2个，求该青蛙跳上一个n级台阶一共有多少种跳法
#实质是斐波那契数列求和
def fogjump1(n):
    a=1
    b=2
    c=0
    if n <=0:
        return 0
    elif n==1 or n==2:
        return n
    else:
        for i in range(n-2):
            c=a+b
            a=b
            b=c
    return c
c=fogjump1(4)
print(c)

#进阶版青蛙跳：一只青蛙一次可以挑1个台阶，也可以跳2个....也可以跳n阶，求该青蛙跳上一个n级台阶一共有多少种跳法
def fogjump2(n):
    a = 1
    b = 2
    if n <= 0:
        return 0
    elif n == 1 :
        return n
    else:
        for i in range(n - 1):
            b=2*a
            a=b
    return b

d=fogjump2(4)
print(d)

