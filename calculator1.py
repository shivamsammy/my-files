from math import *
print(" THIS IS A CALCULATOR :")
num1=float(input(" ENTER THE FIRST NUMBER :"))
num2=float(input(" ENTER THE SECOND NUMBER :"))
task=input(" ENTER THE TASK YOU WANT TO PERFORM :").strip()
def calculator (num1,num2,task):
        j=0
    # if task== True:
        if task=="+":
            return num1+num2
        if task=="-":
            return num1-num2
        if task=="*":
            return num1*num2
        if task=="/":
            return num1/num2
        if task=="^":
            return num1**num2
        if task=='!':
            s=1
            for i in range(1,int(num1+1)):
                s=s*i
            return s
        if task=="`":
            return 1/num1
        if task=="/-":
            return sqrt(num1)
        if task=="s":
            return sin(num1)
        if task=="c":
            return cos(num1)
        if task=="t":
            return tan(num1)
        if task=="cs":
            return 1/sin(num1)
        if task=="sec":
            return 1/cos(num1)
        if task=="ct":
            return 1/tan(num1)
        if task=='C':
            def factorial(a):
                o = 1
                for i in range(1, a + 1):
                    o = o * i
                return o
            e=factorial(int(num1))
            r=factorial(int(num2))
            t=factorial(int(num1-num2))
            return( e/(t*r))
        if task=="b":
            return bin(int(num1))
        if task=='d':
            ff=qq=0
            ss=str(num1)
            ss1=ss[2:]
            for ii in ss1:
                ff=ff+1
                qq= qq + ((ord(ii)) * (2**ff))
            return qq



        # else:
        #     return False
result= calculator(num1,num2,task)
print("  THE RESULT IS : ", result)





