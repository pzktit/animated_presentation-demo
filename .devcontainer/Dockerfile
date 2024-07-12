FROM mcr.microsoft.com/devcontainers/python

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



USER vscode:vscode
WORKDIR /home/vscode
ENV PATH="/home/vscode/.local/bin:${PATH}"        
RUN pip install --upgrade pip && pip install ipykernel manim-slides[magic]
# RUN pip install --user pipx

