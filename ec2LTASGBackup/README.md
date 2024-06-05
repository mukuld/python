# Automatically update Launch Template and Auto Scaling groups

Whenever a running EC2 instance is updated, it immediately deprecates the Launch Templates (LT) and the Autoscaling Group (ASG) associated with the LTs. The operations team would then need to manually update the LTs and the ASGs.

These set of functions eliminate the manual labor and automatically update take a backup of the running EC2 instance. The backup can be scheduled on a regular basis or can be triggered based on an event.

There scripts are orchestrated using Step Functions with a 10 minute wait to allow AMI creation. Choose the right wait period to suit your needs as an EC2 instance with a large volume might take longer time to complete.

There is an optional component where the AMI can be shared with another account. I had built it based on a customer requirement, but it is not mandatory. I have provided two step functions.

* stepFunctionOrchestrator.json --> This function only creates the image and updates the LT and ASG
* stepFunctionOrchestratorwithShare.json --> This function creates the image and shares it with another account and then updates the LT and ASG.

Choose the version that works for you.

Feel free to comment / fork as long as credit is maintained.