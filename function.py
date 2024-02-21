# def largestnumber(numbers):
#     biggest_num =numbers[0]
#     for num in numbers:
#         if num > biggest_num:
#             biggest_num =num
#     return biggest_num
# print(largestnumber([10,20,30,40,50,60,70,80,90,100])) 


# def vowel_count(str):
#     count=0
#     vowel=set("aeiouAEIOU")
#     for alphabet in str:
#         if alphabet in vowel:
#             count=count+1
#     print("no.of vowels:",count)
# str="GeeksforGeeks"
# vowel_count(str)      

# def sum(numbers):
#     total=0
#     for x in numbers:
#         total +=x
#     return total
# print(sum((8,2,3,0,7))) 

# def all_upper(my_list):
#     return [x.upper() for x in my_list]
# print(all_upper(["hello world"]))

# def maximum(a,b,c):
#     if(a>=b)and(a>=c):
#         largest=a
#     elif(b>=a)and(b>=c):
#         largest=b
#     else:
#         largest =c
#     return largest
# a=10
# b=14
# c=12
# print(maximum(a,b,c))

# def multiplyList(myList):
#     result=1
#     for x in myList:
#         result=result*x
#     return result
# list1=[1,2,3]
# list2=[3,2,4]
# print(multiplyList(list1))
# print(multiplyList(list2))

# def my_function(x):
#     return x[::-1]
# mytxt=my_function("123abcd")
# print(mytxt)

# def evennumbers(list,n=0):
#     if n==len(list):
#         exit()
#     if list[n]%2==0:
#         print(list[n],end=" ")
#         evennumbers(list,n+1)
# list1=[2,4,6,8,7,9,3]
# print("even numbers in the list:",end=" ")
# evennumbers(list1)


