polish_str="3 2 * 1 4 * +"

#scan from left to right once you got the operator make the operation save the     result again perform the operation
#result=3

polish_list = polish_str.split(" ")
# polish_list=[]
# for i in polish_str:
#   polish_list.append(i)

# print(polish_list)

####
temp=[]
operator=['*',"+","/","-"]

def operation(o,a,b):
    if o=="+":
        result=a+b
    if o=="-":
        result=a-b
    if o=="*":
        result=a*b
    if o=="/":
        result=a/b
    return result

for i,v in enumerate(polish_list):
    if v in operator:
        print(temp)
        leng=len(temp)
        arg1=temp.pop()
        print("arg1==>",arg1)
        arg2=temp.pop()
        print("arg2==>",arg2)
        result=operation(v,arg1,arg2)
        print("result==>",result)
        temp.append(result)
        print("temp in iteration==>",temp)
    else:
        temp.append(i)
        
