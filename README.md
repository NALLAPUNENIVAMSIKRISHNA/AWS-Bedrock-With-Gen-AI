# AWS Bedrock Integration With Generative AI

## Overview
This project demonstrates how to interact with AWS Bedrock to generate text using AI models like Anthropic's Claude v2 and Meta's Llama 3. The scripts use `boto3` to send prompts and retrieve responses from these models.

## Features
- Uses AWS Bedrock to generate AI-powered text responses.
- Supports multiple models I used(Claude v2 and Llama 3).
- Handles API requests and responses in JSON format.
- Implements error handling for robustness.

## Prerequisites
Before running the project, ensure you have:
- An AWS account with Bedrock access.
- AWS CLI configured with appropriate credentials.
- Python 3 installed.
- Required dependencies installed (see below).

## Installation
Clone the repository:
```bash
git clone https://github.com/your-repository/aws-bedrock-textgen.git
cd aws-bedrock-textgen
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
### Running the Claude v2 Model Script
```bash
python claude_textgen.py
```
This script:
1. Sends a Shakespearean poem request to Claude v2.
2. Parses and prints the AI-generated response.

### Running the Llama 3 Model Script
```bash
python llama3_textgen.py
```
This script:
1. Sends the same prompt to the Llama 3 model.
2. Retrieves and prints the AI-generated response.

## Project Structure
```
aws-bedrock-textgen/
│── claude_textgen.py  # Interacts with Claude v2
│── llama3_textgen.py   # Interacts with Llama 3
│── test.json          # Example API requests
│── requirements.txt   # Dependencies list
│── README.md          # Project documentation
```

## Configuration
Ensure your AWS credentials are configured:
```bash
aws configure
```
Enter your AWS Access Key ID, Secret Access Key, region, and output format.

## Dependencies
The project requires:
```
boto3
awscli
```
Install using:
```bash
pip install boto3 awscli
```

## Error Handling
If you encounter errors:
- Ensure AWS credentials are correctly set up.
- Verify Bedrock access permissions.
- Check for network connectivity issues.

