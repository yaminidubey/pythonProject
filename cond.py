list1 = eval(input("enter an four number"))
print(list1)
if list1[0] > list1[1] and list1[0] > list1[2] and list1[0] > list1[3]:
   print(list1[0])
elif list1[1] > list1[0] and list1[1] > list1[2] and list1[1] > list1[3]:
  print(list1[1])
elif list1[2] > list1[0] and list1[2] > list1[1] and list1[2] > list1[3]:
    print(list1[2])
else:
   print(list1[3])

