import boto3
import os

amplify_client = boto3.client('amplify')

list_response = amplify_client.list_apps()
print("App id is: " + list_response['apps'][0]['appId'])

creation_response = amplify_client.create_backend_environment(
    appId=list_response['apps'][0]['appId'],
    environmentName='botoenva',
    stackName='botoenvaStack',
    deploymentArtifacts='botoenvaArtifacts'
)
