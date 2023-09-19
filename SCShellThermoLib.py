# import shellthermo
import Logger
from Enums import Models, Phases
from Stream import Stream

class SCShellThermoLib:

    def __init__(self, CalculationModel = Models.SMIRK , CalculationPhases = Phases.VLL):
        
        self._CalculationModel = CalculationModel
        self._CalculationPhases = CalculationPhases
        
        if self._CalculationPhases == Phases.Hydrates:
            self._CalculationModel = Models.CPA
        
        self.builder = None
        self.streamDef = None
        self.engine = None

        self._Components = {}

        self._ValidStreamDefinition = False
        self._ValidEngine = False  

        self.stream = None           
        self.scstream = None

        self.logger = Logger.logger
    
    
    def initShellThermoLib(self):
        try:
            if not self._ValidStreamDefinition:
                self._ValidEngine = False
        
                self.builder = shellthermo.EquilibriumSolverBuilder()   #instead of StreamDefinitionBuilder check
                ids = self.ComponentsList()
        
                self.streamDef = self.builder \
                    .withComponents(ids) \
                    .withModel(self._CalculationModel.value) \
                    .withPhases(self._CalculationPhases.value)\
                    .build()
                    
                self._ValidStreamDefinition = True
                self.engine = self.streamDef
                self._ValidEngine = True
                
        except Exception as ex: 
            self.logger.error(f"Received exception: {ex}")
            
        return self._ValidEngine

    
        
    def Composition(self, Component, Amount):
        
        if Component in self._Components.keys():
            if Amount > 0:
                self._Components[Component] = Amount
                self.logger.debug(f"Updated Composition Element '{Component}'. New value {Component}")
            else:
                del self._Components[Component]
                self.logger.debug(f"Composition Element '{Component}' removed from componets list.")
                
                self._ValidStreamDefinition = False
                self.logger.debug(f"ValidStreamDefinition set to '{self._ValidStreamDefinition}'")
        else:
            if Amount > 0:
                self._Components[Component] = Amount
                self.logger.debug(f"Added Composition Element '{Component}'. Value {Amount}")
                
                self._ValidStreamDefinition = False
                self.logger.debug(f"ValidStreamDefinition set to '{self._ValidStreamDefinition}'")


    def Isothermal(self, T, P):
        
        self.logger.debug("Enter Isothermal()")
        try:
            self.logger.debug("Call init Shell Shell Thermo lib.")
            self.initShellThermoLib()

            self.logger.debug("Get all components amounts.")
            z = self.ComponentsAmount()

            self.logger.debug("Perform calculation.")
            self.stream = self.engine.isothermal(T, P, z)

            self.logger.debug("Transform result to legacy objects.")
            self.scstream = self.ProcessCalculationResult(self.stream)

            self.logger.debug("Return legacy objects.")
            return self.scstream
        
        except Exception as ex:
            self.logger.error(f"Received unhandeled exception: {ex}")
            raise


    def Isentropic_T(self, P, TotalEntropy):
        
        self.logger.debug("Enter Isentropic_T()")
        try:
            self.logger.debug("Call init Shell Shell Thermo lib.")
            self.initShellThermoLib()

            self.logger.debug("Get all components amounts.")
            z = self.ComponentsAmount()

            self.logger.debug("Perform calculation.")
            self.stream = self.engine.isentropic_T(P, TotalEntropy, z)

            self.logger.debug("Transform result to legacy objects.")
            self.scstream = self.ProcessCalculationResult(self.stream)

            self.logger.debug("Return legacy objects.")
            return self.scstream
        
        except Exception as ex:
            self.logger.error(f"Received unhandeled exception: {ex}")
            raise


    def Isenthalpic_T(self, P, TotalEnthaply):
        
        self.logger.debug("Enter Isenthalpic_T()")
        try:
            self.logger.debug("Call init Shell Shell Thermo lib.")
            self.initShellThermoLib()

            self.logger.debug("Get all components amounts.")
            z = self.ComponentsAmount()

            self.logger.debug("Perform calculation.")
            self.stream = self.engine.isenthalpic_T(P, TotalEnthaply, z)

            self.logger.debug("Transform result to legacy objects.")
            self.scstream = self.ProcessCalculationResult(self.stream)

            self.logger.debug("Return legacy objects.")
            return self.scstream
        
        except Exception as ex:
            self.logger.error(f"Received unhandeled exception: {ex}")
            raise


    def fixedPhaseFraction_T(self, P, fraction, phaseIndex):
        
        self.logger.debug("Enter fixedPhaseFraction_T()")
        try:
            self.logger.debug("Call init Shell Shell Thermo lib.")     
            self.initShellThermoLib()

            self.logger.debug("Get all components amounts.")
            z = self.ComponentsAmount()

            self.logger.debug("Perform calculation.")
            self.stream = self.engine.fixedPhaseFraction_T(P, fraction, phaseIndex, z)

            self.logger.debug("Transform result to legacy objects.")
            self.scstream = self.ProcessCalculationResult(self.stream)

            self.logger.debug("Return legacy objects.")
            return self.scstream
        
        except Exception as ex:
            self.logger.error(f"Received unhandeled exception: {ex}")
            raise
    
    
    def ProcessCalculationResult(self, stream):
        scstream = Stream(stream, self.ComponentsList())
        return scstream


    def ComponentsList(self):
        return [key for key,value in sorted(self._Components.items()) if value > 0]
    
    
    def ComponentsAmount(self):
       return [value for key,value in sorted(self._Components.items()) if value > 0]
        
   
    @property
    def ValidStreamDefinition(self, ValidStreamDef):
        self._ValidStreamDefinition = ValidStreamDef
        if self._ValidStreamDefinition == False:
            self._ValidEngine = False
