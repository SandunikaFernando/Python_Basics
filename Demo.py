# print("Hello World!")

# print(123) #Integer
# print(2.123) #Float
# print("Hello..")#String
# print('Good Morning')#String
# print(True)
# print(False)
# print(2+3j)

# print("Hello")
# print("World")

# print("Hello \nWorld") #New line

# print("Name\t: Sandunika")
# print("Country\t: Sri Lanka")

# print("Saman said\"Good Morning\"")

# print("Special Character \\n gives us a new line")#Exception \

# a = 10
# b = 3

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)#modulous
# print(a//b)#Floor division
# print(a**b)#power

# a ="Hello"
# b="World"
# c=5
# d=a+" "+b

# print(a+b)#concatenate
# print(a*c)
# print(d)

# a=True
# b=False

# age=50
# is_young=age<18 #comparison operators(==,>=,<=)

# print(is_young)

# c= a and b #logical operators(and, or, not,^=XOR)
# print(c)

# x=5
# x=x+5

# x+=5
# print(x)

# x=10
# z='Hello'

# print(x,type(x),z, type(z))

# a,b,c=10,20,"Hello"
# print(a,b,c)

# a="10"
# b=20
# c=int(a)+b
# print(c)

# print("Enter Your Name: ", end='')
# name=input()
# print("Enter Your Age: ", end='')
# age=input()

# print("Hello",name)
# print("You are",age,"years old")

# x=[12,34,56,67]
# y=x[0]
# x[0]=569
# print(x)

# x=[12,34,56,67]
# x.append(100)#add to last indexes
# x.append(798)

# x.insert(2,500)#INDEX,VALUE

# print(x)

# x.remove(12)#value
# x.pop(2)#INDEX

# print(x)

# x=[12,434,565,77]
# y=[0,10,20,30,40]

# z=x+y

# print(z)

# a=10 in z
# a=10 not in z
# print(a)

#Dictionaries
# x={'1000':"Colombo","12500":"Panadura"}
# x['1200']="Moratuwa"
# x[0]="Zero"
# y=x['1000']
# #x['Cities']=['Kaluthara','Malabe']
# x['Cities']={1:'6876',78:"865678"}
# # print(x)
# print(x.keys())
# # print(x.values())
# y=x['Cities']

# del x[0]
# del x['Cities']

# x.clear()
# print(x)

# x={1:'A', 2:'B'}
# #y=x[3]#key error!
# y=x.get(3,0)#return 0
# print(y)

x={
    "a":['hello','hi','Good Morning'],
    "b":['Bye','Good Night'],
    "c":16
}
y=x['a']
y.append('Aayubowan')
z=x["c"]
z=17
print(x)