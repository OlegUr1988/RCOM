import Logger
from Enums import ErrorCodeClass 
from RecipCompressor import RecipCompressor

logger = Logger.logger
StatusCode = ErrorCodeClass.NoError.value

def CheckRunStatusAndInitiateCalcs(DF): 

    if DF["RS_RunStatusTag"][0] == 100:
        ## load all data in respective classes from DF and then start calculations
    #    try:
        RCOM = RecipCompressor()
        
        RCOM.Load(DF)    #set the input data to corresponding data structures
        logger.info("INFO: RCOM LoadInputData Successful.")
        
        #RCOM.Calculate()      #start the calculations
        
        # logger.info("RCOMs Calculation(s) Successful.")
        StatusCode = ErrorCodeClass.NoError.value
        # except:
        #     logger.info("CCOMs Calculation(s) Failed.")
        #     StatusCode = ErrorCodeClass.CalculationError.value
    else:
        logger.error("Train is in Stopped State. Calculation will be skipped.")
        StatusCode = ErrorCodeClass.Level1StateIsStop.value
    
    # DF["Status"][0] = StatusCode
    
    #collect output and insert in DF
    #Output = RCOM.FetchOutputData()
    
    # return DF
    return RCOM
