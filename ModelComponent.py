from BaseEngine import *
from CCEDataContract import *
from Core.PI import *
from Core.PI.Settings import *
from SpecialMathFunctions import *
from Utilities.Strings import *


from Enums import ModelComponentType

    
class ModelComponent:

    def _initialize_instance_fields(self):
        self.Type = 0
        self.Presentation = None
        self.PiTag = None
        self.UnitOfMeasureCalculating = None
    def get_key_name(self):
        return self.Presentation.keyname

    def set_key_name(self, value):
        self.Presentation.keyname = value
        self.PiTag.KeyName = value
    def get_pi_tag_expression(self):
        return self.Presentation.pitagExpression

    def set_pi_tag_expression(self, value):
        self.Presentation.pitagExpression = value
        self.PiTag.set_expression(value)
        temp_out__ = OutObject()
        if not TryParseHelper.try_parse_float(value, temp_out__):
            _ = temp_out__.arg_value
            self.Presentation.expression = value
            self.PiTag.PiTagExpression = value #Need to remove this. Check once
        else:
            _ = temp_out__.arg_value
    #/ The current value of this component in Double format.
    def get_value_as_double(self):
        return self.Presentation.valueAsDouble

    def set_value_as_double(self, value):
        self.Presentation.valueAsDouble = value
        self.Presentation.value = str(value)

    def get_value_as_string(self):
        return self.Presentation.value

    def set_value_as_string(self, value):
        self.Presentation.value = value
        self.Presentation.valueAsDouble = 0.0

    def ValueAsFixedPointString(self):
        valueAsDouble = str(self.get_value_as_double())

        if StringHelper.IsNumeric(valueAsDouble):
            return self.get_value_as_double().ToString(CommonScMathClass.DetermineNumberOfDecimalPlacesToRoundTo(self.get_value_as_double()))

        return valueAsDouble

    def get_unit_of_measure(self):
        return self.Presentation.UOM

    def set_unit_of_measure(self, value):
        self.Presentation.UOM = value


    def get_description(self):
        return self.Presentation.comment

    def set_description(self, value):
        self.Presentation.comment = value
        self.PiTag.Description = value

    def is_value_set_in_model_file(self):
        return StringHelper.IsPopulated(self.Presentation.pitagExpression)

    def __init__(self):
        self._initialize_instance_fields()
        self._Initialise()

    def __init__(self, type, keyName):
        self._initialize_instance_fields()
        self()
        self.Type = type
        self.set_key_name(keyName)

    def __init__(self, type, keyName, description):
        self._initialize_instance_fields()
        self(type, keyName)
        self.set_description(description)

    def __init__(self, type, keyName, unitOfMeasure, description):
        self._initialize_instance_fields()
        self(type, keyName, description)
        self.set_unit_of_measure(unitOfMeasure)

    def __init__(self, type, keyName, unitOfMeasure, description, readMode):
        self._initialize_instance_fields()
        self(type, keyName, unitOfMeasure, description)
        self.PiTag.ReadMode = readMode

    def __init__(self, modelComponent):
        self._initialize_instance_fields()
        if modelComponent is not None:
            self.Type = modelComponent.Type
            self.PiTag = PiTag(modelComponent.PiTag)
            self.Presentation = Item(modelComponent.Presentation)
            self.UnitOfMeasureCalculating = modelComponent.UnitOfMeasureCalculating

    def InsertPiServerNameInTagExpression(self, hashTable):
        if self.Type == ModelComponentType.INPUT:
            if StringHelper.IsPopulated(hashTable.GetPiServerName()):
                self.Presentation.InsertInputPiServerName(hashTable.GetPiServerName())
        else:
            if StringHelper.IsPopulated(hashTable.GetPiServerName()):
                self.Presentation.InsertOutputPiServerName(hashTable.GetPiServerName())

    def _Initialise(self):
        self.Type = ModelComponentType.INPUT

        self.PiTag = PiTag()
        self.Presentation = Item()

        self.set_key_name(String.Empty)
        self.set_pi_tag_expression(String.Empty)
        self.set_value_as_double(0.0)
        self.set_unit_of_measure(String.Empty)
        self.UnitOfMeasureCalculating = String.Empty
