#این پروژه یک سیستم مدیریت نمرات دانش‌آموزان است که با استفاده از لیست، شرط‌ها، حلقه‌ها و گرفتن ورودی از کاربر ساخته شده است.
##کارهایی که برنامه انجام می‌دهد:
#اضافه کردن دانش‌آموز (نام + نمره)
#نمایش کل دانش‌آموزان
#محاسبه میانگین نمرات
#بررسی وضعیت قبولی/رد شدن دانش‌آموز
#مکان خروج از برنامه
#این پروژه باعث می‌شود مفاهیم زیر را کامل یاد بگیری:
#یست‌های چندبعدی
#دسترسی به اندیس‌ها
#شرط‌ها و حلقه‌ها
#منوی تعاملی
# ا#لگوریتم محاسبه میانگین
#جستجو در لیست
#:white_check_mark: 
#This project is a Student Grade Management System built using Python.
#It uses lists, loops, conditions, and user input to manage students and their grades.
#The program supports:
#Adding a student (name + grade)
#Displaying all students
#Calculating the average grade
#Checking if a student has passed or failed
#Exiting the program
#Skills practiced in this project:
#Working with 2D lists
#Looping through lists
#Conditional logic
#Interactive menu systems
#Average calculation algorithm
#Searching inside a list



students=[]
while True:
    print("-----Student grade management-----")
    print("1 = Add student")
    print("2 = Show all students")
    print("3 = caculate average grade :")
    print("4 = Check student status:")
    print("5 = Exit")

    choice=input("Choose an option (1-5):")
    if choice == 1:
     name=input("Enter student name:")
     score=input("Enter student score:")
     students.append([name,score])
     print("student added successfully")
    if choice == 2:
     if not students:
          print("No students found")
    else:
       for i in students:
            print("name:",students[0],"score:",students[1])
    if choice==3:
       if not students:
            print("No students to calculate average")
       else:
            total=0
            for i in students:
                total+=students[1]
                average=total/len(students)
                print("Average grade:", average)
    if choice==4:
        search_name=input("Enter student name to Check:")
        found=False
        for t in students:
            if students[0]==search_name:
                found=True
            if students[1]>=10:
                print(search_name,"has pssed")
            else:
                print(search_name,"has failed")
                break
        else:
            if not found:
                print("Students not found!")
            elif choice==5:
                print("Exiting program")
                break
            else:
                print("Invalid choise ..Pleas try again")
           
       
          