list01=[
    [2,0,2,0],
    [2,2,0,0],
    [4,4,2,2],
    [4,4,0,0]
]
# def zero_list(list_01):
#     new_list=[]
#     for item in list_01:
#         if item!=0:
#             new_list.append(item)
#     for i in range(list_01.count(0)):
#         new_list.append(0)
#     return new_list

# print(zero_list([4,0,2,0]))
# def zero_list(list_01):
#     for a in len(range(list_01)):
#       new_list=[i for i in list_01[a] if i!=0]
#       new_list+=[0]*list_01[a].count(0)
#     return new_list
# print(zero_list(list01))
# print(zero_list([4,0,2,0]))
#调整
def zero_list(list_01):
    for i in list_01:
        if i==0:
            list_01.remove(0)
            list_01.append(0)
    return list_01
# print(zero_list([0,4,0,3,0,5,0]))
# def zero_list(list_01):
#     new_list_01=[]
#     for a in range(len(list_01)):
#         new_list=[i for i in list_01[a] if i!=0]
#         new_list+=[0]*list_01[a].count(0)
#         new_list_01.append(new_list)
#     return new_list_01
# print(zero_list(list01))
#合并
#合并
def merge(list_01):

    zero_list(list_01)
    for q in range(len(list_01)-1):
        if list_01[q]==list_01[q+1]:
           list_01[q]+=list_01[q+1]
           del list_01[q+1]
           list_01.append(0)

    return list_01
# print(merge([0,2,2,0]))

# print(merge([0,2,2,0]))

#左移
#左移
def move_left():
    for line in list01:
        global list_01
        list_01=line
        merge(list_01)
    return list01
print(move_left())



