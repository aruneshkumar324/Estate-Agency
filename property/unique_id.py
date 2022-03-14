from datetime import datetime as dt



def generate_unique_id():
    """ 21 length long unique id """
    unique_id = dt.now().strftime("%Y%m%w%d%H%M%S%f")
    return unique_id



