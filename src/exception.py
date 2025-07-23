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