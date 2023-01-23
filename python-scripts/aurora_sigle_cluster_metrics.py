import boto3

# Connect to CloudWatch
cloudwatch = boto3.client('cloudwatch')

# Set the parameters for the metric
metric_name = 'WriteThroughput'
namespace = 'AWS/RDS'
dimensions = [{'Name': 'DBClusterIdentifier', 'Value': 'my-cluster-identifier'}]

# Get the write throughput metric
write_metric = cloudwatch.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'm1',
            'MetricStat': {
                'Metric': {
                    'Namespace': namespace,
                    'MetricName': metric_name,
                    'Dimensions': dimensions
                },
                'ReturnData': True
            },
            'ReturnData': True
        }
    ]
)

# Print the write throughput metric
print("Write Throughput: ", write_metric['MetricDataResults'][0]['Values'][0])

# Set the parameters for the read metric
metric_name = 'ReadThroughput'

# Get the read throughput metric
read_metric = cloudwatch.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'm1',
            'MetricStat': {
                'Metric': {
                    'Namespace': namespace,
                    'MetricName': metric_name,
                    'Dimensions': dimensions
                },
                'ReturnData': True
            },
            'ReturnData': True
        }
    ]
)

# Print the read throughput metric
print("Read Throughput: ", read_metric['MetricDataResults'][0]['Values'][0])
