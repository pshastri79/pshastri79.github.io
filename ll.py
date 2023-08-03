class Node:
       def __init__(self, dataval: str):
        self.dataval = dataval;
        self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

while list1.headval:
    print(list1.headval.dataval)
    list1.headval = list1.headval.nextval