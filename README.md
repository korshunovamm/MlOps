# PyTorchLightning

## DVC

Добавим dvc для контроля версий модели, данных и экспериментов

```bash
dvc init
dvc add data/CIFAR10
git commit -m "Добавлены данные CIFAR10 в DVC"
```

### Настройка удалённого хранилища (.dvc/config)
```bash
dvc remote add -d storage <REMOTE_URL> 
dvc push
```

### Воспроизведение (из настроек dvc.yaml)

```bash
dvc repro
```