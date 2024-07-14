PRESENTATION := Title Points
DEVELOPED_SCENE := Points

# Directory paths
SRC_DIR := src/scenes
SLIDES_DIR := slides
# Rendering options
RENDER_OPTIONS := --CE --resolution 1920,1080 --frame_rate 30
# Conversion options
CONVERT_OPTIONS := -ccontrols=true

# List of source files and corresponding JSON files
SRC_FILES := $(foreach scene,$(PRESENTATION),$(SRC_DIR)/$(scene).py)
JSON_FILES := $(patsubst $(SRC_DIR)/%.py,$(SLIDES_DIR)/%.json,$(SRC_FILES))

# Target for unconditional build
.PHONY: all build clean

# Default target is 'all'
all: build link

# Rule to build all scenes
build: $(JSON_FILES)
	@echo "Building all scenes"

# Rule to selectively build developen scene
test: $(DEVELOPED_SCENE)
	@echo "Building $(DEVELOPED_SCENE)"

# Rule to link the built scenes
link: $(JSON_FILES)
	@echo "Linking scenes"
	@echo "Building presentation in preview/index.html for $(notdir $(basename $(JSON_FILES)))"
	@manim-slides convert $(CONVERT_OPTIONS) $(PRESENTATION) preview/index.html

# Rule to build selected scene
%: $(SRC_DIR)/%.py
	@echo "Py2Scene rule. Rendering $< to $@"
	@manim-slides render $(RENDER_OPTIONS) $< $@
	@echo "Py2Scene rule. Coverting to preview/$@.html"
	@manim-slides convert $(CONVERT_OPTIONS) $@ preview/$@.html

# Rule to build JSON file from Python source
$(SLIDES_DIR)/%.json: $(SRC_DIR)/%.py
	@echo "Rendering $< to $@"
	@manim-slides render $(RENDER_OPTIONS) $<

# Clean up generated files
clean:
	@echo "Cleaning up..."
	@rm -f $(JSON_FILES) $(SLIDES_DIR)/files/*/* preview/*_assets/* preview/*.html
	
# Rule for unconditional build
unconditional: clean all

# Rule to build individual scene by class name
%: $(SLIDES_DIR)/%.json

# Override default target for individual scene build
.DEFAULT_GOAL := all
