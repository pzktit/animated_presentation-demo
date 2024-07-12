# > manim-slides render slides.py Title Points
# or
# > manim-slides render slides.py Title
# > manim-slides render slides.py Points
# and then
# > manim-slides convert Tiltle Points preview/index.html
# and then right-click index.html and open in LiveServer

# you can also run the script directly
# > python slides.py
# but first modify the list of scenes to render and convert
# at the end of the script you will find the main function that renders and converts the scenes
scenes_to_render = ["Title"]
scenes_for_conversion = ["Title", "Points"]

from manim import *
from manim_slides import Slide

class Title(Slide):
    def construct(self):
        self.wait_time_between_slides = 0.1
        plane = self.add(NumberPlane())
        title = VGroup(
            Text("Animowane zagadnienia", t2c={"Animowane": BLUE}),
            Text("prezentacji", t2w={"[-9:]": BOLD}, t2c={"[-10:]": YELLOW}),
        ).arrange(DOWN)

        self.play(FadeIn(title))
        self.next_slide()
        self.play(ShrinkToCenter(title))

class Points(Slide):
    def construct(self):
        self.wait_time_between_slides = 0.1
        plane = self.add(NumberPlane())
        # Get the canvas (frame) width in Manim units
        canvas_width = config.frame_width
        rect_width = canvas_width * 0.4
        start_point = np.array([-6.5, 3.5, 0])
        textstring = "Your Text Here"
        first_obj = self.create_text_animation(start_point, rect_width, "To sem ja, pani Havrankowa",background_color=GREEN_B,background_opacity=0.8)
        self.next_slide()
        second_obj = self.create_text_animation(first_obj, rect_width, "Good morning",background_color=GREEN_B,background_opacity=0.8)
        self.wait()

    def create_text_animation(self, point_or_mobject, rect_width, textstring, origin=ORIGIN, next_to=DOWN, text_color=BLACK, font_size=12, background_color=WHITE, background_opacity=1):
        text = Text(textstring, color=text_color, font_size=font_size)
        # Create background
        rect_height = text.height + 0.2  # Small padding
        rectangle = RoundedRectangle(width=rect_width, height=rect_height, corner_radius=0.1, color=background_color, fill_opacity=background_opacity)
        rectangle.move_to(origin)
        # Position the text to the right edge of the rectangle initially
        text.move_to(rectangle.get_right() + text.width / 2 * RIGHT)
        # Play the animations
        self.play(Wait(1))
        self.play(GrowFromPoint(rectangle, ORIGIN))
        self.play(text.animate.move_to(rectangle.get_left() + text.width / 2 * RIGHT).set_run_time(5))                

        gr = VGroup(rectangle,text)
        # gr.shift(-gr.get_corner(UL)) # update anchor to Upper left corner
        if isinstance(point_or_mobject, Mobject):  # Move the group to the specified position or next to the mobject
            move_to_position = gr.animate.next_to(point_or_mobject, next_to).set_run_time(2)
        else:
            move_to_position = gr.animate.move_to(point_or_mobject-gr.get_corner(UL)).set_run_time(2)
        self.play( move_to_position )
        self.play(Indicate(gr))
        return gr   

class SlideNG(Slide):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wait_time_between_slides = 0.1
    def create_text_animation(self, point_or_mobject, rect_width, textstring, origin=ORIGIN, next_to=DOWN, text_color=BLACK, font_size=12, background_color=WHITE, background_opacity=1):
        text = Text(textstring, color=text_color, font_size=font_size)
        # Create background
        rect_height = text.height + 0.2  # Small padding
        rectangle = RoundedRectangle(width=rect_width, height=rect_height, corner_radius=0.1, color=background_color, fill_opacity=background_opacity)
        rectangle.move_to(origin)
        # Position the text to the right edge of the rectangle initially
        text.move_to(rectangle.get_right() + text.width / 2 * RIGHT)
        # Play the animations
        self.play(Wait(1))
        self.play(GrowFromPoint(rectangle, ORIGIN))
        self.play(text.animate.move_to(rectangle.get_left() + text.width / 2 * RIGHT).set_run_time(5))                

        gr = VGroup(rectangle,text)
        # gr.shift(-gr.get_corner(UL)) # update anchor to Upper left corner
        if isinstance(point_or_mobject, Mobject):  # Move the group to the specified position or next to the mobject
            move_to_position = gr.animate.next_to(point_or_mobject, next_to).set_run_time(2)
        else:
            move_to_position = gr.animate.move_to(point_or_mobject-gr.get_corner(UL)).set_run_time(2)
        self.play( move_to_position )
        self.play(Indicate(gr))
        return gr   
  
class PointsNG(SlideNG):
    def construct(self):
        plane = self.add(NumberPlane())
        # Get the canvas (frame) width in Manim units
        canvas_width = config.frame_width
        rect_width = canvas_width * 0.4
        start_point = np.array([-6.5, 3.5, 0])
        textstring = "Your Text Here"
        first_obj = self.create_text_animation(start_point, rect_width, "To sem ja, pani Havrankowa",background_color=GREEN_B,background_opacity=0.8)
        self.next_slide()
        second_obj = self.create_text_animation(first_obj, rect_width, "Good morning",background_color=GREEN_B,background_opacity=0.8)
        self.wait()

import os
import subprocess

def main():
    # Get the name of the current script to use in commands
    script_name = os.path.basename(__file__)
    
    # Base command for rendering
    render_command_base = f"manim-slides render {script_name}"
    
    # Render each scene
    for scene in scenes_to_render:
        render_command = f"{render_command_base} {scene}"
        subprocess.run(render_command, shell=True, check=True)
    
    # Convert command with scenes for conversion
    convert_command = f"manim-slides convert {' '.join(scenes_for_conversion)} preview/index.html"
    print(convert_command)
    subprocess.run(convert_command, shell=True, check=True)

if __name__ == "__main__":
    main()