## Arrays vs linked list operations runtimes


| Operation      | Array  | Linked List |
|----------------|--------|-------------|
| Insertion      | O(n)   | O(1)        |
| Reading        | O(1)   | O(n)        |
| Deletion       | O(n)   | O(1)*note        |


- NOTE: Only if you can directly access the node to be deleted. Otherwise, it is O(n) to find the node first. It is common practice to keep track of the first and last
items in a linked list for this reason.
- Arrays have fast reads and slow inserts. 
- Linked lists have slow reads and fast inserts.
- Lists are better if you want to insert elements into the middle.
- Arrays can access random elements individually whereas linked lists require traversal from the head.
- Additionally, arrays tend to use less memory because linked lists use extra memory 
for storing pointers.
Arrays tend to be used more often than linked list except in specific use cases.