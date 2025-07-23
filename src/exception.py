#The code defines a custom exception handling system in Python to provide detailed debugging information, especially useful in larger projects or production systems.



import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    #sys.exc_info() (accessed here as error_detail.exc_info()) returns a tuple of three values concerning the current exception: (type, value, traceback).We are interested in the traceback object (exc_tb), which contains information about where the exception occurred in the code.
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))
    #file_name: The name of the Python script.exc_tb.tb_lineno: The line number in the script where the exception occurred.str(error): The string representation of the actual error message (e.g., "division by zero").
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

        def __str__(self):
            return self.error_message   
        #The primary purpose of __str__ is to provide a user-friendly, informal string representation of an object, suitable for display to end-users or for logging. It prioritizes readability and conciseness, often omitting internal details that are not relevant to the user.

        #It likens CustomException to a "SuperCar" inheriting from a "basic car" (Exception). The super().__init__(error_message) call is like telling the "basic car" part of your "SuperCar" its fundamental "color" (the initial error_message). This is crucial because:
        #It properly initializes the base Exception class with a default message.
        #This ensures your CustomException behaves correctly even when treated as a generic Exception (e.g., in a broad except Exception as e: block or when Python prints an unhandled exception), allowing that basic message to be displayed.