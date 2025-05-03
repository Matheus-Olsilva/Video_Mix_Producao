from manim import *
from scenes.base_scene import BaseScene
from constants import *
import utils

class GraphicalSolutionScene(BaseScene):
    """Scene that shows the graphical solution of the optimization problem"""
    
    def construct(self):
        self.setup()
        self.show_graphical_solution()
    
    def show_graphical_solution(self):
        """Show the graphical representation of the problem and solution"""
        # Create axes
        axes = utils.create_axes()
        
        # Define all constraint lines with complete arrows
        lines_and_equations = []
        for i, constraint in enumerate(CONSTRAINTS):
            # Skip constraints without both intercepts
            if constraint["x_intercept"] is not None and constraint["y_intercept"] is not None:
                # Standard line with two intercepts
                line = Line(
                    axes.coords_to_point(constraint["x_intercept"], 0),
                    axes.coords_to_point(0, constraint["y_intercept"]),
                    color=constraint["color"]
                )
                intercepts = [(constraint["x_intercept"], 0), (0, constraint["y_intercept"])]
            elif constraint["x_intercept"] is not None:
                # Vertical line (x = constant)
                line = Line(
                    axes.coords_to_point(constraint["x_intercept"], 0),
                    axes.coords_to_point(constraint["x_intercept"], 3500),
                    color=constraint["color"]
                )
                intercepts = [(constraint["x_intercept"], 0)]
            elif constraint["y_intercept"] is not None:
                # Horizontal line (y = constant)
                line = Line(
                    axes.coords_to_point(0, constraint["y_intercept"]),
                    axes.coords_to_point(4000, constraint["y_intercept"]),
                    color=constraint["color"]
                )
                intercepts = [(0, constraint["y_intercept"])]
                
            lines_and_equations.append((
                line,
                constraint["name"],
                MathTex(constraint["inequality"], font_size=36, color=WHITE),
                intercepts
            ))
        
        # Create legend
        legend = VGroup()
        all_line_dots = []  # Store all dots for lines
        
        for line, label, equation, _ in lines_and_equations:
            color = line.get_color()
            entry = VGroup(
                Dot(color=color, radius=0.05),
                MathTex(label, font_size=36, color=WHITE),
                equation.copy()
            ).arrange(RIGHT, buff=0.3)
            legend.add(entry)
            
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        legend.to_corner(UR, buff=0.5)
        legend.scale(0.7)
        legend.set_opacity(0)  # Initially transparent
        
        # Initial animation of axes
        self.play_with_factor(Create(axes, run_time=1.5))
        self.wait_with_factor(0.5)
        
        # Animation of each line with its dots
        for i, (line, label, equation, intercepts) in enumerate(lines_and_equations):
            # Create dots for intercepts with the line's color
            line_dots = VGroup(*[
                Dot(axes.coords_to_point(x, y), color=line.get_color(), radius=0.07)
                for x, y in intercepts
            ])
            all_line_dots.append(line_dots)  # Store dots
            
            # Animate line, dots, and legend entry
            self.play_with_factor(
                Create(line),
                LaggedStartMap(GrowFromCenter, line_dots, lag_ratio=0.3),
                legend[i].animate.set_opacity(1).shift(LEFT*0.1),
                run_time=1.5
            )
            self.wait_with_factor(0.8)
        
        # Create arrow groups to indicate feasible directions
        arrow_mobjects = utils.create_arrows_for_region(axes)
        
        # Animate arrow groups in sequence
        # 1. Horizontal top arrows
        self.play_with_factor(
            LaggedStart(*[
                FadeIn(arrow, scale=0.95) 
                for arrow in arrow_mobjects["horizontal_top"]
            ], lag_ratio=0.15),
            run_time=1.5
        )
        
        # 2. Diagonal arrows
        self.play_with_factor(
            LaggedStart(*[
                FadeIn(arrow, scale=0.95) 
                for arrow in arrow_mobjects["diagonal"]
            ], lag_ratio=0.08),
            run_time=1.6
        )
        
        # 3. Long diagonal arrows
        self.play_with_factor(
            LaggedStart(*[
                FadeIn(arrow, scale=0.95) 
                for arrow in arrow_mobjects["diagonal_long"]
            ], lag_ratio=0.04),
            run_time=1.8
        )
        
        # 4. Vertical right arrows
        self.play_with_factor(
            LaggedStart(*[
                FadeIn(arrow, scale=0.95) 
                for arrow in arrow_mobjects["vertical_right"]
            ], lag_ratio=0.08),
            run_time=1.5
        )
        
        # Group all arrows for later animation
        all_arrows = VGroup(
            *arrow_mobjects["horizontal_top"],
            *arrow_mobjects["diagonal"],
            *arrow_mobjects["diagonal_long"],
            *arrow_mobjects["vertical_right"]
        )
        
        # Subtle highlight effect for arrows
        self.play_with_factor(
            AnimationGroup(
                all_arrows.animate.set_color("#6E6EFF"),  # Slightly lighter blue
                all_arrows.animate.set_stroke_width(4),   # Slightly thicker
            ),
            run_time=1.5,
            rate_func=there_and_back_with_pause
        )
        
        self.wait_with_factor(1.5)
        
        # Explanation of arrows
        explicacao = Tex(
            r"As setas sinalizam o sentido das \\ desigualdades em cada restrição, \\ apontando a região de solução", 
            font_size=30, color=WHITE, stroke_width=0.3
        ).next_to(legend, LEFT, buff=1.0).shift(UP*1)
        
        self.play_with_factor(Write(explicacao, run_time=3))
        self.wait_with_factor(2)
        
        # Graceful fade out
        self.play_with_factor(
            FadeOut(explicacao, shift=UP*0.2),
            FadeOut(all_arrows, lag_ratio=0.04, scale=0.9),
            run_time=2
        )
        
        # Highlight important intersections
        intersections = [
            ((320, 450), ["R5", "R6"]),
            ((1457.14, 450), ["R1", "R6"]),
            ((1250, 812.5), ["R1", "R2"]),
            ((320, 1277.5), ["R2", "R5"])
        ]
        
        # Create intersection dots and labels
        intersection_dots = VGroup()
        intersection_labels = VGroup()
        
        for point, labels in intersections:
            x, y = point
            dot = Dot(axes.coords_to_point(x, y), color=YELLOW, radius=0.1)
            label = MathTex(
                f"{{{', '.join(labels)}}}", 
                font_size=30, 
                color=WHITE
            ).next_to(dot, UP, buff=0.2)
            
            intersection_dots.add(dot)
            intersection_labels.add(label)
        
        # Animate intersection dots and labels
        self.play_with_factor(
            LaggedStartMap(GrowFromCenter, intersection_dots, lag_ratio=0.2),
            LaggedStartMap(FadeIn, intersection_labels, shift=UP, lag_ratio=0.2),
            run_time=2.5
        )
        self.wait_with_factor(1.5)
        
        # Create feasible region polygon
        feasible_region = utils.create_feasible_region(axes)
        
        # Create boundary lines of the feasible region
        clipped_lines = utils.create_constraint_boundary_lines(axes)
        
        # Remove non-boundary constraints (R3 and R4)
        non_boundary_indices = [2, 3]  # R3 and R4
        non_boundary_lines = VGroup(*[lines_and_equations[i][0] for i in non_boundary_indices])
        non_boundary_dots = VGroup(*[all_line_dots[i] for i in non_boundary_indices])
        
        self.play_with_factor(
            FadeOut(non_boundary_lines),
            FadeOut(non_boundary_dots),
            run_time=2
        )
        
        # Remove original lines and show the clipped ones with the feasible region
        original_line_indices = [0, 1, 4, 5]  # R1, R2, R5, R6
        original_lines = VGroup(*[lines_and_equations[i][0] for i in original_line_indices])
        original_dots = VGroup(*[all_line_dots[i] for i in original_line_indices])
        
        self.play_with_factor(
            FadeOut(original_lines),
            FadeOut(original_dots),
            Create(clipped_lines),
            FadeIn(feasible_region),
            run_time=1.5
        )
        
        # Explain the feasible region
        explicacao_regiao = Tex(
            r"A região viável indica o espaço de solução,\\que satisfaz todas as restrições", 
            font_size=28, color=WHITE, stroke_width=0.3
        ).next_to(legend, LEFT, buff=0.5).shift(LEFT*1)
        
        arrow5 = Arrow(
            explicacao_regiao.get_center() + DOWN*0.5, 
            feasible_region.get_center(), 
            color=HIGHLIGHT_COLOR, 
            buff=0, 
            max_stroke_width_to_length_ratio=5,
            max_tip_length_to_length_ratio=0.3
        )
        
        self.play_with_factor(Write(explicacao_regiao, run_time=2))
        self.play_with_factor(Create(arrow5))
        self.wait_with_factor(3)
        self.play_with_factor(FadeOut(explicacao_regiao), FadeOut(arrow5))
        
        # Clean up everything for transition to next scene
        self.play_with_factor(
            FadeOut(axes),
            FadeOut(clipped_lines),
            FadeOut(feasible_region),
            FadeOut(intersection_dots),
            FadeOut(intersection_labels),
            FadeOut(legend),
            run_time=2
        )