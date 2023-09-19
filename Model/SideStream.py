import math 
# import sys
# import os
# current = os.getcwd() 
# parent = os.path.dirname(current) 
# sys.path.append(parent)
from Enums import OEM, CylinderMode, CylinderEndType, SideStreamType, SideStreamControllerType 
import Logger
import DefaultMapper as DM

class SideStream:  
    def __init__(self, stageno ):  
        
        self.stageno = 0
        
        self.SS_IN_DFType = None
        self.SS_IN_DF = 0
        self.SS_IN_DFTemperature = 0
        self.SS_OUT_DFType = None
        self.SS_Out_DF = 0
        
    def Load(self, DF ):
        
        self.SS_IN_DFType =  SideStreamType (DM.setFloatValue(DF['Stage_{stageno}_SS_IN_DFType'.format(stageno = self.stageno)][0], 0) )
         
        self.SS_IN_DF =             DM.setFloatValue(DF['Stage_{stageno}_SS_IN_DF'.format(stageno = self.stageno)][0], 0) 
        self.SS_IN_DFTemperature =  DM.setFloatValue(DF['Stage_{stageno}_SS_IN_DFTemperature'.format(stageno = self.stageno)][0], 0) 
        
        self.SS_OUT_DFType =  SideStreamType ( DM.setFloatValue(DF['Stage_{stageno}_SS_OUT_DFType'.format(stageno = self.stageno)][0], 0) )
            
        self.SS_Out_DF =            DM.setFloatValue(DF['Stage_{stageno}_SS_Out_DF'.format(stageno = self.stageno)][0], 0)   
         
     
        
     
        
     
        
     
        
     
        
     
        
     
#     #/ Initialises a new instance of the SideStream class.
#     def __init__(self, Id:int, sectionId:int): 
        
        
        
#         self.HasInvalidPressureValue = bool
#         self.Id = Id
#         self.SectionId = sectionId
#         self.Type = None   # Enum   SideStreamType
#         self.ControllerType = # Enum SideStreamControllerType
        
#         self.Flow = None    # ModelComponent
#         self.Pressure = None
#         self.Temperature = None
#         self.ValvePosition = None
#         self.SetPoint = None
#         self.PresentValue = None 
        

#     def Load(self, DF):
#             # Settings.
#             self.Type = DM.setStringValue(DF['Stage_{stageno}_SS_IN_DFType'.format(stageno = cylinderIndex)][0], 0) 
            
#             setIntValue
            
            
#             Stage_{stageno}_SS_IN_DFType
#             setStringValue
            
#             DM.setStringValue(DF['Stage_{stageno}_SS_IN_DFType'.format(stageno = cylinderIndex)][0], 0) 
            
#             DM.setStringValue(DF[KNP + 'LocationofMeter'][0], "").upper()
#             LoadSideStreamType(DF.Read(string.Format(SideStreamInputKey.Type, Id), "0", ParsingType.Integer))
#             LoadSideStreamControllerType(DF.Read(string.Format(SideStreamInputKey.ControllerType, Id), "0", ParsingType.Integer))
        
#             # Inputs.
#             Flow.
#             PiTagExpression = DF.Read(string.Format(SideStreamInputKey.Flow, Id), String.Empty)
#             Flow.PiTag.PiTagExpression = DF.SetPiTagExpression(string.Format(SideStreamInputKey.Flow, Id), String.Empty)
#             Flow.Presentation.expression = DF.SetPiTagExpression(string.Format(SideStreamInputKey.Flow, Id), String.Empty)
            
#             Pressure
#             .PiTagExpression = DF.Read(string.Format(SideStreamInputKey.Pressure, Id), String.Empty)
#             Pressure.PiTag.PiTagExpression = DF.SetPiTagExpression(string.Format(SideStreamInputKey.Pressure, Id), String.Empty)
#             Pressure.Presentation.expression = DF.SetPiTagExpression(string.Format(SideStreamInputKey.Pressure, Id), String.Empty)
            
#             Temperature
#             .PiTagExpression = DF.Read(string.Format(SideStreamInputKey.Temperature, Id), String.Empty)
#             Temperature.PiTag.PiTagExpression = DF.SetPiTagExpression(string.Format(SideStreamInputKey.Temperature, Id), String.Empty)
#             Temperature.Presentation.expression = DF.SetPiTagExpression(string.Format(SideStreamInputKey.Temperature, Id), String.Empty)
            
