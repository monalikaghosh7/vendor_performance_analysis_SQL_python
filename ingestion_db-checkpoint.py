import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time
logging.basicConfig(
    filename= "logs/ingestion_db.log",
    level= logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)
engine= create_engine('sqlite:///inventory.db')
def ingest_db(df, table_name, engine, if_exists='replace'):
    df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)

def load_raw_data():
    '''Load large CSVs in chunks and ingest all records into db'''
    start = time.time()
    logging.info('Starting ingestion process...')

    for file in os.listdir('data'):
        if file.endswith('.csv'):
            file_path = os.path.join('data', file)
            table_name = file[:-4]
            logging.info(f"Processing {file} in chunks...")

            try:
                chunk_num = 0
                for chunk in pd.read_csv(
                    file_path,
                    chunksize=50000,              # reduce chunksize for large files
                    low_memory=False,
                    on_bad_lines='skip',          # skip malformed lines
                    encoding='utf-8'              # optional: adjust if needed
                ):
                    chunk_num += 1
                    ingest_db(chunk, table_name, engine, if_exists='append' if chunk_num > 1 else 'replace')
                    logging.info(f"Chunk {chunk_num} of {file} ingested. Rows: {len(chunk)}")
            except Exception as e:
                logging.error(f"Error processing file {file}: {e}")

    end = time.time()
    total_time = (end - start) / 60
    logging.info('Ingestion Complete')
    logging.info(f'Total Time Taken: {total_time:.2f} minutes')
    
if  __name__ == '__main__':
     load_raw_data()