# This is my version of Pandas
# Author: Sandeep Ghosh
import  numpy as np

__version__ = '0.0.1'

class DataFrame: # Description of this class below.

    """
    Whenever the user is going to construct a dataframe, 
    they are going to pass a single parameter.
    We are going to enforce the fact that it is a 
    dictionary of strings mapped 1-D numpy array.
    We will also have to check whether all the array lengths 
    are same or not. Also we need to convert any unicode characters
    into objects.

    """
    def __init__(self,data): # Initialize upon object creation
        
        # Check for correct input types
        self._check_input_types(data)

        # Check for equal array lengths
        self._check_array_lengths(data)

        # Convert unicode arrays to object
        self._data = self._convert_unicode_to_object(data)

        # Allow for special methods for strings
        #self.str = StringMethods(self)
        #self._add_docs()

    # Checking that the input data is infact a dictionary
    # The strings will eventually be our column names
    def _check_input_types(self,data): # Single _ : Private method
                                       # Only meant to be accessed internally 
                                       # by this class only
        
        if not isinstance(data, dict):
            raise TypeError('`Data` must be a dictionary ')
        for key,values in data.items():
            if not isinstance(key,str):
                raise TypeError('Keys of `data` must be string')
            if not isinstance(values,np.ndarray):
                raise TypeError('Values of `data` must be numpy array')
            if values.ndim != 1:
                raise ValueError('Value must be 1-D')
            
    #...........STEP-1 Complete..........................

    def _check_array_lengths(self,data): # Checking if all the arrays
                                         # in dictionary is of the same length.
                                         # Data Frames have to have same no. of elements 
                                         # in each columns
        for i, value in enumerate(data.values()):
            if i == 0: # 0th position
                length = len(value) # Length of the first array
            elif length != len(value):
                raise ValueError('All arrays must be of the same length')   

    #...........STEP-2 Complete..........................        
                                         
    def _convert_unicode_to_object(self,data):
        new_data = {}
        for key, value in data.items():
            if value.dtype.kind == 'U':
                new_data[key] = value.astype('object')
            else:
                new_data[key] = value
        return new_data

    #...........STEP-3 Complete..........................

    def __len__(self):
        pass


    #print('Testing the init method')



    ##...........................................##

