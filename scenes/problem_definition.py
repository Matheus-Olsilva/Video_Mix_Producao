from manim import *
from scenes.base_scene import BaseScene
from constants import *

class ProblemDefinitionScene(BaseScene):
    """Scene that defines the optimization problem"""
    
    def construct(self):
        self.setup()
        self.show_minimum_requirements()
        self.show_additional_info()
        self.show_contribution_margin_table()
        self.show_objective_function_example()
        self.show_resource_constraints_table()
    
    def show_minimum_requirements(self):
        """Show minimum production requirements"""
        texto_intro = Tex(
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Devido a razões contratuais, a empresa necessita produzir\\uma quantidade mínima diária:",
            font_size=40, color=WHITE, stroke_width=0.3
        ).to_edge(LEFT)

        lista_quantidades = self.create_bulleted_list(
            [
                r"\raggedright \fontfamily{IBM Plex Sans}\selectfont 320kg de iogurte;",
                r"\raggedright \fontfamily{IBM Plex Sans}\selectfont 380kg de queijo.",
            ],
            font_size=40,
            buff=0.5
        ).to_edge(LEFT)

        texto_final = Tex(
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont A área comercial da empresa garante que existe mercado \\ para absorver qualquer nível de produção.",
            font_size=40, color=WHITE, stroke_width=0.3
        ).to_edge(LEFT)

        grupo = VGroup(texto_intro, lista_quantidades, texto_final)
        grupo.arrange(DOWN, aligned_edge=LEFT, buff=1.0).to_edge(LEFT, buff=0.5)

        # Animations
        self.play_with_factor(Write(texto_intro, run_time=2))
        self.wait_with_factor(1.5)
        self.play_with_factor(Write(lista_quantidades, running_start=2))
        self.wait_with_factor(1.5)
        self.play_with_factor(Write(texto_final, run_time=2))
        self.wait_with_factor(5)
        self.play_with_factor(FadeOut(grupo))

    def show_additional_info(self):
        """Show additional information about resources and constraints"""
        # Introduction text
        texto_intro = Tex(
            r"Você também possui informações sobre:",
            font_size=40, color=WHITE, stroke_width=0.3
        ).to_edge(LEFT)

        # List of information points
        lista_info = VGroup(
            self.create_bulleted_list([r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Matérias-primas usadas para fabricar cada produto;"], 
                                     font_size=40),
            self.create_bulleted_list([r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Disponibilidade de matérias-primas e demandas;"], 
                                     font_size=40),
            self.create_bulleted_list([r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Margem de contribuição de cada produto."], 
                                     font_size=40)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)

        # Group all elements
        grupo = VGroup(texto_intro, lista_info)
        grupo.arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(LEFT, buff=0.5)

        # Animations
        self.play_with_factor(Write(texto_intro, run_time=2))
        self.wait_with_factor(2.5)
        self.play_with_factor(Write(lista_info[0], run_time=2))
        self.play_with_factor(Write(lista_info[1], run_time=2))
        self.play_with_factor(Write(lista_info[2], run_time=2))
        self.wait_with_factor(4)
        self.play_with_factor(FadeOut(grupo))

    def show_contribution_margin_table(self):
        """Show table with product contribution margins"""
        titulo = Text(
            "Tabela 1: Margem de Contribuição Unitária (R$/kg)",
            font=DEFAULT_FONT, 
            color=WHITE,
            font_size=25,
            stroke_width=0.5
        ).to_edge(UP, buff=0.3)
        
        tabela = Table(
            [
                ["3,20", "2,40", "0,80"],
                ["6,30", "5,15", "1,15"],
            ],
            row_labels=[
                Text("Iogurte", font_size=20, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5),
                Text("Queijo Mussarela", font_size=20, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5)
            ],
            col_labels=[
                Text("Preço (R$/kg)", font_size=20, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5),
                Text("Custos Variáveis (R$/kg)", font_size=20, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5),
                Text("Margem (R$/kg)", font_size=20, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5)
            ],
            top_left_entry=Text("Produto", font_size=20, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5),
            include_outer_lines=True,
            h_buff=0.5,
            v_buff=0.3,
            element_to_mobject_config={
                "font_size": 24, 
                "color": WHITE,
                "font": DEFAULT_FONT,
                "stroke_width": 0.2
            }
        ).scale(0.9).next_to(titulo, DOWN, buff=0.3)
        
        texto_intro = Tex(
            r"\raggedright " 
            r"De acordo com os dados da tabela, vamos escrever um modelo matemático simples para resolver o problema.",
            font_size=32, color=WHITE, stroke_width=0.3
        ).to_edge(LEFT, buff=0.5)
        
        texto_variaveis = Tex(
            r"\raggedright " 
            r"Primeiro, definimos as variáveis: \\"
            r"$x_1$ = quantidade de iogurte a ser produzida \\"
            r"$x_2$ = quantidade de queijo a ser produzida",
            font_size=32, color=WHITE, stroke_width=0.3
        ).next_to(texto_intro, DOWN, aligned_edge=LEFT, buff=0.4)

        texto_fun_obj = Tex(
            r"\raggedright " 
            r"O nosso objetivo é maximizar o lucro total, que é a soma das margens de contribuição unitárias multiplicadas pelas quantidades de cada item: \\",
            font_size=32, color=WHITE, stroke_width=0.3
        ).next_to(texto_variaveis, DOWN, aligned_edge=LEFT, buff=0.4)

        texto_modelo = Tex(
            r"\raggedright " 
            r"Modelo: \\"
            r"$\text{Max } Z = 0,8x_1 + 1,15x_2$",
            font_size=32, color=WHITE, stroke_width=0.3
        ).next_to(texto_fun_obj, DOWN, aligned_edge=LEFT, buff=0.4)
        
        grupo = VGroup(titulo, tabela, texto_intro, texto_variaveis, texto_fun_obj, texto_modelo)
        grupo.arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(LEFT, buff=0.5)

        # Animations
        self.play_with_factor(Write(titulo, run_time=2))
        self.play_with_factor(Create(tabela, run_time=2))
        self.wait_with_factor(2.5)
        self.play_with_factor(Write(texto_intro, run_time=2))
        self.play_with_factor(Write(texto_variaveis, run_time=2))
        self.wait_with_factor(1.5)
        self.play_with_factor(Write(texto_fun_obj, run_time=2))
        
        # Highlight the margin column
        margem_col = tabela.get_columns()[3]  
        retangulo_destaque = SurroundingRectangle(
            margem_col,
            color=RED,
            buff=0.1,
            stroke_width=3
        )
        self.play_with_factor(Create(retangulo_destaque))
        self.wait_with_factor(2)

        self.wait_with_factor(3)
        self.play_with_factor(Write(texto_modelo, run_time=2))
        self.wait_with_factor(3)
        self.play_with_factor(FadeOut(grupo), FadeOut(retangulo_destaque))

    def show_objective_function_example(self):
        """Show example calculation of the objective function"""
        exemplicificacao = Tex(
            r"\raggedright \linespread{1.5}\selectfont " 
            r"Por exemplo, se produzirmos 400 kg de iogurte e 500 kg de queijo, o lucro total em Reais será: \\"
            r"$\text{Max } Z = 0,8x_1 + 1,15x_2$ \\"
            r"$Z = 0,8 \times 400 + 1,15 \times 500 = 320 + 575 = 895$",
            font_size=32, color=WHITE, stroke_width=0.3
        ).to_edge(LEFT, buff=0.5).shift(UP*2)
        
        exemplicificacao_restricoes = Tex(
           r"\raggedright \linespread{1.5}\selectfont "
            r"Porém, na prática, existem restrições de produção, como capacidade \\ de produção, demanda, etc.\\",
            r"Encontrar a solução que maximiza o lucro respeitando essas restrições é chamada de solução ótima.",
            font_size=32, color=WHITE, stroke_width=0.3
        ).next_to(exemplicificacao, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play_with_factor(Write(exemplicificacao, run_time=5))
        self.wait_with_factor(1.5)
        self.play_with_factor(Write(exemplicificacao_restricoes, run_time=5))
        self.wait_with_factor(3)
        self.play_with_factor(FadeOut(exemplicificacao), FadeOut(exemplicificacao_restricoes))

    def show_resource_constraints_table(self):
        """Show table with resource constraints"""
        explicacao_rest_materias_primas = Tex(
            r"\raggedright \linespread{1.5}\selectfont " 
            r"Vamos, então, elaborar um modelo simplificado para representar as restrições \\ de capacidade produtiva e demandas mínimas, conforme a tabela abaixo:",
            font_size=32, color=WHITE, stroke_width=0.3
        ).to_edge(LEFT, buff=0.5).shift(UP*2.5)
        
        tabela = Table(
            [
                ["0,70", "0,16", "0,25", "0,05", "320"],
                ["0,40", "0,32", "0,33", "0,09","450"],
                ["1200", "460", "650", "170", "-"]
            ],
            row_labels=[
                Text("Iogurte", font_size=24, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5),
                Text("Queijo", font_size=24, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5),
                Text("Capacidade", font_size=24, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5),
            ],
            col_labels=[
                Text("Leite (L)", font_size=24, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5),
                Text("Soro (L)", font_size=24, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5),
                Text("Gordura (kg)", font_size=24, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5),
                Text("Mão de obra (h)", font_size=24, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5),
                Text("Demandas (Kg)", font_size=24, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5)
            ],
            top_left_entry=Text("Produto", font_size=24, color=WHITE, font=DEFAULT_FONT, stroke_width=0.5),
            include_outer_lines=True,
            h_buff=0.5,
            v_buff=0.3,
            element_to_mobject_config={
                "font_size": 24, 
                "color": WHITE,
                "font": DEFAULT_FONT,
                "stroke_width": 0.2
            }
        ).scale(0.7).next_to(explicacao_rest_materias_primas, DOWN, buff=0.5)
        
        # Explanation text - resource usage
        onde_texto1 = self.create_bulleted_list(
            [r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Leite, soro e gordura são as matérias-primas utilizadas, enquanto a mão de obra representa o tempo, em horas-homem, necessário para a produção de cada produto;"],
            font_size=25,
            buff=0.4
        ).next_to(tabela, DOWN, buff=0.4).to_edge(LEFT)
        
        # Resource constraints
        restricoes = VGroup(
            MathTex(r"Leite(L) : 0,70x_1 + 0,40x_2", color=WHITE),
            MathTex(r"Soro(L) : 0,16x_1 + 0,32x_2", color=WHITE),
            MathTex(r"Gordura(kg) : 0,25x_1 + 0,33x_2", color=WHITE),
            MathTex(r"\text{Mão de Obra (h)} : 0,05x_1 + 0,09x_2", color=WHITE)
        ).arrange(DOWN, buff=0.4).scale(0.55).next_to(onde_texto1, DOWN).to_edge(LEFT)
        
        # Capacity constraints
        capacidades = VGroup(
            MathTex(r"&\leq 1200", color=WHITE),
            MathTex(r"&\leq 460", color=WHITE),
            MathTex(r"&\leq 650", color=WHITE),
            MathTex(r"&\leq 170", color=WHITE)
        ).arrange(DOWN, buff=0.4).scale(0.55)
        
        # Position capacity constraints next to resource constraints
        for i, cap in enumerate(capacidades):
            cap.next_to(restricoes[i], RIGHT, buff=0.1)
        
        # Decision variables
        texto_variaveis = Tex(
            r"\raggedright "
            r"$x_1$ = quantidade de iogurte a ser produzida \\"
            r"$x_2$ = quantidade de queijo a ser produzida",
            font_size=32, color=WHITE, stroke_width=0.3
        ).next_to(restricoes, RIGHT, buff=0.2).shift(RIGHT*1.5+UP*0.6)
        
        # Animations
        self.play_with_factor(Write(explicacao_rest_materias_primas, run_time=6))
        self.wait_with_factor(1.5)
        self.play_with_factor(Create(tabela, run_time=2.5))
        self.wait_with_factor(3)
        self.play_with_factor(Write(onde_texto1, run_time=5))
        
        # Highlight resource columns
        margem_col = tabela.get_columns()[1:5]
        retangulo_destaque = SurroundingRectangle(
            margem_col,
            color=RED,
            buff=0.1,
            stroke_width=3
        )
        self.play_with_factor(Create(retangulo_destaque))
        self.wait_with_factor(4)
        self.play_with_factor(Write(restricoes, run_time=6))
        self.wait_with_factor(3)
        
        # Highlight variables explanation
        retangulo_destaque_var = SurroundingRectangle(
            texto_variaveis,
            color=RED,
            buff=0.2,
            stroke_width=4
        )
        
        self.play_with_factor(
            Write(texto_variaveis, run_time=2.5),
            Create(retangulo_destaque_var),
            run_time=2
        )
        self.wait_with_factor(3)
        self.play_with_factor(FadeOut(retangulo_destaque_var))
        
        # Clean up first part
        self.play_with_factor(FadeOut(onde_texto1), FadeOut(retangulo_destaque))
        
        # Capacity explanation
        onde_texto2 = self.create_bulleted_list(
            [r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Capacidade é a quantidade máxima de cada matéria-prima (Kg) disponível e mão de obra (h);"],
            font_size=25,
            buff=0.4
        ).next_to(tabela, DOWN, buff=0.4).to_edge(LEFT)
        
        complementar_onde_texto2 = Tex(
            r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Vamos agora adicionar a capacidade ao modelo.",
            font_size=25, color=WHITE, stroke_width=0.3
        ).next_to(onde_texto2, DOWN, buff=0.2).to_edge(LEFT)
        
        self.play_with_factor(Write(onde_texto2, run_time=5))
        self.wait_with_factor(3)
        
        # Highlight capacity row
        margem_col = tabela.get_rows()[3]  
        retangulo_destaque1 = SurroundingRectangle(
            margem_col,
            color=RED,
            buff=0.05,
            stroke_width=3
        )
        self.play_with_factor(Create(retangulo_destaque1))
        self.wait_with_factor(1.5)
        self.play_with_factor(Write(complementar_onde_texto2, run_time=2.5))
        self.wait_with_factor(1.5)
        self.play_with_factor(Write(capacidades, run_time=6))
        self.wait_with_factor(3)
        
        # Clean up second part
        self.play_with_factor(
            FadeOut(onde_texto2), 
            FadeOut(retangulo_destaque1), 
            FadeOut(capacidades), 
            FadeOut(complementar_onde_texto2), 
            FadeOut(restricoes)
        )
        
        # Demand constraints
        onde_texto3 = self.create_bulleted_list(
            [r"\raggedright \fontfamily{IBM Plex Sans}\selectfont Demandas (Kg) são as quantidades mínimas de cada produto que devem ser produzidas."],
            font_size=25,
            buff=0.4
        ).next_to(tabela, DOWN, buff=0.4).to_edge(LEFT)
        
        Demanda_modelo = VGroup(
            MathTex(r"\text{Demanda de iogurte: } x_1 \geq 320", color=WHITE),
            MathTex(r"\text{Demanda de queijo: } x_2 \geq 450", color=WHITE)
        ).arrange(DOWN, buff=0.5).scale(0.55).next_to(onde_texto3, DOWN).to_edge(LEFT)
        
        self.play_with_factor(Write(onde_texto3, run_time=5))
        
        # Highlight demand column
        margem_col = tabela.get_columns()[5]
        retangulo_destaque2 = SurroundingRectangle(
            margem_col,
            color=RED,
            buff=0.05,
            stroke_width=3
        )
        self.play_with_factor(Create(retangulo_destaque2))
        self.wait_with_factor(3)
        self.play_with_factor(Write(Demanda_modelo, run_time=6))
        self.wait_with_factor(3)
        
        # Clean up everything
        self.play_with_factor(
            FadeOut(onde_texto3), 
            FadeOut(retangulo_destaque2), 
            FadeOut(Demanda_modelo), 
            FadeOut(texto_variaveis), 
            FadeOut(tabela), 
            FadeOut(explicacao_rest_materias_primas)
        )