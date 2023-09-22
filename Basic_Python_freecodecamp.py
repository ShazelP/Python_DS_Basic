#!/usr/bin/env python
# coding: utf-8

# # This is Python Tutorial

# This is our first program in python: It is just started here

# In[1]:


print("Hello World")


# $a=b+c$

# # Variables

# In[1]:


x = 3


# In[2]:


get_ipython().run_line_magic('whos', '# what variable is saved so far')


# In[3]:


print(type(x))


# In[4]:


x = 5.7


# In[5]:


get_ipython().run_line_magic('whos', '')


# In[6]:


print(type(x))


# In[7]:


abcd = 556.32


# In[8]:


get_ipython().run_line_magic('whos', '')


# In[9]:


a,b,c,d,f = 3,5,6.0,7.2,-3


# In[10]:


get_ipython().run_line_magic('whos', '')


# In[11]:


del abcd


# In[12]:


get_ipython().run_line_magic('whos', '')


# In[13]:


print(abcd)


# In[14]:


c = 2+4j


# In[15]:


print(type(c))


# In[16]:


s = "hellow how are you"


# In[17]:


print(type(s))


# # Operators

# In[18]:


get_ipython().run_line_magic('whos', '')


# In[19]:


sumOfaAndb = a+b #variables name should give you the look and feel what the data has


# In[20]:


print(sumOfaAndb)


# In[21]:


type(sumOfaAndb)


# In[22]:


type(a+d) #float is super set than int and Python follows the super set


# In[23]:


v = ((a+d)**3)/4


# In[24]:


print(v)


# In[26]:


s1 = "hellow"
s2 = "world"
s = s1+s2
print(s)


# In[27]:


10//3 #quotient


# In[28]:


10/3


# In[29]:


_ # stores the result of the above expression


# In[30]:


3x = 5 #can a variable name start with a digit i.e. 3x? NO


# In[31]:


@y = 4 #can't start a variable name with @


# In[32]:


*t=4 #can't start a variable name with * including special sign other then _


# In[33]:


_e = 6 # not recommended


# In[34]:


startingTimeOfTheCourse = 2.0


# In[35]:


get_ipython().run_line_magic('whos', '')


# # Bool

# In[36]:


a = True
b = True
c = False


# In[37]:


get_ipython().run_line_magic('whos', '')


# In[39]:


print(a and b)
print(a and c)
print(c and a)


# In[41]:


d = a or c
print(d)


# In[42]:


not(a)


# In[43]:


not(b)


# In[44]:


not(c)


# In[45]:


t = not(d)


# In[46]:


type(t)


# In[47]:


print(t)


# In[48]:


not((a and b) or (c or d))


# # Comparisons

# In[49]:


print(2<3)


# In[50]:


c = 2<3
print(type(c))
print(c)


# In[51]:


d = 3==4


# In[52]:


print(d)


# In[53]:


3==3.0


# In[54]:


x = 4
y = 9
z = 8.3
r = -3


# In[55]:


(x<y) and (z<y) or (r==x)


# In[56]:


(r==x) and (x<y) or (z>y)


# In[61]:


(True or False) and False # and first and then or


# In[62]:


print((not(2!=3)and Ture)or(False and True))


# In[63]:


print(round(4.556))


# In[64]:


print(round(4.345))


# In[67]:


print(round(4.556389,3))


# In[68]:


divmod(22,10)


# In[71]:


G = divmod(34,9)


# In[72]:


type(G)


# In[73]:


print(G)


# In[74]:


G[0]


# In[75]:


G[1]


# In[76]:


34//9


# In[77]:


34%9 #remainder


# In[78]:


isinstance(3,int) # is object a type of sth?


# In[81]:


isinstance(3.4,(float,int))


# In[83]:


isinstance(2+3j,(int,float,str,complex))


# In[84]:


pow(2,4) # same with 2**4


# In[85]:


2**4


# In[86]:


pow(2,4,7) #2**4%7


# In[87]:


x = input("enter a number :")


# In[88]:


type(x)


# In[89]:


x = int(x) #change the type of x as integer


# In[90]:


type(x)


# In[91]:


print(x-34)


# In[92]:


a = float(input("Enter a real number :"))


# In[93]:


type(a)


# In[94]:


b = float(input("Enter a real number : "))


# In[98]:


pow? #don't know how to use the function then add ?


# In[99]:


help(input) #don't know how to use the function then use help()


# In[101]:


a = int(input())
b = int(input())
if a>b:
    print(a)
    print("I am still inside if condition")
