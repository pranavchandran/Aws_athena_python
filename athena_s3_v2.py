# __Author__ = "Pranav Chandran"
# __Date__ = 19-06-2024
# __Time__ = 13:14
# __FileName__ = athena_connection_s3.py

import boto3
import os

# Initialize a session using your new credentials
session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name='us-east-1'  # e.g., 'us-east-1'
)


# Use the session to create an Athena client
client = session.client('athena')

# Example function to run an Athena query
def run_athena_query(query, database, output_location):
    try:
        response = client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={'Database': database},
            ResultConfiguration={'OutputLocation': output_location}
        )
        return response
    except Exception as e:
        print(f"Error running Athena query: {e}")
        return None

# Example usage
query = """SELECT * FROM "default"."s3_salaries" LIMIT 10;"""  # Use triple quotes for multi-line strings
database = "s3_analyze_salaries_db"
output_location = "s3://athenajenkinstestbucket/"

response = run_athena_query(query, database, output_location)
if response:
    print("Query executed successfully. Query execution ID:", response['QueryExecutionId'])
else:
    print("Query execution failed.")

