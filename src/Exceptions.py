import sys
import logging
def error_handling(error,error_detail:sys):
    _,_,execut_tb=error_detail.exc_info()
    file_name=execut_tb.tb_frame.f_code.co_filename
    error_massage="Error are in file name [{0}] line numer [{1} error massage [{2}]]".format(
        file_name, execut_tb.tb_lineno,str(error))
    return error_massage

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_handling(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
""" 
if __name__=="__main__":
     try:
       a=1/0
     except Exception as ex: 
       logging.info("devision by zero")
       raise CustomException(ex,sys)
       """