#             ValvePosition
#             .PiTagExpression = DF.Read(string.Format(SideStreamInputKey.ValvePosition, Id), String.Empty)
#             ValvePosition.PiTag.PiTagExpression = DF.SetPiTagExpression(string.Format(SideStreamInputKey.ValvePosition, Id), String.Empty)
#             ValvePosition.Presentation.expression = DF.SetPiTagExpression(string.Format(SideStreamInputKey.ValvePosition, Id), String.Empty)
            
#             SetPoint
#             .PiTagExpression = DF.Read(string.Format(SideStreamInputKey.SetPoint, Id), String.Empty)
#             SetPoint.PiTag.PiTagExpression = DF.SetPiTagExpression(string.Format(SideStreamInputKey.SetPoint, Id), String.Empty)
#             SetPoint.Presentation.expression = DF.SetPiTagExpression(string.Format(SideStreamInputKey.SetPoint, Id), String.Empty)
            
#             PresentValue
#             .PiTagExpression = DF.Read(string.Format(SideStreamInputKey.PresentValue, Id), String.Empty)
#             PresentValue.PiTag.PiTagExpression = DF.SetPiTagExpression(string.Format(SideStreamInputKey.PresentValue, Id), String.Empty)
#             PresentValue.Presentation.expression = DF.SetPiTagExpression(string.Format(SideStreamInputKey.PresentValue, Id), String.Empty)


 
#     #/ Loads the section data from the supplied web data contract. 
#     def Load(self, webSideStreamData, sideStreamId):
#         # Settings.
#         LoadSideStreamType(int(webSideStreamData.Type.value))
#         LoadSideStreamControllerType(int(webSideStreamData.ControlledType.value))
#         Id = sideStreamId
    
#         # Inputs.
#         Flow.
#         PiTagExpression = webSideStreamData.Flow.pitagExpression
#         Pressure.
#         PiTagExpression = webSideStreamData.Pressure.pitagExpression
#         Temperature.
#         PiTagExpression = webSideStreamData.Temperature.pitagExpression
#         ValvePosition.
#         PiTagExpression = webSideStreamData.Valveposition.pitagExpression
#         SetPoint.
#         PiTagExpression = webSideStreamData.SetPoint.pitagExpression
#         PresentValue.
#         PiTagExpression = webSideStreamData.PresentValue.pitagExpression
    
    
     
#     #/ Reads the PI tags for the section using the supplied PI interface helper. 
#     def Load(self, piDataWrapper, unitConversionData, atmosphericPressureBara, dataContractType):
#         # Read Side Steam mass flow (converts from Input Units to CCOMS Core Units, tonnes/day) then convert to STOMS Core Units kg/s.
#         piDataWrapper.ReadValue(Flow, unitConversionData.FlowUIn, 0.0)
#         Flow.ValueAsDouble = InputUnitConverter.MassFlow(Flow.ValueAsDouble)
#         Flow.UnitOfMeasure = FlowLabel.Kg_sec
#         Flow.UnitOfMeasureCalculating = FlowLabel.Kg_sec
    
#         # Read pressure (converts from Input Units to CCOMS Core Units, kPa absolute or kPag) then convert to STOMS Core Units bara.
#         piDataWrapper.ReadValue(Pressure, unitConversionData.PressUIn, 0.0)
#         Pressure.ValueAsDouble = InputUnitConverter.Pressure(Pressure.ValueAsDouble, unitConversionData, atmosphericPressureBara)
#         Pressure.UnitOfMeasure = PressureLabel.Bara
#         Pressure.UnitOfMeasureCalculating = PressureLabel.Bara
    
#         # Check for negative pressure.
#         if CoreMaths.IsZeroOrNegative(Pressure.ValueAsDouble):
#             HasInvalidPressureValue = True
#             nlogger.Log(LogLevel.Warn, "Side Stream {0} Pressure Section {1} is negative. Please validate the input.", Id, SectionId)
    
#         # Read and convert temperature.
#         piDataWrapper.ReadValue(Temperature, unitConversionData.TempUIn, unitConversionData.TempAddUIn)
#         Temperature.UnitOfMeasure = TemperatureLabel.C
#         Temperature.UnitOfMeasureCalculating = TemperatureLabel.C
    
#         # No unit conversion required for these Inputs.
#         piDataWrapper.ReadValue(ValvePosition)
#         piDataWrapper.ReadValue(SetPoint)
#         piDataWrapper.ReadValue(PresentValue)







        
#         self.VolumeFlowIn = None
#         self.VolumeFlowOut = None
#         self.TemperatureIn = None
        