print("I am outside the if condition") # diff block which not depend on if condition/ regardless of the result, should print this


# In[103]:


a = int(input())
b = int(input())
if a>b:
    print(a)
if b>a:
    print(b)


# In[106]:


a = int(input())
b = int(input())
if a>b:
    print(a)
    print("if part")
else:
    print(b)
    print("else part")


# In[109]:


a = 10
b = 10
if a==b:
    print("Equal")
elif a>b:
    print("A")
else:
    print("B")
print("Not in if")


# In[111]:


a = int(input("Enter Marks :"))
if a >= 85:
    print("A Grade")
elif (a < 85) and (a >= 80): #write prenthesis makes it more readable
    print("A- Grade")
elif (a < 80) and (a >= 75):
    print("B Grade")
elif (a < 75) and (a >= 70):
    print("B- Grade")
else:
    print("Below Average")


# In[112]:


#esle 안쓰고 else 사용하기
a = 3
if a>10:
    print(">10")
elif not(a>10):
    print("Else part")


# In[114]:


a = int(input())
if a > 10:
    print(">10")
    print("Inside the top if")
    if a > 20:
        print(">20")
        print("Inside the nested if")
        if a>30:
            print(">30")
            print("inside the nested if of nested if")
        else:
            print("<=30")
            print("inside the else part of nested if of nested if")
    else:
        print("<=20")
        print("Inside the else part of nested if")
print("Outside all ifs")


# In[132]:


#single line comment
""" Multi line comment
User will enter a floating point number let say 238.915. 
Your task is to find out the integer portion before the point (in this case 238)
and then check if that integer portion is an even number or not
"""
x = float(input("Enter a real number :"))
y = round(x)
if x>0:
    if y>x:
        intPortion = y-1 #29.6
    else:
        intPortion = y
else:
    if y<x:
        intPortion = y+1
    else:
        intPortion = y

if intPortion%2 == 0:
    print("Evne")
else:
    print("Odd")


# In[119]:


round(-9.3)


# In[120]:


round(-9.6)


# In[133]:


n = int(input())
i = 1
while (i < n):
    print(i**2)
    print("This is iteration number:", i)
    i += 1 #i = i+1
print("Loop done")


# In[134]:


n = 10
i = 1
while True:
    if i%9 == 0:
        print("Inside if")
        break
    else:
        print("Inside else")
        i = i+1
print("done")


# In[135]:


n = 10
i = 1
while True:
    if i%9 != 0:
        print("inside if")
        i +=1
        continue
    print("something")
    print("somethingelse")
    break
    
print("done")


# In[137]:


L = []
for i in range(0,10,2): #0 start/10 end/ 2 step size
    print(i)
    L.append(i**2)
print(L)


# In[139]:


S = {"apple", 4.9, "cherry"}
i = 1
for x in S: #as long as the x in S
    print(x)
    i += 1
    if i == 3:
        break
    else:
        pass
else:
    print("Loop terminates with success")
print("Out side the loop")


# In[142]:


D = {"A":10, "B":-19, "C":"abc"}
for x in D:
    print(x, D[x])


# In[148]:


""" Given a list of numbers i.e. [1,2,4,-5,7,9,3,2], make another list
that contains all the items in sorted order from min to max. i.e. your 
result will be another list like [-5,1,2,2,3,4,7,9]
"""
L = [1,2,4,-5,7,9,3,2]
for j in range(len(L)): #length of L
    m = L[j]
    idx = j
    c = j
    for i in range(j,len(L)):
        if L[i]<m:
            m = L[i]
            idx = c
        c += 1
    tmp = L[j]
    L[j] = m
    L[idx] = tmp
print(L)


# In[150]:


#Refer stackoverflow answers
L = [1,2,4,-5,7,9,3,2]
m = L[0]
idx = 0
for i in L:
    if i<m:
        m = i
    idx += 1
print(idx, m)


# # Functions

# In[151]:


def printSuccess():
    print("I am done")
    print("send me another task")


# In[152]:


printSuccess()


# In[153]:


3+8


# In[154]:


printSuccess()


# In[155]:


def printSuccess2():
    """This funcion is doing nothing except printing a message.
    That message is "hellow"
    """ #this is doc string #use doc string whenever use functions
    print("hellow")


# In[161]:


help(printSuccess2)


# In[162]:


printSuccess2()


# In[163]:


def printMessage(msg):
    """The function prints the message supplied by the user
    or prints that msg is not in the form of string"""

    if isinstance(msg,str):
        print(msg)
    else:
        print("Your input argument is not string")
        print("Here is the type of what you have supplied :", type(msg))


