#Excercise 1 
def triple(a):
    x=a*3
    return x
result=triple(4)
print(result)
#Exercise 2
def subtract(a,b):
    x=b-a
    return x
result=subtract(3,6)
print(result)

#Exercise 3
list_tuple=[('cat',3),('dog',5.1)]
def dictionary_maker(list_tuple):
    dictionary={}
    for key, value in list_tuple:
        dictionary[key]=value
    return dictionary
result=dictionary_maker(list_tuple)
print(result)  