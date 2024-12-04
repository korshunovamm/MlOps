FROM ubuntu:22.04

# Обновление и установка необходимых пакетов
RUN apt update && apt install -y \
    g++ \
    python3 \
    python3-pip \
    python3.10-venv \
    libgtest-dev \
    cmake \
    git

# Установка Python-зависимостей
RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install pybind11
RUN pip install build
RUN pip install numpy
RUN pip install scipy

RUN pip install torch==2.0.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

# Установка pytorch-lightning без лишних зависимостей
RUN pip install --no-cache-dir pytorch-lightning[base] 
RUN pip install hydra-core
RUN pip install tensorboard

WORKDIR /usr/src/app
COPY ./ /usr/src/app

# Сборка C++ Python-биндингов
WORKDIR /usr/src/app/chebyshevDistance
RUN python3 setup.py build
RUN python3 setup.py install

# Возврат в основную директорию проекта
WORKDIR /usr/src/app

ENTRYPOINT ["python3", "train.py"]