# In[164]:


help(printMessage)


# In[167]:


get_ipython().run_line_magic('pinfo2', 'printMessage')


# In[168]:


printMessage("This is the message")


# In[169]:


printMessage(23)


# In[170]:


y = "hellow there"
printMessage(y)


# In[171]:


#multiple arguments
def mypow(a,b):
    """this function compute power just like builtin pow function"""
    c = a**b
    print(c)


# In[172]:


get_ipython().run_line_magic('pinfo', 'mypow')


# In[173]:


mypow(3,4)


# In[174]:


def checkArgs(a,b,c):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        print((a+b+c)**2)
    else:
        print("Error: the input arguments are not of the expected types")


# In[175]:


checkArgs(3,4,5)


# In[176]:


checkArgs(3,4,"g")


# In[177]:


checkArgs(3,4)


# In[178]:


checkArgs(2,3,4,5)


# In[179]:


#Order of input arguments
def f(a,b,c):
    print("A is :", a)
    print("B is :", b)
    print("C is :", c)


# In[181]:


#f(2,3,"game")
f(3,"game",2)


# In[183]:


#f(a = 2, b = 3, c ="game")
f(c = "game", a = 2, b = 3)


# In[191]:


#Function(return statement)
def myadd(a,b):
    sumValue = a+b
    return sumValue


# In[192]:


d = myadd(2,3)
print(d)


# In[193]:


variableOutSideTheFunction = 3


# In[201]:


def g():
    variableOutSideTheFunction = 5
    print(variableOutSideTheFunction) # inside the function


# In[203]:


g()


# In[199]:


print(variableOutSideTheFunction) # outside the function


# In[204]:


def g():
    variableOutSideTheFunction = 5
    #print(variableOutSideTheFunction) # inside the function


# In[206]:


print(g()) #if print isn't set inside the function, then none will be result when print(that func()).
print(type(g()))


# In[215]:


def h():
    print("A")
    a = 3
    b = 5
    c = a+b
    print("something")
    return  # Like this if I dont return anything, it means exit the function right away
    print("B")
    print("C")


# In[216]:


print(h())


# In[217]:


def h():
    print("A")
    a = 3
    b = 5
    c = a+b
    print("something")
    return c
    print("B")
    print("C")


# In[218]:


print(type(h()))


# In[219]:


def r():
    a = 5
    b = 7
    d = "something"
    return a,b,d #can return multiple values


# In[220]:


x,y,z = r()
print(x,y,z)


# In[221]:


def myAddUniversal(*args):
    s = 0
    for i in range(len(args)):
        s += args[i] #s = s+args[i]
    return s


# In[222]:


print(myAddUniversal(2,4,5))


# In[223]:


def printAllVariableNamesAndValues(**args):# ** you'll receive key value pair list
    for x in args:
        print("Variable Name is :", x,"and Value is :", args[x])


# In[224]:


printAllVariableNamesAndValues(a = 3, b = "B", c = "CCC", y = 6.7)


# In[225]:


#default value
def gg(s=4):
    print(s) #once press shift+enter, s is assigned as 4


# In[226]:


gg()


# In[227]:


gg(56)


# In[228]:


L = [1,2,3]
L2 = L
L2[0] = -9
print(L)


# In[229]:


def ff(L =[1,2]):
    for i in L:
        print(i)


# In[230]:


L2 = [12,3,4]
ff()


# In[231]:


ff(L2)


# In[232]:


ff() #already default value is assigned as L = [1,2]


# In[233]:


#Modules

import sys
sys.path.append('/Users/soyeonpark/ABC')


# In[234]:


#import all functions
import my_universal_functions as myfs

#import one function
#from my_universal_functions import addAllNumerics


# In[235]:


get_ipython().run_line_magic('pinfo2', 'myfs.addAllNumerics')


# In[237]:


c = myfs.addAllNumerics(2,3,4,6)


# In[238]:


print(c)


# In[239]:


myfs.myName


# In[240]:


""" Given a list of numbers i.e. [1,2,4,-5,7,9,3,2], make another list
that contains all the items in sorted order from min to max. i.e. your 
result will be another list like [-5,1,2,2,3,4,7,9]
"""


# In[250]:


def findMin(L, startIndx):
    m = L[startIndx]
    idx = startIndx
    for i in range(startIndx,len(L)):
        x = L[i]
        if x<m:
            m = x
            idx = i
        else:
            pass
        i += 1
    return m, idx


