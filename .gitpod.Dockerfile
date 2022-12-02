FROM gitpod/workspace-full

RUN pyenv install 3.10.7 && \
    pyenv virtualenv 3.10.7 advent-of-code-2022 &&
