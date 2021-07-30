# weight-chart-alexa-skill
An Alexa Skill to Track and Chart a person's weight


# Setup Environment
- make sure to install requirements.txt in WeightChart/aws_resources (`pip install -r WeightChart/aws_resources/requirements.txt`)
- to prevent the Alexa Skill Id from being committed run the command `pre-commit install` after installing the requirements in requirements.txt

# Deployment
While it is possible to deploy the AWS resources without serverless, it would probably be a bit tedious. Additionally, the Infrastructure as Code pattern provided by the Serverless Framework is a useful mechanism for deployment and maintainability. These is the procedure for deploying with the Serverless Framework
- Ensure aws credential are setup with `aws-configure --profile aws-serverless`
- to deploy ensure you're in the `WeightChart/aws_resources/` directory, then run `serverless deploy --stage dev --region us-east-1 --aws-profile aws-serverless`
- you can change the stage name depending on the environment, it will default to `dev` if not provided though

# Required Tools
- [Python 3.8](https://www.python.org/)


# Recommended Tools
- [Visual Studio Code](https://code.visualstudio.com/)
	- [Alexa Skills Toolkit](https://marketplace.visualstudio.com/items?itemName=ask-toolkit.alexa-skills-kit-toolkit)
- [AWS CLI](https://aws.amazon.com/cli/)
- [Serverless Framework](https://www.serverless.com/)
	- [Serverless Python Requirements](https://www.serverless.com/plugins/serverless-python-requirements)
	