

# __init__ = constructor → initializes object attributes.
# __str__ = string representation → controls what users see when the object is printed.
# __init__ usually doesn't return anything (None implicitly).
# __str__ must return a string.



"""
    class:
        collection of "variables and functions" called as class
        "class" is the keyword, used to declare the class
        "pass" is the keyword, used to create "empty" class
        "constructors" are used to "declare data / initilize data" dynamically
        __init__(), used to declare the constructor
"""
# class Test:
#     pass

# obj1 = Test()
# print(id(obj1))
# print(obj1)

# class Test:
#     def __str__(self):
#         return "Hello"
# obj = Test()
# print(obj)


# class Test:
#     def __init__(self):
#         self.sub = "Agentic AI"

# obj1 = Test()
# obj1.sub = "Super AI"

# obj2 = Test()


# print(obj1.sub)
# print(obj2.sub)


# class Test:
#     def __init__(self,param1,param2):
#         self.id = param1
#         self.sub = param2

# obj1 = Test(111,"Agentic AI")

# obj2 = Test(222,"Super AI")

# obj3 = Test(333,"Quantum Computing")
# print(obj1.id, obj1.sub)
# print(obj2.id, obj2.sub)
# print(obj3.id, obj3.sub)


# class Test:
#     def db_conn(self):
#         print("chromadb conn soon...!")
# obj = Test()
# obj.db_conn()


# class Test:
#     # no para - no return type
#     def add1(self):
#         num1 = 200
#         num2 = 100
#         res = num1 + num2
#         print(res)
#     # with para - no return type
#     def add2(self,param1,param2):
#         res = param1 + param2
#         print(res)
#     # no para - with return type

#     # with para - with return type

# obj = Test()
# obj.add1()
# obj.add2(200,100)


class Test:
    def __init__(self):
        self.wish = "Hello"
        print("1:",self.wish)
    def greet(self):
        print("2:",self.wish)
obj = Test()
obj.greet()


 #####  my practce code

 
# class Test:
#     pass

# obj1 = Test()
# print(id(obj1))

# print(type(obj1))


# class Test:
#     def __init__(self):
#         return "hello"
    
# obj = Test()
# print(obj)


class Test:
    def __init__(self,sub,version):
            self.sub = sub
            self.version = version

    def __str__(self):
        return f"Subject: {self.sub}, Version: {self.version}"

test_obj = Test("Gen AI",200)
print(test_obj)

obj1 = Test("Gen AI",2)


print(obj1.sub)
#print(obj1.version)

# obj2 = Test()
# obj2.sub = "Super AI"
# print(obj2.sub)






# obj2 = Test()


# print(obj1.sub)
# print(obj2.sub)


# class Test:
#     def __str__(self):
#         return f"ID: {self.id}, Subject: {self.sub}"

#     # def __init__(self, id, sub):
#     #     self.id = id
#     #     self.sub = sub

# obj1 = Test(101,"Gen AI")
# obj2 = Test(102,"Super AI")     
# obj3 = Test(103,"Com AI")

# print(obj1)
# print(obj2)
# print(obj3)
# print(obj1.__dict__)


# class Test:
#     def __init__(self):
#             self.wish = "hello"
#             print("1 :",self.wish)

#     def greet(self):
        
#         print("2 :",self.wish)

# obj = Test()
# obj.greet()