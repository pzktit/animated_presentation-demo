from manim_slides import Slide
from manim import *
from addons.addons import addons

class Title(Slide,addons):
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
        self.next_slide(auto_next=True)

class Points(Slide,addons):
    def construct(self):
        plane = self.add(NumberPlane())
        # Get the canvas (frame) width in Manim units
        canvas_width = config.frame_width
        rect_width = canvas_width * 0.4
        start_point = np.array([-6.5, 3.5, 0])
        textstring = "Your Text Here"
        first_obj = self.create_text_animation(
            start_point, rect_width, "To sem ja, pani Havrankowa", background_color=GREEN_B, background_opacity=0.8)
        self.next_slide()
        second_obj = self.create_text_animation(
            first_obj, rect_width, "Good morning", background_color=GREEN_B, background_opacity=0.8)
        self.wait()
