#!/usr/bin/env python
# coding: utf-8

# In[1]:


class student():
   
    def __init__(self):
        __name=""
        __level=0
        __nosubj=0
        subj={}
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
    def getlevel(self):
        return self.__level
    def setlevel(self,level):
        self.__level=name
    def getnosubj(self):
        return self.__nosubj
    def setnosubj(self,nosubj):
        self.__nosubj=nosubj        
    def getdata (self):
        self.__name=input("please enter your name:")
        self.__level=int(input("please enter your level :"))
        self.subj={}
        self.__nosubj=int(input("please enter the number of subject:"))
        for i in range(self.__nosubj):
            print("subject number#"+str(i+1))
            teacher=[]
            subject=input("please enter subject name:")
            teacher.append("teacher name -->")
            teachern=input("please enter your "+subject+" teacher name :")
            teacher.append(teachern)
            teacher.append("teacher salary -->")
            salary=int(input("please enter teacher salary :"))
            teacher.append(salary)
            teacher.append("student marks -->")
            mark=int(input("please enter the mark over 100:"))
            teacher.append(mark)
            self.subj[subject]=teacher
    def showdata(self):
        print("your name:"+self.__name)
        print("your level :"+str (self.__level))
        print("your subjects and subject teacher ")
        print(self.subj)
    def costs(self):
        the_cost=0
        for i in self.subj:
            the_cost=the_cost+self.subj[i][3]
        print ("the total costs")
        print(the_cost)
    def marks(self):
        
        total_marks=0
        for i in self.subj:
            total_marks=total_marks+self.subj[i][5]
        print ("the total marks over "+str(self.__nosubj*100))
        print(total_marks)
  
        


# In[5]:


no_student=int(input("please enter the number of the students:"))
students=[0] * no_student
for i in range(no_student):
    students[i]=student()
for i in range(no_student):
    print("student number#"+str(i+1))
    students[i].getdata()
   
    print("---------------------------------------------")
for i in range(no_student):
    print("student number#"+str(i+1))
    students[i].showdata()
   
    print("---------------------------------------------")
for i in range(no_student):
    print("student number#"+str(i+1))
    students[i].costs()
   
    print("---------------------------------------------")
for i in range(no_student):
    print("student number#"+str(i+1))
    students[i].marks()
   
    print("---------------------------------------------")
ones=0
twos=0
threes=0
fours=0
for i in range(no_student):
    
    if (students[i].getlevel()==1):
        ones=ones+1
    elif (students[i].getlevel()==2):
        twos=twos+1
    elif (students[i].getlevel()==3):
        threes=threes+1
    elif (students[i].getlevel()==4):
        fours=fours+1
print("the number of student in level one="+str(ones))
print("the number of student in level two="+str(twos))
print("the number of student in level three="+str(threes))
print("the number of student in level foue="+str(fours))
one=[]
two=[]
three=[]
four=[]
for i in range(no_student):
    
    if (students[i].getlevel()==1):
        one.append(students[i].getname())
    elif (students[i].getlevel()==2):
        two.append(students[i].getname())
    elif (students[i].getlevel()==3):
        three.append(students[i].getname())
    elif (students[i].getlevel()==4):
        four.append(students[i].getname())
print("the students in level one=")
print(one)
print("the students in level two=")
print(two)
print("the students in level three=")
print(three)
print("the students in level four=")
print(four)
arabic_teacher=0
english_teacher=0
physics_teacher=0
chimestry_teacher=0
biology_teacher=0
geology_teacher=0

for i in range(no_student):
    for j in students[i].subj:
        if (j=="arabic"):
            arabic_teacher=arabic_teacher+students[i].subj[j][3]
        elif (j=="english"):
            english_teacher=english_teacher+students[i].subj[j][3]
        elif (j=="physics"):
            physics_teacher=physics_teacher+students[i].subj[j][3]
        elif (j=="chimestry"):
            chimestry_teacher=chimestry_teacher+students[i].subj[j][3]
        elif (j=="biology"):
            biology_teacher=biology_teacher+students[i].subj[j][3]
        elif (j=="geology"):
            geology_teacher=geology_teacher+students[i].subj[j][3]
print("the total arabic teacher salary")
print(arabic_teacher)
print("the total english teacher salary")
print(english_teacher)
print("the total physics teacher salary")
print(physics_teacher)
print("the total chimestry teacher salary")
print(chimestry_teacher)
print("the total biology teacher salary")
print(biology_teacher)
print("the total geology teacher salary")
print(geology_teacher)

