#!/usr/bin/env python3

import os
import subprocess
import sys
import shutil
import manim

# run and then right-click index.html and open in LiveServer
scenes_to_render = sys.argv[2:]
presentation_file = sys.argv[1]

def main():
    # Get the name of the current script to use in commands
    script_name = os.path.basename(__file__)

    # Base command for rendering
    render_command_base = f"manim render -qh {presentation_file}"

    # Render each scene
    for scene in scenes_to_render:
        render_command = f"{render_command_base} {scene}"
        subprocess.run(render_command, shell=True, check=True)
        presentation_file_name = os.path.splitext(presentation_file)[0]
        partial_movie_folder = manim.config.get_dir("partial_movie_dir", scene_name=f"{scene}", module_name=f"{presentation_file_name}")
        print(f"Partial movie folder: {partial_movie_folder}")
        texts_folder = manim.config.get_dir("text_dir",module_name=f"{presentation_file_name}")
        print(f"Texts folder: {texts_folder}")
        images_folder = manim.config.get_dir("images_dir",module_name=f"{presentation_file_name}")
        print(f"Images folder: {images_folder}")
        # Delete files in partial_movie_folder, texts_folder, and images_folder
        folders_to_delete = [partial_movie_folder, texts_folder, images_folder]
        for folder in folders_to_delete:
            if os.path.exists(folder):
                shutil.rmtree(folder)
                print(f"Deleted {folder}")

    # Convert command with scenes for conversion
    convert_command = f"manim-slides convert -ccontrols=true {' '.join(scenes_to_render)} preview/index.html"
    print(convert_command)
    subprocess.run(convert_command, shell=True, check=True)

if __name__ == "__main__":
    main()
