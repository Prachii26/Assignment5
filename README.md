# Assignment 5

Module 6: Data Structures and Strings in Python


## Task 1

Create a Dictionary of Student Marks

Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.



### Code

```python
data={"Alice":85,"Tom":92,"Harry":78,"Jenny":81}
name=input("Enter student's name: ")
if name in data.keys():
    print("{} marks: {}".format(name,data[name]))
else:
    print("Student not found")
```

### Output

```
Enter student's name: Alice
Alice marks: 85
```
```
Enter student's name: John
Student not found
```
## Task 2
Demonstrate List Slicing 

Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

### Code

```python
list=[1,2,3,4,5,6,7,8,9,10]
ext=list[0:5]
rev=ext[::-1]
print("Orignal list: {}\nExtracted first five elements: {}\nReversed extracted elements: {}".format(list,ext,rev)) 
```

### Output

```
Orignal list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
```
