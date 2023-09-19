from SCShellThermoLib import SCShellThermoLib
from CompositionData import CompositionData
from Enums import PhaseState, EOSModelType, Models, Phases
from PhaseOfMatter import PhaseOfMatter
import MathematicalConstant, ScientificConstants
import Logger
import DefaultMapper as DM

class ThermodynamicsStl:
    
    def __init__(self):
        
        self.shellThermoLibWrapper = None
        
        self.molarEnthalpy = 0.0
        self.molarEntropy = 0.0
        self.specificEnthalpy = 0.0
        self.specificEntropy = 0.0
        
        self.totalDensity = 0.0
        self.densityatStandardConditions = 0.0
        
        self.temperatureCalculated = 0.0
        self.numberOfPhasesPossible = 0.0
        self.totalMolecularWeight = 0.0
        
        self.Mw = 0.0
        self.MwCalc = 0.0
        self.SpecificGravity = 0.0
        self.phases = []
        
        self.Vapour = None
        self.Liquid = None
        self.HeavyLiquid = None
        self.HeavyLiquid2 = None
        
        self.GasComposition = None
    
        self.selectedSTLphases = None
        self.selectedSTLModel = None
        
        self.logger = Logger.logger
        
    @property
    def DensityatStandardConditions(self):
        return self.densityatStandardConditions

    @property
    def TemperatureCalculated(self):
        return self.temperatureCalculated if self.temperatureCalculated else None

    @property
    def TotalDensity(self):
        return self.totalDensity

    @property
    def SpecificEnthalpy(self):
        return self.specificEnthalpy

    @property
    def SpecificEntropy(self):
        return self.specificEntropy

    @property
    def NumberOfPhases(self):
        return self.numberOfPhasesPossible

    #checked above
    
    #public methods
    
    #checked
    def LoadGasComposition(self, DF, keyNamePrefix):
        
        self.GasComposition = CompositionData()
        
        self.GasComposition.EquationofStateModel = EOSModelType(DM.setIntValue(DF[keyNamePrefix+'GasCalcType'], EOSModelType.SMIRK.value))
        try:
            for item in self.GasComposition.Components:
                
                ColName = keyNamePrefix + item.KeyName  
                if ColName in DF.columns: 
                    item.Value = DM.setFloatValue(DF[ColName][0], 0.0) 
                else: 
                    raise
        except:
            self.logger.error("Error in Loading Gas Composition {keyNamePrefix}")
            raise
    
        self.GasComposition.CalculateAbsoluteMoleSum()
        
        return self.GasComposition
    
    #checked
    def IsoThermalFlashatStandardConditions(self, pressureInKiloPascal, temperatureInKelvin):
        
        try:
            if self.GasComposition.EquationofStateModel == EOSModelType.NoCalculation:
                self.SetGasPropertiesWhenNoCalculationWillBePerformed(self.GasComposition)
            else:
                self.InitialiseShellThermoLibWrapper()
                
                if self.shellThermoLibWrapper is not None:
                    
                    self.PopulateShellThermoLibWithGasComposition(self.GasComposition)
                    
                    self.logger.debug(f"Calculating Isothermal at Standard Conditions(P:{pressureInKiloPascal * 1000} T:{temperatureInKelvin})")
                    IsothermalatSTDStream = self.shellThermoLibWrapper.Isothermal(T=temperatureInKelvin, P=pressureInKiloPascal * 1000)
                    self.logger.debug("Calculating Isothermal at Standard Conditions done")
    
                    self.pressureCalculated = pressureInKiloPascal
                    self.temperatureCalculated = temperatureInKelvin
    
                    self.ProcessStreamPhases(IsothermalatSTDStream)
                    self.ProcessStream(IsothermalatSTDStream)
    
                    self.densityatStandardConditions = self.totalDensity
    
                    if IsothermalatSTDStream.Phase(0).state() != PhaseState.Vapour:
                        self.logger.error("Phase state cannot be liquid for calculation of gas properties at standard condtitions")
                        raise Exception("Phase state cannot be liquid for calculation of gas properties at standard condtitions")
        except Exception as ex:
            self.logger.error(f"{ex} Calculating Isothermal at Standard Conditions (P:{pressureInKiloPascal * 1000} T:{temperatureInKelvin})")
            raise


    #checked
    def IsoThermalFlash(self, pressureInKiloPascal, temperatureInKelvin):

        try:
            if self.GasComposition.EquationofStateModel == EOSModelType.NoCalculation:
                self.SetGasPropertiesWhenNoCalculationWillBePerformed(self.GasComposition)
            else:
                self.InitialiseShellThermoLibWrapper()
                
                if self.shellThermoLibWrapper is not None:
                    
                    self.PopulateShellThermoLibWithGasComposition(self.GasComposition)
    
                    pressureInPascal = pressureInKiloPascal * 1000.0
                    
                    self.logger.debug(f"Calculating Isothermal  (P:{pressureInPascal} T:{temperatureInKelvin})")
                    IsothermalStream = self.shellThermoLibWrapper.Isothermal(T=temperatureInKelvin, P=pressureInPascal)
                    self.logger.debug("Calculating Isothermal done")
                    
                    self.numberOfPhasesPossible = IsothermalStream.numberOfPhasesPresent()
                    
                    if self.numberOfPhasesPossible == 0:
                        self.logger.error(f"Number Of Phases Present: {self.NumberOfPhases}")
                        raise Exception("No Phases Present for Isothermal Calculations at given Temperature & Pressure conditions")
                    
                    self.logger.debug(f"Number Of Phases Present: {self.NumberOfPhases}")
                    
                    if IsothermalStream.Phase(0).state() != PhaseState.Vapour and self.NumberOfPhases == 1:
                        self.logger.info(f"No Gas Phase Present. First Phase Present is: {str(IsothermalStream.Phase(0).state())}" )
    
                    self.pressureCalculated = pressureInKiloPascal
                    self.temperatureCalculated = temperatureInKelvin
    
                    self.ProcessStreamPhases(IsothermalStream)
                    self.ProcessStream(IsothermalStream)
    
                    self.Mw = self.GasComposition.Mw if (self.GasComposition.Mw > 0) else self.totalMolecularWeight
                    self.SpecificGravity = self.Mw / MathematicalConstant.AIR_MW
        
        except Exception as ex:
            self.logger.error(f"{ex} Calculating IsoThermalFlash  (P:{pressureInKiloPascal * 1000} T:{temperatureInKelvin})")
            raise
            

    #checked
    def IsoEnthalpicFlash_T(self, pressureInKiloPascal, Enthalpy):
        try:
            self.InitialiseShellThermoLibWrapper()
            
            if self.shellThermoLibWrapper is not None:
                
                self.PopulateShellThermoLibWithGasComposition(self.GasComposition)
    
                pressure_Pascal = pressureInKiloPascal * 1000.0
                
                self.logger.debug(f"Calculating Isenthalpic_T (P:{pressure_Pascal} H:{Enthalpy})" )
                EnthalpicStream = self.shellThermoLibWrapper.Isenthalpic_T(P=pressure_Pascal, TotalEnthaply=Enthalpy)
                self.logger.debug("Calculating Isenthalpic_T done")
                
                if EnthalpicStream.numberOfPhasesPresent() == 0:
                    self.logger.error(f"Number Of Phases Present: {EnthalpicStream.numberOfPhasesPresent()}")
                    raise Exception("No Phases Present for Isenthalpic Calculations")
    
                self.pressureCalculated = pressureInKiloPascal
                self.temperatureCalculated = EnthalpicStream.T()
    
                self.ProcessStreamPhases(EnthalpicStream)
                self.ProcessStream(EnthalpicStream)
                
        except Exception as ex:
            self.logger.error(f"{ex} Calculating IsoEnthalpicFlash (P:{pressureInKiloPascal * 1000} H:{Enthalpy})")
            raise


    #checked
    def IsoEntropicFlash_T(self, pressureInKiloPascal, molarEntropy):
        try:
            self.InitialiseShellThermoLibWrapper()
            
            if self.shellThermoLibWrapper is not None:
            
                self.PopulateShellThermoLibWithGasComposition(self.GasComposition)
                
                pressure_Pascal = pressureInKiloPascal * 1000.0
                
                self.logger.debug(f"Calculating Isentropic  (P:{pressure_Pascal} S:{molarEntropy})")
                IsentropicStream = self.shellThermoLibWrapper.Isentropic_T(P=pressure_Pascal, TotalEntropy=molarEntropy * self.GasComposition.AbsoluteMoleSum)
                self.logger.debug("Calculating Isentropic  done")
                
                if IsentropicStream.numberOfPhasesPresent() == 0:
                    self.logger.error(f"Number Of Phases Present: {IsentropicStream.numberOfPhasesPresent()}");
                    raise Exception("No Phases Present for Isentropic Calculations")
    
                self.pressureCalculated = pressureInKiloPascal
                self.temperatureCalculated = IsentropicStream.T()
    
                self.ProcessStreamPhases(IsentropicStream)
                self.ProcessStream(IsentropicStream)
                
        except Exception as ex:
            self.logger.error(f"{ex} Calculating IsoEntropicFlash (P:{pressureInKiloPascal * 1000} S:{molarEntropy})")
            raise
            
            
    #checked
    def FindShellThermoLibModel(self, EOSModelType):
        model = Models.SMIRK
        if (EOSModelType == EOSModelType.SMIRK):
            model = Models.SMIRK
        elif (EOSModelType == EOSModelType.CPA):
            model = Models.CPA
        elif (EOSModelType == EOSModelType.CPA_SMIRK):
            model = Models.CPA_SMIRK
        elif (EOSModelType == EOSModelType.CPA_SMIRK_LKP):
            model = Models.CPA_SMIRK_LKP
        elif (EOSModelType == EOSModelType.CPA_LKP):
            model = Models.CPA_LKP
        elif (EOSModelType == EOSModelType.PR78):
            model = Models.PR78
        elif (EOSModelType == EOSModelType.PSRK_NRTL):
            model = Models.PSRK_NRTL
        elif (EOSModelType == EOSModelType.PSRK_UNIFAC):        
            model = Models.PSRK_UNIFAC
        elif (EOSModelType == EOSModelType.STEAM):
            model = Models.STEAM
        elif (EOSModelType == EOSModelType.STL_HydrateFormationCalculations):
            self.logger.error(f"Init STL Model with Hydrate model for temporary usage until it is added by MARK to the STL, {model}")
            model = Models.SMIRK

        self.logger.debug(f"Init STL Model {model}")
        return model


    #checked
    def ProcessStream(self, sTLstream):
        self.GetTotalMolecularWeight(sTLstream)
        self.GetTotalDensitys(sTLstream)
        self.ProcessStreamEnthalpyEntropyData(sTLstream)


    #checked    
    def InitialisePhases(self):
        self.numberOfPhasesPossible = 0;
        self.Vapour = PhaseOfMatter()
        self.Liquid = PhaseOfMatter()
        self.HeavyLiquid = PhaseOfMatter()
        self.HeavyLiquid2 = PhaseOfMatter()


    #checked
    def ProcessStreamPhases(self, sTLstream):
        
        self.InitialisePhases()
        self.numberOfPhasesPossible = sTLstream.numberOfPhasesPossible()  
        self.phases = []
        for i in range(self.numberOfPhasesPossible):

            if sTLstream.isPhasePresent(i):
                
                phase = PhaseOfMatter()
                phase.PhaseSTL = sTLstream.Phase(i)
                phase.State = phase.PhaseSTL.state()
                phase.StlStreamPhaseArrayIndex = i

                phase.State = sTLstream.Phase(i).state()
                phase.Fraction = sTLstream.Phase(i).fraction()
                phase.MolecularWeight = sTLstream.Phase(i).molarWeight()
                phase.Density = sTLstream.Phase(i).density()

        
                #unnecessary below commented        
                #IsobaricSpecificHeatCp = sTLstream.Phase(i).specificHeatCapacity() * ScientificConstants.SIConversion_JouletoKJoule
                phase.IsobaricSpecificHeatCp = sTLstream.Phase(i).molarHeatCapacity() / sTLstream.Phase(i).molarWeight()   #Cp

                #IsochoricHeatCapacityCv = sTLstream.Phase(i).specificIsochoricHeatCapacity() * ScientificConstants.SIConversion_JouletoKJoule
                phase.IsochoricHeatCapacityCv = sTLstream.Phase(i).molarIsochoricHeatCapacity() / sTLstream.Phase(i).molarWeight()  #Cv

                #SpecificHeatRatio = sTLstream.Phase(i).heatCapacityRatio()
                phase.SpecificHeatRatio = sTLstream.Phase(i).molarHeatCapacity() / sTLstream.Phase(i).molarIsochoricHeatCapacity()   #k

                #Compressibility = sTLstream.Phase(i).z()
                phase.Compressibility = (sTLstream.P() * sTLstream.Phase(i).molarWeight()) / (sTLstream.Phase(i).density() * (ScientificConstants.RU * 1000) * sTLstream.T())  #Z

                #specificEnthalpy = sTLstream.Phase(i).specificEnthalpy() * ScientificConstants.SIConversion_JouletoKJoule
                phase.SpecificEnthalpy = (sTLstream.Phase(i).molarEnthalpy() / sTLstream.Phase(i).molarWeight()) + self.GasComposition.EnthalpyOffset

                #specificEntropy = sTLstream.Phase(i).specificEntropy() * ScientificConstants.SIConversion_JouletoKJoule
                phase.SpecificEntropy = (sTLstream.Phase(i).molarEntropy() / sTLstream.Phase(i).molarWeight()) + self.GasComposition.EntropyOffset
                phase.Viscosity = sTLstream.Phase(i).viscosity()
                self.phases.append(phase)   #changed 

        self.IdentifyLightandHeavyLiquid(self.phases)
        #self.IdentifyHydrates(self.phases)
        self.IdentifySurfaceTensions(sTLstream)
    
    
    #checked
    def IdentifyLightandHeavyLiquid(self, phases):
        liquidphases = []

        for phase in phases:
            if (phase.State == PhaseState.Vapour):
                self.Vapour = phase
            
            if (phase.State == PhaseState.Liquid):            
                liquidphases.append(phase)
            
        liquidphases.sort(key= lambda x: x.Density)

        if len(liquidphases) >= 1:
            self.Liquid = liquidphases[0]
        
        if len(liquidphases) >= 2:
            self.HeavyLiquid = liquidphases[1]
        
        if len(liquidphases) >= 3:
            self.HeavyLiquid2 = liquidphases[2]
            
            
    #checked
    def IdentifySurfaceTensions(self, sTLstream):
        
        if self.Vapour.IsStateKnown():
            if self.Vapour != None:
                if self.Liquid != None:
                    if self.Liquid.IsStateKnown():
                        twophase = sTLstream.Phase(self.Liquid.StlStreamPhaseArrayIndex).andPhase(self.Vapour.StlStreamPhaseArrayIndex)
                        self.Liquid.SurfaceTension = twophase.interfaceTension()
                if self.HeavyLiquid != None:
                    if self.HeavyLiquid.IsStateKnown():
                        twophase = sTLstream.Phase(self.HeavyLiquid.StlStreamPhaseArrayIndex).andPhase(self.Vapour.StlStreamPhaseArrayIndex)
                        self.HeavyLiquid.SurfaceTension = twophase.interfaceTension()

        
    #checked
    def ProcessStreamEnthalpyEntropyData(self, sTLstream):
        
        self.specificEnthalpy = sTLstream.specificEnthalpy() * ScientificConstants.SIConversion_JouletoKJoule + self.GasComposition.EnthalpyOffset
        self.specificEntropy = sTLstream.specificEntropy() * ScientificConstants.SIConversion_JouletoKJoule + self.GasComposition.EntropyOffset

        self.molarEnthalpy = sTLstream.molarEnthalpy()
        self.molarEntropy = sTLstream.molarEntropy()
    
    
    #checked
    def GetTotalMolecularWeight(self, sTLstream):
        
        self.totalMolecularWeight = sTLstream.molarWeight()
        self.MwCalc = self.totalMolecularWeight            
    
    
    #checked
    def GetTotalDensitys(self, sTLstream):
        self.totalDensity = sTLstream.density()     
    
    
    #checked
    def SetGasPropertiesWhenNoCalculationWillBePerformed(self, gasData):
        if self.Vapour == None:
            self.Vapour = PhaseOfMatter()    

        if gasData.Mw != 0.0:
            self.Vapour.MolecularWeight = gasData.Mw
            self.totalMolecularWeight = gasData.Mw

        if gasData.K != 0.0:
            self.Vapour.SpecificHeatRatio = gasData.K

        if gasData.Z != 0.0:
            self.Vapour.Compressibility = gasData.Z

        if gasData.VapourDensity != 0.0:
            self.Vapour.Density = gasData.VapourDensity

        if gasData.VapourViscosity != 0.0:
            self.Vapour.Viscosity = gasData.VapourViscosity
            

    #checked
    def InitialiseShellThermoLibWrapper(self):
        
        phase = Phases.VLL
        model = self.FindShellThermoLibModel(self.GasComposition.EquationofStateModel)            
        self.InitialiseShellThermoLib(model, phase)


    #checked
    def InitialiseShellThermoLib(self, model, phase):
        
        if self.shellThermoLibWrapper == None or self.selectedSTLModel != model or self.selectedSTLphases != phase:
            
            self.selectedSTLphases = phase
            self.selectedSTLModel = model
            self.logger.debug(f"Init STL with Model {self.selectedSTLModel}, Phases {self.selectedSTLphases}")
            self.shellThermoLibWrapper = SCShellThermoLib(model, phase)
        else:       
            self.logger.debug(f"Init STL not needed because already available, Model {self.selectedSTLModel}, Phases {self.selectedSTLphases}")

    
    #checked
    def PopulateShellThermoLibWithGasComposition(self, gasData):
        self.logger.debug("Filling composition..")

        if self.shellThermoLibWrapper != None:
            self.GasComposition.CalculateAbsoluteMoleSum()

            for item in gasData.Components:
                self.shellThermoLibWrapper.Composition(item.MfdCode, item.Value)
                            
        
    

         
    
