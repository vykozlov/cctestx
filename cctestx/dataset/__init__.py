"""Subpackage to prepare the dataset
"""

import logging
from pathlib import Path
import cctestx.config as cfg

logger = logging.getLogger(__name__)
logger.setLevel(cfg.log_level)

# = HAVE TO MODIFY FOR YOUR NEEDS =
def mkdata(input_filepath, output_filepath):
    """ Main/public function to run data processing to turn raw data
        from (data/raw) into cleaned data ready to be analyzed.
    """

    logger.info('Making final data set from raw data')

    # EXAMPLE for finding various files
    project_dir = Path(__file__).resolve().parents[2]