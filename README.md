# Chebyshev Distance
Рассчет расстояния Чебышева между двумя веторами с использованием python bindings, сравнение работой scipy.spatial.distance.chebyshev.

Создать образ и запустить в интерактивном режиме:
```bash
docker build -t trace .
docker run --rm -it trace /bin/bash
```

Собрать проект:
```bash
make ChebyshevDistance
python3 -m build
pip3 install dist/*.whl
```

Сравнить время работы алгоритма на C++ с pybinding и библиотченого scipy:
```bash
python3 perf.py
```