#         self.VolumeFlow = 0
#         self.FlowIn = None
#         self.FlowOut = None
 
#         self._InitialiseInputItems()

#         # Initialize Flow objects to null by default (this will be constructed during Load).
#         self.FlowIn = None
#         self.FlowOut = None 

# #CCOM
#     def LoadSideStreamData(self, DF, thermodynamics, sideStreamIndex, uomActual, operatingConditions):
#         self.Actual.LoadSideStreamActualData(DF, thermodynamics, sideStreamIndex, uomActual, operatingConditions)
#         self.Design.LoadSideStreamDesignData(DF, thermodynamics, sideStreamIndex)
        
        
#     #/ Intialises all Input Model Component objects.
#     def _InitialiseInputItems(self):
#         self.VolumeFlowIn = DM.setFloatValue(DF['Cylinder_{cylinderno}_MaximumAllowableWorkingPressure'][0], 0) 
#         SideStreamVolumeFlowIn, FlowLabel.Mmscfd, "Volume Flow In")
    
#         self.VolumeFlowOut = DM.setFloatValue(DF['Cylinder_{cylinderno}_MaximumAllowableWorkingPressure'][0], 0) 
#         SideStreamVolumeFlowOut, FlowLabel.Mmscfd, "Volume Flow Out")
    
#         self.TemperatureIn = DM.setFloatValue(DF['Cylinder_{cylinderno}_MaximumAllowableWorkingPressure'][0], 0) 
#         SideStreamTemperatureIn, TemperatureLabel.R, "Temperature In") 




#     #/ Loads the Input values for the current Side Stream from Flow Object
#     def Load(self, DF, stageNumber):
#         # For side stream Flow In.
#         flowMeterSelection = FlowMeterSelection(FlowInputKeyName.RcomsV2SideStreamInFlowPrefix, FluidType.PROCESSGASSIDESTREAM)
#         self.FlowIn = flowMeterSelection.CreateAndLoadFlowMeter(DF, stageNumber, True)

#         # For side stream Flow Out.
#         flowMeterSelection = FlowMeterSelection(FlowInputKeyName.RcomsV2SideStreamOutFlowPrefix, FluidType.PROCESSGASSIDESTREAM)
#         self.FlowOut = flowMeterSelection.CreateAndLoadFlowMeter(DF, stageNumber, True)

#         if self.FlowIn is not None and self.FlowOut is not None:
#             Rcoms2Engine.Models.SideStream._nlogger.Log(LogLevel.Debug, "Loaded Input Tags. stageNumber = '{0:s}', FlowIn = '{1:s}', TempIn = '{2:s}', FlowOut = '{3:s}'".format(stageNumber, self.FlowIn.FlowMeterPiTag.Expression, self.FlowIn.FlowMeterTemperaturePiTag.Expression, self.FlowOut.FlowMeterPiTag.Expression))

#         if self.FlowIn is None:
#             Rcoms2Engine.Models.SideStream._nlogger.Log(LogLevel.Warn, "SideStream Input Flow could not be created.")

#         if self.FlowOut is None:
#             Rcoms2Engine.Models.SideStream._nlogger.Log(LogLevel.Warn, "SideStream Output Flow could not be created.")


#     #/ Loads the Input Pi tag values for the current Side Stream from Flow Object & PI and converts them from Input to Core Unit values
#     def Load(self, piDataWrapper):
#         # Read Tag value from PI
#         # For Flow In
#         if self.FlowIn is not None:
#             self.VolumeFlowIn.PiTagExpression = self.FlowIn.FlowMeterPiTag.Expression
#             self.TemperatureIn.PiTagExpression = self.FlowIn.FlowMeterTemperaturePiTag.Expression
#             piDataWrapper.ReadValue(self.VolumeFlowIn)
#             piDataWrapper.ReadValue(self.TemperatureIn)

#             Rcoms2Engine.Models.SideStream._nlogger.Log(LogLevel.Debug, "Loaded Input data from Pi. VolumeFlowIn = '{0:s}', TemperatureIn = '{1:s}'".format(self.VolumeFlowIn.ValueAsDouble, self.TemperatureIn.ValueAsDouble))

#         # For Flow Out
#         if self.FlowOut is not None:
#             self.VolumeFlowOut.PiTagExpression = self.FlowOut.FlowMeterPiTag.Expression
#             piDataWrapper.ReadValue(self.VolumeFlowOut)