# In[245]:


a,b = findMin([2,3,4,0,9])


# In[246]:


print(a,b)


# In[247]:


def swapValues(L,idx1,idx2):
    tmp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = tmp
    return L


# In[249]:


L = [2,3,6,7]
L2 = swapValues(L,1,3)
print(L2)


# In[267]:


from my_universal_functions import checkIfNotNumeric
def sortList(L):
    if not(checkIfNotNumeric2(L)):
        print("Error: List does not contain numeric values")
        return
    else:
        c = 0
        for x in L:
            m, idx = findMin(L, c)
            L = swapValues(L,c,idx)
            c += 1
    return L


# In[268]:


L2 = sortList([2,1,5,3,-8,17])
print(L2)


# In[253]:


get_ipython().run_line_magic('pinfo2', 'checkIfNotNumeric')


# In[264]:


checkIfNotNumeric2([2,1,5,3,-8,17])


# In[263]:


def checkIfNotNumeric2(L):
    for x in L:
        if not(isinstance(x, (int, float))):
            return False
    return True


# In[269]:


#String
s = "Python is a good language"
t = 'Its good for data science'


# In[270]:


type(s)


# In[271]:


print(s)


# In[272]:


print("hellow", 12, "hellow2", 'who are you', 5.9)


# In[275]:


v = s + " " + t #str+str+str
print(v)


# In[282]:


price = 12
s = "The price of this book"
v = s + ' is: '+ str(price) #str+str+int X --> str(int) 
print(v)
print(s,"is:", price) #print() automatically add space between arguments/ in thic case, don't need to chage the type


# In[284]:


#String(Multi line String)
a = """this is line 1
this is line 2
this is last line and this line is 3"""
print(a)


# In[286]:


print(""" The following options are available: 
            -a      :does nothing
            -b      :also does nothing
""")


# In[288]:


s = "How are you and who are you"
print(s[5])


# In[289]:


print(type(s[5]))


# In[290]:


s[3:8]


# In[291]:


s[-1] #negative index is starting from right / -1 is the last letter


# In[293]:


s[-12:-3]


# In[294]:


s[1] = "e"  # it's not possible. it's inmutable(unchanable) once the string is declared


# In[295]:


s[0:12:2] # it skips with the step size 2 till 12(excluded) s[start:end:step]


# In[296]:


s


# In[297]:


s[:12]


# In[298]:


s[3:]


# In[299]:


s[1:12]


# In[300]:


s[::-1] # reverse the way


# In[301]:


print(len(a))


# In[302]:


print(len(a[3:8]))


# In[304]:


a = "    abc def     hgq   asdgeg" 
b = a.strip() #remove space in the beginning and end
print(b)


# In[305]:


a = "ABC deFg ;; sadfa QF"
b = a.lower() #change all the characters into lower case
print(b)


# In[306]:


c = a.upper() # change to upper case
print(c)


# In[307]:


d = a.replace(";","*") #replace the first one to the second one
print(d)


# In[308]:


d = a.replace(";","**&&^^%%")
print(d)


# In[309]:


d = a.replace(";;","two semi colons")
print(d)


# In[310]:


a = "abc;def;hgydfa;yy23" # want to separate them
L = a.split(";") #split elements by the standard " "
print(L) #abc is one element


# In[311]:


L[1]


# In[313]:


#. and tap button --> appear all the functions that can be used
print(a.capitalize())


# In[314]:


"abdAfadfGGQ".capitalize()


# In[315]:


help(a.count)


# In[317]:


"abc" in "asdfsafsjflskfjabclskjf"


# In[318]:


"abc" == "abc" #can use == at string


# In[319]:


"abc" < "def" #what does it mean? --> following alphabet order in Python


# In[320]:


"$%" < "*&"


# In[322]:


"acd" not in "ackljlkfj"


# In[323]:


print("we are learning "string" here")


# In[325]:


print("we are learning \"string\"here") #use backslash


# In[326]:


print('we are learning "string" here') # or use single quot 


# In[327]:


print("we are \n now on another line") # for another line, use \n


# In[328]:


print("we are \t now on another line")


# In[329]:


print("c:\name\drive") # here \n acts like for another line


# In[330]:


print(r"c:\name\drive") # use r ahead to accept it as a raw string


# # Data Structures

# In[331]:


#List
L = [1,3,4.9,"name",3]
#Tuple
T = (1,3,4.9,"name",3)
#Set
S = {1,3,4.9,"name",3}
#Dictionary
D = {23:"twothree", 'B':43, 'C':'CCD'}


