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

    def __len__(self): # int: the number of rows in the dataframe
        
       # for loop process 
       for value in self._data.values():
           return len(value) 

    """
        (Another process)

        return len(self._data.values()[0])
        This is a dict view
        Doesn't allow indexing...so we can't use return(df[0])
        Error: 'dict_values' object does not support indexing
    """
    """
        (Yet another process)

        Create iterator
        Manually iterating
        return len(next(iter(self._data.values())))
        next()..very first iteration..very first numpy array
    
    """
    ##...........................................##

    @property # Python property decorator
              # Will transform what looks 
              # like a method into an attribute
    def columns(self): # Return columns as a list
        # Works only with Python 3.6+
        return list(self._data)
        # we are only getting the keys(col. names) not the values
        # chill !! 
        # Works this way when we iterate
       # Original
       
    @columns.setter
    def columns(self, columns): # Setting new column names
        if not isinstance(columns, list):
            raise TypeError('New columns must be a list')
        if len(columns) != len(self.columns):
            raise ValueError(f'New column names must be {len(self._data)}')
        else:
            for col in columns:
                if not isinstance(col, str):
                    raise TypeError('New column names must be strings')
        if len(columns) != len(set(columns)): # Sets have unique values
            raise ValueError('Columns names must be unique')

        new_data = dict(zip(columns, self._data.values()))
        self._data = new_data
        
    @property
    def shape(self): # two-item tuple of number of rows and columns
       return len(self), len(self._data) 
       #len(self._data) is similar to len(self.columns) 
       # We already did __len__ ... so we call that on self

    def _repr_html(self):

        """
        Used to create a string of HTML to nicely display the DataFrame
        in a Jupyter Notebook. Different string formatting is used for
        different data types.

        The structure of the HTML is as follows:
        <table>
            <thead>
                <tr>
                    <th>data</th>
                    ...
                    <th>data</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>{i}</strong></td>
                    <td>data</td>
                    ...
                    <td>data</td>
                </tr>
                ...
                <tr>
                    <td><strong>{i}</strong></td>
                    <td>data</td>
                    ...
                    <td>data</td>
                </tr>
            </tbody>
        </table>
        """

        html = '<table><thread><tr><th></th>'
        for col in self.columns:
            html += f"<th>{col:10}</th>"

        
        html += '</tr></thead>'
        html += "<tbody>"

        only_head = False
        num_head = 10
        num_tail = 10
        if len(self) <= 20:
            only_head = True
            num_head = len(self)

        for i in range(num_head):
            html += f'<tr><td><strong>{i}</strong></td>'
            for col, values in self._data.items():
                kind = values.dtype.kind
                if kind == 'f':
                    html += f'<td>{values[i]:10.3f}</td>'
                elif kind == 'b':
                    html += f'<td>{values[i]}</td>'
                elif kind == 'O':
                    v = values[i]
                    if v is None:
                        v = 'None'
                    html += f'<td>{v:10}</td>'
                else:
                    html += f'<td>{values[i]:10}</td>'
            html += '</tr>'

        if not only_head:
            html += '<tr><strong><td>...</td></strong>'
            for i in range(len(self.columns)):
                html += '<td>...</td>'
            html += '</tr>'
            for i in range(-num_tail, 0):
                html += f'<tr><td><strong>{len(self) + i}</strong></td>'
                for col, values in self._data.items():
                    kind = values.dtype.kind
                    if kind == 'f':
                        html += f'<td>{values[i]:10.3f}</td>'
                    elif kind == 'b':
                        html += f'<td>{values[i]}</td>'
                    elif kind == 'O':
                        v = values[i]
                        if v is None:
                            v = 'None'
                        html += f'<td>{v:10}</td>'
                    else:
                        html += f'<td>{values[i]:10}</td>'
                html += '</tr>'

        html += '</tbody></table>'
        return html




       
        
        

        




    ##...........................................##

