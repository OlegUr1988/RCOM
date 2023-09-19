import math    
# import sys
# import os
# current = os.getcwd() 
# parent = os.path.dirname(current) 
# sys.path.append(parent) 
import Logger 
import CompositionData as CompositionData
from Enums import OEM, CylinderMode, CylinderEndType#, SideStream
import DefaultMapper as DM 

import math 
import Model.Range 
from Model import SideStream , Limits 
import ThermodynamicsStl

class Stage:  
    #/ Initialises a new instance of the Stage class for Stage number. 
    def __init__(self, stageNumber): 
        
        self.StageNumber = stageNumber 
        self.SuctionFixedPressureDrop = 0
        self.SuctionPressureDropPercentage = 0
        self.DischargeFixedPressureDrop = 0
        self.DischargePressureDropPercentage = 0 
        
        self.GasCompositionActual = None    # class CompositionData
        self.GasComposition = None          # class CompositionData
        self.Limits = Limits.Limits()      # class Limits
        self.SideStream = None  # class SideStream
        self.SideStream = SideStream.SideStream(stageNumber)
        self.Cylinders = []
        
        
        self.IsFirstStage = False
        self.IsLastStage = False
        self._SuctionTemperatureCalculated = 0
        self._Displacement = 0
        self._TotalDisplacement = 0
        self._EffectiveDisplacement = 0
        self._FlowAdjustment = 0
        self._FlowAdjustmentFactor = 0
        self._EffectiveClearance = 0
        self._AverageBoreDiameter = 0
        self._BaseVolume = 0
        self._EffectiveVolume = 0
        self._CountOfBores = 0
        self._SumOfBoreDiameter = 0
        self.PredictedStageFlow = 0
        self.IsentropicHorsePower = 0
        self.Slippage = 0
        
        # Following are temporary variables used as part of calculations
        self._NextIteration3 = 0
        self._NextIteration4 = 0
        self.IsActualTemperatureAvailable = False
        
        # Following properties are used in calculation as well as Web presentation
        self.SuctionPressureCalculated = None
        self.DischargePressureCalculated = None
        self.SuctionTemperatureAtTransmitter = None
        self.AverageDischargeTemperature = None
        self.SuctionPressureAtTransmitter = None
        
        # Input Suction Pressure At Transmitter is set at First Stage. For other stages it can be empty in model and is set to 0.0 in code
        self.DischargePressureAtTransmitter = None
        self.DischargeTemperatureAtTransmitter = None
        self.CompressionRatio = None
        self.GasK = None
        self.Flow = None
        self.BrakePower = None
        self.IsentropicEfficiency = None
        self.SuctionPressureAtFlange = None
        self.DischargePressureAtFlange = None
        self.DischargeTemperatureCalculated = None
        self.DischargeTemperatureCalculatedDelta = None
        self.InterstagePressureCalculatedDelta = None
        self.SpecificGravity = None
        self.Zs = None
        self.Zd = None
        self.MolecularWeight = None
        self.SuctionDensity = None
        self.DischargeDensity = None
        self.SuctionSpecificHeat = None
        self.DischargeSpecificHeat = None
        
        self.CalculatedFlowConversion = 0  
        
    # def _InitialiseInputItems(self):
    #     SuctionTemperatureAtTransmitter = ModelComponent(ModelComponentType.Input, RecipModelInputKeys.SuctionTemperatureAtTransmitter, TemperatureLabel.R, "Suction Temperature At Transmitter")
    #     SuctionPressureAtTransmitter = ModelComponent(ModelComponentType.Input, RecipModelInputKeys.SuctionPressureAtTransmitter, PressureLabel.Psia, "Suction Pressure At Transmitter")
    #     DischargePressureAtTransmitter = ModelComponent(ModelComponentType.Input, RecipModelInputKeys.DischargePressure, PressureLabel.Psia, "Discharge Pressure At Transmitter")
    #     DischargeTemperatureAtTransmitter = ModelComponent(ModelComponentType.Input, RecipModelInputKeys.DischargeTemperature, TemperatureLabel.R, "Discharge Temperature At Transmitter")
    #     SuctionPressureCalculated = ModelComponent(ModelComponentType.Input, string.Empty, PressureLabel.Psia, "Suction Pressure Calculated")
    #     DischargePressureCalculated = ModelComponent(ModelComponentType.Input, string.Empty, PressureLabel.Psia, "Discharge Pressure Calculated")
    #     AverageDischargeTemperature = ModelComponent(ModelComponentType.Input, string.Empty, TemperatureLabel.R, "Average Discharge Temperature")
    #     CompressionRatio = ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Compression Ratio")
    #     GasK = ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "GasK")
    #     Flow = ModelComponent(ModelComponentType.Input, string.Empty, FlowLabel.Mmscfd, "Flow")
    #     BrakePower = ModelComponent(ModelComponentType.Input, string.Empty, PowerLabel.Hp, "Brake Power")
    #     IsentropicEfficiency = ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Isentropic Efficiency")
    #     SuctionPressureAtFlange = ModelComponent(ModelComponentType.Input, string.Empty, PressureLabel.Psia, "Suction PressureAt Flange")
    #     DischargePressureAtFlange = ModelComponent(ModelComponentType.Input, string.Empty, PressureLabel.Psia, "Discharge Pressure At Flange")
    #     DischargeTemperatureCalculated = ModelComponent(ModelComponentType.Input, string.Empty, TemperatureLabel.R, "Discharge Temperature Calculated")
    #     DischargeTemperatureCalculatedDelta = ModelComponent(ModelComponentType.Input, string.Empty, TemperatureLabel.R, "Discharge Temperature Calculated Delta")
    #     InterstagePressureCalculatedDelta = ModelComponent(ModelComponentType.Input, string.Empty, PressureLabel.Psia, "Interstage Pressure Calculated Delta")
    #     MolecularWeight = ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Molecular Weight")
    #     SpecificGravity = ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Specific Gravity")
    #     SuctionDensity = ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Suction Density")
    #     DischargeDensity = ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Discharge Density")
    #     SuctionSpecificHeat = ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Suction Specific Heat")
    #     DischargeSpecificHeat = ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Discharge Specific Heat")
    #     Zs = ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Compressibility at Suction")
    #     Zd = ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Compressibility at Discharge")
    
    
    #/ Loads the Input values for the current Stage from DF  
    def Load(self, DF, thermodynamics, stageCylinders, numberOfStages:int):
        self.SuctionFixedPressureDrop =  DM.setFloatValue(DF['Stage_{stageno}_SuctionFixedPressureDrop'.format(stageno = self.StageNumber)][0], 0)  
        self.DischargeFixedPressureDrop =  DM.setFloatValue(DF['Stage_{stageno}_DischargeFixedPressureDrop'.format(stageno = self.StageNumber)][0], 0) 
        sucPresDropPercentage = 1.0 if self.StageNumber == 1 else 0.0 
        self.SuctionPressureDropPercentage =  DM.setFloatValue(DF['Stage_{stageno}_SuctionPressureDropPercentage'.format(stageno = self.StageNumber)][0], sucPresDropPercentage)   
        self.DischargePressureDropPercentage =  DM.setFloatValue(DF['Stage_{stageno}_DischargePressureDropPercentage'.format(stageno = self.StageNumber)][0], 2)   
        # Load Pi Tag from Model file
        # CODE: was a string / setStringValue
        self.SuctionTemperatureAtTransmitter = DM.setFloatValue(DF['Stage_{stageno}_SuctionTemperatureAtTransmitter'.format(stageno = self.StageNumber)][0], 0)    
        # CODE: was a string / setStringValue
        self.SuctionPressureAtTransmitter = DM.setFloatValue(DF['Stage_{stageno}_SuctionPressureAtTransmitter'.format(stageno = self.StageNumber)][0], 0)    
        # CODE: was a string / setStringValue
        self.DischargeTemperatureAtTransmitter = DM.setFloatValue(DF['Stage_{stageno}_DischargePressureAtTransmitter'.format(stageno = self.StageNumber)][0], 0)    
 
        # Check and set if the Actual Discharge Temperature At Transmitter is available/configured (NOT empty) in the model file. 
        self.IsActualTemperatureAvailable = math.isnan(DF['Stage_{stageno}_DischargePressureAtTransmitter'.format(stageno = self.StageNumber)][0]) #and len(DischargeTemperatureAtTransmitter) > 0
        self.GasCompositionActual = thermodynamics.LoadGasComposition(DF, 'GasRecip_Stage_' + str(self.StageNumber) + '_')  
        # Initialize to default values.
        self.GasComposition = CompositionData.CompositionData()
        
        
        ''' IT IS NOT USED IN CALC
        # Load Limits for Suction Temperature At Transmitter
        # NOTE: This property is from Limits class. This should not be confused with actual "SuctionTemperatureAtTransmitter" property of Stage which is Input value.
        self.Limits = Limits.Limits()
        self.Limits.SuctionTemperatureAtTransmitter = 

        Range(DM.setFloatValue(DF['Stage_{stageno}_DischargePressureDropPercentage'.format(stageno = self.StageNumber)][0], 2)   ,
              DM.setFloatValue(DF['Stage_{stageno}_DischargePressureDropPercentage'.format(stageno = self.StageNumber)][0], 2)   )
            
            DF.Read(RecipModelInputKeys.MinimumSuctionTemperatureAtTransmitter, "0.0", StageNumber, ParsingType.Double), 
              DF.Read(RecipModelInputKeys.MaximumSuctionTemperatureAtTransmitter, "0.0", StageNumber, ParsingType.Double))
        '''
        # If Stage is the last stage
        if self.StageNumber == numberOfStages:
            # Load Pi Tag from Model file
            self.DischargePressureAtTransmitter = DM.setFloatValue(DF['Stage_{stageno}_DischargePressureAtTransmitter'.format(stageno = self.StageNumber)][0], 0)    
            # DF.Read(DischargePressureAtTransmitter.KeyName, string.Empty, StageNumber, ParsingType.String)
    
            # Check if it is Last Stage
            IsLastStage = True
        
        # If Stage is > 1
        if self.StageNumber > 1:
            # If Stage is 2..n-1
            if self.StageNumber <= numberOfStages:
                # Load Side Stream values from Model file
                self.SideStream.Load(DF )
        elif self.StageNumber == 1:
            # Set if it is First Stage
            IsFirstStage = True
        
        if not IsLastStage:
            self.DischargePressureAtTransmitter = DM.setFloatValue(DF['Stage_{stageno}_SuctionPressureAtTransmitter'.format(stageno = self.StageNumber)][0], 0)
            #DF.Read(SuctionPressureAtTransmitter.KeyName, string.Empty, StageNumber + 1, ParsingType.String)
        
        # Set Cylinders for current Stage
        self.Cylinders = stageCylinders
         
         
        # #/ Loads the Input values for the current Stage from PI and converts the units from Input to Core Units
        # public void Load(PiDataWrapper piDataWrapper, int numberOfStages)
        #     # Read Tag value from PI
        #     piDataWrapper.ReadValue(SuctionTemperatureAtTransmitter)
        #     piDataWrapper.ReadValue(SuctionPressureAtTransmitter)
        #     piDataWrapper.ReadValue(DischargePressureAtTransmitter)
        #     piDataWrapper.ReadValue(DischargeTemperatureAtTransmitter)
        
        #     # If Stage is > 1
        #     if StageNumber > 1:
        #         # If Stage is 2..n-1
        #         if StageNumber <= numberOfStages:
        #             # Load Side Stream values from PI
        #             # Read Tag value from PI
        #             self.SideStream.Load(piDataWrapper)
         
        
    # #/ Initialise all Model Component objects for Output. 
    # def _InitialiseOutputItems(self, UOM, isStageLevel):
    #     if isStageLevel:
    #         GasK = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageGasK, string.Empty, "Stage GasK")
    #         CompressionRatio = ModelComponent(ModelComponentType.Output, string.Empty, string.Empty, "Stage Compression Ratio")
    #         Flow = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageFlow, UOM.Flow.Output.Label, "Stage Flow")
    #         BrakePower = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageBrakePower, UOM.Power.Output.Label, "Stage Brake Power (or Load)")
    #         IsentropicEfficiency = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageIsentropicEfficiency, GeneralLabel.Percentage, "Stage Isentropic Efficiency")
    #         AverageDischargeTemperature = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageDischargeTemperature, UOM.Temperature.Output.Label, "Stage Average Discharge Temperature")
    #         SuctionPressureCalculated = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageSuctionPressureCalculated, UOM.Pressure.Output.Label, "Stage Suction Pressure Calculated")
    #         DischargePressureCalculated = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageDischargePressureCalculated, UOM.Pressure.Output.Label, "Stage Discharge Pressure Calculated")
    #         DischargeTemperatureCalculated = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageDischargeTemperatureCalculated, UOM.Temperature.Output.Label, "Stage Discharge Temperature Calculated")
    #         DischargeTemperatureCalculatedDelta = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageDischargeTemperatureCalculatedDelta, UOM.Temperature.Output.Label, "Stage Discharge Temperature Calculated Delta")
    #         InterstagePressureCalculatedDelta = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageInterstagePressureCalculatedDelta, UOM.Temperature.Output.Label, "Inter Stage Pressure Calculated Delta")
    #         MolecularWeight = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageMolecularWeight, string.Empty, "Molecular Weight")
    #         SpecificGravity = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageSpecificGravity, string.Empty, "Specific Gravity")
    #         SuctionDensity = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageSuctionDensity, string.Empty, "Suction Density")
    #         DischargeDensity = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageDischargeDensity, string.Empty, "Discharge Density")
    #         SuctionSpecificHeat = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageSuctionSpecificHeat, string.Empty, "Suction Specific Heat")
    #         DischargeSpecificHeat = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageDischargeSpecificHeat, string.Empty, "Discharge Specific Heat")
    #         Zs = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageSuctionCompressibility, string.Empty, "Compressibility at Suction")
    #         Zd = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageDischargeCompressibility, string.Empty, "Compressibility at Discharge")
    
    #     # TO DO - validage if these are at Cylinder level or Stage level
    #     SuctionPressureAtFlange = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageSuctionPressureAtFlange, UOM.Pressure.Output.Label, "Stage Suction Pressure At Flange")
    #     DischargePressureAtFlange = ModelComponent(ModelComponentType.Output, RecipModelOutputKeys.StageDischargePressureAtFlange, UOM.Pressure.Output.Label, "Stage Discharge Pressure At Flange")
    
        
        
    # #/ Reset all calculated values for Stage. 
    # def ResetCalculatedValues(self):
    #     SuctionTemperatureCalculated = 0.0
    #     Displacement = 0.0
    #     TotalDisplacement = 0.0
    #     EffectiveDisplacement = 0.0
    #     FlowAdjustment = 0.0
    #     FlowAdjustmentFactor = 0.0
    #     EffectiveClearance = 0.0
    #     AverageBoreDiameter = 0.0
    #     BaseVolume = 0.0
    #     EffectiveVolume = 0.0
    #     CountOfBores = 0
    #     SumOfBoreDiameter = 0.0
    #     PredictedStageFlow = 0.0
    #     IsentropicHorsePower = 0.0
    #     Slippage = 0.0
    #     NextIteration3 = 0.0
    #     NextIteration4 = 0.0
    
    #     SuctionPressureCalculated.ValueAsDouble = 0.0
    #     DischargePressureCalculated.ValueAsDouble = 0.0
    #     AverageDischargeTemperature.ValueAsDouble = 0.0
    #     CompressionRatio.ValueAsDouble = 0.0
    #     GasK.ValueAsDouble = 0.0
    #     Flow.ValueAsDouble = 0.0
    #     BrakePower.ValueAsDouble = 0.0
    #     IsentropicEfficiency.ValueAsDouble = 0.0
    #     SuctionPressureAtFlange.ValueAsDouble = 0.0
    #     DischargePressureAtFlange.ValueAsDouble = 0.0
    #     DischargeTemperatureCalculated.ValueAsDouble = 0.0
    #     DischargeTemperatureCalculatedDelta.ValueAsDouble = 0.0
    #     InterstagePressureCalculatedDelta.ValueAsDouble = 0.0
    #     SpecificGravity.ValueAsDouble = 0.0
    #     Zs.ValueAsDouble = 0.0
    #     Zd.ValueAsDouble = 0.0
    #     MolecularWeight.ValueAsDouble = 0.0
    #     SuctionDensity.ValueAsDouble = 0.0
    #     DischargeDensity.ValueAsDouble = 0.0
    #     SuctionSpecificHeat.ValueAsDouble = 0.0
    #     DischargeSpecificHeat.ValueAsDouble = 0.0
    
    #     # Reset Calculated Values for each Cylinder
    #     for cylinder in Cylinders:
    #         cylinder.ResetCalculatedValues()
    
    #     #CalculatedFlowConversion = 0.0
    
    #     # Reset Calculated Values for Side Stream
    #     SideStream.ResetCalculatedValues()
    
    
     
    # #/ Loads the data from PI for Performance Tables on the Web.  
    # def LoadPiDataForPerformanceTables(self, DF, piDataWrapper, UOM, isStageLevel, atmosphericPressureInAbsoluteUnit):
    #     # Initialize Output Items along with Output Units
    #     InitialiseOutputItems(UOM, isStageLevel)
    
    #     # Request is for Cylinder level data and/or Stage level data
    #     # For Suction Pressure At Flange
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, SuctionPressureAtFlange, StageNumber)
    
    #     # For Discharge Pressure At Flange
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, DischargePressureAtFlange, StageNumber)
    
    
    #     # For Compression Ratio
    #     # Suction & Discharge Pressures are stored & retrieved in Output units in PI.
    #     # However the CR is calculated is in Absolute pressure units.
    #     # So Suction & Discharge pressures should be converted to Absolute before CR calculation.
    
    #     suctionPressureAtFlange = SuctionPressureAtFlange.ValueAsDouble
    #     dischargePressureAtFlange = DischargePressureAtFlange.ValueAsDouble
    
    #     # If the Unit is in Gauge, convert the values to Absolute
    #     if UnitSelectionHelper.IsInputGaugePressure(UOM.Pressure):
    #         # For Suction Pressure At Flange
    #         suctionPressureAtFlange = SuctionPressureAtFlange.ValueAsDouble + atmosphericPressureInAbsoluteUnit
    
    #         # For Discharge Pressure At Flange
    #         dischargePressureAtFlange = DischargePressureAtFlange.ValueAsDouble + atmosphericPressureInAbsoluteUnit
    
    #         nlogger.Log(LogLevel.Debug, string.Format("Pressure is Gauge. So Atmospheric pressure is added."))
    
    #     CalculateCompressionRatio(suctionPressureAtFlange, dischargePressureAtFlange)
    
    #     # For Slippage
    #     CalculateSlippage()
    
    #     # Request is for Stage level data
    #     if isStageLevel:
    #         # GasK from flow balance routine
    #         Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, GasK, StageNumber)
    
    #         # Brake Power or Load
    #         Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, BrakePower, StageNumber)
    
    #         # Load additional Pi data for Performance Table
    #         LoadPiDataForPerformanceTablesOrSvg(DF, piDataWrapper, UOM)
