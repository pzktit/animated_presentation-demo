from manim import *
from manim_slides import Slide

CONFIG = {
    "camera_config":{"background_image": "assets/images/background.png"}
} 

class SquareToCircle(Slide):
   def construct(self):
      # self.camera.background_image = 
      # self.camera.background_color = WHITE
      # self.camera.background_color = WHITE
      image = ImageMobject("assets/images/background.png")
      image.move_to(ORIGIN)
      image.scale_to_fit_height(self.camera.frame_height)
      image.scale_to_fit_width(self.camera.frame_width)
      grid = NumberPlane()
      self.play(FadeIn(image))
      self.play(FadeIn(grid))
      self.next_slide()
      square = Square()
      circle = Circle()
      circle.set_fill(PINK, opacity=0.5)
      self.play(Create(square))
      self.next_slide()
      self.play(Transform(square, circle))
      self.next_slide()
      learn_more_text = (
            VGroup(
                Text("Learn more about Manim Slides:"),
                Text("https://github.com/jeertmans/manim-slides", color=YELLOW),
            )
            .arrange(DOWN)
            .scale(0.75)
        )
      self.play(Transform(square, learn_more_text))
      self.next_slide()
      formulas = (
            VGroup(
                Tex(r"\LaTeX", font_size=144),
                Tex(r"\[ E = m c^2 \]", font_size=144,color=YELLOW)
            )
            .arrange(DOWN)
            .scale(0.75)
        )
      self.play(Transform(square,formulas))
      self.wait()
