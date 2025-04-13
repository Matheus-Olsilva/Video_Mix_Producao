from manim import *
from scenes.base_scene import BaseScene
from constants import *
import utils

class OptimizationModelScene(BaseScene):
    """Scene that shows the complete mathematical model"""
    
    def construct(self):
        self.setup()
        self.show_complete_model()
        self.prepare_for_graphical_method()
        self.show_constraint_calculations()
        self.show_demand_constraint_calculations()
        self.show_constraint_summary_table()  # Renamed method
    
    def show_complete_model(self):
        """Show the complete mathematical model"""
        Resumo_modelo = Tex(
            r"\raggedright \linespread{1.5}\selectfont " 
            r"Recapitulando o que abordamos até o momento, temos o seguinte modelo matemático:",
            font_size=28, color=WHITE, stroke_width=0.3
        ).to_edge(LEFT, buff=0.5).shift(UP*2.5)
    
        variaveis_decisao = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"As variáveis de decisão, que representam a decisão que devemos tomar \\"
            r"$x_1$ = quantidade de iogurte a ser produzida \\"
            r"$x_2$ = quantidade de queijo a ser produzida",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(Resumo_modelo, DOWN, aligned_edge=LEFT, buff=0.4)

        funcao_objetivo = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Função objetivo: \\"
            r"Maximizar $Z = 0,80x_1 + 1,15x_2$",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(variaveis_decisao, DOWN, aligned_edge=LEFT, buff=0.4)

        restricoes = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Restrições de Capacidade Produtiva: \\"
            r"$0.70x_1 + 0.40x_2 \leq 1200$ \\"
            r"$0.16x_1 + 0.32x_2 \leq 460$ \\"
            r"$0.25x_1 + 0.33x_2 \leq 650$ \\"
            r"$0.05x_1 + 0.09x_2 \leq 170$",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(funcao_objetivo, DOWN, aligned_edge=LEFT, buff=0.4)

        restricoes_demanda = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Restrições de Demanda: \\"
            r"$x_1 \geq 320$ \\"
            r"$x_2 \geq 450$",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(restricoes, RIGHT, aligned_edge=LEFT, buff=0.4).shift(RIGHT*2.5+UP*0.45)

        # Animation sequence
        self.play_with_factor(Write(Resumo_modelo, run_time=3))
        self.play_with_factor(Write(variaveis_decisao, run_time=3))
        self.play_with_factor(Write(funcao_objetivo, run_time=6))
        self.play_with_factor(Write(restricoes, run_time=6))
        self.play_with_factor(Write(restricoes_demanda, run_time=6))
        self.wait_with_factor(2)
        
        # Store references to these elements
        self.resumo_modelo = Resumo_modelo
        self.variaveis_decisao = variaveis_decisao
        self.funcao_objetivo = funcao_objetivo
        self.restricoes = restricoes
        self.restricoes_demanda = restricoes_demanda
    
    def prepare_for_graphical_method(self):
        """Prepare the model for graphical method explanation"""
        # First, fade out the title and variables to make room
        self.play_with_factor(FadeOut(self.resumo_modelo), FadeOut(self.variaveis_decisao))

        # Move the remaining elements up to make room for explanation
        self.play_with_factor(
            self.funcao_objetivo.animate.scale(0.9).shift(UP * 3.5),
            self.restricoes.animate.scale(0.9).shift(UP * 3.8),
            self.restricoes_demanda.animate.scale(0.9).shift(UP * 3.8 +LEFT*0.5),
            run_time=2
        )

        # Explanation of graphical method
        metodo_grafico = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Para resolver este problema, utilizaremos o Método Gráfico que consiste em \\"
            r"encontrar a solução ótima do problema através da análise gráfica das restrições do modelo. Vamos começar analisando as restrições de capacidade produtiva:\\",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(self.restricoes, DOWN, aligned_edge=LEFT, buff=0.3).shift(UP*3.8)

        self.play_with_factor(Write(metodo_grafico, run_time=6))
        self.wait_with_factor(3)
        self.play_with_factor(FadeOut(metodo_grafico))

        # Explanation for constraint equations
        resolucao = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Consideraremos as inequações como equações e as representaremos graficamente por meio de retas nos eixos $x_1$ e $x_2$. Vamos agora encontrar interseções em $x_1$ e $x_2$",
            font_size=24, color=WHITE, stroke_width=0.3
        ).next_to(self.restricoes, DOWN, aligned_edge=LEFT, buff=0.2).shift(UP*3.8)

        self.play_with_factor(Write(resolucao, run_time=6))
        self.wait_with_factor(3)
        
        # Store reference
        self.resolucao = resolucao
    
    def show_constraint_calculations(self):
        """Show calculations for constraint equations intercepts"""
        # Convert inequalities to equations
        restricoes2 = MathTex(
            r"""
            0.70x_1 + 0.40x_2 &= 1200 \\
            0.16x_1 + 0.32x_2 &= 460 \\
            0.25x_1 + 0.33x_2 &= 650 \\
            0.05x_1 + 0.09x_2 &= 170
            """,
            font_size=25, color=WHITE
        ).next_to(self.resolucao, DOWN, aligned_edge=LEFT, buff=0.2)

        self.play_with_factor(Write(restricoes2, run_time=6))
        self.wait_with_factor(3)
        self.play_with_factor(FadeOut(restricoes2))

        # Calculate intercepts for first two constraints
        restricoes3 = MathTex(
            r"0.70x_1 + 0.40x_2 &= 1200\\",
            r"\quad \text{Para } x_1 = 0 &\rightarrow 0.40x_2 = 1200 \rightarrow x_2 = 3000\\",
            r"\quad \text{Para } x_2 = 0 &\rightarrow 0.70x_1 = 1200 \rightarrow x_1 = 1714.29\\",
            r"0.16x_1 + 0.32x_2 &= 460\\",
            r"\quad \text{Para } x_1 = 0 &\rightarrow 0.32x_2 = 460 \rightarrow x_2 = 1437.5\\",
            r"\quad \text{Para } x_2 = 0 &\rightarrow 0.16x_1 = 460 \rightarrow x_1 = 2875\\",
            font_size=25, color=WHITE
        ).next_to(self.resolucao, DOWN, aligned_edge=LEFT, buff=0.2)

        # Calculate intercepts for last two constraints
        restricoes4 = MathTex(
            r"0.25x_1 + 0.33x_2 &= 650\\",
            r"\quad \text{Para } x_1 = 0 &\rightarrow 0.33x_2 = 650 \rightarrow x_2 = 1969.7\\",
            r"\quad \text{Para } x_2 = 0 &\rightarrow 0.25x_1 = 650 \rightarrow x_1 = 2600\\",
            r"0.05x_1 + 0.09x_2 &= 170\\",
            r"\quad \text{Para } x_1 = 0 &\rightarrow 0.09x_2 = 170 \rightarrow x_2 = 1888.9\\",
            r"\quad \text{Para } x_2 = 0 &\rightarrow 0.05x_1 = 170 \rightarrow x_1 = 3400", 
            font_size=25, color=WHITE
        ).next_to(restricoes3, RIGHT, aligned_edge=LEFT, buff=0.3).shift(RIGHT*3.0)
        
        self.play_with_factor(Write(restricoes3, run_time=12))
        self.play_with_factor(Write(restricoes4, run_time=12))

        # Após criar e animar restricoes3 e restricoes4
        self.restricoes3 = restricoes3
        self.restricoes4 = restricoes4
        
        # Clean up for next part
        self.play_with_factor(
            FadeOut(self.resolucao), 
            FadeOut(self.restricoes), 
            FadeOut(self.funcao_objetivo), 
            FadeOut(self.restricoes_demanda)
        )

        self.play(FadeOut(restricoes3), FadeOut(restricoes4))
    
    def show_demand_constraint_calculations(self):
        """Show calculations for demand constraints"""
        restricoes_demanda1 = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Aplicaremos agora o mesmo procedimento para as restrições de demandas mínimas.", 
            font_size=25, color=WHITE, stroke_width=0.3
        ).to_edge(LEFT, buff=0.5).shift(UP*3.0)

        restricoes_demanda2 = MathTex(
            r"x_1 \geq 320 \\",
            r"x_2 \geq 450", 
            font_size=25, color=WHITE
        ).next_to(restricoes_demanda1, DOWN, aligned_edge=LEFT, buff=0.4)

        restricoes_demanda3 = MathTex(
            r"x_1 &= 320 \\",
            r"x_2 &= 450", 
            font_size=25, color=WHITE
        ).next_to(restricoes_demanda2, RIGHT, aligned_edge=LEFT, buff=1.5).shift(RIGHT*1.0)

        seta1 = Arrow(
            start=restricoes_demanda2.get_right(), 
            end=restricoes_demanda3.get_left(),
            buff=0.2,
            color=SECONDARY_COLOR,
            max_stroke_width_to_length_ratio=5,
            max_tip_length_to_length_ratio=0.5
        )

        self.play_with_factor(Write(restricoes_demanda1, run_time=3))
        self.wait_with_factor(1.5)
        self.play_with_factor(Write(restricoes_demanda2, run_time=3))
        self.wait_with_factor(1.5)
        self.play_with_factor(Create(seta1))
        self.wait_with_factor(1.5)
        self.play_with_factor(Write(restricoes_demanda3, run_time=3))
        self.wait_with_factor(1.5)

        explicativo = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Como as restrições de demanda são equações mais diretas, não precisamos fazer a divisão dos coeficientes.\\"
            r"Assim, temos que $x_1 = 320$ e $x_2 = 450$.", 
            font_size=25, color=WHITE, stroke_width=0.3
        ).next_to(restricoes_demanda2, DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play_with_factor(Write(explicativo, run_time=6))
        self.wait_with_factor(1.5)
        
        # Store references
        self.restricoes_demanda1 = restricoes_demanda1
        self.restricoes_demanda2 = restricoes_demanda2
        self.restricoes_demanda3 = restricoes_demanda3
        self.explicativo = explicativo
        self.seta1 = seta1
    
    def show_constraint_summary_table(self):  # Renamed this method
        """Create a summary table of all constraints"""
        tabela_final = self.create_constraint_table(scale=0.4)  # Now calls the parent method properly
        tabela_final.next_to(self.explicativo, DOWN, buff=0.5).shift(LEFT*1.0)

        self.play_with_factor(Create(tabela_final, run_time=5))
        self.wait_with_factor(3)
        
        # Clean up everything for the next scene
        self.play_with_factor(
            FadeOut(self.restricoes_demanda1),
            FadeOut(self.restricoes_demanda2),
            FadeOut(self.restricoes_demanda3),
            FadeOut(self.explicativo),
            FadeOut(self.seta1),
            FadeOut(tabela_final)
        )