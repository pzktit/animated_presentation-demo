FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

RUN apt-get update -qq \
    && apt-get install --no-install-recommends -y \
        build-essential \
        gcc \
        cmake \
        libcairo2-dev \
        libffi-dev \
        libpango1.0-dev \
        ffmpeg \
        freeglut3-dev \
        pkg-config \
        make \
        wget \
        ghostscript \
        dvisvgm \
        texlive-latex-extra \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN mkdir /work && chown -R vscode:vscode /work
USER vscode:vscode
ENV PATH="/home/vscode/.local/bin:${PATH}"        

RUN pip install --upgrade pip && pip install ipykernel manim manim-slides
# RUN pip install --user pipx
# RUN pipx install --verbose "manim-slides[manim,magic]"

