#!/usr/bin/python3

import boto3

ec2_ob = boto3.resource('ec2')

print ("[ec2]")
for each_instance in ec2_ob.instances.all():
    ec2_instance = ec2_ob.Instance(each_instance.id)
    public_dns_name = ec2_instance.public_dns_name
    username = ""
    if(public_dns_name != ""):
        if (ec2_instance.platform == 'Ubuntu'):
            username = "ubuntu"
        elif (ec2_instance.platform == 'Red Hat'):
            username = "ec2-user"
        
        print(public_dns_name, " ansible_user=", username)