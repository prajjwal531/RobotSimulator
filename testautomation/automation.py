import  boto3
client = boto3.client('cloudformation')
s3 = boto3.resource('s3')
import requests, sys

def get_api_bucket_name():

    response = client.describe_stacks(
        StackName=sys.argv[1]
    )
    for output in response['Stacks'][0]['Outputs']:
        if (output['OutputKey'] == "S3Bucket"):
            bucketname = output['OutputValue']
        else:
            apiurl = output['OutputValue']
    return bucketname, apiurl

def test_robot():
    bucketName, apiurl = get_api_bucket_name()
    s3.meta.client.upload_file('instruction.txt', bucketName, 'instruction.txt')
    response = requests.get(apiurl)
    response_data = response.json()
    if (response_data['x'] == 3 and response_data['y'] == 3 and response_data['direction'] == "NORTH"):
        print ("===== Robot is working as expected =======")
    else:
        print ("==== there is some error while robot operation =====")
        sys.exit(1)

test_robot()

