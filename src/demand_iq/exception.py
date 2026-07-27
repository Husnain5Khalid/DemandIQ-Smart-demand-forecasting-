import sys


def error_message_detail(error, error_detail):
    """
    Create a detailed error message with file name and line number.
    """

    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    return (
        f"\nError occurred in Python script: [{file_name}]"
        f"\nLine Number: [{exc_tb.tb_lineno}]"
        f"\nError Message: [{str(error)}]"
    )


class DemandIQException(Exception):
    """
    Custom exception class for the Demand IQ project.
    """

    def __init__(self, error, error_detail):
        super().__init__(str(error))
        self.error_message = error_message_detail(
            error,
            error_detail
        )

    def __str__(self):
        return self.error_message