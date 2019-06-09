import boto3
client = boto3.client('ec2')

resp = client.terminate_instances(InstanceIds=['i-0158ab7a03bb6a954'])

for instance in resp['TerminatingInstances']:
    print("The instance with id {} Terminated".format(instance['InstanceId']))

