from Enums import FlowMeterType, FlowMeterLocationType, FlowStatus 
from ThermodynamicsParametersatStandardConditions import ThermodynamicsParametersatStandardConditions
import Logger
import DefaultMapper as DM 
from UnitConversionHelper import UnitConversionHelper
from Labels import TemperatureLabel
from ConversionData import PressureConversion

class Flow: 
    def __init__(self, keyNamePrefix, flowMeterType, fluidType): 
        self.KeyNamePrefix = keyNamePrefix  
        self.FlowStatus = FlowStatus.Unknown   #used in set 
        self.FluidType = fluidType 
        self.FlowMeterType = flowMeterType
        
        self.FlowMeter = None 
        self.FlowMeterLocation = ""
        self.FlowMeterTemperature = None 
        self.FlowMeterPressure = None 
        self.FlowMeterDifferentialPressure = None 
        self.AtmosphericPressure = None 
    
        self.standardConditionsParameters = ThermodynamicsParametersatStandardConditions()
        
        self.atmosphericPressureInKiloPascal = 0.0
        self.differentialPressureInKiloPascal = 0.0
        
        self.MassFlow = None
        self.StdVolumetricFlow = None
        self.ActualVolumetricFlow = None
    
        self.DensityAtStandardConditions = None 
        self.TotalDensity = None 
        
        self.IsInputGaugePressure = None 
        self.IsInputMassFlow = None 
        
        self.MassOrVolumeFlowInput = None 
    
        #needed extra
        self.K = None 
        self.DensityStd = None 
        self.PressureInKiloPascal = None 
        self.TemperatureInKelvin = None
        self.flowTemperature = None
        self.flowPressure = None
        self.flowDensity = None

        self.logger = Logger.logger

 
    def Load(self, DF):
        try:
        
            KNP = self.KeyNamePrefix
            
            self.AtmosphericPressure =           DM.setFloatValue(DF['GN_ATM_P'][0], 0.0)
            self.FlowMeter =                     DM.setFloatValue(DF[KNP + 'FlowMeter'][0], 0.0)
            self.FlowMeterTemperature =          DM.setFloatValue(DF[KNP + 'FlowMeterTemperature'][0], 0.0)
            self.FlowMeterPressure =             DM.setFloatValue(DF[KNP + 'FlowMeterPressure'][0], 0.0)
            self.FlowMeterDifferentialPressure = DM.setFloatValue(DF[KNP + 'FlowMeterDP'][0], 0.0)
            
            if not KNP.startswith('Flow_SS'):
                self.FlowMeterLocation =         DM.setStringValue(DF[KNP + 'LocationofMeter'][0], "").upper()
            else:
                self.FlowMeterLocation = ""
            
            self.standardConditionsParameters.Load()
        

            self.logger.info("INFO_Flow_Load done,  KeyNamePrefix" + str(self.KeyNamePrefix))  
        except:
            self.logger.error("ERROR_Flow_Load")
    
    
    
    
    
    
    
    # #completed
    # def SetFlowData(self, flowUnit):
        
    #     if self.FlowMeter != 0.0:
            
    #         flowValue = 0.0
    #         if self.IsFlowMeterTypeMeasuredFlow(self.FlowMeterType):
    #             flowValue = self.FlowMeter
    #             if UnitSelectionHelper.IsMassFlow(flowUnit.Input.Label):
    #                 self.MassFlow = flowValue
    #                 self.IsInputMassFlow = True
    #             else:
    #                 self.StdVolumetricFlow = flowValue  
    #             self.MassOrVolumeFlowInput = flowValue
                
    #             self.logger.debug(f"IsInputMassFlow : {self.IsInputMassFlow}")
                
    #         elif self.FlowMeterType == FlowMeterType.FlowPiTagActualFlow:
    #             self.ActualVolumetricFlow = flowValue
    #             self.logger.debug(f"Volumetric Actual Flow : {self.FlowMeter}")
        
    #     # if self.FlowMeterTemperature != 0.0:
    #     #     self.Temperature = self.FlowMeterTemperature
    #     if self.FlowMeterPressure != 0.0:
    #         self.PressureInKiloPascal = self.FlowMeterPressure
    #     if self.FlowMeterDifferentialPressure != 0.0:
    #         self.differentialPressureInKiloPascal = self.FlowMeterDifferentialPressure
        
    #     self.FlowStatus = FlowStatus.Known if self.FlowMeter != 0.0 else FlowStatus.Unknown 
    
    
    # #completed
    # def ConvertInputUnitToCoreUnit(self, atmPressureInPa, pressureUnit, diffPressureUnit, temperatureUnit, flowUnit):
        
    #     if self.MassFlow != 0.0 and self.MassFlow != None:
    #         self.logger.debug("Before Conversion: Mass Flow = {self.MassFlow}")
    #         self.MassFlow = UnitConversionHelper.ConvertUnit(self.MassFlow, flowUnit)
    #         self.logger.debug("After Conversion: Mass Flow = {self.MassFlow}")
    #     if self.StdVolumetricFlow != 0.0 and self.StdVolumetricFlow != None:
    #         self.logger.debug("Before Conversion: StdVolumetric Flow = {self.StdVolumetricFlow}")
    #         self.StdVolumetricFlow = UnitConversionHelper.ConvertUnit(self.StdVolumetricFlow, flowUnit)
    #         self.logger.debug("After Conversion: StdVolumetric Flow = {self.StdVolumetricFlow}")
    #     if self.ActualVolumetricFlow != 0.0 and self.ActualVolumetricFlow != None:
    #         self.logger.debug("Before Conversion: Act Volume Flow = {self.ActualVolumetricFlow}")
    #         self.ActualVolumetricFlow = UnitConversionHelper.ConvertUnit(self.ActualVolumetricFlow, flowUnit)
    #         self.logger.debug("After Conversion: Act Volume Flow = {self.ActualVolumetricFlow}")   
    #     # if self.Temperature != 0.0 and self.Temperature != None:
    #     #     self.Temperature = UnitConversionHelper.ConvertUnit(self.Temperature, temperatureUnit, TemperatureLabel.K)
    #     #     self.TemperatureInKelvin = self.Temperature
    #     if self.PressureInKiloPascal != 0.0 and self.PressureInKiloPascal != None:
    #         self.PressureInKiloPascal = UnitConversionHelper.ConvertUnit(self.PressureInKiloPascal, pressureUnit)
    #         if UnitSelectionHelper.IsInputGaugePressure(pressureUnit):
    #             self.PressureInKiloPascal += atmPressureInPa
    #             self.logger.debug("Pressure is Gauge. So Atmospheric pressure is added.")
    #         self.PressureInKiloPascal = PressureConversion.PaToKPaAlt(self.PressureInKiloPascal)
    #     if self.differentialPressureInKiloPascal != 0.0 and self.differentialPressureInKiloPascal != None:
    #         self.differentialPressureInKiloPascal = UnitConversionHelper.ConvertUnit(self.differentialPressureInKiloPascal, diffPressureUnit)
    #         if UnitSelectionHelper.IsInputGaugePressure(diffPressureUnit):
    #             self.differentialPressureInKiloPascal += atmPressureInPa
    #             self.logger.debug("Pressure is Gauge. So Atmospheric pressure is added.")
    #         self.differentialPressureInKiloPascal = PressureConversion.PaToKPaAlt(self.differentialPressureInKiloPascal)
        
    #     self.atmosphericPressureInKiloPascal = PressureConversion.PaToKPaAlt(atmPressureInPa)
    #     self.standardConditionsParameters.ConvertPressure(pressureUnit.Input.Conversion.Factor, self.atmosphericPressureInKiloPascal)
    #     self.standardConditionsParameters.ConvertTemperature(temperatureUnit.Input.Conversion.Offset, temperatureUnit.Input.Conversion.Factor)
        
        
            
    # def IsFlowMeterLocatedAtDischarge(self):
    #     return self.FlowMeterLocation == FlowMeterLocationType.Discharge.value
        
    # def IsFlowMeterLocatedAtSuction(self):
    #     return self.FlowMeterLocation == FlowMeterLocationType.Suction.value

    # #checked
    # def FlowMeterCalc(self, pressureInKpa, temperatureInK, thermodynamicsStl, molecularWeightMeasured):
        
    #     thermodynamicsStl.IsoThermalFlashatStandardConditions(self.standardConditionsParameters.PSTD, self.standardConditionsParameters.TSTD)
        
    #     molecularWeightCorrectionFactor = 1.0 if molecularWeightMeasured == 0.0 else molecularWeightMeasured / thermodynamicsStl.MwCalc

    #     self.DensityAtStandardConditions = thermodynamicsStl.DensityatStandardConditions    

    #     if not self.IsFlowMeterTypeMeasuredFlow(self.FlowMeterType):
    #         return
        
    #     thermodynamicsStl.IsoThermalFlash(pressureInKpa, temperatureInK)
    #     self.TotalDensity = thermodynamicsStl.TotalDensity

    #     if self.DensityAtStandardConditions > 0.0:
    #         if self.StdVolumetricFlow is None:
    #             self.StdVoumetricFlow = self.MassFlow / self.DensityAtStandardConditions
            
    #         if self.MassFlow is None:
    #             self.MassFlow = self.StdVolumetricFlow * self.DensityAtStandardConditions
            
    #     if self.MassFlow is not None and self.TotalDensity is not None:
    #         self.ActualVolumetricFlow = self.MassFlow / self.TotalDensity
    #         self.logger.debug("MassFlow at STD conditions = {self.MassFlow} tonn/d",)
        
    #     return molecularWeightCorrectionFactor


    # #checked
    # def IsFlowMeterTypeMeasuredFlow(self, flowMeterType):
    #     if flowMeterType in (FlowMeterType.FlowPiTagAtStandardConditions, FlowMeterType.Venturi, FlowMeterType.Orifice):
    #         return True
    #     else:
    #         return False