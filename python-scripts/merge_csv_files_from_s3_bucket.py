import boto3
import pandas as pd

# Connect to S3
s3 = boto3.client('s3')

# Get the list of CSV files in the S3 bucket
result = s3.list_objects(Bucket='my-bucket')
csv_files = [content['Key'] for content in result.get('Contents', []) if content['Key'].endswith('.csv')]

# Read the first CSV file into a pandas DataFrame
obj = s3.get_object(Bucket='my-bucket', Key=csv_files[0])
df = pd.read_csv(obj['Body'])

# Iterate through the remaining CSV files
for csv_file in csv_files[1:]:
    # Read the next CSV file into a pandas DataFrame
    obj = s3.get_object(Bucket='my-bucket', Key=csv_file)
    next_df = pd.read_csv(obj['Body'])

    # Merge the next DataFrame into the first DataFrame
    df = pd.concat([df, next_df], axis=0)

# save the final dataframe to s3
df.to_csv('s3://my-bucket/merged_file.csv', index=False)
