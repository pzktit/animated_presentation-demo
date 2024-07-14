
from manim import *

class GenScene(Scene):
    def construct(self):
        text = Text("Sample Text", font="Avenir", color=BLUE).to_edge(UL)
        underline = Line(start=text.get_left(), end=text.get_right(), color=YELLOW).next_to(text, DOWN, buff=0.1)
        self.play(Write(text), Create(underline))
        
        dot = Dot().next_to(text, DOWN, buff=text.height)
        self.play(FadeIn(dot))
        
        smaller_text = Text("Smaller Text", font="Avenir", color=BLUE).scale(0.5)
        combo = VGroup(dot, smaller_text).arrange(RIGHT, aligned_edge=UP).next_to(text, DOWN, aligned_edge=LEFT)
        
        self.play(Transform(dot, combo))
