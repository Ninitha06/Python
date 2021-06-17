print("Hello", "I", "am", "Learning", "Python", sep=" ")
print("Hello", "I", "am", "Learning", "Python", sep="\n")
a = 10
b = 20
print(a,end=',')
print(b)
a = "Indians"
b = "Mangoes"
print("{0} love {1}".format(a, b))
print("{0} love {1}".format(b, a))
print("{1} love {0}".format(b, a))

#C syntax
a = 10
b = 20

print("you entered %d and %d and %d" % (a, b, b))

print(type(a))

#input returns a string.. so we need to typecast it to int and typecast it back to str to concatenate
#python does not allow you to concatenate a string with an integer

a = int(input("Enter a number :- ")) 
print("Square := "+str(a*a))


