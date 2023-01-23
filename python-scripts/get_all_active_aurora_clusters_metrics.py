import boto3

# Connect to RDS
rds = boto3.client('rds')
# Connect to CloudWatch
cloudwatch = boto3.client('cloudwatch')

# Get the list of all active Aurora RDS clusters
clusters = rds.describe_db_clusters(Filters=[
    {
        'Name': 'engine',
        'Values': ['aurora']
    }
])['DBClusters']

metric_name = 'WriteThroughput'
namespace = 'AWS/RDS'

for cluster in clusters:
    dimensions = [{'Name': 'DBClusterIdentifier', 'Value': cluster['DBClusterIdentifier']}]

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
    print("Cluster: ", cluster['DBClusterIdentifier'])
    print("Write Throughput: ", write_metric['MetricDataResults'][0]['Values'][0])
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
    print("Read Throughput: ", read_metric['MetricDataResults'][0]['Values'][0])
    print("\n")
