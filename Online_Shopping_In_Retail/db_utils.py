import yaml
import psycopg2
import pandas as pd
from sqlalchemy import create_engine


def read_db_credentials(file_path):
    
    with open(file_path, 'r') as f:
        creds = yaml.safe_load(f)
    return creds


class RDSDatabaseConnector:
    
    def __init__(self, creds_dict):
        
        self.creds_dict = creds_dict
    
    def init_db_engine(self):
        
        creds_dict = read_db_credentials(self.creds_dict)
        database_type = 'postgresql'
        dbapi = 'psycopg2'
        host = creds_dict['RDS_HOST']
        user = creds_dict['RDS_USER']
        password = creds_dict['RDS_PASSWORD']
        database = creds_dict['RDS_DATABASE']
        port = creds_dict['RDS_PORT']
        engine = create_engine(f'{database_type}+{dbapi}://{user}:{password}@{host}:{port}/{database}')
        engine.connect()
        
        return engine
    
    def read_rds_table(self, table_name):
        
        engine = self.init_db_engine()
        df = pd.read_sql_table(table_name, con=engine)
        
        return df

def save_table(df):
    df.to_csv('Online_Shopping_In_Retail/customer_activity.csv', index=False)

def read_csv_table(table_name):
    df = pd.read_csv(table_name)
    return df

if __name__ == '__main__':
    db_con = RDSDatabaseConnector("Online_Shopping_In_Retail/credentials.yaml")
    customer_activity_df = db_con.read_rds_table('customer_activity')
    save_table(customer_activity_df)
    