#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-30 18:11:05
# @Author  : emmmmm

from manimlib.imports import *

"""
python manim.py from_umm233/lifan.py lifan -pl
"""

class lifan(Scene):
    def construct(self):
        ## Marking object

        def creat_square(self, i):
            """
            i start from 0
            """
            scale0 = 0.1
            square_list = []
            center_pointx = -5 + 2 * i
            center_pointy = 2.5

            # 确定每个靶子的中心位置,以(-4,-2)为起点,j:每次向右移动两个单位,i:向上移动2个单位
            for d_r in range(i+2):
                square1 = Square(fill_color=BLUE, color=BLUE, fill_opacity=0.5)
                square1.scale(scale0 * (i+1))
                center_pointx = center_pointx + scale0 * 2 * (i+1)
                square1.shift(np.array([center_pointx, center_pointy, 0]))

                # self.play(FadeIn(square1)) # 画靶子
                square_list.append(square1) # 存储每个靶子对象

            for d_d in range(1, i+2):
                square1 = Square(fill_color=BLUE, color=BLUE, fill_opacity=0.5)
                square1.scale(scale0 * (i+1))
                center_pointy = center_pointy - scale0 * 2 * (i+1)
                square1.shift(np.array([center_pointx, center_pointy, 0]))

                # self.play(FadeIn(square1)) # 画靶子
                square_list.append(square1) # 存储每个靶子对象

            for d_l in range(1, i+2):
                square1 = Square(fill_color=BLUE, color=BLUE, fill_opacity=0.5)
                square1.scale(scale0 * (i+1))
                center_pointx = center_pointx - scale0 * 2 * (i+1)
                square1.shift(np.array([center_pointx, center_pointy, 0]))

                # self.play(FadeIn(square1)) # 画靶子
                square_list.append(square1) # 存储每个靶子对象

            for d_u in range(1, i+1):
                square1 = Square(fill_color=BLUE, color=BLUE, fill_opacity=0.5)
                square1.scale(scale0 * (i+1))
                center_pointy = center_pointy + scale0 * 2 * (i+1)
                square1.shift(np.array([center_pointx, center_pointy, 0]))

                # self.play(FadeIn(square1)) # 画靶子
                square_list.append(square1) # 存储每个靶子对象
            return square_list

        text_sq_list = []
        scale1 = 0.1
        for n in range(1,4):
            example_text = TextMobject("4*%d" % n)
            example_sqare = Square(fill_color=BLUE, color=BLUE, fill_opacity=0.5)
            example_sqare.scale(scale1*n)

            self.play(ApplyMethod(example_text.next_to, np.array([-3, 3, 0])+DOWN*(n-1), 0))
            self.play(ApplyMethod(example_sqare.next_to, example_text.get_right()+0.2*RIGHT))
            text_sq_list.append(example_sqare)

        square_list0 = creat_square(self, 0)
        group0 = VGroup(*square_list0[:])

        square_list1 = creat_square(self, 1)
        group1 = VGroup(*square_list1[:])

        square_list2 = creat_square(self, 2)
        group2 = VGroup(*square_list2[:])

        # Move Objrct
        group0.next_to(np.array([0, 0, 0]), 0)
        group1.next_to(np.array([0, 0, 0]), 0)
        group2.next_to(np.array([0, 0, 0]), 0)

        self.play(TransformFromCopy(text_sq_list[0], group0))
        self.play(TransformFromCopy(text_sq_list[1], group1))
        self.play(TransformFromCopy(text_sq_list[2], group2))

        self.wait(2)

