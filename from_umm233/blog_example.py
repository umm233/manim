#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-26 14:10:55
# @Author  : emmmmm

from manimlib.imports import *

"""
python manim.py from_umm233/blog_example.py <classname> -pl
"""

class create_circle(Scene): # 创建一个继承自Scene的类
    def construct(self):  # 生成动画函数
        # 创建图形对象
        circle = Circle(radius=2, fill_color=BLUE, color=RED, fill_opacity=0.5)
        self.play(ShowCreation(circle))
        self.wait(1)


class create_text(Scene): # 创建一个继承自Scene的类
    def construct(self):
        # 创建文本对象
        text =TextMobject("黑夜给了我一双黑色的眼睛", color=RED, height=0.5, width=5)
        self.play(ShowCreation(text))
        self.wait(1)

class create_group(Scene): # 创建一个继承自Scene的类
    def construct(self):  # 生成动画函数
        # 组合对象
        square = Square(fill_color=RED, color=RED, fill_opacity=0.5)
        rectangle = Rectangle(height=0.8, width=4, fill_color=RED, color=RED, fill_opacity=0.5)
        group = VGroup(square, rectangle) # 组合对象
        self.play(ShowCreation(square))
        self.play(ShowCreation(rectangle))
        self.play(ApplyMethod(group.shift, LEFT * 4)) # 左移四个单位
        # self.play(ApplyMethod(group.shift, np.array([1.5, 0, 0]))) # 左移四个单位
        # self.play(ApplyMethod(group.shift, np.array([-1.5, 0, 0]))) # 左移四个单位
        self.wait(1)

class move_object1(Scene):
    def construct(self):
        circle = Circle(radius=1, fill_color=BLUE, color=RED, fill_opacity=0.5)
        self.play(ShowCreation(circle))
        self.play(ApplyMethod(circle.shift, LEFT * 4))
        self.wait(1)

class move_object2(Scene):
    def construct(self):
        circle = Circle(radius=1, fill_color=BLUE, color=RED, fill_opacity=0.5)
        dot = Dot()
        self.play(ShowCreation(circle))
        self.play(ShowCreation(dot))
        self.play(ApplyMethod( circle.move_to, np.array([2, 2, 0]) ) )
        self.play(ApplyMethod( circle.move_to, np.array([0, 0, 0]) ) )
        self.wait(1)

class gridon(Scene):
    def construct(self):
        # plane = self.plane = NumberPlane(
        #     x_min=-3,
        #     x_max=3,
        #     y_min=-2,
        #     y_max=2,
        #     axis_config={
        #         "stroke_color": LIGHT_GREY,
        #     }
        # )
        # plane = NumberPlane(x_radius=14, y_radius=8)
        plane = NumberPlane()
        plane.add_coordinates()
        self.play(ShowCreation(plane))
        self.wait(1)

class move_test1(Scene):
    def construct(self):
        # grid on
        plane = NumberPlane() # 创建网格
        plane.add_coordinates() # 添加坐标
        circle = Circle(color=BLUE) # 创建圆形
        dot = Dot() # 原点兼圆心
        dot1 = dot.copy()
        circle_dot = VGroup(circle, dot1) # 组合圆形和圆心

        line = Line(np.array([0, 0, 0]), np.array([2, 2, 0]), color=YELLOW)

        self.play(ShowCreation(plane)) # 显示网格
        self.add(dot) # 显示dot
        self.play(ShowCreation(circle)) # 显示网格

        # circle.move_to(np.array([2,2,0]))
        self.play(ApplyMethod( circle_dot.move_to, np.array([2,2,0]) ))
        self.play(FadeIn(line))
        self.add(line)
        self.wait(1)

