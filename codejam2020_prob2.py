# -*- coding: utf-8 -*-
"""codejam2020_prob2.ipynb

Automatically generated by Colaboratory.
"""

#number of test cases
no_test=int(input())

for j in range(no_test):
    input_string=input()
    input_list=list(input_string)

    final=[]
    for i in range(len(input_list)):
        a=input_list[i]
        if(a=='0'):
            final.append('0')
        elif(a=='1'):
            final.append('(')
            final.append('1')
            final.append(')')
        elif(a=='2'):
            final.append('(')
            final.append('(')
            final.append('2')
            final.append(')')
            final.append(')')
        elif(a=='3'):
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('3')
            final.append(')')
            final.append(')')
            final.append(')')
        elif(a=='4'):
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('4')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
        elif(a=='5'):
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('5')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
        elif(a=='6'):
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('6')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
        elif(a=='7'):
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('7')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
        elif(a=='8'):
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('8')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
        elif(a=='9'):
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('(')
            final.append('9')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')
            final.append(')')

#Cancelling the brackets
    x=1
    y=0
    for i in range(len(final)):
        while(x<len(final) and y<len(final)):
            if(final[y]==')' and final[x]=='('):
                del final[y]
                del final[x-1]
                if(y!=0):
                    x-=1
                    y-=1
            else:
                x+=1
                y+=1
                break
    print('Case #{}: {}'.format(j+1,''.join(final)))