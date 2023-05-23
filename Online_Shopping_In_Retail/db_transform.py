import pandas as pd

class DataTransform:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def transform_column_types(self):
        self.dataframe['administrative_duration'] = self.dataframe['administrative_duration'].round(2).astype(float)
        
        columns_to_convert = ['month', 'operating_systems', 'browser', 'region', 'traffic_type', 'visitor_type']
        self.dataframe[columns_to_convert] = self.dataframe[columns_to_convert].astype('category')
        
        category_mapping = {'MACOS': 'MacOS'}
        self.dataframe['operating_systems'] = self.dataframe['operating_systems'].replace(category_mapping)
        
        return self.dataframe

