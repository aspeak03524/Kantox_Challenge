from flask import Flask, jsonify
import boto3
import os

app = Flask(__name__)

MAIN_BUCKET = 'main-api-bucket-andrew'  
AUX_BUCKET = 'auxiliary-bucket-andrew'  

s3 = boto3.client('s3')

def read_from_s3(bucket_name, object_key):
    try:
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        file_content = response['Body'].read().decode('utf-8')
        return file_content
    except Exception as e:
        print(f"Error reading from S3: {e}")
        return None

def write_to_s3(bucket_name, object_key, content):
    try:
        s3.put_object(Bucket=bucket_name, Key=object_key, Body=content.encode('utf-8'))
        print(f"Successfully wrote to S3: {bucket_name}/{object_key}")
    except Exception as e:
        print(f"Error writing to S3: {e}")

@app.route('/aux_data', methods=['GET'])
def aux_data():
    # Example: Read from auxiliary bucket
    aux_s3_data = read_from_s3(AUX_BUCKET, 'aux-data.txt')  # Replace with your object key
    if aux_s3_data:
        print(f"Data from auxiliary bucket: {aux_s3_data}")

    # Example: Write to main bucket
    write_to_s3(MAIN_BUCKET, 'aux-service-data.txt', 'Data from auxiliary service') # Replace with your object key

    return jsonify({'message': 'Data from auxiliary service', 'aux_s3_data': aux_s3_data})

if __name__ == '__main__':
    print("AWS_ROLE_ARN: " + os.environ.get("AWS_ROLE_ARN", "Not Set"))
    print("AWS_WEB_IDENTITY_TOKEN_FILE: " + os.environ.get("AWS_WEB_IDENTITY_TOKEN_FILE", "Not Set"))
    app.run(host='0.0.0.0', port=4000, debug=True)