import boto3

# Set up Boto3 client for DynamoDB in the desired region
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Get a list of all table names in the region
table_list = dynamodb.list_tables()['TableNames']

# Loop through each table and update the provisioned capacity units
for table_name in table_list:
    # Get the billing mode for the table
    billing_mode = dynamodb.describe_table(TableName=table_name)['Table']['BillingModeSummary']['BillingMode']
    
    if billing_mode == 'PAY_PER_REQUEST':
        # Update the provisioned capacity units for the table
        dynamodb.update_table(
            TableName=table_name,
            BillingMode='PAY_PER_REQUEST'
        )
        
        print(f"Updated billing mode for table '{table_name}' to PAY_PER_REQUEST")
    else:
        print(f"Table '{table_name}' is already using billing mode {billing_mode}, skipping update")
