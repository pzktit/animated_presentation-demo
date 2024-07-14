from manim_slides import Slide
from manim import *
from lib.addons import addons


class Title(Slide,addons):
    def construct(self):
        self.font=f"Latin Modern Sans"
        self.font_size=48
        plane = self.add(NumberPlane())
        title = VGroup(
            Text("Animowane zagadnienia", t2c={"Animowane": BLUE},font=self.font,font_size=self.font_size),
            Text("prezentacji", t2w={"[-9:]": BOLD}, t2c={"[-10:]": YELLOW},font=self.font,font_size=self.font_size)
        ).arrange(DOWN)
        self.play(FadeIn(title))
        self.next_slide(auto_next=True)
        self.play(ShrinkToCenter(title), run_time=2)
