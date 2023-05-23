import pandas as pd

class DataFrameInfo:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def describe_columns(self):
        return self.dataframe.dtypes
    
    def extract_statistics(self):
        return self.dataframe.describe()
    
    def count_distinct_values(self):
        distinct_counts = {}
        for column in self.dataframe.select_dtypes(include='category'):
            distinct_counts[column] = self.dataframe[column].nunique()
        return distinct_counts
    
    def print_dataframe_shape(self):
        print(f"DataFrame shape: {self.dataframe.shape}")
    
    def count_null_values(self):
        null_counts = self.dataframe.isnull().sum()
        null_percentages = (null_counts / self.dataframe.shape[0]) * 100
        return pd.DataFrame({'Null Count': null_counts, 'Null Percentage': null_percentages}, 
                            columns=['Null Count', 'Null Percentage'])
