import student

ls = []
ch = 0
  
print("\nOperations used:\n")
print("\n1.Add Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Exit")
  

while ch != 5:
	print("\n\nEnter Choice:")
	ch = int(input())
	if(ch == 1):
		temp = student.add()
		ls.append(temp)
		 
	elif(ch == 2):
		print("\n")
		print("\nList of Students\n")
		student.display(ls)
		     
	elif(ch == 3):
		print("Enter rollNo :" )
		rn = input()
		i = student.search(rn,ls)
		 
	elif(ch == 4):
		print("Enter rollNo :" )
		rn = input()
		ls = student.delete(rn,ls)
		print("After deletion")
		student.display(ls)
		     
print("Thank You !")
