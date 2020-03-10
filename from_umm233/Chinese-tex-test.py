#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-31 13:04:40
# @Author  : emmmmm

from manimlib.imports import *

"""
python manim.py from_umm233/Chinese-tex-test.py text_cn -pl
"""

class test_cn(Scene): # 创建一个继承自Scene的类
    def construct(self):  # 生成动画函数
        ## Marking object
        text01 = TextMobject("黑夜给了我一双黑色的眼睛，")
        text02 = TextMobject("我却用它寻找光明。")
        text_group = VGroup(text01, text02)
        text03 = TextMobject("顾城 《一代人》")
        text02.next_to(text01, DOWN)

        self.play(Write(text01))
        self.wait(1)

        # self.play(ApplyMethod(text02.next_to, text01.get_center()+DOWN))
        self.play(TransformFromCopy(text01, text02))
        self.wait(1)

        self.play(Transform(text_group,text03))
        self.wait(2)

