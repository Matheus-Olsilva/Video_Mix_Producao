from manim import *
from scenes.base_scene import BaseScene
from constants import *

class IntroScene(BaseScene):
    """Introduction scene with logo and company presentation"""
    
    def __init__(self):
        super().__init__()
        self.logo = None
        self.harumi_text = None
    
    def construct(self):
        self.setup()
        self.show_intro_logo()
        self.wait_with_factor(2)
        self.show_company_intro()
    
    def show_intro_logo(self):
        """Show company logo animation"""
        # Load logo image
        logo = ImageMobject(LOGO_PATH).scale(0.9).shift(LEFT*1.5)
        
        # Create rectangle with proportions
        rect = Rectangle(
            width=logo.height * (102/157),
            height=logo.height,
            color=WHITE,
            stroke_width=10
        ).move_to(logo)
        
        # Create letters for "HARUMI"
        letters = VGroup(*[
            Text(letter, font="IBM Plex Mono", font_size=80, color=WHITE, stroke_width=0.5)
            for letter in "HARUMI"
        ])
        letters.arrange(RIGHT, buff=0.3)
        
        # Position the text
        harumi_text = letters
        logo_right_edge = logo.get_right()
        harumi_text.move_to(logo_right_edge + RIGHT * 1.8).align_to(logo, DOWN * 0)
        
        # Animate logo appearance
        self.play_with_factor(
            Create(rect, run_time=2),
            rate_func=rate_functions.ease_in_out_sine
        )
        self.play_with_factor(
            FadeIn(logo, run_time=1.5),
            rect.animate.set_stroke(opacity=0),
            lag_ratio=0.5
        )
        self.play_with_factor(
            Write(harumi_text, run_time=1.5),
            rate_func=rate_functions.ease_in_out_sine
        )
        
        # Store references to logo elements
        self.logo = logo
        self.harumi_text = harumi_text
        self.rect = rect
        
    def hide_intro_logo(self):
        """Fade out the logo elements"""
        # Check if the logo elements exist before trying to fade them out
        logo_elements = []
        if hasattr(self, 'logo') and self.logo is not None:
            logo_elements.append(FadeOut(self.logo))
        
        if hasattr(self, 'harumi_text') and self.harumi_text is not None:
            logo_elements.append(FadeOut(self.harumi_text))
            
        if logo_elements:
            self.play_with_factor(
                *logo_elements,
                run_time=1.2
            )
        else:
            # If no logo elements exist, just create a placeholder logo to fade out
            # This handles the case where show_company_intro is called directly
            temp_logo = ImageMobject(LOGO_PATH).scale(0.9).shift(LEFT*1.5)
            temp_text = Text("HARUMI", font="IBM Plex Mono", font_size=80, color=WHITE)
            temp_text.next_to(temp_logo, RIGHT)
            
            self.add(temp_logo, temp_text)
            self.play_with_factor(
                FadeOut(temp_logo),
                FadeOut(temp_text),
                run_time=1.2
            )
            
        self.wait_with_factor(0.5)
    
    def show_company_intro(self):
        """Show company introduction with products and objectives"""
        # First hide the logo
        self.hide_intro_logo()
        
        # Create background grid
        # grid = NumberPlane(
        #     x_range=(-10, 10, 1),
        #     y_range=(-6, 6, 1),
        #     background_line_style={
        #         "stroke_width": 0.5,
        #         "stroke_opacity": 0.2,
        #         "stroke_color": RED
        #     }
        # ).set_opacity(0.05)
        
        # Company header text
        text1 = Tex(
            r"Imagine que você possui uma empresa de laticínios",
            font_size=40, color=WHITE
        )
        text1.to_corner(UL).shift(DOWN*1.0)
        
        # Factory icon
        factory = SVGMobject(FACTORY_SVG)
        factory.scale(0.7)
        factory.next_to(text1, RIGHT, buff=0.5)
        
        # Profit text
        text2 = Tex(
            r"e deseja aumentar os seus lucros",
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
        
        # Animation sequence
        # self.play_with_factor(
        #     Create(grid, run_time=1.5, lag_ratio=0.1),
        #     rate_func=smooth
        # )
        
        self.play_with_factor(Write(text1, run_time=3.5))
        self.wait_with_factor(0.8)
        self.play_with_factor(FadeIn(factory))
        self.play_with_factor(FadeIn(grupo_text_money))
        self.wait_with_factor(1.5)
        self.play_with_factor(GrowArrow(arrow))
        self.wait_with_factor(0.8)
        self.play_with_factor(FadeIn(heading))
        self.wait_with_factor(1.5)
        self.play_with_factor(FadeIn(products))
        
        self.play_with_factor(
            Create(highlight_cheese),
            Create(highlight_yogurt),
            run_time=1.5
        )
        
        self.wait_with_factor(4)
        self.play_with_factor(
            FadeOut(grupo),
            FadeOut(arrow),
            FadeOut(highlight_cheese),
            FadeOut(highlight_yogurt),
            # FadeOut(grid)
        )