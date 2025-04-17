from manim import *
from scenes.base_scene import BaseScene
from constants import *
import utils

class ConclusionScene(BaseScene):
    """Final scene showing the optimal solution and conclusion"""
    
    def construct(self):
        self.setup()
        self.show_final_solution()
    
    def show_final_solution(self):
        """Show the optimal solution and its interpretation"""
        # Get the optimal solution values
        x1_otimo = 1250  # kg of yogurt
        x2_otimo = 812.5  # kg of cheese
        lucro_otimo = OBJECTIVE_FUNCTION["yogurt_coef"] * x1_otimo + OBJECTIVE_FUNCTION["cheese_coef"] * x2_otimo
        
        # Create axes for the graph
        axes = Axes(
            x_range=[0, 2000, 500],
            y_range=[0, 1500, 500],
            x_length=5.5,
            y_length=3.5,
            axis_config={"color": BLUE_E, "include_tip": True}
        ).scale(0.8).to_edge(LEFT, buff=1.8).shift(UP*1.0)
        
        # Create the optimal point
        ponto_otimo = Dot(axes.coords_to_point(x1_otimo, x2_otimo), color=SECONDARY_COLOR, radius=0.1)
        
        # Create dashed lines to the axes
        linha_x = DashedLine(
            start=axes.coords_to_point(x1_otimo, x2_otimo),
            end=axes.coords_to_point(x1_otimo, 0),
            color=BLUE_E, 
            stroke_width=2
        )
        
        linha_y = DashedLine(
            start=axes.coords_to_point(x1_otimo, x2_otimo),
            end=axes.coords_to_point(0, x2_otimo),
            color=BLUE_E, 
            stroke_width=2
        )
        
        # Add axis labels
        label_x = MathTex("x_1", color=WHITE).next_to(axes.coords_to_point(2000, 0), RIGHT, buff=0.2).set_opacity(0.8)
        label_y = MathTex("x_2", color=WHITE).next_to(axes.coords_to_point(0, 1500), UP, buff=0.2).set_opacity(0.8)
        
        # Add coordinate values
        valor_x = MathTex(f"{x1_otimo}", color=SECONDARY_COLOR).next_to(linha_x, DOWN, buff=0.2)
        valor_y = MathTex(f"{x2_otimo}", color=SECONDARY_COLOR).next_to(linha_y, LEFT, buff=0.2)
        
        # Create the feasible region
        regiao_viavel = Polygon(
            axes.coords_to_point(320, 450),
            axes.coords_to_point(1457.14, 450),
            axes.coords_to_point(1250, 812.5),
            axes.coords_to_point(320, 1277.5),
            fill_color=BLUE_E,
            fill_opacity=0.2,
            stroke_color=BLUE_D,
            stroke_width=1.5
        )
        
        # Create container for conclusion text
        text_box = Rectangle(
            width=6, 
            height=3, 
            fill_color=BLACK,
            fill_opacity=0,  # Transparent 
            stroke_width=0
        ).to_edge(RIGHT, buff=0.8).shift(UP*1.5)
        
        # Create conclusion text
        texto_intro = Text(
            "Para maximizar o lucro,", 
            font=DEFAULT_FONT, 
            font_size=32, 
            color=WHITE
        )
        
        texto_otimo = Text(
            "a empresa deve produzir:", 
            font=DEFAULT_FONT, 
            font_size=32, 
            color=WHITE
        )
        
        texto_intro_grupo = VGroup(texto_intro, texto_otimo).arrange(DOWN, aligned_edge=LEFT)
        texto_intro_grupo.move_to(text_box).align_to(text_box, UP)
        
        # Production values
        texto_prod1 = Text("• ", font_size=32, color=SECONDARY_COLOR)
        texto_valor1 = Text(f"1250 kg", font=DEFAULT_FONT, font_size=30, color=SECONDARY_COLOR)
        texto_desc1 = Text(" de iogurte", font=DEFAULT_FONT, font_size=30, color=WHITE)
        prod1_grupo = VGroup(texto_prod1, texto_valor1, texto_desc1).arrange(RIGHT, buff=0.1)
        
        texto_prod2 = Text("• ", font_size=32, color=SECONDARY_COLOR)
        texto_valor2 = Text(f"812.5 kg", font=DEFAULT_FONT, font_size=30, color=SECONDARY_COLOR)
        texto_desc2 = Text(" de queijo", font=DEFAULT_FONT, font_size=30, color=WHITE)
        prod2_grupo = VGroup(texto_prod2, texto_valor2, texto_desc2).arrange(RIGHT, buff=0.1)
        
        # Position production lines
        VGroup(prod1_grupo, prod2_grupo).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        prod1_grupo.next_to(texto_otimo, DOWN, buff=0.4).align_to(texto_otimo, LEFT)
        prod2_grupo.next_to(prod1_grupo, DOWN, buff=0.3).align_to(prod1_grupo, LEFT)
        
        # Objective function
        funcao_obj = MathTex(
            "Z = 0{,}8x_1 + 1{,}15x_2", 
            font_size=32, 
            color=WHITE
        ).next_to(axes, DOWN, buff=0.5).shift(DOWN*0.5+LEFT*1)
        
        # Profit calculation
        eq1 = MathTex(
            "Z = 0{,}8 \\times 1250 + 1{,}15 \\times 812{,}5", 
            font_size=30, 
            color=WHITE
        ).next_to(funcao_obj, DOWN, buff=0.4)
        
        eq2 = MathTex(
            "Z = 1000 + 934{,}38", 
            font_size=30, 
            color=WHITE
        ).next_to(eq1, DOWN, buff=0.3)
        
        lucro_final = MathTex(
            "Z = 1934{,}38", 
            font_size=42, 
            color=SECONDARY_COLOR
        ).next_to(eq2, DOWN, buff=0.3)
        
        # Daily profit text
        lucro_texto = Text(
            "Gerando um lucro diário de", 
            font=DEFAULT_FONT, 
            font_size=30,
            color=WHITE
        )
        
        lucro_valor = Text(
            "R$ 1934.38", 
            font=DEFAULT_FONT, 
            font_size=30,
            color=SECONDARY_COLOR
        )
        
        # Position profit text below production details
        lucro_grupo = VGroup(lucro_texto, lucro_valor).arrange(DOWN, buff=0.5)
        lucro_grupo.next_to(prod2_grupo, DOWN, buff=1.0).align_to(prod2_grupo, LEFT).shift(DOWN*0.8)
        
        # Highlight box for profit value
        destaque_box = SurroundingRectangle(
            lucro_valor, 
            color=BLUE, 
            buff=0.2, 
            corner_radius=0.1,
            stroke_width=3
        )
        
        # Animation sequence
        # Show the graph first
        self.play_with_factor(Create(axes, run_time=2))
        self.play_with_factor(
            Write(label_x),
            Write(label_y),
            run_time=1.5
        )
        self.play_with_factor(FadeIn(ponto_otimo, scale=1.2), run_time=1)
        self.play_with_factor(
            Create(linha_x),
            Create(linha_y),
            run_time=2
        )
        self.play_with_factor(
            Write(valor_x),
            Write(valor_y),
            run_time=1.5
        )
        
        # Show feasible region
        self.play_with_factor(
            DrawBorderThenFill(regiao_viavel),
            run_time=2
        )
        
        # Show text box and intro text
        self.play_with_factor(
            FadeIn(text_box),
            run_time=0.5
        )
        
        self.play_with_factor(Write(texto_intro, run_time=1.5))
        self.play_with_factor(Write(texto_otimo, run_time=1.5))
        
        # Show production values (animated from graph)
        self.play_with_factor(
            TransformFromCopy(valor_x, texto_valor1),
            FadeIn(texto_prod1),
            FadeIn(texto_desc1),
            run_time=2
        )
        
        self.play_with_factor(
            TransformFromCopy(valor_y, texto_valor2),
            FadeIn(texto_prod2),
            FadeIn(texto_desc2),
            run_time=2
        )
        
        # Show objective function and calculation
        self.play_with_factor(Write(funcao_obj, run_time=2))
        self.play_with_factor(Write(eq1, run_time=2))
        self.play_with_factor(Write(eq2, run_time=2))
        self.play_with_factor(Write(lucro_final, run_time=2))
        
        # Show profit conclusion
        self.play_with_factor(
            TransformFromCopy(lucro_final, lucro_valor),
            FadeIn(lucro_texto, shift=UP*0.3),
            run_time=2.5
        )
        
        # Highlight the profit value
        self.play_with_factor(Create(destaque_box, run_time=1.5))
        self.play_with_factor(
            destaque_box.animate.scale(1.1).set_stroke(width=4),
            lucro_valor.animate.scale(1.05),
            rate_func=there_and_back_with_pause,
            run_time=2.5
        )
        
        self.wait_with_factor(4)
        
        # Group elements for fade out
        grupo_grafico = VGroup(
            axes, ponto_otimo, linha_x, linha_y,
            label_x, label_y, valor_x, valor_y,
            regiao_viavel, funcao_obj, eq1, eq2, lucro_final
        )
        
        grupo_texto = VGroup(
            text_box, texto_intro_grupo,
            prod1_grupo, prod2_grupo,
            lucro_grupo, destaque_box
        )
        
        # Fade out everything
        self.play_with_factor(FadeOut(grupo_grafico), run_time=2)
        self.play_with_factor(FadeOut(grupo_texto), run_time=2)

        # Final

        texto_final = Text(
            "Vamos aprender como gerar o código dessa modelagem no próximo vídeo",
            font="IBM Plex Sans", 
            font_size=30,
            color=WHITE
        ).to_edge(UP, buff=0.5)

        self.play(Write(texto_final), run_time = 1.5)
        self.wait(1.0)
        
        # Load the image
        imagem = ImageMobject("assets/1740659060956.jpeg")
        imagem.set_height(5.0)
        imagem.to_edge(DOWN, buff=0.5)
        
        # Create a frame around the image (3b1b style)
        frame = SurroundingRectangle(imagem, color=BLUE_A, buff=0.1, stroke_width=3)
        
        # 3b1b style dot in the corner that transforms into the text
        dot = Dot(color=BLUE_A).scale(2)
        dot.to_corner(UL, buff=0.5)
          
        # Reveal the image with elegant animation
        self.play(
            FadeIn(imagem, shift=UP*0.5),
            run_time=1.5
        )
        
        # Create frame with drawing animation
        self.play(
            Create(frame),
            run_time=1.2
        )
        
        # Add subtle pulsing effect to frame (very 3b1b)
        self.play(
            frame.animate.scale(1.05),
            rate_func=there_and_back,
            run_time=1.5
        )

        self.wait(2.0)
        
        self.clear()