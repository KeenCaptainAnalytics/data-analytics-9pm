
list1 = [10, 20,30,40,150,78, 93, 12, 8, 54]

max= list1[0] #150
secondMax = list1[0] #93

for ele in list1:
    if(ele > max):
        secondMax= max
        max= ele
    elif  (ele>secondMax):
        secondMax= ele
    else:
        pass

print(max)
print(secondMax)

# sum =0
#
# for ele in list1:
#     # print(ele)
#     sum=sum+ele
#
# print(sum)

# for i in range(0,len(list1)):
#     # print(list1[i])
#     sum=sum+list1[i]
#
# print(sum)

# Lists are collection of data/elements
# these elements are ordered
# mutable
# data/elemnts => can be of different types

# list1 = ["red","blue","green","brown","yellow","green"]
#
#
# list1.clear();
# print(list1)

# print(list1[2:5])
# print(list1[3::2])
# print(list1[-2:-9:-2])

# list2 =  list1.copy();
# list3 = list1
# list2.append("list2")
# list3.append("list3")
# print(list1)
# print(list2)
# print(list3)

# list1.sort()
# print(list1)

# list1.reverse();

# list1.remove("green")



# ans= list1.pop(2)
# # list1.insert(-2,"teal" )
# print(list1)
# print(ans)

# list1.append(1234)
# list1.append("golden")
# print(list1)
# print(list1.index("green",6, 10))


# num = list1.count("green")
# print(num)


# print(len(list1))

# print(list1[3])

# list2 = ["red", 123 , ["red","blue"]]
#
# print(list1)
# print(list2)
