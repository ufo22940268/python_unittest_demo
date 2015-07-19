__author__ = 'cc'


def out():
    print "foo"


name = "TsinghuaUniversity"
age = "46"
teacher = "asdf"


class School:

    name = "JiaXingXueYuan"
    age = "12"

    def __init__(self):
        print "init school"
        self.name = "Mingzhu"

    def hire_teacher(self):
        print "Hire teacher for " + self.name
        print "Instance age " + self.age
        print "Instance teacher" + teacher

    @classmethod
    def sell(cls):
        print "Sell school " + cls.age

        global teacher
        teacher = "kkkkk"


print "Module name:" + name