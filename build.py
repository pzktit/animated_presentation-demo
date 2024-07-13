# run and then right-click index.html and open in LiveServer

import os
import subprocess

scenes_to_render = ["Title", "Points"]
scenes_for_conversion = ["Title", "Points"]

def main():
    # Get the name of the current script to use in commands
    script_name = os.path.basename(__file__)

    # Base command for rendering
    render_command_base = f"manim render -qh presentation.py"

    # Render each scene
    for scene in scenes_to_render:
        render_command = f"{render_command_base} {scene}"
        subprocess.run(render_command, shell=True, check=True)

    # Convert command with scenes for conversion
    convert_command = f"manim-slides convert --to html -c controls=True -c progress=True -c slide_number=True   {' '.join(scenes_for_conversion)} preview/index.html"
    print(convert_command)
    subprocess.run(convert_command, shell=True, check=True)


if __name__ == "__main__":
    main()
