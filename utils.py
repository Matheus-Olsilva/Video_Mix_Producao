from manim import *
from constants import *

def create_axes(x_range=[0, 4000, 1000], y_range=[0, 3500, 1000], 
                x_length=12, y_length=6, scale_factor=1.0):
    """Create and return coordinate axes with given parameters"""
    axes = Axes(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        axis_config={"include_numbers": True, "font_size": 24},
    ).add_coordinates()
    
    if scale_factor != 1.0:
        axes.scale(scale_factor)
        
    return axes

def create_constraint_lines(axes, constraints=None):
    """Create lines for constraints on the given axes"""
    if constraints is None:
        constraints = CONSTRAINTS
        
    lines = []
    for constraint in constraints:
        if constraint["x_intercept"] is not None and constraint["y_intercept"] is not None:
            # Standard line with two intercepts
            line = Line(
                axes.coords_to_point(constraint["x_intercept"], 0),
                axes.coords_to_point(0, constraint["y_intercept"]),
                color=constraint["color"]
            )
        elif constraint["x_intercept"] is not None:
            # Vertical line (x = constant)
            line = Line(
                axes.coords_to_point(constraint["x_intercept"], 0),
                axes.coords_to_point(constraint["x_intercept"], axes.y_range[1]),
                color=constraint["color"]
            )
        elif constraint["y_intercept"] is not None:
            # Horizontal line (y = constant)
            line = Line(
                axes.coords_to_point(0, constraint["y_intercept"]),
                axes.coords_to_point(axes.x_range[1], constraint["y_intercept"]),
                color=constraint["color"]
            )
            
        lines.append(line)
        
    return VGroup(*lines)

def create_feasible_region(axes, vertices=None):
    """Create a polygon representing the feasible region"""
    if vertices is None:
        vertices = VERTICES
        
    # Convert vertex coordinates to points on the axes
    points = [axes.coords_to_point(x, y) for x, y in vertices]
    
    # Create the polygon
    feasible_region = Polygon(
        *points,
        fill_color=BLUE,
        fill_opacity=0.3,
        stroke_opacity=0
    )
    
    return feasible_region

def create_constraint_boundary_lines(axes, vertices=None):
    """Create lines representing the boundary of the feasible region"""
    if vertices is None:
        vertices = VERTICES
        
    # Create lines connecting the vertices in order
    lines = []
    points = [axes.coords_to_point(x, y) for x, y in vertices]
    
    # Colors for each segment
    colors = [RED, GREEN, PURPLE, ORANGE]  # R1, R2, R5, R6
    
    # Connect vertices in order (including last to first)
    for i in range(len(points)):
        line = Line(
            points[i],
            points[(i+1) % len(points)],
            color=colors[i]
        )
        lines.append(line)
        
    return VGroup(*lines)

def calculate_objective_value(x1, x2):
    """Calculate the value of the objective function for given x1, x2"""
    return OBJECTIVE_FUNCTION["yogurt_coef"] * x1 + OBJECTIVE_FUNCTION["cheese_coef"] * x2

def create_arrows_for_region(axes, arrow_groups=None):
    """Create arrows indicating the feasible direction for constraints"""
    if arrow_groups is None:
        arrow_groups = ARROW_GROUPS
        
    arrow_mobjects = {}
    
    for group_name, arrow_coords in arrow_groups.items():
        arrows = []
        for start, end in arrow_coords:
            arrow = Arrow(
                axes.coords_to_point(start[0], start[1]),
                axes.coords_to_point(end[0], end[1]),
                color=ARROW_COLOR,
                buff=0,
                stroke_width=6,
                tip_length=0.25,
                max_stroke_width_to_length_ratio=6,
                max_tip_length_to_length_ratio=0.35
            )
            arrows.append(arrow)
            
        arrow_mobjects[group_name] = VGroup(*arrows)
        
    return arrow_mobjects