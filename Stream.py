from Phase import Phase

class Stream:
    
    def __init__(self, stream, components):
        
        self._T = stream.T()
        self._p = stream.P()
        self._numberOfPhasesPossible = int(stream.numberOfPhasesPossible())
        self._numberOfComponents = int(stream.numberOfComponents())
        self._numberOfPhasesPresent = int(stream.numberOfPhasesPresent())
        self._amount = stream.amount()
        
        self._componentAmount = {components[c]: stream.componentAmount(c) for c in range(self._numberOfComponents)}
        self._componentFraction = {components[c]: stream.componentFraction(c) for c in range(self._numberOfComponents)}
        
        self._mass = stream.mass()
        self._volume = stream.volume()
        self._enthalpy = stream.enthalpy()
        self._entropy = stream.entropy()
        self._gibbs = stream.gibbs()
        self._molarWeight = stream.molarWeight()
        self._molarVolume = stream.molarVolume()
        self._density = stream.density()
        self._molarEnthalpy = stream.molarEnthalpy()
        self._molarEntropy = stream.molarEntropy()
        self._molarGibbs = stream.molarGibbs()
        self._specificEnthalpy = stream.specificEnthalpy()
        self._specificEntropy = stream.specificEntropy()
        self._specificGibbs = stream.specificGibbs()
        
        self._phases = []
        for p in range(self._numberOfPhasesPossible):
            if stream.isPhasePresent(p):
                self._phases.append(Phase(stream.phase(p), components, self._numberOfPhasesPossible))

    def T(self):
        return self._T

    def P(self):
        return self._p
    
    def numberOfPhasesPossible(self):
        return self._numberOfPhasesPossible

    def numberOfPhasesPresent(self):
        return self._numberOfPhasesPresent

    def molarWeight(self):
        return self._molarWeight

    def density(self):
        return self._density

    def molarEnthalpy(self):
        return self._molarEnthalpy

    def molarEntropy(self):
        return self._molarEntropy

    def specificEnthalpy(self):
        return self._specificEnthalpy

    def specificEntropy(self):
        return self._specificEntropy

    def isPhasePresent(self, phaseIndex):
        return phaseIndex < len(self._phases)

    def Phase(self, phaseIndex):
        if not self.isPhasePresent(phaseIndex):
            raise PhaseNotPresentException(f"Phase {phaseIndex} requested, but it wasn't present.")
        return self._phases[phaseIndex]

class PhaseNotPresentException(Exception):
    def PhaseNotPresentException(self, message):
        raise Exception(message)