# In[334]:


print("The type of L is ", type(L))
print("The type of T is ", type(T))
print("The type of S is ", type(S))
print("The type of D is ", type(D))


# In[335]:


print(L[1])
print(T[1])
print(3 in S)
print(D[23])


# In[336]:


print(D['B'])


# In[337]:


S # no duplicate


# In[338]:


L


# In[339]:


L[1:3]


# In[340]:


L[::-1]


# In[341]:


T[:3]


# In[342]:


L = L + ["how", "are", 6, "you"] #add element


# In[343]:


L


# In[344]:


L.append(6.8) #add element


# In[345]:


L


# In[348]:


T2 = ('a', 'b', 45)
T3 = T + T2  #combine tuples


# In[349]:


T3


# In[350]:


S


# In[351]:


S.add(56) #add element


# In[352]:


S


# In[353]:


S.update({23,"game",1}) #add multiple elements


# In[354]:


S


# In[355]:


D


# In[356]:


D['newKey'] = "newValue"


# In[357]:


D


# In[358]:


D2 = {"y":"YY", "z":10}


# In[370]:


D3 = D + D2 #not possible to combine Dictionaries /But can update like D.update(D2)


# In[361]:


L


# In[362]:


del L[3] #delete element


# In[363]:


L


# In[364]:


S


# In[365]:


S.remove('game')


# In[366]:


S


# In[367]:


D


# In[368]:


del D['C']


# In[369]:


D


# In[371]:


#copy function
L


# In[372]:


L2 = L


# In[373]:


L2 #is saved in the same memory. so if we change one element in one list then the other is also changed


# In[374]:


L2[2] = "four point nine"


# In[375]:


L2


# In[376]:


L


# In[377]:


L2 = L.copy() # should use copy function to save different memory/ Same at Set, Dictionary (Tuple doesn't use it)


# In[378]:


L2


# In[379]:


L


# In[380]:


L2[1] = 'one'


# In[381]:


L2


# In[382]:


L


# In[383]:


L3 = L[1:5] #L3 is completely in new memory


# In[384]:


L3


# In[385]:


L3[0] = "three"


# In[386]:


L


# In[387]:


help(L.append)


# In[388]:


get_ipython().run_line_magic('pinfo', 'L.clear')


# In[389]:


get_ipython().run_line_magic('pinfo', 'L.pop')


# In[390]:


L.reverse()


# In[391]:


L


# In[392]:


L[::-1]


# In[393]:


get_ipython().run_line_magic('pinfo', 'D.items')


# In[394]:


L


# In[395]:


T


# In[396]:


S


# In[397]:


D


# In[398]:


D2 = {'A':L, 'B':T, 'C':S, 'D':D} # one data structure can have the other structure as element


# In[400]:


D2['A'][3] #at the Value of A, want to know the third position


# In[401]:


K = D2['D']


# In[402]:


K


# In[403]:


for x in K:
    print(x,K[x])


# In[404]:


L3 = [L,T,D,23,"game"] # it's also possible


# In[405]:


type(L3[2])


# In[406]:


L3 = [x**2 for x in range(10)]


# In[407]:


L3


# In[408]:


S3 = {x**2 for x in range(2,20,3)}


# In[409]:


S3


# In[414]:


"""Let say you are a teacher and you have different student 
records containing id fo a student and the marks list in each subject
where different students have taken different number of subjects .All
these records are in hard copy. You want to enter all the data in computer
and want to compute the average marks of each student and display"""

def getDataFromUser():
    D = {}
    while True:
        studentId = input("Enter student ID: ")
        marksList = input("Enter the marks by comma separated values: ")
        moreStudents = input('Enter "no" to quit insertion: ')
        if studentId in D:
            print(studentId, "is already inserted")
        else:
            D[studentId] = marksList.split(",")
        if moreStudents.lower() == "no":
            return D


# In[415]:


studentData = getDataFromUser()


# In[416]:


studentData


# In[420]:


def getAvgMarks(D):
    avgMarks = {}
    for x in D:
        L = D[x]
        s = 0
        for marks in L:
            s += int(marks)
        avgMarks[x] = s/len(L)
    return avgMarks


# In[422]:


avgM = getAvgMarks(studentData)


# In[423]:


avgM


# In[424]:


for x in avgM:
    print("Student :", x, "got avg Marks as: ", avgM[x])


# # Numpy

# In[425]:


import numpy as np


# In[443]:


