from Enums import PhaseState

class Phase:
    
    def __init__(self, phase, components, numberOfPhasesPossible):
        
        self._index = int(phase.index())
        self._T = phase.T()
        self._P = phase.P()
        self._amount = phase.amount()
        self._fraction = phase.fraction()

        self._componentFraction = {}
        self._componentAmount = {}
        self._lnFugacityCoefficient = {}
        self._fugacityCoefficient = {}
        self._fugacity = {}
            
        for c in range(len(components)):
            self._componentFraction[components[c]] = phase.componentFraction(c)
            self._componentAmount[components[c]] = phase.componentAmount(c)
            self._lnFugacityCoefficient[components[c]] = phase.lnFugacityCoefficient(c)
            self._fugacityCoefficient[components[c]] = phase.fugacityCoefficient(c)
            self._fugacity[components[c]] = phase.fugacity(c)

        self._molarWeight = phase.molarWeight()
        self._molarVolume = phase.molarVolume()
        self._density = phase.density()
        self._volume = phase.volume()
        self._z = phase.z()
        self._mass = phase.mass()
        self._molarEnthalpy = phase.molarEnthalpy()
        self._molarEntropy = phase.molarEntropy()
        self._molarGibbs = phase.molarGibbs()
        self._molarHeatCapacity = phase.molarHeatCapacity()
        self._molarIsochoricHeatCapacity = phase.molarIsochoricHeatCapacity()
        self._enthalpy = phase.enthalpy()
        self._entropy = phase.entropy()
        self._gibbs = phase.gibbs()
        self._heatCapacity = phase.heatCapacity()
        self._isochoricHeatCapacity = phase.isochoricHeatCapacity()
        self._specificEnthalpy = phase.specificEnthalpy()
        self._specificEntropy = phase.specificEntropy()
        self._specificGibbs = phase.specificGibbs()
        self._specificHeatCapacity = phase.specificHeatCapacity()
        self._specificIsochoricHeatCapacity = phase.specificIsochoricHeatCapacity()
        self._heatCapacityRatio = phase.heatCapacityRatio()
        self._isothermalCompressibility = phase.isothermalCompressibility()
        self._isentropicCompressibility = phase.isentropicCompressibility()
        self._isochoricThermalPressureCoefficient = phase.isochoricThermalPressureCoefficient()
        self._isentropicThermalPressureCoefficient = phase.isentropicThermalPressureCoefficient()
        self._isobaricThermalExpansionCoefficient = phase.isobaricThermalExpansionCoefficient()
        self._jouleThomsonCoefficient = phase.jouleThomsonCoefficient()
        self._speedOfSound = phase.speedOfSound()
        self._viscosity = phase.viscosity()
        self._thermalConductivity = phase.thermalConductivity()

        if phase.state() == 1:
            self._state = PhaseState.Liquid
        elif phase.state() == 2:
            self._state = PhaseState.Solid
        elif phase.state() == 0:
            self._state = PhaseState.Vapour
        else:
            self._state = PhaseState.Unknown

        for p in range(numberOfPhasesPossible):
            try:
                tp = phase.andPhase(p)
                self._twophases.append(TwoPhase(p, components, tp))
            except:
                pass


    def state(self):
        return self._state

    def fraction(self):
        return self._fraction

    def molarWeight(self):
        return self._molarWeight

    def density(self):
        return self._density
    
    def z(self):
        return self._z

    def molarEnthalpy(self):
        return self._molarEnthalpy

    def molarEntropy(self):
        return self._molarEntropy

    def molarHeatCapacity(self):
        return self._molarHeatCapacity

    def molarIsochoricHeatCapacity(self):
        return self._molarIsochoricHeatCapacity

    def specificEnthalpy(self):
        return self._specificEnthalpy

    def specificEntropy(self):
        return self._specificEntropy

    def specificHeatCapacity(self):
        return self._specificHeatCapacity

    def specificIsochoricHeatCapacity(self):
        return self._specificIsochoricHeatCapacity

    def heatCapacityRatio(self):
        return self._heatCapacityRatio

    def viscosity(self):
        return self._viscosity



class TwoPhase:
    
    def __init__(self, index, components, twoPhase):
        
        self._index = index
        self._interfaceTension = twoPhase.interfaceTension()
        
        self._lnKfactor = {}
        self._Kfactor = {}
        
        for c in components: 
            self._lnKfactor[c] = twoPhase.lnKfactor(c)
            self._Kfactor[c] = twoPhase.Kfactor(c)
        
    
    def Index(self):
        return self._index
                 
    def interfaceTension(self):
        return self._interfaceTension
