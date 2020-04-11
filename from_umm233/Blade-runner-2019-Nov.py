#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-08 15:20:38
# @Author  : emmmmm

from manimlib.imports import *

"""
python manim.py from_umm233/Blade-runner-2019-Nov.py showText -pl
"""

class showText(Scene): # 创建一个继承自Scene的类
    def construct(self):  # 生成动画函数
        ## Marking object
        text01 = TextMobject("LOS ANGELES")
        text02 = TextMobject("NOVEMBER, 2019")
        text_group = VGroup(text01, text02)
        text02.next_to(text01, DOWN)

        self.play(Write(text01))
        self.wait(1)

        # self.play(ApplyMethod(text02.next_to, text01.get_center()+DOWN))
        self.play(TransformFromCopy(text01, text02))
        self.wait(2)
