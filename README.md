# PyTorchLightning

## DVC

Добавим dvc для контроля версий модели, данных и экспериментов

```bash
dvc init
dvc add data/CIFAR10
git commit -m "Добавлены данные CIFAR10 в DVC"
```

### Настройка удалённого хранилища
```bash
dvc remote add -d storage <REMOTE_URL>
dvc push
```

### Воспроизведение (из настроек dvc.yaml)

```bash
avc repro
```

### Добавление логов
```
dvc add logs
git add logs.dvc
git commit -m "Добавлены логи тренировок в DVC"
dvc push
```