#             Rcoms2Engine.Models.SideStream._nlogger.Log(LogLevel.Debug, "Loaded Input data from Pi. VolumeFlowOut = '{0:s}'".format(self.VolumeFlowOut.ValueAsDouble))


#     # #/ Reset all calculated values for Side Stream.
#     # def ResetCalculatedValues(self):
#     #     self.VolumeFlow = 0.0
        
#     # #/ Converts the input values from Input Unit to Core Unit
#     # def ConvertValuesFromInputUnitToCoreUnit(self, uom, calculatedFlowConversion):
#     #     Rcoms2Engine.Models.SideStream._nlogger.Log(LogLevel.Debug, "Before converting Input to Core Unit - Input Units: VolumeFlowIn = '{0:s}', VolumeFlowOut = '{1:s}', TemperatureIn = '{2:s}'; Input Values: VolumeFlowIn = '{3:s}', VolumeFlowOut = '{4:s}', TemperatureIn = '{5:s}'".format(uom.Flow.Input.Label, uom.Flow.Input.Label, uom.Temperature.Input.Label, self.VolumeFlowIn.ValueAsDouble, self.VolumeFlowOut.ValueAsDouble, self.TemperatureIn.ValueAsDouble))

#     #     self.TemperatureIn.ValueAsDouble = Rcoms2Helper.ConvertUnit(self.TemperatureIn.ValueAsDouble, uom.Temperature)

#     #     # If the input units are given in Actual instead of Default Standard units,
#     #     # convert the Actual values to Standard before Unit conversion from Input to Core
#     #     if UnitSelectionHelper.IsVolumeFlowUnitInActuals(uom.Flow.Input.Label):
#     #         # Important comment - do NOT delete.
#     #         # If the Volume Flow is given in 'Actual Unit' (instead of 'Standard Volume Flow Unit') in the model file, the following conversion & steps are followed for calculations/conversion.
#     #         # 'Actual Unit' value in Model file --> convert to 'Standard Unit' value --> convert to 'Core Unit' value --> do calculations.
#     #         # Ex: 'acfm' (Actual) in Model File (Input) --> convert to 'scfm' (Standard) --> convert to Core 'mmscfd' --> do calculations                
#     #         self.VolumeFlowIn.ValueAsDouble = UnitConversionHelper.ConvertActualFlowToStandardFlow(self.VolumeFlowIn.ValueAsDouble, calculatedFlowConversion)
#     #         self.VolumeFlowOut.ValueAsDouble = UnitConversionHelper.ConvertActualFlowToStandardFlow(self.VolumeFlowOut.ValueAsDouble, calculatedFlowConversion)

#     #         # Now both FlowIn & FlowOut are in Standard Unit
#     #         # After this step, conversion from 'Standard' to 'Core' unit will be done as usual

#     #     self.VolumeFlowIn.ValueAsDouble = Rcoms2Helper.ConvertUnit(self.VolumeFlowIn.ValueAsDouble, uom.Flow)
#     #     self.VolumeFlowOut.ValueAsDouble = Rcoms2Helper.ConvertUnit(self.VolumeFlowOut.ValueAsDouble, uom.Flow)

#     #     Rcoms2Engine.Models.SideStream._nlogger.Log(LogLevel.Debug, "Before converting Input to Core Unit - Input Units: VolumeFlowIn = '{0:s}', VolumeFlowOut = '{1:s}', TemperatureIn = '{2:s}'; Input Values: VolumeFlowIn = '{3:s}', VolumeFlowOut = '{4:s}', TemperatureIn = '{5:s}'".format(uom.Flow.Input.Label, uom.Flow.Input.Label, uom.Temperature.Input.Label, self.VolumeFlowIn.ValueAsDouble, self.VolumeFlowOut.ValueAsDouble, self.TemperatureIn.ValueAsDouble))





#     # def CalculateVolumeFlow(self, flowAdjustmentFactor, previousStageVolumeFlow):
#     #     if self.FlowIn is not None or self.FlowOut is not None:
#     #         # TODO: No check for divide by zero?
#     #         self.VolumeFlow = previousStageVolumeFlow + (self.VolumeFlowIn.ValueAsDouble - self.VolumeFlowOut.ValueAsDouble) / flowAdjustmentFactor
#     #     else:
#     #         Rcoms2Engine.Models.SideStream._nlogger.Log(LogLevel.Warn, "SideStream Input and Output Flows could not be created - Volume Flow cannot be calculated.")

