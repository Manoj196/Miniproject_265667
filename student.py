def add():
    print("Enter Name")
    name = input() 
    print("Enter Roll No")
    rollno = input() 
    print("Enter m1")
    m1 = input() 
    print("Enter m2")
    m2 = input()
    return [name, rollno, m1, m2]

# Function to display student details     
def display(ls):
    for i in range(len(ls)):
        print("Name   : ", ls[i][0])
        print("RollNo : ", ls[i][1])
        print("Marks1 : ", ls[i][2])
        print("Marks2 : ", ls[i][3])
        print("\n")    

# Search Function    
def search(rn,ls):
    for i in range(len(ls)):
        if(ls[i][1] == rn):
            print("Student Found : ")
            print("Name   : ", ls[i][0])
            print("RollNo : ", ls[i][1])
            print("Marks1 : ", ls[i][2])
            print("Marks2 : ", ls[i][3])    
            return i
# Delete Function                                  
def delete(rn,ls):
    i = search(rn,ls)      
    ob = ls[i]
    ls.remove(ob)
    return ls
