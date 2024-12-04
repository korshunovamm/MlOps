import hydra
import pytorch_lightning as pl
from pytorch_lightning import Trainer
from pytorch_lightning.loggers import TensorBoardLogger
from lightning_modules.data_module import CIFAR10DataModule
from lightning_modules.model import CIFAR10Classifier
from omegaconf import DictConfig


@hydra.main(version_base="1.3", config_path="configs", config_name="config")
def main(cfg: DictConfig):
    pl.seed_everything(42)

    data_module = CIFAR10DataModule(cfg.data.data_dir, cfg.data.batch_size)
    
    model = CIFAR10Classifier(lr=cfg.model.lr)

    logger = TensorBoardLogger(
        save_dir=cfg.logger.save_dir,
        name=cfg.logger.logs_file
    )

    trainer = Trainer(logger=logger, **cfg.trainer)
    trainer.fit(model, datamodule=data_module)


if __name__ == "__main__":
    main()
