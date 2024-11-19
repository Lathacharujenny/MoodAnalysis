from src.logger import logging 
from src.exception import CustomException
from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.pipeline.stage_02_data_cleaning import DataCleaningPipeline
from src.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.pipeline.stage_04_data_splitting import DataSplittingPipeline
from src.pipeline.stage_05_data_tokenization import DataTokenizationPipeline
from src.pipeline.stage_06_model_training import ModelTrainingPipeline
from src.pipeline.stage_07_model_evaluation import ModelEvaluationPipeline
import sys



# STAGE_NAME = "Data Ingestion Stage"
# try:
#     logging.info(f'>>>>>>>>>> stage {STAGE_NAME} started >>>>>>>>>>>>')
#     data_ingestion = DataIngestionPipeline()
#     data_ingestion.main()
#     logging.info(f'>>>>>>>>>> stage {STAGE_NAME} ended >>>>>>>>>>>>')
# except Exception as e:
#     logging.error(f'Error occured:{e}')
#     raise CustomException(e,sys)


# STAGE_NAME = "Data Cleaning Stage"
# try:
#     logging.info(f'>>>>>>>>>> stage {STAGE_NAME} started >>>>>>>>>>>>')
#     data_ingestion = DataCleaningPipeline()
#     data_ingestion.main()
#     logging.info(f'>>>>>>>>>> stage {STAGE_NAME} ended >>>>>>>>>>>>')
# except Exception as e:
#     logging.error(f'Error occured:{e}')
#     raise CustomException(e,sys)
    
# STAGE_NAME = 'Data Transformation Stage'
# try:
#     logging.info(f'>>>>>>>>>>>> stage {STAGE_NAME} started >>>>>>>>>>>>>>>>')
#     data_transformation = DataTransformationPipeline()
#     data_transformation.main()
#     logging.info(f'>>>>>>>>>>>>>> stage {STAGE_NAME} ended >>>>>>>>>>>>>')
# except Exception as e:
#     logging.error(f'Error Occured: {e}')
#     raise CustomException(e,sys)

# STAGE_NAME = 'Data Splitting Stage'
# try:
#     logging.info(f'>>>>>>>>>>>>>> stage {STAGE_NAME} started')
#     data_splitting = DataSplittingPipeline()
#     data_splitting.main()
#     logging.info(f'>>>>>>>>>>>>> stage {STAGE_NAME} ended >>>>>>>>>>>>>>>')
# except Exception as e:
#     logging.error(f'Error Occured: {e}')
#     raise CustomException(e,sys)

# STAGE_NAME = "Data Tokenization Stage"
# try:
#     logging.info(f'>>>>>>>>>>>> stage {STAGE_NAME} started')
#     data_tokenization = DataTokenizationPipeline()
#     data_tokenization.main()
#     logging.info(f'>>>>>>>>>>>>>>> stage {STAGE_NAME} ended >>>>>>>>>>>>>>>')
# except Exception as e:
#     logging.error(f'Error Occured: {e}')
#     raise CustomException(e,sys)

# STAGE_NAME = "Model Training Stage"
# try:
#     logging.info(f'>>>>>>>>>>>> stage {STAGE_NAME} started')
#     model_training = ModelTrainingPipeline()
#     model_training.main()
#     logging.info(f'>>>>>>>>>>>> stage {STAGE_NAME} ended >>>>>>>>>>>>>>>>>>')
# except Exception as e:
#     logging.error(f'Error Occured: {e}')
#     raise CustomException(e,sys)

STAGE_NAME = "Model Evaluation Stage"
try:
    logging.info(f'>>>>>>>>>> stage {STAGE_NAME} started >>>>>>>>>>>>>>>')
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logging.info(f'>>>>>>>>>> stage {STAGE_NAME} ended')
except Exception as e:
    logging.error(f'Error Occured: {e}')
    raise CustomException(e,sys)