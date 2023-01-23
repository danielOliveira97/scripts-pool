import boto3
import pandas as pd
import pyarrow as pa

# Connect to S3
s3 = boto3.client('s3')

# Get the list of text files in the S3 bucket
result = s3.list_objects(Bucket='my-bucket')
text_files = [content['Key'] for content in result.get('Contents', []) if content['Key'].endswith('.txt')]

# Iterate through the text files
for text_file in text_files:
    # Read the text file as a pandas DataFrame
    obj = s3.get_object(Bucket='my-bucket', Key=text_file)
    df = pd.read_csv(obj['Body'])
    
    # Convert the DataFrame to Parquet
    table = pa.Table.from_pandas(df)
    pq = pa.RecordBatchFileWriter('s3://my-bucket/'+text_file.replace('.txt', '.parquet'), table.schema)
    pq.write(table)
    pq.close()
    # Delete the original text file
    s3.delete_object(Bucket='my-bucket', Key=text_file)

