from manim import *
from scenes.base_scene import BaseScene
from constants import *

class IntroScene(BaseScene):    
    def show_company_intro(self):
        """Show company introduction with products and objectives"""
        
        # Company header text
        text1 = Tex(
            r"Imagine que você possui uma empresa de laticínios.",
            font_size=40, color=WHITE
        )
        text1.to_corner(UL).shift(DOWN*1.0)
        
        # Factory icon
        factory = SVGMobject(FACTORY_SVG)
        factory.scale(0.7)
        factory.next_to(text1, RIGHT, buff=0.5)
        
        # Profit text
        text2 = Tex(
            r"e deseja aumentar os seus lucros.",
            font_size=40, color=WHITE
        )
        text2.next_to(factory, DOWN * 2.5, buff=0.5).to_edge(LEFT)
        
        # Money icon
        money = SVGMobject(MONEY_SVG).scale(0.4)
        money.next_to(text2, RIGHT, buff=0.2)
        
        grupo_text_money = VGroup(text2, money)
        
        # Up arrow
        arrow = Arrow(
            start=ORIGIN,
            end=UP*1.5,
            color=RED,
            max_stroke_width_to_length_ratio=5,
            max_tip_length_to_length_ratio=0.3
        )
        arrow.next_to(money, RIGHT, buff=0.2)
        
        # Products text
        heading = Tex(
            r"A sua empresa produz:",
            font_size=40, color=WHITE
        )
        heading.to_edge(LEFT).shift(DOWN * 2.0)
        
        # Product icons
        # Cheese
        cheese = SVGMobject(CHEESE_SVG).scale(0.4)
        cheese_text = Tex("Queijo", font_size=30, color=WHITE)
        cheese_group = VGroup(cheese, cheese_text).arrange(DOWN, buff=0.2)
        
        # Yogurt
        yogurt = SVGMobject(YOGURT_SVG).scale(0.4)
        yogurt_text = Tex("Iogurte", font_size=30, color=WHITE)
        yogurt_group = VGroup(yogurt, yogurt_text).arrange(DOWN, buff=0.2)
        
        # Position products
        products = VGroup(cheese_group, yogurt_group).arrange(RIGHT, buff=0.5)
        products.next_to(heading, RIGHT, buff=0.4)
        
        # Highlight circles for products
        highlight_cheese = Circle(color=RED, stroke_width=2).surround(cheese, buffer_factor=1.2)
        highlight_yogurt = Circle(color=RED, stroke_width=2).surround(yogurt, buffer_factor=1.2)
        
        # Group all elements
        grupo = VGroup(text1, factory, text2, money, heading, products)
        
        self.play_with_factor(Write(text1, run_time=1.5))
        self.play_with_factor(FadeIn(factory), run_time = 1)
        self.play_with_factor(FadeIn(grupo_text_money), run_time = 1)
        self.play_with_factor(GrowArrow(arrow), run_time = 1.5)
        self.play_with_factor(FadeIn(heading), run_time = 1.5)
        self.play_with_factor(FadeIn(products), run_time = 1.5)
        
        self.play_with_factor(
            Create(highlight_cheese),
            Create(highlight_yogurt),
            run_time=1.0
        )
        
        self.wait_with_factor(1)
        self.play_with_factor(
            FadeOut(grupo),
            FadeOut(arrow),
            FadeOut(highlight_cheese),
            FadeOut(highlight_yogurt),
        )