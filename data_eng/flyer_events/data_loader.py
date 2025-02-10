import pandas as pd
import os
from .logger import setup_logger

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.logger = setup_logger("DataLoader")
        self.df = None

    def load_data(self):
        """
        Loads data using Pandas.
        """
        if not os.path.exists(self.file_path):
            self.logger.error("File not found.")
            return

        self.logger.info(f"Loading data from {self.file_path}")
        self.df = pd.read_csv(self.file_path,
                              dtype={'user_id': 'string', 'event':'string'},
                              parse_dates=['timestamp'])
        self.df['flyer_id'] = pd.to_numeric(self.df['flyer_id'], errors='coerce')
        self.df['merchant_id'] = pd.to_numeric(self.df['merchant_id'], errors='coerce')
        self.df = self.df.dropna(subset=['timestamp'])
        self.logger.info("Data loaded successfully.")
        return self.df
