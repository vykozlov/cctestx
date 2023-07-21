"""Subpackage to build training and inference pipelines
"""

import logging
import cctestx.config as cfg
import cctestx.dataset as dtst

logger = logging.getLogger(__name__)
logger.setLevel(cfg.log_level)

# create model
# = HAVE TO MODIFY FOR YOUR NEEDS =
def create_model(**kwargs):
    """Main/public method to create AI model
    """
    # define model parameters
    
    # build model based on the deep learning framework
    
    return model

# predict
# = HAVE TO MODIFY FOR YOUR NEEDS =
def predict(**kwargs):
    """Main/public method to perform prediction
    """
    # if necessary, preprocess data
    
    # choose AI model, load weights
    
    # return results of prediction
    predict_result = {'result': 'not implemented'}
    logger.debug(f"[predict()]: {predict_result}")

    return predict_result

# train
# = HAVE TO MODIFY FOR YOUR NEEDS =
def train(**kwargs):
    """Main/public method to perform training
    """
    # prepare the dataset, e.g.
    # dtst.mkdata()
    
    # create model, e.g.
    # create_model()
    
    # train model
    # describe training steps

    # return training results
    train_result = {'result': 'not implemented'}
    logger.debug(f"[train()]: {train_result}")
    
    return train_result
