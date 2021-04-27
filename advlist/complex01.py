#!/usr/bin/env python3
# create a list called list1
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
# display list1
print(list1)

# display list[1] should only diplsay second element
print(list1[1])
# create a list with a single item
list2 = ["juniper"]
#extend list1 by list2
list1.extend(list2)
#dispaly new list1
print(list1)
# create list3
list3 = ["10.1.0.1", "10.2.0.1", "10.1.0.1"]
#use the append method to append list 1 to list 3
list1.append(list3)
#siaplY the new complex list1
print(list1)
print(list1[4])
