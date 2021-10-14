## Robot Simulator

This solution is developed using Python. This solution is developed using SAM ( Serverless Application Model).
robotSimulator contains main source for robot.

Assumptions: 

1. Currently robot will process one movement only. Multiple movements are not supported at this moment.

Note: Currently Robot reads instructions from a text file, stored on S3 ( Assuming a streaming function will dump that file on S3)

###robotSimulator:
1. CommandParsor.py - This module is the starting point where all commands will be refined and made available to use.
2. Robot.py        - This is the main brain of robot responsible for movement.
###tests:
1. testsimulator.py - unit tests are used to test the robot functionality
###testautomation:
1. automation.py - this file is used to perform integration testing after robot is deployed on AWS. This module will use 
instruction.txt as baseline to test against deployed robot.

Template.yml - This is the SAM template that deploys the robot. As a result an API backed by lambda function will be created.

CodePipeline.yml - This template is used to deploy CodePipeline for CI/CD.

###Usage:

Note: Please ensure aws cli is installed and AWS credentails are created and have required permissions to create these resources.

Unit Test:

python -m unittest tests/testsimulator.py

###Deploy From Local:

sam deploy --no-confirm-changeset --no-fail-on-empty-changeset --stack-name <"StackName"> --s3-bucket <"Bucket for Sam to upload artifact">  --capabilities CAPABILITY_IAM

Run Automated testing:

cd testautomation

python automation.py <StackName>


###CI/CD

1. Deploy codePipeline.yml Cloudformation template. ( Please provide required input or lave them default)
2. A codecommit repository has been created, push the whole source code in the repository.
3. Monitor the CodePipeline and it will deploy resources automatically.

You can test the robot on the url provided by APIGateway. ( Please look for SAM output )