import Logger
import InputParserR as IP
import pandas as pd
from tqdm import tqdm
import os
import RCOMSModel as model
     
InputDir = "C:\_Temp_Python\____ShellREM\RCOM\__CurrentModel\Static_Files"

InputDirPath = os.path.abspath(InputDir)
files=os.listdir(InputDir)

logger = Logger.logger

for file in tqdm(files):  
    
    if file.endswith('.csv'):    
        print('CurrentFileName: ',file)
       
        if '_Static_' in file:
            DF = IP.ReadStaticDataFile(InputDirPath,file)
            logger.info("INFO_ Statis file was loaded into DF")
         
        #review code later until flag1
        elif '_Pi_Output' in file:
            #print('Identified Time Series Data File')
            AsIsFile = file.split('_Pi_Output')[0] + '.csv'
            #print('Corresponding Info File: ',AsIsFile) 
        else:
            print('Identified As Is Model File, this will be processed with the corressponding PI Output Time series file.')
            continue
    else:
        print('Incorrect File Provided: ',file)
        continue
    
    #flag1
    #if static - returns with results 
     
    RCOM = model.CheckRunStatusAndInitiateCalcs(DF) 
    
    
    