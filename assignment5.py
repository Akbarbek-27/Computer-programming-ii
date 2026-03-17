# A web application needs a flexible form validation system. 
# Some validators follow a strict abstract contract, while one custom validator works through duck typing alone.

# Create an abstract base class Validator that accepts and stores name. 
# Define an abstract method validate(self, value) that should return True or False. 
# Add a regular method check(self, value) that calls self.validate(value), determines the status string "PASS" or "FAIL", prints "[<status>] <name>: <value>", and returns the boolean.
# Create a subclass LengthValidator(Validator) that accepts min_len and max_len, sets its name to "Length(<min_len>-<max_len>)". 
# Its validate returns True if min_len <= len(value) <= max_len.
# Create a subclass ContainsDigitValidator(Validator) with name "ContainsDigit". 
# Its validate returns True if the value contains at least one digit.
# Create a subclass NoSpacesValidator(Validator) with name "NoSpaces". 
# Its validate returns True if the value contains no spaces.
# Create a class StartsWithUpperValidator (not inheriting from Validator) with name set to "StartsWithUpper". 
# It has validate(self, value) that returns True if the value is non-empty and starts with an uppercase letter, and check(self, value) that prints the same format as Validator.
# check and returns the boolean.
# Create a class ValidationReport that stores a list of entries. 
# It has add(self, validator_name, value, passed) that appends a tuple (validator_name, value, passed), and summary(self) that counts total, passed, and failed, then prints "Total: <total>, Passed: <passed>, Failed: <failed>".
# Create a class FormField that accepts field_name and holds a list of validators and a ValidationReport (composition). 
# It has add_validator(self, validator), validate(self, value) (prints 'Validating <field_name>: "<value>"', runs each validator’s check method, adds each outcome to the report, and returns True only if all validators passed), and show_report(self) (prints "--- Report for <field_name> ---" then calls the report’s summary method).
# For all methods: save the return value in a variable called `result` before returning it

from abc import ABC,abstractmethod
class Validator(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def validate(self,value):
        pass
    def check(self,value):
        if self.validate(value):
            status = "PASS"
        else:
            status = "FAIL"
        print(f"[{status}] {self.name}: {value}")
        result = self.validate(value)
        return result
class LengthValidator(Validator):
    def __init__(self, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len
        super().__init__(f"Length({min_len}-{max_len})")
    def validate(self, value):
        result = self.min_len <= len(value) <= self.max_len
        return result
class ContainsDigitValidator(Validator):
    def __init__(self,name="ContainsDigit"):
        super().__init__(name)
    def validate(self, value):
        digits = set("0123456789")
        result = bool(set(value) & digits)
        return result
class NoSpacesValidator(Validator):
    def __init__(self, name="NoSpaces"):
        self.name = name
    def validate(self, value):
        result = (" ") not in value 
        return result
class StartsWithUpperValidator:
    def __init__(self,name="StartsWithUpper"):
        self.name = name
    def validate(self, value):
        result = bool(value) and value[0].isupper()
        return result
    def check(self, value):
        if self.validate(value):
            status = "PASS"
        else:
            status = "FAIL"
        print(f"[{status}] {self.name}: {value}")
        result = self.validate(value)
        return result
class ValidationReport:
    def __init__(self):
        self.list_of_entries = []
    def add(self, validator_name, value, passed):
        self.list_of_entries.append((validator_name, value, passed))
    def summary(self):
        total = len(self.list_of_entries)
        passed = 0
        for entry in self.list_of_entries:
            if entry[2] == True: 
                passed += 1
        failed = total - passed
        print(f"Total: {total}, Passed: {passed}, Failed: {failed}")
class FormField:
    def __init__(self, field_name):
        self.field_name = field_name
        self.validators = []
        self.report = ValidationReport()
    def add_validator(self, validator):
        self.validators.append(validator)
    def validate(self, value):
        print(f'Validating {self.field_name}: "{value}"')
        total_passed = True
        for validator in self.validators:
            passed = validator.check(value)
            self.report.add(validator.name,value,passed)
            if not passed:
                total_passed = False
        result = total_passed
        return result
    def show_report(self):
        print(f"--- Report for {self.field_name} ---")
        self.report.summary()
username_field = FormField('username')
username_field.add_validator(LengthValidator(3, 15))
username_field.add_validator(NoSpacesValidator())
username_field.add_validator(ContainsDigitValidator())
username_field.add_validator(StartsWithUpperValidator())

valid1 = username_field.validate('Admin1')
print(f'Valid: {valid1}')
print()

valid2 = username_field.validate('no')
print(f'Valid: {valid2}')
print()

valid3 = username_field.validate('has space')
print(f'Valid: {valid3}')
print()

username_field.show_report()

try:
    v = Validator('test')
except TypeError:
    print('Cannot instantiate abstract class')