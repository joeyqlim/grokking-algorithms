2.1:
Lists.
Arrays have fast reads and slow inserts. Linked lists have slow reads and fast inserts. Because you’ll be inserting more often than reading, it makes sense to use a linked list. Also, linked lists have slow reads only if you’re accessing random elements in the list. Because you’re reading every element in the list, linked lists will do well on reads too.

2.2:
Linked list. Lots of inserts (orders). Orders are taken in order and not randomly accessed.

2.3:
(Sorted) Array. Binary search needs random access.

2.4:
Arrays have slow inserts as elements need to be shifted down, in order to have a sorted array for binary search to work.

2.5:
Array of linked lists would be slower than arrays for searching but faster for inserting. The elements in the array need not be shifted down.

Array of linked lists would be faster than linked lists for searching but _same amount of time_ for inserting. The number of elements are split into 26 linked lists instead of searching through one big linked list.
