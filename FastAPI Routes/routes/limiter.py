from slowapi import Limiter 
from slowapi.util import get_remote_address # its a function that will retrive a client ip address

# create a limiter instance
limiter = Limiter(key_func=get_remote_address)
