import math 
# import sys
# import os
# current = os.getcwd() 
# parent = os.path.dirname(current) 
# sys.path.append(parent) 
import Logger 
from Enums import OEM
import DefaultMapper as DM

class LoadStepCylinder: 
    def __init__(self): 
        self.logger = Logger.logger
        self.CylinderName = None
        
        self.IsHeadEndActive = False
        self.HeadEndClearance = 0
        self.HeadEndFixedPocketClearance = 0 # for old version
        self.HeadEndPocketPosition = None
        
        self.IsCrankEndActive = False
        self.CrankEndClearance = 0
        self.CrankEndFixedPocketClearance = 0 # for old version
        
        self.IsEffectiveClearanceSetDirectly = False # for old version
      
        # self.HeadEndFixedPocketClearance =                    # # ModelComponent(ModelComponentType.INPUT, string.Empty, string.Empty, "Cylinder Head End - Fixed Pocket Clearance")
        # self.HeadEndPocketPosition =                          # # ModelComponent(ModelComponentType.INPUT, string.Empty, string.Empty, "Cylinder Head End - Pocket Position")
        # self.CrankEndFixedPocketClearance =                   # # ModelComponent(ModelComponentType.INPUT, string.Empty, string.Empty, "Cylinder Crank End - Fixed Pocket Clearance")
         
    
    def Load(self, DF, loadStepIndex, cylinderIndex):   #/ Loads input values for LoadStepCylinder from DF
        try:
            self.CylinderName = DM.setStringValue(DF['LoadStep_{loadstep}_CL_{cylinderno}_Name'.format(cylinderno = cylinderIndex,loadstep = loadStepIndex,)][0], 0)   #DF.Read(RecipModelInputKeys.LoadStepCylinderName, string.Empty, loadStepIndex, cylinderIndex, ParsingType.STRING)
            self.IsHeadEndActive = DM.setBoolValue(DF['LoadStep_{loadstep}_CL_{cylinderno}_HE_IsActive'.format(cylinderno = cylinderIndex,loadstep = loadStepIndex,)][0], "False")   #DF.Read(RecipModelInputKeys.LoadStepCylinderHeadEndIsActive, "False", loadStepIndex, cylinderIndex, ParsingType.BOOLEAN)
            self.HeadEndClearance = DM.setFloatValue(DF['LoadStep_{loadstep}_CL_{cylinderno}_HE_TotalActivePocketClearance'.format(cylinderno = cylinderIndex,loadstep = loadStepIndex,)][0], 0)   #DF.Read(RecipModelInputKeys.LoadStepCylinderHeadEndEffectiveClearance, "0.0", loadStepIndex, cylinderIndex, ParsingType.DOUBLE)
            self.HeadEndPocketPosition = DM.setFloatValue(DF['LoadStep_{loadstep}_CL_{cylinderno}_HE_PocketPosition'.format(cylinderno = cylinderIndex,loadstep = loadStepIndex,)][0], 0)   #DF.Read(RecipModelInputKeys.LoadStepCylinderHeadEndPocketPosition, string.Empty, loadStepIndex, cylinderIndex, ParsingType.STRING)
            
            self.IsCrankEndActive = DM.setBoolValue(DF['LoadStep_{loadstep}_CL_{cylinderno}_CE_IsActive'.format(cylinderno = cylinderIndex,loadstep = loadStepIndex,)][0], "False")   #DF.Read(RecipModelInputKeys.LoadStepCylinderCrankEndIsActive, "False", loadStepIndex, cylinderIndex, ParsingType.BOOLEAN)
            self.CrankEndClearance = DM.setFloatValue(DF['LoadStep_{loadstep}_CL_{cylinderno}_CE_TotalActivePocketClearance'.format(cylinderno = cylinderIndex,loadstep = loadStepIndex,)][0], 0)   # DF.Read(RecipModelInputKeys.LoadStepCylinderCrankEndEffectiveClearance, "0.0", loadStepIndex, cylinderIndex, ParsingType.DOUBLE)
 
    
            self.logger.info("INFO_LoadStepCylinder_ Load done, loadStepIndex:" + str(loadStepIndex) + ", cylinderIndex:" +str(cylinderIndex))  
        except:
            self.logger.error("ERROR_LoadStepCylinder_ Load")  
    
 
        # Check if the Model is of old/new format. For new model templates, Effective Clearance key is not used at all.
        # It is fine to check the Head/Crank end to check if the key is present.
        # key = string.Format(RecipModelInputKeys.LoadStepCylinderHeadEndEffectiveClearance, loadStepIndex, cylinderIndex)
        # self.IsEffectiveClearanceSetDirectly = DF.CheckIfKeyExist(key)

        # self.HeadEndFixedPocketClearance.PiTagExpression = DF.Read(RecipModelInputKeys.LoadStepCylinderHeadEndFixedPocketClearance, string.Empty, loadStepIndex, cylinderIndex, ParsingType.STRING)
        # self.HeadEndPocketPosition.PiTagExpression = DF.Read(RecipModelInputKeys.LoadStepCylinderHeadEndPocketPosition, string.Empty, loadStepIndex, cylinderIndex, ParsingType.STRING)
        # self.CrankEndFixedPocketClearance.PiTagExpression = DF.Read(RecipModelInputKeys.LoadStepCylinderCrankEndFixedPocketClearance, string.Empty, loadStepIndex, cylinderIndex, ParsingType.STRING)
  
    # #/ Loads PI Tag input values for Operating Conditions of Recip from PI
    # def Load(self, piDataWrapper, uom):
    #     # Read Tag value from PI
    #     piDataWrapper.ReadValue(self.HeadEndFixedPocketClearance)
    #     piDataWrapper.ReadValue(self.HeadEndPocketPosition)
    #     piDataWrapper.ReadValue(self.CrankEndFixedPocketClearance)

    #     # Convert the Units values
    #     self._ConvertValuesFromInputUnitToCoreUnit(uom) 

    # #/ Converts the input values from Input Unit to Core Unit
    # def _ConvertValuesFromInputUnitToCoreUnit(self, uom):
    #     # HeadEndClearance is read as "%" value from model - it must be devided by 100 after reading to be used as a fraction value
    #     self.HeadEndClearance = self.HeadEndClearance / 100.0

    #     # CrankEndClearance is read as "%" value from model - it must be devided by 100 after reading to be used as a fraction value
    #     self.CrankEndClearance = self.CrankEndClearance / 100.0

    #     self.HeadEndFixedPocketClearance.ValueAsDouble = Rcoms2Helper.ConvertUnit(self.HeadEndFixedPocketClearance.ValueAsDouble, uom.Volume)
    #     self.HeadEndPocketPosition.ValueAsDouble = Rcoms2Helper.ConvertUnit(self.HeadEndPocketPosition.ValueAsDouble, uom.Length)
    #     self.CrankEndFixedPocketClearance.ValueAsDouble = Rcoms2Helper.ConvertUnit(self.CrankEndFixedPocketClearance.ValueAsDouble, uom.Volume)
