from manim import *

class TextAnimation(Scene):
    def construct(self):
        # Example usage of the new method
        self.create_text_animation(ORIGIN, RIGHT, 6, "Your Text Here")

    def create_text_animation(self, point_or_mobject, next_to, width, text, origin=ORIGIN):
        # Define the text
        text_mobject = Text(text, color=BLACK, font_size=48)

        # Define the rectangle dimensions based on the width
        rect_width = width
        rect_height = text_mobject.height + 0.2  # Small padding

        # Define the rounded rectangle with the specified width and height
        rectangle = RoundedRectangle(width=rect_width, height=rect_height, corner_radius=0.2, color=WHITE, fill_opacity=1)
        initial_rectangle = RoundedRectangle(width=0.2, height=rect_height, corner_radius=0.2, color=WHITE, fill_opacity=0)  # Initial rectangle with 0 opacity

        # Position the initial objects
        rectangle.move_to(origin)
        initial_rectangle.move_to(origin)
        text_mobject.move_to(rectangle.get_right() + text_mobject.width / 2 * RIGHT)

        # Create the animations
        wait_before_fade_in = Wait(1)  # Wait for 1 second
        fade_in_initial = FadeIn(initial_rectangle, run_time=1)
        grow_rect = Transform(initial_rectangle, rectangle, run_time=1)

        # Move text to the left edge of the rectangle
        move_text = text_mobject.animate.move_to(rectangle.get_left() + text_mobject.width / 2 * LEFT)

        # Move the rectangle to the specified position or next to the mobject
        if isinstance(point_or_mobject, Mobject):
            move_to_position = rectangle.animate.next_to(point_or_mobject, next_to).set_run_time(2)
            move_text_to_position = text_mobject.animate.next_to(point_or_mobject, next_to).set_run_time(2)
        else:
            move_to_position = rectangle.animate.move_to(point_or_mobject).set_run_time(2)
            move_text_to_position = text_mobject.animate.move_to(point_or_mobject).set_run_time(2)

        # Adjust anchor point to upper left corner of the rectangle
        rectangle.shift(-rectangle.get_corner(UL))

        # Play the animations
        self.play(wait_before_fade_in,
                  fade_in_initial,
                  grow_rect,
                  move_text,
                  move_to_position,
                  move_text_to_position)

# To preview or render the scene
if __name__ == "__main__":
    from manim import config

    # Set the output file name and location
    config.media_dir = "./media"
    config.output_file = "TextAnimation"
    config.quality = "low_quality"  # Use "high_quality" for a higher resolution

    # Render the scene
    scene = TextAnimation()
    scene.render()
