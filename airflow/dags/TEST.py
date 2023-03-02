# import boto3
# import csv
# import os
#
# import great_expectations_provider
# import pandas as pd
# import psycopg2
# from datetime import datetime, timedelta
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.operators.bash import BashOperator
# # from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
# from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
#
#
# goes_bucket = "noaa-goes18"
# nexrad_bucket = "noaa-nexrad-level2"
# des_bucket = "damg7245-ass1"
#
# # Define DAG arguments
# default_args = {
#     'owner': 'Charu Singh',
#     'depends_on_past': False,
#     'start_date': datetime(2023, 3, 1)
# }
# # aws_access_key_id = os.environ.get('AWS_ACCESS_KEY')
# # aws_secret_access_key = os.environ.get('AWS_SECRET_KEY')
#
# #
# # aws_access_key_id = 'AKIAVDK4IUCRNV5UP46G'
# # aws_secret_access_key = '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'
#
# # s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id=aws_access_key_id,
# #                   aws_secret_access_key=aws_secret_access_key)
#
#
# # def GOES_scrap_load():
# #     goes18_dict = {
# #         'id': [],
# #         'product': [],
# #         'year': [],
# #         'day': [],
# #         'hour': []
# #     }
# #     prefix = 'ABI-L1b-RadC/'
# #     delimiter = '/'
# #     id = 1
# #     result = s3.list_objects(Bucket=goes_bucket, Prefix=prefix, Delimiter='/')
# #     for o in result.get('CommonPrefixes'):
# #         path = o.get('Prefix').split('/')
# #         prefix_new = prefix + path[-2] + "/"
# #         sub_folder = s3.list_objects(
# #             Bucket=goes_bucket, Prefix=prefix_new, Delimiter=delimiter)
# #         if sub_folder is not None:  # Check if sub_folder is not None
# #             for p in sub_folder.get('CommonPrefixes'):
# #                 sub_path = p.get('Prefix').split('/')
# #                 prefix_new2 = prefix_new + sub_path[-2] + "/"
# #                 sub_sub_folder = s3.list_objects(
# #                     Bucket=goes_bucket, Prefix=prefix_new2, Delimiter=delimiter)
# #                 if sub_sub_folder is not None:
# #                     for q in sub_sub_folder.get('CommonPrefixes'):
# #                         sub_sub_path = q.get('Prefix').split('/')
# #                         sub_sub_path = sub_sub_path[:-1]
# #                         goes18_dict['id'].append(id)
# #                         goes18_dict['product'].append(sub_sub_path[0])
# #                         goes18_dict['year'].append(sub_sub_path[1])
# #                         goes18_dict['day'].append(sub_sub_path[2])
# #                         goes18_dict['hour'].append(sub_sub_path[3])
# #                         id += 1
# #
# #     df = pd.DataFrame(goes18_dict)
# #     print(df)
# #     # # Connect to PostgreSQL database
# #     # conn = psycopg2.connect(host="db", database="noaa", user="root", password="root")
# #     # cur = conn.cursor()
# #     #
# #     # # Create table for metadata
# #     # cur.execute('''CREATE TABLE IF NOT EXISTS metadata_goes18
# #     #             (id integer, product integer, year integer, day integer, hour integer)''')
# #     #
# #     # # insert the DataFrame into a new table named 'metadata_goes18'
# #     # for row in df.iterrows():
# #     #     cur.execute("INSERT INTO metadata_goes18 (id, product, year, day, hour) VALUES (%s, %s, %s, %s, %s)",
# #     #                 (row[0], row[1], row[2], row[3], row[4]))
# #     #
# #     # # Commit changes and close database connection
# #     # conn.commit()
# #     # conn.close()
# #
# #
# # def NEXRAD_scrap_load():
# #     NEXRAD_dict = {
# #         'id': [],
# #         'year': [],
# #         'month': [],
# #         'day': [],
# #         'station': []
# #     }
# #     years = ['2022', '2023']
# #     id = 1
# #     delimiter = '/'
# #
# #     for y in years:
# #         prefix = y + '/'
# #         result = s3.list_objects(Bucket=nexrad_bucket, Prefix=prefix, Delimiter='/')
# #         for o in result.get('CommonPrefixes'):
# #             path = o.get('Prefix').split('/')
# #             prefix_new = prefix + path[-2] + "/"
# #             sub_folder = s3.list_objects(Bucket=nexrad_bucket, Prefix=prefix_new, Delimiter='/')
# #             if sub_folder is not None:  # Check if sub_folder is not None
# #                 for p in sub_folder.get('CommonPrefixes'):
# #                     sub_path = p.get('Prefix').split('/')
# #                     prefix_new2 = prefix_new + sub_path[-2] + "/"
# #                     sub_sub_folder = s3.list_objects(Bucket=nexrad_bucket, Prefix=prefix_new2, Delimiter='/')
# #                     if sub_sub_folder is not None:
# #                         for q in sub_sub_folder.get('CommonPrefixes'):
# #                             sub_sub_path = q.get('Prefix').split('/')
# #                             sub_sub_path = sub_sub_path[:-1]
# #                             NEXRAD_dict['id'].append(id)
# #                             NEXRAD_dict['year'].append(sub_sub_path[0])
# #                             NEXRAD_dict['month'].append(sub_sub_path[1])
# #                             NEXRAD_dict['day'].append(sub_sub_path[2])
# #                             NEXRAD_dict['station'].append(sub_sub_path[3])
# #                             id += 1
# #
# #     df = pd.DataFrame(NEXRAD_dict)
# #     print(df)
#
#
# # GOES_scrap_load()
# # NEXRAD_scrap_load()
#
# help(great_expectations_provider.operators.great_expectations)