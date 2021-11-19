import ioda_obs_space as ios
import pandas as pd

__all__ = ['IODA']

class IODA:

    def __init__(self, filepath, name=None):
        """
        IODA constructor
        
        Args:
            filepath: path to IODA file
            name: (optional) obs space string name
        """
        self.obsspace = ios.ObsSpace(filepath, mode='r', name=name)
        self.filepath = filepath
        self.name = name

    def get_var(self, vname, gname):
        """
        Grab specified variable from IODA ObsSpace
        
        Args:
            vname: string of variable name
            gname: string of group name
        """
        _var = self.obsspace.Variable(varname=vname, groupname=gname)
        data = _var.read_data()
        
        return data
    
#     def get_var_attr(self, vname, gname, attrname): 
#         """
#         Grab specified variable attribute from IODA ObsSpace
#         
#         Args:
#             vname: string of variable name
#             gname: string of group name
#             attrname: string of attribute name
#         """
#         _var = self.obsspace.Variable(varname=vname, groupname=gname)
#         
#         attr = _var.read_attr(attrname)
#         
#         return attr