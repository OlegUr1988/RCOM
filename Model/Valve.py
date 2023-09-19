# import sys
# import os
# current = os.getcwd() 
# parent = os.path.dirname(current) 
# sys.path.append(parent) 
import Logger
import math  
import DefaultMapper as DM
from Enums import CylinderEndType, ValveType 

class Valve:    
    def __init__(self, valveType): 
        self.logger = Logger.logger 
        self.ValveNoseDiameter = 0  
        self.Type = valveType
        
    def Load(self, DF, cylinderIndex:int, cylinderEndType):    #/ Loads the Input values for the current Valve of Cylinder from DF 
        try: 
            if cylinderEndType == CylinderEndType.HeadEnd:
                if self.Type == ValveType.Suction:
                    self.ValveNoseDiameter = DM.setFloatValue(DF['Cylinder_{cylinderno}_HESuctionValveValveNoseDiameter'.format(cylinderno = cylinderIndex)][0], 0) 
                elif self.Type == ValveType.Discharge:
                    self.ValveNoseDiameter = DM.setFloatValue(DF['Cylinder_{cylinderno}_HEDischargeValveValveNoseDiameter'.format(cylinderno = cylinderIndex)][0], 0)
                     
            elif cylinderEndType == CylinderEndType.CrankEnd:
                if self.Type == ValveType.Suction:
                    self.ValveNoseDiameter = DM.setFloatValue(DF['Cylinder_{cylinderno}_CESuctionValveValveNoseDiameter'.format(cylinderno = cylinderIndex)][0], 0) 
                elif self.Type == ValveType.Discharge:
                    self.ValveNoseDiameter = DM.setFloatValue(DF['Cylinder_{cylinderno}_CEDischargeValveValveNoseDiameter'.format(cylinderno = cylinderIndex)][0], 0)
                  
            self.logger.info("INFO_Valve_ Load done, cylinderIndex:" + str(cylinderIndex) + ", cylinderEndType:" +str(cylinderEndType))  
        except:
            self.logger.error("ERROR_Valve_ Load")  
