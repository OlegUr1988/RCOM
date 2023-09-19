import math
# import sys
# import os
# current = os.getcwd() 
# parent = os.path.dirname(current) 
# sys.path.append(parent)
import Logger 
from Enums import OEM,  RodLoadCalculationMethod,  FlowMeterLocation  
from Model.BaseCondition import BaseCondition 

    
class OperatingConditions:    
    def __init__(self):
        self.logger = Logger.logger
        
        self.OEM = 0
        self.RodLoadCalcMethod = 0
        self.NoOfStages = 0
        self.NoOfLoadSteps = 0
        self.BaseCondition = None
        
        self.AtmosphericPressure = None
        self.AtmosphericPressureInAbsoluteUnit = None
        
        self.OperatingSpeed = None
        self.OperatingLoadStep = None 
        self.IsDualService = False
        self.Service2BrakePower = None
        self.Service2Torque = None
        
        self.FlowTuneFactor = 0
        self.FlowMeterLocation = 0
        self.FlowRateOfPotentialRecycleOrSideStreamOut = 0 
 
    def Load(self, DF):
        try: 
            self.OEM = OEM(DF["OC_OEM"][0])
            self.RodLoadCalcMethod = RodLoadCalculationMethod(DF["OC_RodLoadCalculationMethod"][0])
            self.NoOfStages = DF["OC_NumberOfStages"][0]
            self.NoOfLoadSteps = DF["OC_NumberOfLoadSteps"][0]
            self.BaseCondition = BaseCondition(DF["GN_ATM_T"][0] , DF["GN_ATM_P"][0])
            
            self.AtmosphericPressure = DF["GN_ATM_P"][0]            # new ModelComponent(ModelComponentType.Input, RecipModelInputKeys.Service2Torque, GeneralLabel.Percentage, "Service2 Torque");
            
            # To use then as initial data
            self.AtmosphericPressureInAbsoluteUnit =    DF["GN_ATM_P"][0]             # new ModelComponent(ModelComponentType.Input, RecipModelInputKeys.Service2Torque, GeneralLabel.Percentage, "Service2 Torque");
            
            self.OperatingSpeed =       DF["OC_OperatingSpeed"][0]        # new ModelComponent(ModelComponentType.Input, RecipModelInputKeys.Service2Torque, GeneralLabel.Percentage, "Service2 Torque");
            self.OperatingLoadStep =    DF["OC_OperatingLoadStep"][0]  # new ModelComponent(ModelComponentType.Input, RecipModelInputKeys.Service2Torque, GeneralLabel.Percentage, "Service2 Torque");
            self.IsDualService =        DF["OC_IsDualService"][0]
            self.Service2BrakePower =   DF["OS_BrakePower"][0]        # it is not used # new ModelComponent(ModelComponentType.Input, RecipModelInputKeys.Service2Torque, GeneralLabel.Percentage, "Service2 Torque");
            self.Service2Torque =       DF["OS_Torque"][0]                # it is not used # new ModelComponent(ModelComponentType.Input, RecipModelInputKeys.Service2Torque, GeneralLabel.Percentage, "Service2 Torque");
            
            self.FlowMeterLocation = FlowMeterLocation(DF["GN_FlowMeterLocation"][0])
            self.FlowRateOfPotentialRecycleOrSideStreamOut = 0
            
               
            if math.isnan(DF["GN_FlowTuneFactor"][0]) or (DF["GN_FlowTuneFactor"][0]) < 0.25:  self.FlowTuneFactor = 1
            else:  self.FlowTuneFactor = DF["GN_FlowTuneFactor"][0]  
            
            self.logger.info("INFO_OperatingConditions_ Load is done" ) 
        except:
            self.logger.error("ERROR_OperatingConditions_ Load") 


