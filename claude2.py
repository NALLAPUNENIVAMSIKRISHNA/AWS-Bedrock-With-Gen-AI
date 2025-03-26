import boto3
import json

prompt_data = """
Human: Act as a Shakespeare and write a poem on Generative AI.

Assistant:
"""
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1") # Added region

payload = {
    "prompt": prompt_data,
    "max_tokens_to_sample": 300,
    "temperature": 0.5,
    "top_k": 250,
    "top_p": 1,
    "stop_sequences": ["\n\nHuman:"], 
    "anthropic_version": "bedrock-2023-05-31"
}

body = json.dumps(payload)
model_id = "anthropic.claude-v2:1"

try: 
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )

    response_body = json.loads(response.get("body").read())
    response_text = response_body.get("completion")

    print(response_text)

except Exception as e:
    print(f"Error: {e}")