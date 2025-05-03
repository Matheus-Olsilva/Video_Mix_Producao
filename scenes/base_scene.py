from manim import *
from constants import *
import utils

class BaseScene(Scene):
    """Base scene with common functionality for all scenes"""
    
    def setup(self):
        """Setup common configuration for all scenes"""
        self.camera.background_color = BACKGROUND_COLOR
        config.frame_width = FRAME_WIDTH
        config.frame_height = FRAME_HEIGHT
    
    def wait_with_factor(self, duration=1.0):
        """Wait for a duration adjusted by the timing factor"""
        self.wait(duration * TIMING_FACTOR)
        
    def play_with_factor(self, *animations, **kwargs):
        """Play animations with run_time adjusted by the timing factor"""
        if 'run_time' in kwargs:
            kwargs['run_time'] *= TIMING_FACTOR
        self.play(*animations, **kwargs)
        
    def create_titled_text(self, title_text, content_text, font_size=None, title_color=WHITE, content_color=WHITE):
        """Create a titled text block with a title and content"""
        if font_size is None:
            font_size = TEXT_FONT_SIZE
            
        title = Text(title_text, font=DEFAULT_FONT, font_size=font_size, color=title_color)
        content = Text(content_text, font=DEFAULT_FONT, font_size=font_size, color=content_color)
        
        group = VGroup(title, content).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        return group
        
    def create_bulleted_list(self, items, font_size=None, color=WHITE, buff=0.5):
        """Create a bulleted list from a list of text items"""
        if font_size is None:
            font_size = TEXT_FONT_SIZE
        
        bulleted_list = BulletedList(
            *items,
            font_size=font_size,
            buff=buff,
            color=color,
            stroke_width=0.3
        )
        
        return bulleted_list
    
    def create_equation(self, equation_text, font_size=None, color=WHITE):
        """Create a mathematical equation text"""
        if font_size is None:
            font_size = TEXT_FONT_SIZE
            
        return MathTex(equation_text, font_size=font_size, color=color)
    
    def create_constraint_table(self, scale=1.0):
        """Create a table of constraints with their intercepts"""
        
        # Prepare data for the table
        data = []
        for constraint in CONSTRAINTS:
            x_intercept = str(constraint["x_intercept"]) if constraint["x_intercept"] is not None else "0"
            y_intercept = str(constraint["y_intercept"]) if constraint["y_intercept"] is not None else "0"
            
            row = [
                Text(constraint["name"], color=WHITE, stroke_width=0.5),
                MathTex(constraint["equation"], color=WHITE),
                Tex(x_intercept, color=WHITE, stroke_width=0.3),
                Tex(y_intercept, color=WHITE, stroke_width=0.3)
            ]
            data.append(row)
            
        # Create the table
        table = Table(
            table=data,
            col_labels=[
                MathTex("\\text{Lines}", color=WHITE),
                MathTex("\\text{Constraint}", color=WHITE),
                MathTex("\\text{Intercept } x_1", color=WHITE),
                MathTex("\\text{Intercept } x_2", color=WHITE)
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
            v_buff=0.6,
            h_buff=1.2,
            element_to_mobject=lambda element: element 
        ).scale(scale)
        
        return table
    
    def highlight_cell(self, table, row=None, col=None, color=RED, buff=0.1, stroke_width=3):
        """Highlight a specific cell, row, or column in a table"""
        if row is not None and col is not None:
            # Highlight specific cell
            target = table.get_entries((row, col))
        elif row is not None:
            # Highlight entire row
            target = table.get_rows()[row]
        elif col is not None:
            # Highlight entire column
            target = table.get_columns()[col]
        else:
            return None
            
        highlight = SurroundingRectangle(
            target,
            color=color,
            buff=buff,
            stroke_width=stroke_width
        )
        
        return highlight