# Abstraction
# Encapsulation
# Polymorphism--> multiple forms
# Inheritence-->classes and objects


# Encapsulation
student1={
    "name":"Sailesh sai",
    "marks":100
}
student2={
    "name":"Sanjeev",
    "marks":90
}


# class-->classes are callable
class person:
    pass
p = person()
print(p)


hex(id(p))


# class with a method

class person:
    name="Sailesh sai"

    def say_hi(self):
        print(f"Hello everyone ! I am {self.name}")
p=person()

p.say_hi()
person.say_hi(p)
