"""
patient not found exception
"""
class PatientNotFoundException(Exception):#patient id not found
    """
    patient not found exception
    """
    def __init__(self, message="patient not found"):
        self.message = message
        super().__init__(self.message)