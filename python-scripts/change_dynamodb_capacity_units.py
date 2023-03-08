import boto3

# Set up Boto3 client for DynamoDB in the desired region
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Get a list of all table names in the region
table_list = dynamodb.list_tables()['TableNames']

# Loop through each table and update the provisioned capacity units
for table_name in table_list:
    # Get the current provisioned capacity units for the table
    current_provisioning = dynamodb.describe_table(TableName=table_name)['Table']['ProvisionedThroughput']
    current_read_capacity = current_provisioning['ReadCapacityUnits']
    current_write_capacity = current_provisioning['WriteCapacityUnits']
    
    # Calculate the desired new provisioned capacity units
    new_read_capacity = current_read_capacity * 2
    new_write_capacity = current_write_capacity * 2
    
    # Update the provisioned capacity units for the table
    dynamodb.update_table(
        TableName=table_name,
        ProvisionedThroughput={
            'ReadCapacityUnits': new_read_capacity,
            'WriteCapacityUnits': new_write_capacity
        }
    )
    
    print(f"Updated provisioned capacity units for table '{table_name}' to {new_read_capacity} read capacity units and {new_write_capacity} write capacity units")
