def my_friend(a,b,c,d):
    print(a,b,c,d)


my_friend("satish","suraj","sagar","amol")

#Suppose now i want to add name of my 5th and 6th friend .for this i ahve to change function.this is not good way to change in function
#now here we use *args mechanism .we can pass any number of parameter without changing any function
#Data type of * args is"Tuple"args is variable we can use any name instead of args


def my_friend_1(*args):
    print(type(args))
    print(*args)
friends = ["satish","suraj","sagar","amol","tushar"]
my_friend_1(*friends)


# Python program to illustrate
# *args for variable number of arguments
def myFun2(*argv):
    for arg in argv:
        print(arg)


myFun2('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def myfun3(normal,*args):
    normal = "This is first statement."
    print(normal)
    for i in args:
        print(i)

myfun3("pune","mumbai","Ahmednagar","Nashik")

# Normal argument should be passed first.this is the condition in *args mechanism


#  Example for usage of **kwargs:

# Python program to illustrate
# *kargs for variable number of keyword arguments

def myFun(**kwargs):
	for key, value in kwargs.items():
		print ("{} is {}".format(key,value))

# Driver code
myFun(first ='Geeks', mid ='for', last='Geeks')
