import InputHelperR as IPR
import pandas as pd
import os
import numpy as np
from warnings import filterwarnings
filterwarnings('ignore')
def getBoolValue(Value):
    Value = str(Value)
    if Value.upper() == 'FALSE':
        return False
    elif Value.upper() == 'TRUE':
        return True


def ReadStaticDataFile(InputDirPath,file):
    DF = pd.DataFrame()
    DF["Timestamp"] = pd.to_datetime({'year': [1999],'month': [1],'day': [1]})
    MI =pd.read_csv(os.path.join(InputDirPath,file), header = None, skip_blank_lines= True, names = ['Property','PropertyValue','PropertyType'])  
    modelInput = MI.set_index('Property').to_dict()['PropertyValue']
    #print(modelInput)    
        #for timeseries separate from here -pass model input - as 1 timestamp
    for entry in IPR.InputMapping:
        DataType = entry[1]
        if DataType == 'float':
            try:
                DF[entry[2]] = float(modelInput[entry[0]])
            except:
                DF[entry[2]] = np.nan
        elif DataType == 'str':
            try:
                DF[entry[2]] = str(modelInput[entry[0]])
            except:
                 DF[entry[2]] = np.nan
        elif DataType == 'int':
            try:
                DF[entry[2]] = int(modelInput[entry[0]])
            except:
                DF[entry[2]] = np.nan
        elif DataType == 'bool':
            try:
                DF[entry[2]] = getBoolValue(modelInput[entry[0]])
            except:
                DF[entry[2]] = np.nan      
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
                    try:
                        DF[entry[2].format(loadstep=i,cylinderno=j)] = float(modelInput[entry[0].format(loadstep=i,cylinderno=j)])
                    except:
                        continue
                elif DataType == 'str':
                    DF[entry[2].format(loadstep=i,cylinderno=j)] = str(modelInput[entry[0].format(loadstep=i,cylinderno=j)])
                elif DataType == 'int':
                    try:
                        DF[entry[2].format(loadstep=i,cylinderno=j)] = int(modelInput[entry[0].format(loadstep=i,cylinderno=j)]) 
                    except:
                        continue
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
                try:
                    DF[entry[2].format(stageno=i)] = float(modelInput[entry[0].format(stageno=i)])
                except:
                    continue
            elif DataType == 'str':
                DF[entry[2].format(stageno=i)] = str(modelInput[entry[0].format(stageno=i)])
            elif DataType == 'int':
                try:
                    DF[entry[2].format(stageno=i)] = int(modelInput[entry[0].format(stageno=i)])
                except:
                    continue
            elif DataType == 'bool':
                DF[entry[2].format(stageno=i)] = getBoolValue(modelInput[entry[0].format(stageno=i)])

        for entry in IPR.GasRecipStage:
            DataType = entry[1]
            if DataType == 'float':
                try:
                    DF[entry[2].format(stageno=i)] = float(modelInput[entry[0].format(stageno=i)])
                except:
                    DF[entry[2].format(stageno=i)] = np.nan
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
                try:
                    DF[entry[2].format(cylinderno=i)] = float(modelInput[entry[0].format(cylinderno=i)])
                except:
                    continue
            elif DataType == 'str':
                DF[entry[2].format(cylinderno=i)] = str(modelInput[entry[0].format(cylinderno=i)])
            elif DataType == 'int':
                try:
                    DF[entry[2].format(cylinderno=i)] = int(modelInput[entry[0].format(cylinderno=i)])
                except:
                    continue
            elif DataType == 'bool':
                DF[entry[2].format(cylinderno=i)] = getBoolValue(modelInput[entry[0].format(cylinderno=i)])

    for i in range(1,DF.OC_NumberOfStages[0]+1):
        for entry in IPR.SideStream :
            DataType = entry[1]
            if DataType == 'float':
                try:
                    DF[entry[2].format(stageno=i)] = float(modelInput[entry[0].format(stageno=i)])
                except:
                    continue
            elif DataType == 'str':
                try:
                    DF[entry[2].format(stageno=i)] = str(modelInput[entry[0].format(stageno=i)])
                except:
                    continue
            elif DataType == 'int':
                try:
                    DF[entry[2].format(stageno=i)] = int(modelInput[entry[0].format(stageno=i)])
                except:
                    continue
            elif DataType == 'bool':
                DF[entry[2].format(stageno=i)] = getBoolValue(modelInput[entry[0].format(stageno=i)])
    return DF

# # Input directory containing CSV files
# input_dir = "C:/_Projects/ShellREM/RCOMS/Static_Files/Static"
# InputDirPath = os.path.abspath(input_dir)
# files=os.listdir(input_dir)

# # Output directory for Excel files
# output_dir = "C:/_Projects/ShellREM/RCOMS/Static_Files/Output_Parsing"

 

# # #process_script2(master_df1,input_csv)
# files = os.listdir(input_dir)
# for file in files:
#     df = ReadStaticDataFile(InputDirPath,file)
#     output_excel = os.path.join(output_dir, f"{os.path.splitext(file)[0]}_Output2.xlsx")
#     # Create an Excel writer object
#     excel_writer = pd.ExcelWriter(output_excel, engine='xlsxwriter')
#     df.to_excel(excel_writer, sheet_name='Parsed_File', index=False)
#     excel_writer.save()
