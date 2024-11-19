import os
import logging
from pathlib import Path


root_dir = Path(__file__).resolve().parents[1]
logging_str = '[%(asctime)s]: - %(levelname)s - %(module)s - %(lineno)d - %(message)s'
log_dir = 'logs'
log_file_path = os.path.join(root_dir/log_dir, 'running_logs.log')
os.makedirs(root_dir/log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_file_path)
    ]
)