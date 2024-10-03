from src.exception import SensorException
from src.logger import logging
import sys
import os

def test_exception():
    try:
        logging.info("error will occured in this file ")
        a = 1/0
    except Exception as e:
       raise SensorException (e,sys)
        



if __name__ == "__main__":
    try:
        test_exception()  # Call the function with parentheses
    except SensorException as se:
        print(se)  # Print the detailed error message from the custom exception
    except Exception as e:
        print(e)  # This will catch any other exceptions not raised as SensorException