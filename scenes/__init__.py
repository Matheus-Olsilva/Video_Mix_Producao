# Import all scene classes for easy access
from scenes.base_scene import BaseScene
from scenes.intro_scene import IntroScene
from scenes.problem_definition import ProblemDefinitionScene
from scenes.optimization_model import OptimizationModelScene
from scenes.graphical_solution import GraphicalSolutionScene
from scenes.vertices_calculation import VerticesCalculationScene
from scenes.conclusion_scene import ConclusionScene

# Export all scenes
__all__ = [
    'BaseScene',
    'IntroScene',
    'ProblemDefinitionScene',
    'OptimizationModelScene',
    'GraphicalSolutionScene',
    'VerticesCalculationScene',
    'ConclusionScene'
]