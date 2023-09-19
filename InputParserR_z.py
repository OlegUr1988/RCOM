import Logger
import InputHelperR as IPR
import pandas as pd
import os 

def getBoolValue(Value):
    if Value.upper() == 'FALSE':
        return False
    elif Value.upper() == 'TRUE':
        return True
        
def ReadStaticDataFile(InputDirPath,file):
    
    DF = pd.DataFrame()
    DF["Timestamp"] = pd.to_datetime({'year': [1999],'month': [1],'day': [1]})
    #InputDirPath="C:\_Temp_Python\____ShellREM\RCOM\__CurrentModel\Static_Files"
    #file= 'DS_USA_AO1_GEP_K-S110_Static_20230620100000.csv'
    MI =pd.read_csv(os.path.join(InputDirPath,file), header = None, skip_blank_lines= True, names = ['Property','PropertyValue','PropertyType'])  
    modelInput = MI.set_index('Property').to_dict()['PropertyValue']
    #print(modelInput)    
        #for timeseries separate from here -pass model input - as 1 timestamp
    for entry in IPR.InputMapping:
        DataType = entry[1]
        if DataType == 'float':
            DF[entry[2]] = float(modelInput[entry[0]])
        elif DataType == 'str':
            DF[entry[2]] = str(modelInput[entry[0]])
        elif DataType == 'int':
            DF[entry[2]] = int(modelInput[entry[0]]) 
        elif DataType == 'bool':
            DF[entry[2]] = getBoolValue(modelInput[entry[0]])
            
     #For LimitsStage       
    for i in range(1,DF.OC_NumberOfStages[0]+1):
        for entry in IPR.LimitsStage:
            DataType = entry[1]
            if DataType == 'float':
                DF[entry[2].format(stageno=i)] = float(modelInput[entry[0].format(stageno=i)])
            elif DataType == 'str':
                DF[entry[2].format(stageno=i)] = str(modelInput[entry[0].format(stageno=i)])
            elif DataType == 'int':
                DF[entry[2].format(stageno=i)] = int(modelInput[entry[0].format(stageno=i)]) 
            elif DataType == 'bool':
                DF[entry[2].format(stageno=i)] = getBoolValue(modelInput[entry[0].format(stageno=i)])
    
    #For LoadStep_Cylinderno
    for i in range(1,DF.OC_NumberOfLoadSteps[0]+1):
        for j in range(1,DF.FM_NumberOfCylinders[0]+1):
           for entry in IPR.LoadStep_Cylinderno:
                DataType = entry[1]
                if DataType == 'float':
                    DF[entry[2].format(loadstep=i,cylinderno=j)] = float(modelInput[entry[0].format(loadstep=i,cylinderno=j)])
                elif DataType == 'str':
                    DF[entry[2].format(loadstep=i,cylinderno=j)] = str(modelInput[entry[0].format(loadstep=i,cylinderno=j)])
                elif DataType == 'int':
                    DF[entry[2].format(loadstep=i,cylinderno=j)] = int(modelInput[entry[0].format(loadstep=i,cylinderno=j)]) 
                elif DataType == 'bool':
                    DF[entry[2].format(loadstep=i,cylinderno=j)] = getBoolValue(modelInput[entry[0].format(loadstep=i,cylinderno=j)])
        
    # For Thorws
    for i in range(1,DF.FM_NumberOfThrows[0]+1):
        for entry in IPR.Throws:
            DataType = entry[1]
            if DataType == 'float':
                DF[entry[2].format(throwno=i)] = float(modelInput[entry[0].format(throwno=i)])
            elif DataType == 'str':
                DF[entry[2].format(throwno=i)] = str(modelInput[entry[0].format(throwno=i)])
            elif DataType == 'int':
                DF[entry[2].format(throwno=i)] = int(modelInput[entry[0].format(throwno=i)]) 
            elif DataType == 'bool':
                DF[entry[2].format(throwno=i)] = getBoolValue(modelInput[entry[0].format(throwno=i)])
    #For Stages
    for i in range(1,DF.OC_NumberOfStages[0]+1):
        for entry in IPR.Stages:
            DataType = entry[1]
            if DataType == 'float':
                DF[entry[2].format(stageno=i)] = float(modelInput[entry[0].format(stageno=i)])
            elif DataType == 'str':
                DF[entry[2].format(stageno=i)] = str(modelInput[entry[0].format(stageno=i)])
            elif DataType == 'int':
                DF[entry[2].format(stageno=i)] = int(modelInput[entry[0].format(stageno=i)]) 
            elif DataType == 'bool':
                DF[entry[2].format(stageno=i)] = getBoolValue(modelInput[entry[0].format(stageno=i)])
                
        for entry in IPR.GasRecipStage:
            DataType = entry[1]
            if DataType == 'float':
                DF[entry[2].format(stageno=i)] = float(modelInput[entry[0].format(stageno=i)])
            elif DataType == 'str':
                DF[entry[2].format(stageno=i)] = str(modelInput[entry[0].format(stageno=i)])
            elif DataType == 'int':
                DF[entry[2].format(stageno=i)] = int(modelInput[entry[0].format(stageno=i)]) 
            elif DataType == 'bool':
                DF[entry[2].format(stageno=i)] = getBoolValue(modelInput[entry[0].format(stageno=i)])
    
    for i in range(1,DF.FM_NumberOfCylinders[0]+1):            
        for entry in IPR.Cylinders :
            DataType = entry[1]
            if DataType == 'float':
                DF[entry[2].format(cylinderno=i)] = float(modelInput[entry[0].format(cylinderno=i)])
            elif DataType == 'str':
                DF[entry[2].format(cylinderno=i)] = str(modelInput[entry[0].format(cylinderno=i)])
            elif DataType == 'int':
                DF[entry[2].format(cylinderno=i)] = int(modelInput[entry[0].format(cylinderno=i)]) 
            elif DataType == 'bool':
                DF[entry[2].format(cylinderno=i)] = getBoolValue(modelInput[entry[0].format(cylinderno=i)])
    
    for i in range(2,DF.OC_NumberOfStages[0]+1):
        for entry in IPR.SideStream :
            DataType = entry[1]
            if DataType == 'float':
                DF[entry[2].format(stageno=i)] = float(modelInput[entry[0].format(stageno=i)])
            elif DataType == 'str':
                DF[entry[2].format(stageno=i)] = str(modelInput[entry[0].format(stageno=i)])
            elif DataType == 'int':
                DF[entry[2].format(stageno=i)] = int(modelInput[entry[0].format(stageno=i)]) 
            elif DataType == 'bool':
                DF[entry[2].format(stageno=i)] = getBoolValue(modelInput[entry[0].format(stageno=i)])
                
    
    return DF # 