__author__ = 'cc'
#coding:utf-8

import pack

##第一种引用方式
# import pack.foo

##第二种引用方式
from pack import foo

##第三种引用方式
from pack.foo import out

from pack.foo import School

if __name__ == '__main__':
    print "tutorial"
    # pack.foo.out()
    # foo.out()
    out()

    #实例方法
    school = School()
    school.hire_teacher()

    #类方法
    School.sell()
