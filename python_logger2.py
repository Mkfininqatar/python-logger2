import logging
import time
from datetime import datetime

class SpatialTemporalLogger:
    def __init__(self, project="QNV_HPC", node="HPC_NODE_01", log_path=None, golden_sync_enabled=True, level=logging.INFO):
        self.project = project
        self.node = node
        self.log_path = log_path
        self.golden_sync_enabled = golden_sync_enabled
        
        self.logger = logging.getLogger(project)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.setLevel(level)

    def log_state(self, state, metrics, correlation_id=""):
        log_msg = f"State: {state} | ID: {correlation_id} | Metrics: {metrics}"
        self.logger.info(log_msg)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)