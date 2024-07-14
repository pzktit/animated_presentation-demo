from manim_slides import Slide
from manim import *
from lib.addons import addons

class Points(Slide,addons):
    def slide_point(self, text, position=np.array([-6.5, 3.5, 0]), width=config.frame_width * 0.4, font="DejaVu Sans", font_size=24):
        return self.next_list_element(position, width, text, background_color=GREEN_B, background_opacity=0.8,font=font, font_size=font_size)
    def show_points(self, texts, initpos, callback=None):
        pos = initpos
        for text in texts:
            pos = self.slide_point(text,pos)
            if callback is not None:
                callback()

    def construct(self):
        self.font=f"IBM Plex Sans"
        self.head_font_size=36
        plane = self.add(NumberPlane())
        self.item_font_size=24
        slide_texts = ["To sem ja, pani Havrankowa", "Good morning", "Good morning"]
        initpos = np.array([-6.5, 3.5, 0])
        header = self.items_header(initpos, "Bardzo ważne treści",font=self.font, font_size=self.head_font_size)
        self.next_slide()        
        self.show_points(slide_texts, header.get_corner(DL)+0.5*RIGHT+0.2*DOWN, callback=self.next_slide)
        self.wait()
