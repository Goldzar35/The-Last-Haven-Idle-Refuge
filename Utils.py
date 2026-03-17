import sys
import os


def resource_path(relative_path):
    '''Return the correct path to a resource, whether running from source or as a PyInstaller bundle'''
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
