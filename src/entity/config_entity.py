from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    data_url: str

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    pipeline_path: Path
    labels_path: Path

@dataclass
class DataSplittingConfig:
    root_dir: Path
    data_path: Path

@dataclass
class DataTokenizationConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    pickle_path: Path
    tokenizer_data_path: Path

@dataclass
class ModelTrainingConfig:
    root_dir: Path
    x_train_data_path: Path
    y_train_data_path: Path
    x_test_data_path: Path
    y_test_data_path: Path
    maxlen_path: Path

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    model_path: Path
    model_history_path: Path
    x_test_data_path: Path
    y_test_data_path: Path
