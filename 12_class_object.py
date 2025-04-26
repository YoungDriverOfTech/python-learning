# define class, class name use camel spell
class People:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

class Student(People): # 继承People类

    # constructor
    def __init__(self, name, clazz):
        super().__init__(name) # 调用父类构造方法，设置名字
        self.clazz = clazz # 子类设置班级

    def change_clazz(self, clazz):
        self.clazz = clazz

    def get_clazz(self):
        return self.clazz

# use class to new instance
student = Student("zhang san", "1 ban")
print(f"{student.get_name()} : {student.get_clazz()}")

# change attribute and printout new attribute
student.change_name("li si")
student.change_clazz("2 ban")
print(f"{student.get_name()} : {student.get_clazz()}")