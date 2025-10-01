import sys
import traceback
from typing import Optional


def build_error_message(error: Exception, sys_module=sys) -> str:
    """
    Create a detailed error message with file name, line number, and stack trace.
    """
    # Grab the current exception info (type, value, traceback)
    exc_type, exc_value, exc_tb = sys_module.exc_info()

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_no = exc_tb.tb_lineno
    else:
        # Fallbacks (shouldn’t happen when called inside except)
        file_name = "<unknown file>"
        line_no = -1

    # Optional: include a compact stack trace line
    trace = "".join(traceback.format_exception(exc_type, exc_value, exc_tb)).strip()

    return (
        f"Error occurred in script [{file_name}] at line [{line_no}]: {error}. "
        f"Traceback:\n{trace}"
    )


class CustomException(Exception):
    """
    A standardized exception that enriches the original error with filename/line info.
    """
    def __init__(self, error: Exception, sys_module=sys):
        message = build_error_message(error, sys_module=sys_module)
        super().__init__(message)         # properly call super
        self.error_message = message      # keep a copy if you want to print in __str__

    def __str__(self) -> str:
        return self.error_message
