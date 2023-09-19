import Model.Valve as Valve  
import math    
# import sys
# import os
# current = os.getcwd() 
# parent = os.path.dirname(current) 
# sys.path.append(parent) 
import Logger
import MathematicalConstant 
from Enums import CylinderEndType, ValveType
import DefaultMapper as DM

        
class CylinderEnd:
    def __init__(self, cylinderEndType):     # Initialises a new instance of the CylinderEnd class.
        self.logger = Logger.logger
        # Following properties are part of Input from Model file
        self.Type = None
        self.IsActive = False
        self.RodDiameter = 0
        self.SuctionValves = []
        self.DischargeValves = []
        self.ResistanceFactorAtSuctionAtActiveEnd = 0
        self.ResistanceFactorAtDischargeAtActiveEnd = 0
        self.ResistanceFactorAtSuctionAtDeactivatedEnd = 0
        
        self._SuctionPocketArea = 0  # Float
        self._DischagePocketArea = 0  # Float
        
        self._PistonArea = 0
        self.PistonDisplacement = 0
        self._DeviationFactor = 0
        self.ValveLossHorsePowerAtSuction = 0
        self.ValveLossHorsePowerAtDischarge = 0
        self._ClearanceAdjustmentFactor = 0
        
        # Holds the data for P-T (Pressure vs Time where time is the angle) 
        self._SuctionPressureDelta = {} 
        self._DischargePressureDelta = {}
         
        self.Pressure = {} 
        
        self.AveragePressureDropAtSuction = 0
        self.AveragePressureDropAtDischarge = 0
        self.SuctionPressureModified = 0
        self.DischargePressureModified = 0
         
        # Following properties are used in calculation as well as Web presentation
        self.BrakePower = None
        self.Flow = None
        self.EffectiveClearance = None
        self.BaseClearance = 0      # Base Clearance of the Cylinder End
        
        # % Clearance per inch travel (only for Head End, not applicable for Crank End)
        self.PercentClearance = 0
        
        self.ValveLoss = None
        self.ParasiticLossAtSuction = None
        self.VolumetricEfficiencyAtSuction = None
        self.VolumetricEfficiencyAtDischarge = None
        self.AdiabaticPower = None  
        
        self.Type = cylinderEndType
        self.SuctionValves = []
        self.DischargeValves = [] 

    # Following properties are part of Calculations 
    @property
    def SuctionPocketArea(self):
        print('SuctionPocketArea')
        self._SuctionPocketArea = self.CalculatePocketArea(len(self.SuctionValves), self.SuctionValves[0].ValveNoseDiameter) 
        return self._SuctionPocketArea
    
    @property
    def DischagePocketArea(self): 
        print('DischagePocketArea')
        self._DischagePocketArea = self.CalculatePocketArea(len(self.DischargeValves), self.DischargeValves[0].ValveNoseDiameter) 
        return self._DischagePocketArea
        
        
    # def Initialise_CylinderEndType(self, cylinderEndType):    # Initialises a new instance of the CylinderEnd class with Cylinder End type
    #     self._initialize_instance_fields() 
    #     self.Type = cylinderEndType
    #     self.SuctionValves = []
    #     self.DischargeValves = [] 
        
    # def _InitialiseInputItems():  
    #     BrakePower = ModelComponent(ModelComponentType.Input, string.Empty, PowerLabel.Hp, "Cylinder End - Brake (Total) Power")
    #     Flow = ModelComponent(ModelComponentType.Input, string.Empty, FlowLabel.Mmscfd, "Cylinder End - Flow")
    #     EffectiveClearance = ModelComponent(ModelComponentType.Input, string.Empty, GeneralLabel.Percentage, "Cylinder End - Effective Clearance")
    #     ValveLoss = ModelComponent(ModelComponentType.Input, string.Empty, PowerLabel.Hp, "Cylinder End - Valve Loss")
    #     ParasiticLossAtSuction = ModelComponent(ModelComponentType.Input, string.Empty, PowerLabel.Hp, "Cylinder End - Parasitic Loss At Suction")
    #     VolumetricEfficiencyAtSuction = ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Cylinder End - Volumetric Efficiency At Suction")
    #     VolumetricEfficiencyAtDischarge = ModelComponent(ModelComponentType.Input, RecipModelOutputKeys.CylinderHeadEndVolumetricEfficiencyAtDischarge, string.Empty, "Cylinder End - Volumetric Efficiency At Discharge uction")
    #     AdiabaticPower = ModelComponent(ModelComponentType.Input, RecipModelOutputKeys.CylinderHeadEndAdiabaticPower, string.Empty, "Cylinder End - Adiabetic Power")
   
    
    def Load(self, DF, cylinderIndex:int, headEnd):     #/ Loads Input values for Cylinder End based on type from DF
        try:
            noOfSuctionValves = 0
            noOfDischargeValves = 0  
            
            #####################
            ###  For HeadEnd  ###
            #####################  
            if self.Type == CylinderEndType.HeadEnd:  
                self.RodDiameter = DM.setFloatValue(DF['Cylinder_{cylinderno}_HERodDiameter'.format(cylinderno = cylinderIndex)][0], 0) 
                self.ResistanceFactorAtSuctionAtActiveEnd = DM.setFloatValue(DF['Cylinder_{cylinderno}_HEResistanceFactorAtSuctionActiveEnd'.format(cylinderno = cylinderIndex)][0], 100)
                self.ResistanceFactorAtDischargeAtActiveEnd = DM.setFloatValue(DF['Cylinder_{cylinderno}_HEResistanceFactorAtDischargeActiveEnd'.format(cylinderno = cylinderIndex)][0], 100)
                self.ResistanceFactorAtSuctionAtDeactivatedEnd = DM.setFloatValue(DF['Cylinder_{cylinderno}_HEResistanceFactorAtSuctionDeactiveEnd'.format(cylinderno = cylinderIndex)][0], 100) 
                
                self.BaseClearance = DM.setFloatValue(DF['Cylinder_{cylinderno}_HEBaseClearance'.format(cylinderno = cylinderIndex)][0], 0)  
                self.PercentClearance = DM.setFloatValue(DF['Cylinder_{cylinderno}_HEPerClearancePerInchTravel'.format(cylinderno = cylinderIndex)][0], 0)  
    
                # Read Number of Suction Valves 
                noOfSuctionValves = DM.setIntValue(DF['Cylinder_{cylinderno}_HENumberOfSuctionValves'.format(cylinderno = cylinderIndex)][0], 0)  
                # For each Suction Valve 
                valveIndex = 1
                while valveIndex <= noOfSuctionValves:  
                    suctionValve = None
                    suctionValve = Valve.Valve(ValveType.Suction)     # Create Suction Valve object   
                    suctionValve.Load(DF, cylinderIndex, CylinderEndType.HeadEnd)        # Load Input values from Model file for each Suction Valve 
                    self.SuctionValves.append(suctionValve)     # Add to the list of Suction Valves
                    valveIndex += 1
                
                # Read Number of Discharge Valves 
                noOfDischargeValves = DM.setIntValue(DF['Cylinder_{cylinderno}_HENumberOfDischargeValves'.format(cylinderno = cylinderIndex)][0], 0) 
                # For each Discharge Valve 
                valveIndex = 1
                while valveIndex <= noOfDischargeValves:
                    dischargeValve = Valve.Valve(ValveType.Discharge)     # Create Dischage Valve object 
                    dischargeValve.Load(DF, cylinderIndex, CylinderEndType.HeadEnd)      # Load Input values from Model file for each Discharge Valve 
                    self.DischargeValves.append(dischargeValve)     # Add to the list of Discharge Valves
                    valveIndex += 1 
                
                
            #######################
            ###  For Crand End  ###
            #######################  
            elif self.Type == CylinderEndType.CrankEnd:      # For Crand End 
                
                self.RodDiameter = DM.setFloatValue(DF['Cylinder_{cylinderno}_CERodDiameter'.format(cylinderno = cylinderIndex)][0], 0) 
                self.ResistanceFactorAtSuctionAtActiveEnd = DM.setFloatValue(DF['Cylinder_{cylinderno}_CEResistanceFactorAtSuctionActiveEnd'.format(cylinderno = cylinderIndex)][0], 100)
                self.ResistanceFactorAtDischargeAtActiveEnd = DM.setFloatValue(DF['Cylinder_{cylinderno}_CEResistanceFactorAtDischargeActiveEnd'.format(cylinderno = cylinderIndex)][0], 100)
                self.ResistanceFactorAtSuctionAtDeactivatedEnd = DM.setFloatValue(DF['Cylinder_{cylinderno}_CEResistanceFactorAtSuctionDeactiveEnd'.format(cylinderno = cylinderIndex)][0], 100) 
                
                self.BaseClearance = DM.setFloatValue(DF['Cylinder_{cylinderno}_CEBaseClearance'.format(cylinderno = cylinderIndex)][0], 0)  
                self.PercentClearance = 0.0      #= DM.setFloatValue(DF['Cylinder_{cylinderno}_CEPerClearancePerInchTravel'.format(cylinderno = self.cylinderIndex)][0], 0)   
            
                # Read Number of Suction Valves
                noOfSuctionValves = DM.setIntValue(DF['Cylinder_{cylinderno}_CENumberOfSuctionValves'.format(cylinderno = cylinderIndex)][0], 0)   
            
                # If CE is not active and user enters No.of Valves & VND as '0' for CE, then force no.of valves to '1' and use the same VND as HE
                useVNDOfHeadEnd = False 
                
                
                # If Crank End is NOT active (SuctionValves)
                if not self.IsActive:    
                    # Read the VND of the the 'first' Valve configured in the model file
                    valveNoseDiameter = DM.setFloatValue(DF['Cylinder_{cylinderno}_CESuctionValveValveNoseDiameter'.format(cylinderno = cylinderIndex)][0], 0)  
                    if noOfSuctionValves == 0 and valveNoseDiameter == 0.0:
                        noOfSuctionValves = 1
                        useVNDOfHeadEnd = True
    
                # For each Suction Valve 
                valveIndex = 1
                while valveIndex <= noOfSuctionValves: 
                    suctionValve = Valve.Valve(ValveType.Suction) 
                    suctionValve.Load(DF, cylinderIndex, CylinderEndType.CrankEnd)   # Load Input values from Model file for each Suction Valve
                    self.SuctionValves.append(suctionValve) # Add to the list of Suction Valves
                    valveIndex += 1
        
        
                # If we need to use the VND of HeadEnd for Crank End
                #   headEnd   is used here !!!
                if useVNDOfHeadEnd:
                    self.SuctionValves[0].ValveNoseDiameter = headEnd.SuctionValves[0].ValveNoseDiameter
                
                
                
                # Read Number of Discharge Valves
                noOfDischargeValves = DM.setIntValue(DF['Cylinder_{cylinderno}_CENumberOfDischargeValves'.format(cylinderno = cylinderIndex)][0], 0)    
                
                # If CE is not active and user enters No.of Valves & VND as '0' for CE, then force no.of valves to '1' and use the same VND as HE
                useVNDOfHeadEnd = False 
                
                
                # If Crank End is NOT active (DischargeValves)
                if not self.IsActive:
                    # Read the VND of the the 'first' Valve configured in the model file
                    valveNoseDiameter = DM.setFloatValue(DF['Cylinder_{cylinderno}_CEDischargeValveValveNoseDiameter'.format(cylinderno = cylinderIndex)][0], 0)   
                
                    if noOfDischargeValves == 0 and valveNoseDiameter == 0.0:
                        noOfDischargeValves = 1
                        useVNDOfHeadEnd = True
            
                # For each Discharge Valve  # Actual index in model file starts with 1 
                valveIndex = 1
                while valveIndex <= noOfDischargeValves: 
                    dischargeValve = Valve.Valve(ValveType.Discharge) # Create Suction Valve object 
                    dischargeValve.Load(DF, cylinderIndex, CylinderEndType.CrankEnd)    # Load Input values from Model file for each Discharge Valve 
                    self.DischargeValves.append(dischargeValve) # Add to the list of Discharge Valves
                    valveIndex += 1
                
                # If we need to use the VND of HeadEnd for Crank End
                #   headEnd   is used here !!!
                if useVNDOfHeadEnd: 
                    self.DischargeValves[0].ValveNoseDiameter = headEnd.DischargeValves[0].ValveNoseDiameter  
                
                 
        
            self.logger.info("INFO_CylinderEnd_Load done,  cylinderIndex:" + str(cylinderIndex) + ", headEnd:" +str(headEnd))  
        except:
            self.logger.error("ERROR_CylinderEnd_Load")  
        
     
        
     
        
     
        
        # #/ Loads the data from PI for Performance Tables on the Web. 
        # def LoadPiDataForPerformanceTables(self, DF, piDataWrapper, uom, cylinderNumber):
        #     nlogger.Log(LogLevel.Debug, "Loading Pi data for Cylinder sequence number: '{0:s}'.".format(cylinderNumber))
        
        #     # Initialize Output Items along with Output Units
        #     InitialiseOutputItems(uom)
        
        #     # For Brake (Total) Power
        #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, BrakePower, cylinderNumber)
        
        #     # For Flow
        #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, Flow, cylinderNumber)
        
        #     # For Effective Clearance
        #     # Effective Clearance is already set from Input
        
        #     # For Valve Loss
        #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, ValveLoss, cylinderNumber)
        
        #     # For Parasitic Loss At Suction
        #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, ParasiticLossAtSuction, cylinderNumber)
        
        #     # For Volumetric Efficiency At Suction
        #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, VolumetricEfficiencyAtSuction, cylinderNumber)


    #/ Reset all calculated values for Cylinder End.
    #/ This is to prevent the previous values being used for multiple calculations for Web.
    def ResetCalculatedValues(self):
        self.SuctionPocketArea = 0  # Float
        self.DischagePocketArea = 0  # Float
        self._PistonArea = 0.0
        self.PistonDisplacement = 0.0
        self._DeviationFactor = 0.0
        self.ValveLossHorsePowerAtSuction = 0.0
        self.ValveLossHorsePowerAtDischarge = 0.0
        self._ClearanceAdjustmentFactor = 0.0

        self._SuctionPressureDelta = {}
        self._DischargePressureDelta = {}
        self.Pressure = {}

        self.AveragePressureDropAtSuction = 0.0
        self.AveragePressureDropAtDischarge = 0.0
        self.SuctionPressureModified = 0.0
        self.DischargePressureModified = 0.0

        self.BrakePower.ValueAsDouble = 0.0
        self.Flow.ValueAsDouble = 0.0
        self.ValveLoss.ValueAsDouble = 0.0
        self.ParasiticLossAtSuction.ValueAsDouble = 0.0
        self.VolumetricEfficiencyAtSuction.ValueAsDouble = 0.0
        self.VolumetricEfficiencyAtDischarge.ValueAsDouble = 0.0
        self.AdiabaticPower.ValueAsDouble = 0.0

        # Note: EffectiveClearance should NOT be reset. 
        # Its values is set as part of Input from LoadStep config.
        # This is NOT a calculated value.
        # EffectiveClearance.ValueAsDouble = 0.0
        
        
    #/ Calculate Pocket Area of Valves     #/ Equations 2-7 (Suction) & 2-8 (Discharge)
    #/ It is assumed that ValueNoseDiameter is same across all Valves for an End. Hence the first Valve is considered. 
    def CalculatePocketArea(self, valveCount, valveNoseDiameter):
        pocketArea = valveCount * (MathematicalConstant.PI / 4.0) * valveNoseDiameter ** 2  
        return pocketArea


    # def get_suction_pocket_area(self):
    #     return self.CalculatePocketArea(len(self.SuctionValves), self.SuctionValves.First().ValveNoseDiameter)
    # def set_suction_pocket_area(self, value):
    #     pass
    # def get_dischage_pocket_area(self):
    #     return self.CalculatePocketArea(len(self.DischargeValves), self.DischargeValves.First().ValveNoseDiameter)
    # def set_dischage_pocket_area(self, value):
    #     pass