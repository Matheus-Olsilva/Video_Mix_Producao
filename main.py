from manim import *
from constants import *
import scenes

class VideoCompletoMixProducao_ingles(Scene):
    """Main scene that combines all sub-scenes sequentially"""
    
    def construct(self):
        # Setup the environment
        self.camera.background_color = BACKGROUND_COLOR
        config.frame_width = FRAME_WIDTH
        config.frame_height = FRAME_HEIGHT
        
        # Instanciar todas as cenas uma vez
        intro_scene = scenes.IntroScene()
        intro_scene.setup()
        problem_scene = scenes.ProblemDefinitionScene()
        problem_scene.setup()
        model_scene = scenes.OptimizationModelScene()
        model_scene.setup()
        graphical_scene = scenes.GraphicalSolutionScene()
        graphical_scene.setup()
        vertices_scene = scenes.VerticesCalculationScene()
        vertices_scene.setup()
        conclusion_scene = scenes.ConclusionScene()
        conclusion_scene.setup()
        
        # ========== PART 1: Introduction and Problem Definition ==========
        # Copy animations from IntroScene
        # self.execute_animation_method(intro_scene, "show_intro_logo")
        # self.wait(2)
        self.execute_animation_method(intro_scene, "show_company_intro")
        
        # Copy animations from ProblemDefinitionScene
        self.execute_animation_method(problem_scene, "show_minimum_requirements")
        self.execute_animation_method(problem_scene, "show_additional_info")
        self.execute_animation_method(problem_scene, "show_contribution_margin_table")
        self.execute_animation_method(problem_scene, "show_objective_function_example")
        self.execute_animation_method(problem_scene, "show_resource_constraints_table")
        
        # Copy animations from OptimizationModelScene
        self.execute_animation_method(model_scene, "show_complete_model")
        self.execute_animation_method(model_scene, "prepare_for_graphical_method")
        self.execute_animation_method(model_scene, "show_constraint_calculations")
        self.execute_animation_method(model_scene, "show_demand_constraint_calculations")
        self.execute_animation_method(model_scene, "show_constraint_summary_table")
        
        # Copy animations from GraphicalSolutionScene
        self.execute_animation_method(graphical_scene, "show_graphical_solution")
        
        
        # ========== PART 2: Vertex Calculation ==========
        #Copy animations from VerticesCalculationScene
        self.execute_animation_method(vertices_scene, "introduce_fundamental_theorem")
        self.execute_animation_method(vertices_scene, "calculate_vertex_320_450")
        self.execute_animation_method(vertices_scene, "calculate_vertex_1457_450")
        self.execute_animation_method(vertices_scene, "calculate_vertex_1250_812")
        self.execute_animation_method(vertices_scene, "calculate_vertex_320_1277")
        self.execute_animation_method(vertices_scene, "show_optimal_solution_table")
        
        # Conclusion
        self.execute_animation_method(conclusion_scene, "show_final_solution")
    
    def execute_animation_method(self, scene_instance, method_name):
        """Execute a method from a scene and copy its animations to the main scene"""
        # Collect animations by monkey-patching play and wait methods
        collected_animations = []
        
        # Save original methods
        original_play = scene_instance.play
        original_wait = scene_instance.wait
        
        # If the scene has the play_with_factor method, save it too
        has_play_with_factor = hasattr(scene_instance, "play_with_factor")
        if has_play_with_factor:
            original_play_with_factor = scene_instance.play_with_factor
        
        # If the scene has the wait_with_factor method, save it too
        has_wait_with_factor = hasattr(scene_instance, "wait_with_factor")
        if has_wait_with_factor:
            original_wait_with_factor = scene_instance.wait_with_factor
        
        # Define replacement methods that capture animations
        def capture_play(*args, **kwargs):
            collected_animations.append(("play", args, kwargs))
        
        def capture_wait(duration=1, **kwargs):
            collected_animations.append(("wait", duration, kwargs))
        
        def capture_play_with_factor(*args, **kwargs):
            # Adjust run_time if present
            if 'run_time' in kwargs:
                kwargs['run_time'] *= TIMING_FACTOR
            collected_animations.append(("play", args, kwargs))
        
        def capture_wait_with_factor(duration=1, **kwargs):
            collected_animations.append(("wait", duration * TIMING_FACTOR, kwargs))
        
        # Replace methods with our capturing versions
        scene_instance.play = capture_play
        scene_instance.wait = capture_wait
        if has_play_with_factor:
            scene_instance.play_with_factor = capture_play_with_factor
        if has_wait_with_factor:
            scene_instance.wait_with_factor = capture_wait_with_factor
        
        # Execute the method
        method = getattr(scene_instance, method_name)
        method()
        
        # Restore original methods
        scene_instance.play = original_play
        scene_instance.wait = original_wait
        if has_play_with_factor:
            scene_instance.play_with_factor = original_play_with_factor
        if has_wait_with_factor:
            scene_instance.wait_with_factor = original_wait_with_factor
        
        # Execute the collected animations in the main scene
        for anim_type, *anim_args in collected_animations:
            if anim_type == "play":
                args, kwargs = anim_args
                self.play(*args, **kwargs)
            elif anim_type == "wait":
                duration, kwargs = anim_args
                self.wait(duration, **kwargs)

if __name__ == "__main__":
    """
    To render the animation, run:
    manim -pql main.py MixProducaoCompleto
    """
    # This allows running the file directly with Python
    # If no command-line arguments are specified, it will run with default config
    pass