import sys
from src.logger import logging

def error_message_details(error: Exception, error_detail: sys.exc_info) -> str:
    """
    This function generates an error message with the following details:
    1. The name of the file where the error occurred
    2. The line number where the error occurred
    3. The error details

    Args:
        error (Exception): The error that occurred
        error_detail (sys.exc_info): The error details

    Returns:
        str: The error message with the error details
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in python script name [{file_name}] Line number [{exc_tb.tb_lineno}] Error detail [{error}]"
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: sys.exc_info) -> None:
        """
        Initialize the CustomException class.

        Args:
            error_message (str): The error message.
            error_detail (sys.exc_info): The error details.
        """
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail= error_detail)
    
    def __str__(self) -> str:
        return self.error_message