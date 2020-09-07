"""
Tutorial here: https://blog.ipswitch.com/how-to-create-an-ec2-instance-with-python
Getting started:
pip3 install awscli boto3 <-- installs the AWS command line interface and boto3
Create a user with programmatic access in the AWS console
Do aws configure to run the configuration tool so you can log in
To check that your configuration has worked, you can run "aws ec2 describe-instances"
"""

import boto3

ec2 = boto.resource("ec2")

"""
If you'd like to make a key pair so that you can SSH into the instance later,
you'd do it here. Instructions are in the above tutorial.

For this to work, you need to know the AMI ID of the os you'd like the instance to run on
This can be gained by doing describe-instances on an already existing instance,
or by looking on the AWS console when you launch an instance from there.

Now we can create a new instance.
"""
def lambda_handler(event, context):

    ec2.create_instance(
        # Tell the program which OS we'd like to use
        ImageId = "ami-04137ed1a354f54c4",
        # Tell the program what the minimum amount of instances we'd like to have is
        MinCount = 1,
        # Tell the program what the maximum amount of instances we'd like to have is
        MaxCount = 2,
        # Tell the program what type of instance we'd like to run
        InstanceType = "t2.micro",
        # If we'd made a key pair, we'd put it down here!
        # KeyName = "ec2-keypair",
        # Now to tell the program exactly where we want our instance(s) to be located!
        Placement = {"AvailabilityZone": "eu-west-1a"}
    )
    return {
        # Returns a status code of 200 so we know that the function has been successful.
        # This is not neccessary but is good for testing/debugging purposes.
        "statusCode": 200,
    }
