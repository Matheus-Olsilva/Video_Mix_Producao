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
        # Define a nova cor
        CUSTOM_COLOR = RED
        
        # Mais simples: criar elementos separados em vez de tentar indexar
        
        # Título
        resumo_modelo = Tex(
            r"\raggedright \linespread{1.5}\selectfont " 
            r"Recapitulando o que abordamos até o momento, temos o seguinte modelo matemático:",
            font_size=28, color=WHITE, stroke_width=0.3
        ).to_edge(LEFT, buff=0.5).shift(UP*2.5)
        
        # Título das variáveis
        var_titulo = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"As variáveis de decisão, que representam a decisão que devemos tomar",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(resumo_modelo, DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Variável x1
        var_x1 = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"$x_1$ = quantidade de iogurte a ser produzida",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(var_titulo, DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Variável x2
        var_x2 = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"$x_2$ = quantidade de queijo a ser produzida",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(var_x1, DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Função objetivo título
        obj_titulo = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Função objetivo:",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(var_x2, DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Função objetivo fórmula
        obj_formula = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Maximizar $Z = 0,80x_1 + 1,15x_2$",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(obj_titulo, DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Título restrições
        restricoes_titulo = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Restrições de Capacidade Produtiva:",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(obj_formula, DOWN, aligned_edge=LEFT, buff=0.4)
        
        # Restrições individuais
        restricao1 = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"$0.70x_1 + 0.40x_2 \leq 1200$",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(restricoes_titulo, DOWN, aligned_edge=LEFT, buff=0.2)
        
        restricao2 = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"$0.16x_1 + 0.32x_2 \leq 460$",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(restricao1, DOWN, aligned_edge=LEFT, buff=0.2)
        
        restricao3 = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"$0.25x_1 + 0.33x_2 \leq 650$",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(restricao2, DOWN, aligned_edge=LEFT, buff=0.2)
        
        restricao4 = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"$0.05x_1 + 0.09x_2 \leq 170$",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(restricao3, DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Restrições de demanda
        demanda_titulo = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Restrições de Demanda:",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(restricoes_titulo, RIGHT, aligned_edge=LEFT, buff=4.0)
        
        demanda1 = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"$x_1 \geq 320$",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(demanda_titulo, DOWN, aligned_edge=LEFT, buff=0.2)
        
        demanda2 = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"$x_2 \geq 450$",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(demanda1, DOWN, aligned_edge=LEFT, buff=0.2)
        
        # 3B1B-style animations
        self.play_with_factor(FadeIn(resumo_modelo, shift=UP*0.3), run_time=2)
        self.wait_with_factor(0.5)
        
        # Animações para variáveis de decisão
        self.play_with_factor(Write(var_titulo), run_time=1.5)
        
        self.play_with_factor(Write(var_x1), run_time=1)
        highlight_x1 = SurroundingRectangle(var_x1, buff=0.1, color=CUSTOM_COLOR, stroke_width=1.5)
        self.play_with_factor(Create(highlight_x1), run_time=0.5)
        self.play_with_factor(FadeOut(highlight_x1), run_time=0.5)
        
        self.play_with_factor(Write(var_x2), run_time=1)
        highlight_x2 = SurroundingRectangle(var_x2, buff=0.1, color=CUSTOM_COLOR, stroke_width=1.5)
        self.play_with_factor(Create(highlight_x2), run_time=0.5)
        self.play_with_factor(FadeOut(highlight_x2), run_time=0.5)
        
        # Animações para função objetivo
        self.play_with_factor(Write(obj_titulo), run_time=1)
        self.play_with_factor(Write(obj_formula), run_time=1.5)
        
        # Adicionando apenas um destaque na fórmula completa
        obj_highlight = SurroundingRectangle(obj_formula, buff=0.1, color=CUSTOM_COLOR, stroke_width=1.5)
        self.play_with_factor(Create(obj_highlight), run_time=0.5)
        self.play_with_factor(FadeOut(obj_highlight), run_time=0.5)
        
        # Animações para restrições
        self.play_with_factor(Write(restricoes_titulo), run_time=1.5)
        
        # Animar cada restrição com destaque
        for restricao in [restricao1, restricao2, restricao3, restricao4]:
            self.play_with_factor(Write(restricao), run_time=1)
            
            highlight = SurroundingRectangle(restricao, buff=0.05, color=CUSTOM_COLOR, stroke_width=1.5)
            self.play_with_factor(Create(highlight), run_time=0.4)
            self.play_with_factor(FadeOut(highlight), run_time=0.3)
            self.wait_with_factor(0.2)
        
        # Animações para restrições de demanda
        self.play_with_factor(Write(demanda_titulo), run_time=1.5)
        
        # Apenas escrever as restrições de demanda, sem setas de destaque
        for demanda in [demanda1, demanda2]:
            self.play_with_factor(Write(demanda), run_time=1)
            self.wait_with_factor(0.3)
        
        self.wait_with_factor(1)
        
        # Armazenar referências como grupos para facilitar animações futuras
        self.titulo = resumo_modelo
        self.variaveis = VGroup(var_titulo, var_x1, var_x2)
        self.objetivo = VGroup(obj_titulo, obj_formula)
        self.restricoes_cap = VGroup(restricoes_titulo, restricao1, restricao2, restricao3, restricao4)
        self.restricoes_dem = VGroup(demanda_titulo, demanda1, demanda2)
        self.custom_color = CUSTOM_COLOR
    
    def prepare_for_graphical_method(self):
        """Prepare the model for graphical method explanation"""
        # First, fade out the title and variables
        self.play_with_factor(
            FadeOut(self.titulo, shift=UP*0.3), 
            FadeOut(self.variaveis, shift=UP*0.3)
        )

        # Move the remaining elements up
        self.play_with_factor(
            self.objetivo.animate.scale(0.9).shift(UP * 3.5),
            self.restricoes_cap.animate.scale(0.9).shift(UP * 3.8),
            self.restricoes_dem.animate.scale(0.9).shift(UP * 3.8 + LEFT * 0.5),
            run_time=1.5
        )

        # Explanation of graphical method
        metodo_grafico = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Para resolver este problema, utilizaremos o Método Gráfico que consiste em \\"
            r"encontrar a solução ótima do problema através da análise gráfica das restrições do modelo. Vamos começar analisando as restrições de capacidade produtiva:\\",
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(self.restricoes_cap, DOWN, aligned_edge=LEFT, buff=0.3).shift(UP*3.8)

        # Adicione um destaque ao texto - estilo 3B1B
        metodo_box = SurroundingRectangle(metodo_grafico, buff=0.2, color=self.custom_color, stroke_width=1.5, corner_radius=0.1)
        
        self.play_with_factor(Write(metodo_grafico, run_time=4))
        self.play_with_factor(Create(metodo_box), run_time=0.7)
        self.wait_with_factor(1.5)
        self.play_with_factor(
            FadeOut(metodo_grafico),
            FadeOut(metodo_box)
        )

        # Explanation for constraint equations
        resolucao = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Consideraremos as inequações como equações e as representaremos graficamente por meio de retas nos eixos $x_1$ e $x_2$. Vamos agora encontrar interseções em $x_1$ e $x_2$",
            font_size=24, color=WHITE, stroke_width=0.3
        ).next_to(self.restricoes_cap, DOWN, aligned_edge=LEFT, buff=0.2).shift(UP*3.8)

        self.play_with_factor(Write(resolucao, run_time=3))
        
        # Posicionando os círculos corretamente para x1 e x2
        # Encontrar as posições de x1 e x2 no texto - ajustado conforme imagem
        x1_pos = resolucao.get_center() + RIGHT * 0.8 + LEFT * 0.15
        x2_pos = resolucao.get_center() + RIGHT * 1.3 + LEFT * 0.1
        
        x1_circle = Circle(radius=0.2, color=self.custom_color, stroke_width=2).move_to(x1_pos)
        x2_circle = Circle(radius=0.2, color=self.custom_color, stroke_width=2).move_to(x2_pos)
        
        self.play_with_factor(
            AnimationGroup(
                Create(x1_circle),
                Create(x2_circle),
                lag_ratio=0.5
            ),
            run_time=1.5
        )
        
        self.play_with_factor(
            AnimationGroup(
                FadeOut(x1_circle),
                FadeOut(x2_circle),
                lag_ratio=0.3
            ),
            run_time=0.8
        )
        
        self.wait_with_factor(1)
        
        # Store reference
        self.resolucao = resolucao
    
    def show_constraint_calculations(self):
        """Show calculations for constraint equations intercepts"""
        # Convert inequalities to equations com transformação suave
        restricoes_original = MathTex(
            r"""
            0.70x_1 + 0.40x_2 \leq 1200 \\
            0.16x_1 + 0.32x_2 \leq 460 \\
            0.25x_1 + 0.33x_2 \leq 650 \\
            0.05x_1 + 0.09x_2 \leq 170
            """,
            font_size=25, color=WHITE
        ).next_to(self.resolucao, DOWN, aligned_edge=LEFT, buff=0.2)
        
        restricoes2 = MathTex(
            r"""
            0.70x_1 + 0.40x_2 = 1200 \\
            0.16x_1 + 0.32x_2 = 460 \\
            0.25x_1 + 0.33x_2 = 650 \\
            0.05x_1 + 0.09x_2 = 170
            """,
            font_size=25, color=WHITE
        ).next_to(self.resolucao, DOWN, aligned_edge=LEFT, buff=0.2)

        # Animação estilo 3B1B com transformação
        self.play_with_factor(Write(restricoes_original), run_time=2)
        self.wait_with_factor(1)
        
        # Transformação de ≤ para = (estilo 3B1B)
        self.play_with_factor(
            TransformMatchingTex(
                restricoes_original, 
                restricoes2,
                path_arc=PI/4
            ),
            run_time=1.5
        )
        
        self.wait_with_factor(1)
        self.play_with_factor(FadeOut(restricoes2))

        # Criar cada parte individualmente para evitar indexação complexa
        # Primeira equação e seus cálculos
        eq1 = MathTex(r"0.70x_1 + 0.40x_2 = 1200\\", font_size=25, color=WHITE)
        eq1_calc1 = MathTex(r"\quad \text{Para } x_1 = 0 \rightarrow 0.40x_2 = 1200 \rightarrow x_2 = 3000\\", font_size=25, color=WHITE)
        eq1_calc2 = MathTex(r"\quad \text{Para } x_2 = 0 \rightarrow 0.70x_1 = 1200 \rightarrow x_1 = 1714.29\\", font_size=25, color=WHITE)
        
        # Segunda equação e seus cálculos
        eq2 = MathTex(r"0.16x_1 + 0.32x_2 = 460\\", font_size=25, color=WHITE)
        eq2_calc1 = MathTex(r"\quad \text{Para } x_1 = 0 \rightarrow 0.32x_2 = 460 \rightarrow x_2 = 1437.5\\", font_size=25, color=WHITE)
        eq2_calc2 = MathTex(r"\quad \text{Para } x_2 = 0 \rightarrow 0.16x_1 = 460 \rightarrow x_1 = 2875\\", font_size=25, color=WHITE)
        
        # Terceira equação e seus cálculos
        eq3 = MathTex(r"0.25x_1 + 0.33x_2 = 650\\", font_size=25, color=WHITE)
        eq3_calc1 = MathTex(r"\quad \text{Para } x_1 = 0 \rightarrow 0.33x_2 = 650 \rightarrow x_2 = 1969.7\\", font_size=25, color=WHITE)
        eq3_calc2 = MathTex(r"\quad \text{Para } x_2 = 0 \rightarrow 0.25x_1 = 650 \rightarrow x_1 = 2600\\", font_size=25, color=WHITE)
        
        # Quarta equação e seus cálculos
        eq4 = MathTex(r"0.05x_1 + 0.09x_2 = 170\\", font_size=25, color=WHITE)
        eq4_calc1 = MathTex(r"\quad \text{Para } x_1 = 0 \rightarrow 0.09x_2 = 170 \rightarrow x_2 = 1888.9\\", font_size=25, color=WHITE)
        eq4_calc2 = MathTex(r"\quad \text{Para } x_2 = 0 \rightarrow 0.05x_1 = 170 \rightarrow x_1 = 3400", font_size=25, color=WHITE)
        
        # Posicionar as equações
        eq1.next_to(self.resolucao, DOWN, aligned_edge=LEFT, buff=0.2)
        eq1_calc1.next_to(eq1, DOWN, aligned_edge=LEFT, buff=0.1)
        eq1_calc2.next_to(eq1_calc1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        eq2.next_to(eq1_calc2, DOWN, aligned_edge=LEFT, buff=0.2)
        eq2_calc1.next_to(eq2, DOWN, aligned_edge=LEFT, buff=0.1)
        eq2_calc2.next_to(eq2_calc1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        # Posicionar as equações à direita
        eq3.next_to(eq1, RIGHT, buff=3.0)
        eq3_calc1.next_to(eq3, DOWN, aligned_edge=LEFT, buff=0.1)
        eq3_calc2.next_to(eq3_calc1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        eq4.next_to(eq3_calc2, DOWN, aligned_edge=LEFT, buff=0.2)
        eq4_calc1.next_to(eq4, DOWN, aligned_edge=LEFT, buff=0.1)
        eq4_calc2.next_to(eq4_calc1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        # Animação gradual de cada linha (estilo 3B1B) - primeira coluna
        equations_col1 = [(eq1, eq1_calc1, eq1_calc2), (eq2, eq2_calc1, eq2_calc2)]
        
        for eq, calc1, calc2 in equations_col1:
            # Escreve a equação
            self.play_with_factor(Write(eq), run_time=1)
            
            # Calcula o primeiro intercepto
            self.play_with_factor(Write(calc1), run_time=1.5)
            self.wait_with_factor(0.3)
            
            # Calcula o segundo intercepto
            self.play_with_factor(Write(calc2), run_time=1.5)
            self.wait_with_factor(0.5)
        
        # Animação gradual de cada linha (estilo 3B1B) - segunda coluna
        equations_col2 = [(eq3, eq3_calc1, eq3_calc2), (eq4, eq4_calc1, eq4_calc2)]
        
        for eq, calc1, calc2 in equations_col2:
            # Escreve a equação
            self.play_with_factor(Write(eq), run_time=1)
            
            # Calcula o primeiro intercepto
            self.play_with_factor(Write(calc1), run_time=1.5)
            self.wait_with_factor(0.3)
            
            # Calcula o segundo intercepto
            self.play_with_factor(Write(calc2), run_time=1.5)
            self.wait_with_factor(0.5)

        # Agrupar equações para facilitar a remoção
        restricoes_grupo1 = VGroup(eq1, eq1_calc1, eq1_calc2, eq2, eq2_calc1, eq2_calc2)
        restricoes_grupo2 = VGroup(eq3, eq3_calc1, eq3_calc2, eq4, eq4_calc1, eq4_calc2)
        
        # Clean up for next part com efeito de fade suave
        self.play_with_factor(
            FadeOut(self.resolucao, shift=DOWN*0.2), 
            FadeOut(self.restricoes_cap, shift=DOWN*0.2), 
            FadeOut(self.objetivo, shift=DOWN*0.2), 
            FadeOut(self.restricoes_dem, shift=DOWN*0.2)
        )

        self.play_with_factor(
            FadeOut(restricoes_grupo1, shift=DOWN*0.2), 
            FadeOut(restricoes_grupo2, shift=DOWN*0.2)
        )
    
    def show_demand_constraint_calculations(self):
        """Show calculations for demand constraints"""
        restricoes_demanda1 = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Aplicaremos agora o mesmo procedimento para as restrições de demandas mínimas.", 
            font_size=25, color=WHITE, stroke_width=0.3
        ).to_edge(LEFT, buff=0.5).shift(UP*3.0)

        # Não adiciona o underline que estava na imagem 2

        # Criar as inequações originais
        restricao_x1 = MathTex(r"x_1 \geq 320", font_size=25, color=WHITE)
        restricao_x2 = MathTex(r"x_2 \geq 450", font_size=25, color=WHITE)
        
        # Agrupar as inequações
        restricoes_demanda2 = VGroup(restricao_x1, restricao_x2).arrange(DOWN, buff=0.3)
        restricoes_demanda2.next_to(restricoes_demanda1, DOWN, aligned_edge=LEFT, buff=0.4)

        # Criar as equações transformadas
        equacao_x1 = MathTex(r"x_1 = 320", font_size=25, color=WHITE)
        equacao_x2 = MathTex(r"x_2 = 450", font_size=25, color=WHITE)
        
        # Agrupar as equações
        restricoes_demanda3 = VGroup(equacao_x1, equacao_x2).arrange(DOWN, buff=0.3)
        restricoes_demanda3.next_to(restricoes_demanda2, RIGHT, buff=1.5).shift(RIGHT*1.0)

        seta1 = Arrow(
            start=restricoes_demanda2.get_right(), 
            end=restricoes_demanda3.get_left(),
            buff=0.2,
            color=SECONDARY_COLOR,
            max_stroke_width_to_length_ratio=5,
            max_tip_length_to_length_ratio=0.5
        )

        # Animações estilo 3B1B
        self.play_with_factor(
            Write(restricoes_demanda1), 
            run_time=2
        )
        
        # Remover underline
        self.wait_with_factor(0.5)
        
        # Animar as restrições de demanda uma por uma - SEM círculos nas inequações
        for restricao in [restricao_x1, restricao_x2]:
            self.play_with_factor(Write(restricao), run_time=1)
            self.wait_with_factor(0.3)
        
        # Seta verde
        self.play_with_factor(GrowArrow(seta1), run_time=1)
        self.wait_with_factor(0.5)
        
        # Animar a transformação das restrições
        self.play_with_factor(Write(restricoes_demanda3), run_time=2)
        
        # Destaque os valores com um efeito de pulsação - APENAS nos valores finais (equações)
        for i, equacao in enumerate([equacao_x1, equacao_x2]):
            if i == 0:  # Para x1 = 320
                value_pos = equacao.get_center() + RIGHT * 0.3 + UP * 0.03
            else:  # Para x2 = 450
                value_pos = equacao.get_center() + RIGHT * 0.3 + UP * 0.03
            
            pulse_circle = Circle(
                radius=0.2, 
                color=RED,  # Cor vermelha 
                stroke_width=2
            ).move_to(value_pos)
            
            self.play_with_factor(Create(pulse_circle), run_time=0.4)
            self.play_with_factor(
                pulse_circle.animate.scale(1.3).set_stroke(opacity=0),
                run_time=0.6,
                rate_func=smooth
            )

        explicativo = Tex(
            r"\raggedright \linespread{1.5}\selectfont "
            r"Como as restrições de demanda são equações mais diretas, não precisamos fazer a divisão dos coeficientes.\\"
            r"Assim, temos que $x_1 = 320$ e $x_2 = 450$.", 
            font_size=25, color=WHITE, stroke_width=0.3
        ).next_to(restricoes_demanda2, DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Animação de escrita com destaque
        self.play_with_factor(Write(explicativo), run_time=3)
        
        # Destaque a conclusão com um retângulo
        conclusao_box = SurroundingRectangle(
            explicativo, 
            buff=0.1, 
            color=RED,  # Cor vermelha
            stroke_width=1.5,
            corner_radius=0.05
        )
        self.play_with_factor(Create(conclusao_box), run_time=0.7)
        self.play_with_factor(FadeOut(conclusao_box), run_time=0.5)
        
        self.wait_with_factor(1)
        
        # Store references
        self.restricoes_demanda1 = restricoes_demanda1
        self.restricoes_demanda2 = restricoes_demanda2
        self.restricoes_demanda3 = restricoes_demanda3
        self.explicativo = explicativo
        self.seta1 = seta1
    
    def show_constraint_summary_table(self):
        """Create a summary table of all constraints"""
        tabela_final = self.create_constraint_table(scale=0.4)
        tabela_final.next_to(self.explicativo, DOWN, buff=0.5).shift(LEFT*1.0)

        # Criação progressiva da tabela (estilo 3B1B)
        horizontal_lines = tabela_final.get_horizontal_lines()
        vertical_lines = tabela_final.get_vertical_lines()
        entries = tabela_final.get_entries()
        
        # Animar linhas horizontais com pequeno atraso entre elas
        self.play_with_factor(
            AnimationGroup(
                *[Create(line) for line in horizontal_lines],
                lag_ratio=0.2,
                run_time=1.5
            )
        )
        
        # Animar linhas verticais com pequeno atraso entre elas
        self.play_with_factor(
            AnimationGroup(
                *[Create(line) for line in vertical_lines],
                lag_ratio=0.2,
                run_time=1.5
            )
        )
        
        # Animar entradas uma por uma com agrupamento por linha
        num_cols = 3  # Assumindo que a tabela tem 3 colunas
        
        # Criar grupos de entradas por linha (assumindo que as entradas estão em ordem)
        entry_groups = []
        for i in range(0, len(entries), num_cols):
            end_idx = min(i + num_cols, len(entries))
            row_entries = entries[i:end_idx]
            entry_groups.append(row_entries)
        
        # Animar cada grupo (linha)
        for group in entry_groups:
            self.play_with_factor(
                AnimationGroup(
                    *[Write(entry) for entry in group],
                    lag_ratio=0.2,
                    run_time=1.0
                )
            )
            self.wait_with_factor(0.2)
        
        # Não adicionamos o retângulo de destaque na tabela final, removido conforme solicitado
        self.wait_with_factor(1.5)
        
        # Clean up everything for the next scene com fade suave
        self.play_with_factor(
            FadeOut(self.restricoes_demanda1, shift=DOWN*0.2),
            FadeOut(self.restricoes_demanda2, shift=DOWN*0.2),
            FadeOut(self.restricoes_demanda3, shift=DOWN*0.2),
            FadeOut(self.explicativo, shift=DOWN*0.2),
            FadeOut(self.seta1, shift=DOWN*0.2),
            FadeOut(tabela_final, shift=DOWN*0.2)
        )