a = np.array([1,2,3,5,7]) #can define data type as well / i = integer


# In[434]:


b = np.array((2,3,5), dtype= 'f') # f = float


# In[428]:


print(a)


# In[429]:


type(a)


# In[430]:


print(b)


# In[431]:


type(b)


# In[435]:


a.dtype #what's the data type of a?


# In[436]:


b.dtype #what's the data type of b?


# In[437]:


#Numpy(Dimension)
import numpy as np
a = np.array([[1,2,3],[4,5,6]]) #2 dimensional array


# In[438]:


a.ndim


# In[439]:


a[0,2]


# In[452]:


B = np.array([[1,2,3],[2,4,5,9]])


# In[453]:


B.ndim


# In[449]:


C = np.array([[[1,2,3],[4,5,6],[0,0,-1]],[[-1,-2,-3],[-4,-5,-6],[0,0,1]]])


# In[454]:


C.ndim


# In[455]:


C.shape # each 2 dimensional array has 3 array which have 3 items


# In[451]:


C[1,0,2]


# In[459]:


C.shape[2]


# In[461]:


A = np.array([2]) # [] 


# In[462]:


A.ndim


# In[463]:


B = np.array(3) # no array due to doenst have []


# In[464]:


B.ndim


# In[465]:


C.size # total number of elements


# In[466]:


C.nbytes #how many totals number of bytes


# In[467]:


A = np.arange(100) #np.arange()


# In[468]:


print(A)


# In[470]:


A = np.arange(20,100,3) #(start, last(excluded), size) like for i in range(20,100,3)
print(A)


# In[471]:


print(range(10)) #range() never create a list


# In[472]:


print(list(range(10))) # if you want list then write list


# In[473]:


A = np.random.permutation(np.arange(10)) #the arrage will be shown as randomly
print(A)


# In[475]:


get_ipython().run_line_magic('pinfo', 'np.random.randint')


# In[481]:


v = np.random.randint(20,30) #some random integer btw 20 and 30


# In[482]:


type(v)


# In[483]:


print(v)


# In[484]:


print(v)


# In[485]:


A = np.random.rand(1000) # random number btw 0 to 999


# In[487]:


import matplotlib.pyplot as plt


# In[489]:


plt.hist(A, bins=100)


# In[490]:


B = np.random.randn(10000)
plt.hist(B, bins=200)


# In[491]:


C = np.random.rand(2,3) #creat random dimensional array


# In[492]:


C


# In[493]:


C.ndim


# In[494]:


C = np.random.rand(2,3,4,2)


# In[495]:


C.ndim


# In[496]:


C


# In[497]:


D = np.arange(100).reshape(4,25) #reshape arrange following (a,b)


# In[498]:


D.shape


# In[499]:


D


# In[500]:


D = np.arange(100).reshape(4,5,5)


# In[501]:


D.shape


# In[502]:


D


# In[503]:


get_ipython().run_line_magic('pinfo', 'np.zeros')


# In[504]:


get_ipython().run_line_magic('pinfo', 'np.ones')


# In[564]:


#Numpy(Slicing)
A = np.arange(100)
print(A)


# In[565]:


b = A[3:10]
print(b)


# In[566]:


b[0] = -1200


# In[567]:


b


# In[568]:


A #it's also changed because it's in the same memory / That's the big difference btw ordinary list and slicing


# In[569]:


b = A[3:10].copy() # if want not to change / it's in the different memory


# In[570]:


A[::5]


# In[571]:


A[::-5]


# In[572]:


A[::-1]


# In[573]:


#I want to find where is the position of -1200
B = (A == -1200)*np.arange(A.size)
print(B)


# In[574]:


A.indices(-1200)


# In[575]:


idx = np.argwhere(A==-1200)[0][0]


# In[535]:





# In[576]:


idx


# In[577]:


A[idx] = 3


# In[578]:


A


# In[579]:


A = np.round(10*np.random.rand(5,4))


# In[544]:


#A = np.random.rand(5,4)


# In[545]:


#A


# In[580]:


A


# In[581]:


A[1,2]


# In[582]:


A[1,:] # for whole second row


# In[583]:


A[:,1] # for whole second column


# In[585]:


Z = A[1:3,2:4] #row number 1 to row number 3 & column number 2 to column number 4


# In[586]:


Z


# In[587]:


Z.T # transpose 행과 열 바꾸기


# In[588]:


import numpy.linalg as la #linear algebra library 역행렬구하기


# In[589]:


la.inv(np.random.rand(3,3))