class move_test2(Scene):
    def construct(self):
        # grid on
        plane = NumberPlane() # 创建网格
        plane.add_coordinates() # 添加坐标
        circle = Circle(color=BLUE) # 创建圆形
        dot = Dot() # 原点兼圆心
        dot1 = dot.copy()
        circle_dot = VGroup(circle, dot1) # 组合圆形和圆心
        rectangle = Rectangle(color=RED)
        line = Line(np.array([0, 0, 0]), np.array([2, 2, 0]), color=YELLOW)

        self.play(ShowCreation(plane)) # 显示网格
        self.add(dot) # 显示dot

        # circle.move_to(np.array([2,2,0]))
        self.play(ApplyMethod( circle_dot.move_to, np.array([2,2,0]) ))
        # rectangle.next_to(circle, DOWN+LEFT)
        self.play(ApplyMethod( rectangle.next_to, circle, DOWN+LEFT))
        # self.play(ShowCreation(circle))
        self.play(FadeIn(line))
        self.add(rectangle)
        # self.play(ApplyMethod( circle_dot.move_to, np.array([2,2,0])))
        # self.add(line)
        # grid out
        # self.play(FadeOut(plane))
        self.wait(1)

class move_test3(Scene):
    def construct(self):
        # grid on
        plane = NumberPlane() # 创建网格
        plane.add_coordinates() # 添加坐标
        circle = Circle(color=BLUE) # 创建圆形
        dot = Dot() # 原点兼圆心
        dot1 = dot.copy()
        circle_dot = VGroup(circle, dot1) # 组合圆形和圆心

        line = Line(np.array([0, 0, 0]), np.array([2, 2, 0]), color=YELLOW)

        self.play(ShowCreation(plane)) # 显示网格
        self.add(dot) # 显示dot
        # circle.move_to(np.array([2,2,0]))
        self.play(ShowCreation(circle))
        self.play(ApplyMethod( circle_dot.shift, np.array([2,2,0])))
        self.play(FadeIn(line))
        self.add(line)
        self.wait(2)


class move_test4(Scene):
    def construct(self):
        # grid on
        plane = NumberPlane() # 创建网格
        plane.add_coordinates() # 添加坐标
        circle = Circle(color=BLUE) # 创建圆形
        dot = Dot() # 原点兼圆心
        dot1 = dot.copy()
        circle_dot = VGroup(circle, dot1) # 组合圆形和圆心
        rectangle = Rectangle(color=RED)
        line = Line(np.array([0, 0, 0]), np.array([2, 2, 0]), color=YELLOW)

        self.play(ShowCreation(plane)) # 显示网格
        self.add(dot) # 显示dot

        circle.move_to(np.array([2,2,0]))
        rectangle.next_to(circle, DOWN+LEFT)
        self.play(ShowCreation(circle))
        self.play(FadeIn(line))
        self.add(rectangle)
        self.play(ApplyMethod( rectangle.move_to, circle))
        self.wait(1)

class LDR(Scene): # 创建一个继承自Scene的类
    def construct(self):  # 生成动画函数
        plane = NumberPlane() # 创建网格
        plane.add_coordinates() # 添加坐标

        ## Marking object
        circle01 = Circle(fill_color=RED, color=RED, fill_opacity=0.5)
        circle02 = Circle(fill_color=RED, color=RED, fill_opacity=0.5)
        square01 = Square(fill_color=RED, color=RED, fill_opacity=0.5)
        love = VGroup(circle01, circle02, square01)

        # circle01.shift((UP + LEFT) * np.sqrt(2) / 2)
        # circle02.shift((UP + RIGHT) * np.sqrt(2) / 2)
        square01.rotate(np.pi / 4)
        self.play(ShowCreation(plane)) # 显示网格
        self.play(ApplyMethod( circle01.shift, (UP + LEFT) * np.sqrt(2) / 2))
        self.play(ApplyMethod( circle02.shift, (UP + RIGHT) * np.sqrt(2) / 2))
        self.play(ApplyMethod( square01.rotate, np.pi / 4))


        # self.play(ShowCreation(circle01), ShowCreation(circle02), ShowCreation(square01))
        self.play(ApplyMethod(love.set_opacity, 1))

        self.play(FadeOut(plane))
        self.wait(1)


class fadeIO(Scene):
    def construct(self):
        square = Square(fill_color=RED, color=RED, fill_opacity=0.5)
        for i in range(3):
            self.play(FadeIn(square))
            self.play(FadeOut(square))
            # self.wait(1)

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class SquareToCircle2(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        text = TextMobject("This is a square.")
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        text.shift(UP*2)

        self.play(ShowCreation(square))
        self.play(TransformFromCopy(square, text)) # 方形转换为圆形
        self.wait(1)
