from manim import *

class addons:
    def create_text_animation(self, point_or_mobject, rect_width, textstring, origin=ORIGIN, next_to=DOWN, text_color=BLACK, font_size=12, background_color=WHITE, background_opacity=1):
        text = Text(textstring, color=text_color, font_size=font_size)
        # Create background
        rect_height = text.height + 0.2  # Small padding
        rectangle = RoundedRectangle(width=rect_width, height=rect_height,
                                     corner_radius=0.1, color=background_color, fill_opacity=background_opacity)
        rectangle.move_to(origin)
        # Position the text to the right edge of the rectangle initially
        text.move_to(rectangle.get_right() + text.width / 2 * RIGHT)
        self.play(GrowFromPoint(rectangle, ORIGIN), text.animate.move_to(rectangle.get_left() +
              text.width / 2 * RIGHT).set_run_time(0.1))
        gr = VGroup(rectangle, text)
        self.play(Indicate(gr))
        # gr.shift(-gr.get_corner(UL)) # update anchor to Upper left corner
        # Move the group to the specified position or next to the mobject
        if isinstance(point_or_mobject, Mobject):
            move_to_position = gr.animate.next_to(
                point_or_mobject, next_to).set_run_time(0.1)
        else:
            move_to_position = gr.animate.move_to(
                point_or_mobject-gr.get_corner(UL)).set_run_time(0.1)
        self.play(move_to_position)
        return gr