# In[597]:


Z


# In[598]:


Za = Z.sort(axis=0) #행 축으로 정렬 # 여기부터 다시 해보기 


# In[599]:


Za


# In[559]:


A.sort(axis=1) #열 축으로 정렬


# In[560]:


A


# In[600]:


#Numpy(More Indexing)
A = np.arange(100)


# In[601]:


B = A[[3,5,6]]


# In[602]:


B


# In[605]:


B[0] = -4


# In[606]:


B


# In[604]:


A # A doesn't change becuase we use B = A[[3,5,6]]


# In[607]:


B = A[A<40] # access all elements less than 40


# In[608]:


B


# In[609]:


B = A[(A<40) & (A>30)] # btw 30 and 40


# In[610]:


B


# In[611]:


#& for list / and for single object
#/ for list / or for single object
#~ for list/ not for single object


# In[616]:


#Numpy(Broadcasting)
A = np.round(10*np.random.rand(2,3))


# In[617]:


A


# In[619]:


A+3


# In[620]:


A+(np.arange(2).reshape(2,1)) 


# In[621]:


print(np.arange(2))


# In[622]:


#stacks
B= np.round(10*np.random.rand(2,2))


# In[623]:


A


# In[624]:


B


# In[625]:


C = np.hstack((A,B)) #가로로


# In[626]:


C


# In[627]:


A = np.random.permutation(np.arange(10))


# In[628]:


A


# In[629]:


A.sort() #ascending 오름차순


# In[630]:


A


# In[631]:


np.sort(A)


# In[632]:


A.sort()


# In[633]:


A=A[::-1] #descending 내림차순


# In[634]:


A


# In[635]:


A = np.array(["abc",'howare you','u765','132r'])


# In[636]:


A.sort() # possible in strings like alphabet order


# In[637]:


A


# In[638]:


#Numpy(Speed: ufuncs)  numpy function is faster for large number/elements
B= np.random.rand(1000000)
get_ipython().run_line_magic('timeit', 'sum(B)')
get_ipython().run_line_magic('timeit', 'np.sum(B) #same with B.sum()')


# In[639]:


def mySum(G):
    s = 0
    for x in G:
        s+=x
    return s


# In[640]:


get_ipython().run_line_magic('timeit', 'mySum(B)')


# # Pandas

# In[641]:


import pandas as pd


# In[643]:


print(pd.__version__)


# In[644]:


A = pd.Series([2,3,4,5], index = ['a','b','c','d']) # Series handle one dimensional array


# In[645]:


A.values


# In[646]:


type(A.values)


# In[647]:


type(A)


# In[648]:


A.index


# In[649]:


A['a']


# In[650]:


A['a':'c'] #using idex then the final idex is also included


# In[651]:


#Pandas(Series) using dictionary
grads_dict={'A':4, 'B':3.5, 'C':3, 'D':2.5}
grads = pd.Series(grads_dict)


# In[652]:


grads.values


# In[653]:


marks_dict = {'A':85, 'B':75, 'C':65, 'D':55}
marks = pd.Series(marks_dict)


# In[654]:


marks


# In[655]:


marks['A']


# In[656]:


marks[0:2]


# In[657]:


#Pandas(DataFrame)
D = pd.DataFrame({'Marks':marks, 'Grades':grads})


# In[658]:


D


# In[659]:


D.T #can transpose as well


# In[660]:


D


# In[663]:


D.values


# In[664]:


D.values[2,0] #row #3 column #1


# In[665]:


D.columns


# In[666]:


D


# In[667]:


D['ScaledMarks'] = 100*(D['Marks']/90) # want to add column


# In[668]:


D


# In[669]:


del D['ScaledMarks'] #want to delete column


# In[670]:


D


# In[671]:


G = D[D['Marks']>70] # want to pick some data


# In[672]:


G


# In[675]:


#Pandas(NaN) -- deal with missing values (None)
A = pd.DataFrame([{'a':1, 'b':4}, {'b':-3, 'c':9}])


# In[676]:


A


# In[677]:


A.fillna(0) #fill all na value as 0


# In[680]:


A.dropna #drop all the missing values


# In[681]:


#Pandas(Indexing)
A = pd.Series(['a','b','c'], index = [1, 3, 5])


# In[682]:


A[1]


# In[683]:


A[1:3]


# In[684]:


A.loc[1:3] #loc : use explicit indexes


# In[685]:


A.iloc[1:3] #iloc: use implicit indexes 기본적으로 첫 번째 값 위치 0


