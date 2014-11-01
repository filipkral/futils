#!/usr/bin/python
"""Little helper functions for Python"""
import time

def getTimestampString(form='%Y%m%d%H%M'):
    """Return a string representing current GMT time on local machine in predefined format form, default is yyyymmddHHMM.
    See http://docs.python.org/2/library/time.html#time.strftime for details about time formatting.
    """
    return time.strftime(form, time.gmtime())
