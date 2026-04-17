"""
create doctor not found exception
"""
class AppointmentNotFoundException(Exception):#appointment id not found
    """
    appointment not found exception
    """
    def __init__(self, message="appointment not found"):
        self.message = message
        super().__init__(self.message)
        