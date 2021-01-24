# -*- coding: utf-8 -*-
"""
@Time: 2021/1/22 20:19
@Auth: Jase-lee
@File: test02.py
@IDE: PyCharm
@Motto: 更多内容：https://github.com/Jase-lee

"""
class Cat():
    """猫类"""
    name = 'tomcat'

    def call(self):
        print("啊呜！")

cat = Cat()
print(cat.name)
cat.call()