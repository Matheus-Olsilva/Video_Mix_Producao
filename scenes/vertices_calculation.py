from manim import *
from scenes.base_scene import BaseScene
from constants import *
import utils

class VerticesCalculationScene(BaseScene):
    """Scene showing the calculations for each vertex of the feasible region"""
    
    def __init__(self):
        super().__init__()
        self.grupo_definicao = None
    
    def construct(self):
        self.setup()
        self.introduce_fundamental_theorem()
        self.calculate_vertex_320_450()
        self.calculate_vertex_1457_450()
        self.calculate_vertex_1250_812()
        self.calculate_vertex_320_1277()
        self.show_optimal_solution_table()
    
    def introduce_fundamental_theorem(self):
        """Introduce the fundamental theorem of linear programming"""
        # Title
        titulo_calculos = Text(
            "Cálculo dos Vértices da Região Viável", 
            font=DEFAULT_FONT, 
            font_size=TITLE_FONT_SIZE
        ).set_color(WHITE)
        titulo_calculos.to_edge(UP, buff=0.5).shift(LEFT*1.0)
        
        # Definition text lines
        definicao = Text(
            "O Teorema Fundamental da Programação Linear afirma que, se existir uma", 
            font=DEFAULT_FONT, font_size=TEXT_FONT_SIZE
        ).set_color(WHITE)
        
        definicao2 = Text(
            "solução ótima para um problema de programação linear, ela estará em",
            font=DEFAULT_FONT, font_size=TEXT_FONT_SIZE
        ).set_color(WHITE)
        
        # Special formatting for "um dos vértices"
        um_dos = Text("um dos ", font=DEFAULT_FONT, font_size=TEXT_FONT_SIZE).set_color(WHITE)
        vertices_text = Text("vértices", font=DEFAULT_FONT, font_size=TEXT_FONT_SIZE).set_color(HIGHLIGHT_COLOR)
        da_regiao = Text(" da região viável.", font=DEFAULT_FONT, font_size=TEXT_FONT_SIZE).set_color(WHITE)
        
        # Group "um dos vértices da região viável"
        linha_modificada = VGroup(um_dos, vertices_text, da_regiao).arrange(RIGHT, buff=0.2)
        
        # Arrange all definition lines
        grupo_definicao = VGroup(definicao, definicao2, linha_modificada).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        grupo_definicao.next_to(titulo_calculos, DOWN, buff=0.5)
        
        # Animate the introduction
        self.play_with_factor(Write(titulo_calculos, run_time=2.0))
        self.play_with_factor(Write(definicao, run_time=2.5))
        self.play_with_factor(Write(definicao2, run_time=2.5))
        self.play_with_factor(Write(um_dos, run_time=0.8))
        self.play_with_factor(Write(vertices_text, run_time=1, rate_func=rate_functions.linear))
        self.play_with_factor(Write(da_regiao, run_time=1.2))
        self.play_with_factor(Indicate(vertices_text, color=HIGHLIGHT_COLOR, scale_factor=1.2))
        self.wait_with_factor(3)
        
        # Store reference to the definition group for later use
        self.grupo_definicao = VGroup(titulo_calculos, grupo_definicao)
    
    def create_vertex_calculation_visuals(self, vertex, title, equations, solution):
        """Create visuals for vertex calculation"""
        # Title showing intersecting constraints
        titulo = Text(title, font=DEFAULT_FONT, font_size=25, color=WHITE, stroke_width=0.5)
        
        # Calculation steps
        calculos = VGroup(*[MathTex(eq, font_size=28, color=WHITE) for eq in equations])
        calculos.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        # Final solution
        solution_tex = MathTex(solution, font_size=30, color=WHITE)
        
        # Group all calculation text
        calculo_completo = VGroup(titulo, calculos, solution_tex)
        calculo_completo.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        
        # Create graph components
        axes = utils.create_axes(x_length=4, y_length=3, scale_factor=0.8)
        feasible_region = utils.create_feasible_region(axes)
        boundary_lines = utils.create_constraint_boundary_lines(axes)
        
        # Create dot for the specific vertex
        x, y = vertex
        vertex_dot = Dot(axes.coords_to_point(x, y), color=YELLOW, radius=0.1)
        vertex_label = MathTex(f"({x}, {y})", font_size=24, color=WHITE).next_to(vertex_dot, UR, buff=0.1)
        
        # Group graph elements
        grafico = VGroup(axes, feasible_region, boundary_lines, vertex_dot, vertex_label)
        
        return calculo_completo, grafico
    
    def calculate_vertex_320_450(self):
        """Show calculation for vertex (320, 450)"""
        vertex = (320, 450)
        title = "Interseção de R5 e R6"
        equations = [
            r"\text{Interseção direta das restrições de demanda:}",
            r"\text{Definido por } x_1 = 320 \text{ e } x_2 = 450"
        ]
        solution = r"\text{Solução: } (320, 450)"
        
        calculo, grafico = self.create_vertex_calculation_visuals(
            vertex, title, equations, solution
        )
        
        # Position elements
        calculo.scale(1.0).to_edge(RIGHT, buff=1.0)
        grafico.scale(1.0).to_edge(LEFT, buff=1.5)
        
        # Position both below the definition
        grafico.next_to(self.grupo_definicao, DOWN, buff=0.5).shift(LEFT*3)
        calculo.next_to(self.grupo_definicao, DOWN, buff=0.5).align_to(grafico, UP).shift(RIGHT*3)
        
        # Animation sequence
        self.play_with_factor(Write(calculo[0], run_time=2))  # Title
        
        # Show the graph without the vertex first
        self.play_with_factor(Create(grafico[:-2], run_time=2))
        
        # Animate each step of the calculation
        for i in range(len(equations)):
            self.play_with_factor(Write(calculo[1][i], run_time=2.5))
            self.wait_with_factor(1.5)
        
        # Show solution and vertex dot
        self.play_with_factor(Write(calculo[2], run_time=2.5))
        self.play_with_factor(
            Create(grafico[-2]),  # vertex dot
            Write(grafico[-1]),   # vertex label
            run_time=2
        )
        
        # Highlight the vertex
        self.play_with_factor(
            Circumscribe(grafico[-2], color=YELLOW, time_width=2, run_time=2, stroke_width=5)
        )
        
        self.wait_with_factor(3)
        self.play_with_factor(FadeOut(calculo), FadeOut(grafico))
    
    def calculate_vertex_1457_450(self):
        """Show calculation for vertex (1457.14, 450)"""
        vertex = (1457.14, 450)
        title = "Interseção de R1 e R6"
        equations = [
            r"\text{Interseção de R1 com } x_2 = 450\text{:}",
            r"0.70x_1 + 0.40 \cdot 450 = 1200",
            r"0.70x_1 = 1020",
            r"x_1 = \frac{1020}{0.70} \approx 1457.14"
        ]
        solution = r"\text{Solução: } (1457.14, 450)"
        
        calculo, grafico = self.create_vertex_calculation_visuals(
            vertex, title, equations, solution
        )
        
        # Position elements
        calculo.scale(1.0).to_edge(RIGHT, buff=1.0)
        grafico.scale(1.0).to_edge(LEFT, buff=1.5)
        
        # Position both below the definition
        grafico.next_to(self.grupo_definicao, DOWN, buff=0.5).shift(LEFT*3)
        calculo.next_to(self.grupo_definicao, DOWN, buff=0.5).align_to(grafico, UP).shift(RIGHT*3)
        
        # Animation sequence
        self.play_with_factor(Write(calculo[0], run_time=2))  # Title
        
        # Show the graph without the vertex first
        self.play_with_factor(Create(grafico[:-2], run_time=2))
        
        # Animate each step of the calculation
        for i in range(len(equations)):
            self.play_with_factor(Write(calculo[1][i], run_time=2.5))
            self.wait_with_factor(1.5)
        
        # Show solution and vertex dot
        self.play_with_factor(Write(calculo[2], run_time=2.5))
        self.play_with_factor(
            Create(grafico[-2]),  # vertex dot
            Write(grafico[-1]),   # vertex label
            run_time=2
        )
        
        # Highlight the vertex
        self.play_with_factor(
            Circumscribe(grafico[-2], color=YELLOW, time_width=2, run_time=2, stroke_width=5)
        )
        
        self.wait_with_factor(3)
        self.play_with_factor(FadeOut(calculo), FadeOut(grafico))
    
    def calculate_vertex_1250_812(self):
        """Show calculation for vertex (1250, 812.5)"""
        vertex = (1250, 812.5)
        title = "Interseção de R1 e R2"
        equations = [
            r"0.70x_1 + 0.40x_2 = 1200",
            r"0.16x_1 + 0.32x_2 = 460",
            r"\text{Multiplicar a segunda equação por 1.25:}",
            r"0.20x_1 + 0.40x_2 = 575",
            r"\text{Subtrair da primeira: } 0.50x_1 = 625",
            r"x_1 = 1250",
            r"\text{Substituir em R2: } 0.16 \cdot 1250 + 0.32x_2 = 460",
            r"x_2 = 812.5"
        ]
        solution = r"\text{Solução: } (1250, 812.5)"
        
        calculo, grafico = self.create_vertex_calculation_visuals(
            vertex, title, equations, solution
        )
        
        # Position elements - scale down calculations due to length
        calculo.scale(0.9).to_edge(RIGHT, buff=1.0)
        grafico.scale(1.0).to_edge(LEFT, buff=1.5)
        
        # Position both below the definition
        grafico.next_to(self.grupo_definicao, DOWN, buff=0.5).shift(LEFT*3)
        calculo.next_to(self.grupo_definicao, DOWN, buff=0.5).align_to(grafico, UP).shift(RIGHT*3+UP*0.5)
        
        # Animation sequence
        self.play_with_factor(Write(calculo[0], run_time=2.5))  # Titl
        
        # Show the graph without the vertex first
        self.play_with_factor(Create(grafico[:-2], run_time=2.5))
        
        # Animate each step of the calculation
        for i in range(len(equations)):
            self.play_with_factor(Write(calculo[1][i], run_time=2.5))
            self.wait_with_factor(1.5)
        
        # Show solution and vertex dot
        self.play_with_factor(Write(calculo[2], run_time=2.5))
        self.play_with_factor(
            Create(grafico[-2]),  # vertex dot
            Write(grafico[-1]),   # vertex label
            run_time=2
        )
        
        # Highlight key equations
        destaques = [
            Indicate(calculo[1][1], color=RED, scale_factor=1.2),  # R1
            Indicate(calculo[1][2], color=GREEN, scale_factor=1.2)  # R2
        ]
        self.play_with_factor(AnimationGroup(*destaques, lag_ratio=0.5))
        
        # Highlight the vertex
        self.play_with_factor(
            Circumscribe(grafico[-2], color=YELLOW, time_width=2, run_time=2, stroke_width=5)
        )
        
        self.wait_with_factor(3)
        self.play_with_factor(FadeOut(calculo), FadeOut(grafico))
    
    def calculate_vertex_320_1277(self):
        """Show calculation for vertex (320, 1277.5)"""
        vertex = (320, 1277.5)
        title = "Interseção de R2 e R5"
        equations = [
            r"\text{Interseção de R2 com } x_1 = 320\text{:}",
            r"0.16 \cdot 320 + 0.32x_2 = 460",
            r"51.2 + 0.32x_2 = 460",
            r"0.32x_2 = 408.8",
            r"x_2 = \frac{408.8}{0.32} = 1277.5"
        ]
        solution = r"\text{Solução: } (320, 1277.5)"
        
        calculo, grafico = self.create_vertex_calculation_visuals(
            vertex, title, equations, solution
        )
        
        # Position elements
        calculo.scale(1.0).to_edge(RIGHT, buff=1.0)
        grafico.scale(1.0).to_edge(LEFT, buff=1.5)
        
        # Position both below the definition
        grafico.next_to(self.grupo_definicao, DOWN, buff=0.5).shift(LEFT*3)
        calculo.next_to(self.grupo_definicao, DOWN, buff=0.5).align_to(grafico, UP).shift(RIGHT*3)
        
        # Animation sequence
        self.play_with_factor(Write(calculo[0], run_time=2.5))  # Title
        
        # Show the graph without the vertex first
        self.play_with_factor(Create(grafico[:-2], run_time=2.5))
        
        # Animate each step of the calculation
        for i in range(len(equations)):
            self.play_with_factor(Write(calculo[1][i], run_time=2.5))
            self.wait_with_factor(1.5)
        
        # Show solution and vertex dot
        self.play_with_factor(Write(calculo[2], run_time=2.5))
        self.play_with_factor(
            Create(grafico[-2]),  # vertex dot
            Write(grafico[-1]),   # vertex label
            run_time=2
        )
        
        # Highlight the vertex
        self.play_with_factor(
            Circumscribe(grafico[-2], color=YELLOW, time_width=2, run_time=2, stroke_width=5)
        )
        
        self.wait_with_factor(3)
        
        # Clear everything including the definition before showing the final table
        self.play_with_factor(
            FadeOut(calculo), 
            FadeOut(grafico),
            FadeOut(self.grupo_definicao)
        )
    
    def show_optimal_solution_table(self):
        """Show table with objective function values at each vertex"""
        # Title
        titulo_tabela = Text(
            "Comparação dos Valores na Função Objetivo", 
            font=DEFAULT_FONT, 
            font_size=25, 
            color=WHITE, 
            stroke_width=0.5
        )
        titulo_tabela.to_edge(UP, buff=0.5)
        
        # Objective function
        funcao_objetivo = MathTex(
            r"\text{Função Objetivo: Maximizar } Z = 0{,}8x_1 + 1{,}15x_2", 
            font_size=34, 
            color=SECONDARY_COLOR
        )
        funcao_objetivo.next_to(titulo_tabela, DOWN, buff=0.5).to_edge(LEFT, buff=0.7)
        
        # Calculate objective function values for all vertices
        vertices = []
        for x, y in VERTICES:
            z_value = utils.calculate_objective_value(x, y)
            vertices.append((x, y, z_value))
        
        # Find optimal solution
        max_z_value = max(vertices, key=lambda x: x[2])
        max_z_index = vertices.index(max_z_value)
        
        # Create the table header
        cabecalho = VGroup(
            MathTex(r"\text{\textbf{Vértice }} (x_1, x_2)", font_size=34, color=WHITE),
            MathTex(r"\text{\textbf{Valor de }} Z", font_size=34, color=WHITE)
        ).arrange(RIGHT, buff=2.5)
        
        # Create table rows
        rows = VGroup(cabecalho)
        for i, (x, y, z) in enumerate(vertices):
            # Highlight the row with maximum z-value
            cor = SECONDARY_COLOR if i == max_z_index else WHITE
            
            linha = VGroup(
                MathTex(f"({x}, {y})", font_size=30, color=cor),
                MathTex(f"{z:.2f}", font_size=30, color=cor)
            ).arrange(RIGHT, buff=2.5)
            
            # Align with header
            linha[0].align_to(cabecalho[0], LEFT)
            linha[1].align_to(cabecalho[1], LEFT)
            
            rows.add(linha)
        
        # Arrange rows vertically
        rows.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        rows.next_to(funcao_objetivo, DOWN, buff=0.7).to_edge(LEFT, buff=0.7)
        
        # Add box around the table
        box = SurroundingRectangle(rows, color=WHITE, buff=0.3)
        
        # Create optimum solution text
        titulo_otimo = MathTex(r"\text{Solução Ótima}", font_size=28, color=WHITE)
        valor_otimo = MathTex(f"Z = {max_z_value[2]:.2f}", font_size=28, color=SECONDARY_COLOR)
        solucao_grupo = VGroup(titulo_otimo, valor_otimo).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Create graph for optimal solution
        axes = utils.create_axes(x_length=3.5, y_length=2.5, scale_factor=0.75)
        feasible_region = utils.create_feasible_region(axes)
        boundary_lines = utils.create_constraint_boundary_lines(axes)
        
        # Create dot for the optimal vertex
        x_opt, y_opt, z_opt = max_z_value
        ponto_destacado = Dot(axes.coords_to_point(x_opt, y_opt), color=SECONDARY_COLOR, radius=0.1)
        vertex_label = MathTex(f"({x_opt}, {y_opt})", font_size=18, color=WHITE).next_to(ponto_destacado, UR, buff=0.1)
        
        # Group graph elements
        grafico_final = VGroup(axes, feasible_region, boundary_lines, ponto_destacado, vertex_label)
        
        # Group solution and graph
        grafico_grupo = VGroup(solucao_grupo, grafico_final).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        grafico_grupo.next_to(box, RIGHT, buff=1.0)
        
        # Animation sequence
        self.play_with_factor(Write(titulo_tabela, run_time=2.5))
        self.play_with_factor(Write(funcao_objetivo, run_time=2.5))
        self.play_with_factor(
            Create(box),
            Write(cabecalho),
            run_time=2.5
        )
        
        # Show each row of the table
        for i in range(1, len(rows)):
            self.play_with_factor(Write(rows[i], run_time=2.5))
            self.wait_with_factor(1)
        
        # Show optimal solution
        self.play_with_factor(Write(titulo_otimo, run_time=2.5))
        self.play_with_factor(Write(valor_otimo, run_time=2.5))
        self.play_with_factor(Create(grafico_final, run_time=2.5))
        
        # Highlight the maximum value row
        destaque_max = Circumscribe(
            rows[max_z_index + 1],
            color=SECONDARY_COLOR,
            time_width=2,
            run_time=2,
            stroke_width=5
        )
        self.play_with_factor(destaque_max)
        
        # Highlight the optimal point
        destaque_ponto = Circumscribe(
            ponto_destacado,
            color=SECONDARY_COLOR,
            time_width=2,
            run_time=2,
            stroke_width=5
        )
        self.play_with_factor(destaque_ponto)
        
        self.wait_with_factor(4)
        self.play_with_factor(
            FadeOut(titulo_tabela),
            FadeOut(funcao_objetivo),
            FadeOut(box),
            FadeOut(rows),
            FadeOut(grafico_grupo),
            run_time=2
        )