# In[686]:


D


# In[687]:


D.iloc[2,:]


# In[688]:


D.iloc[::-1,:] # want to reverse all the values


# In[689]:


#Pandas(csv files)
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
df = pd.read_csv('/Users/soyeonpark/Downloads/covid_19_data.csv')


# In[692]:


df.head(10) #first 10 records


# In[693]:


df.drop(['SNo', 'Last Update'], axis = 1, inplace = True)
# want to delete column. 'axis=1' is do that on the column and 'implace=True' is apply this to df


# In[694]:


df.head()


# In[695]:


df.rename(columns = {'ObservationDate':'Date', 'Province/State':'Province', 'Country/Region':'Country'}, inplace = True)
#want to rename the column name


# In[696]:


df.head()


# In[697]:


df['Date'] = pd.to_datetime(df['Date'])
#convert date format to use in Pandas


# In[698]:


df.head()


# In[699]:


df.describe()


# In[700]:


df.info()


# In[703]:


df = df.fillna('NA') # fill in the blank as NA


# In[704]:


df.info()


# In[705]:


df.head(10)


# In[712]:


#EX:how many total confirmed case in each countries?
df2 = df.groupby('Country')[['Country','Confirmed','Deaths','Recovered']].sum(numeric_only=True).reset_index()
#Country 는 숫자 데이터가 아니라서 numeric_only=True 넣어줌


# In[710]:


df2


# In[714]:


#grupby 'Country' and 'Date'
df2 = df.groupby(['Country','Date'])[['Country','Date','Confirmed','Deaths','Recovered']].sum(numeric_only=True).reset_index()


# In[715]:


df2


# In[717]:


df3 = df2[df2['Confirmed']>100] #want case which have confirmed more than 100


# In[718]:


df3


# # Matplotlib

# In[719]:


import matplotlib.pyplot as plt


# In[720]:


x = np.linspace(0,10,1000)
y = np.sin(x)
plt.plot(x,y)


# In[724]:


plt.scatter(x[::10],y[::10], color = 'red')


# In[725]:


# can make two plot
plt.plot(x,y,color='b')
plt.plot(x,np.cos(x),color='g')


# In[809]:


#Project Covid 19 using matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
df = pd.read_csv('/Users/soyeonpark/Downloads/covid_19_data.csv')


# In[810]:


df


# In[811]:


df.drop(['SNo','Last Update'], axis=1, inplace=True)


# In[812]:


df.rename(columns = {'ObservationDate':'Date', 'Province/State':'Province', 'Country/Region':'Country'}, inplace = True)


# In[813]:


df.head()


# In[814]:


df['Date'] = pd.to_datetime(df['Date'])


# In[815]:


df.head()


# In[816]:


imputer = SimpleImputer(strategy='constant') #missing values 결측치처리 좀 더 알아보기
df2 = pd.DataFrame(imputer.fit_transform(df),columns=df.columns)


# In[798]:


df2


# In[819]:


# 왜 confirmed, deaths, recovered 가 안 나오지???
df3 = df2.groupby(['Country','Date'])[['Confirmed','Deaths','Recovered']].sum().reset_index() # only nemeric columns


# In[820]:


df3.head()


# In[805]:


type(df2['Confirmed'])


# In[821]:


countries = df3['Country'].unique()
len(countries)


# In[829]:


for idx in range(0,len(countries)):
    C = df3[df3['Country']==regions[idx]].reset_index()
    plt.scatter(np.arange(0,len(C)),C['Confirmed'],color ='b', label='Confirmed')
    plt.scatter(np.arange(0,len(C)),C['Recovered'],color ='g', label='Recovered')
    plt.scatter(np.arange(0,len(C)),C['Deaths'],color ='r', label='Deaths')
    plt.title(countries[idx])
    plt.xlabel('Days since the first suspect')
    plt.ylabel('Number of cases')
    plt.legend() #범례
    plt.show() #그래프 보여줘


# In[831]:


df4 = df3.groupby(['Date'])[['Confirmed','Deaths','Recovered']].sum().reset_index()


# In[832]:


df4.head


# In[837]:


C = df4
plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='b',label='Confirmed')
plt.scatter(np.arange(0,len(C)),C['Recovered'],color='g',label='Recovered')
plt.scatter(np.arange(0,len(C)),C['Deaths'],color='r',label='Deaths')
plt.title('world')
plt.xlabel('Days since the first suspect')
plt.ylabel('Number of cases')
plt.legend()
plt.show()


# In[ ]:




