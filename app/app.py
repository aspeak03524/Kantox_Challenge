import os
from flask import Flask, jsonify
import requests
import boto3

app = Flask(__name__)

AUX_SERVICE_HOST = os.environ.get('AUX_SERVICE_HOST', 'http://127.0.0.1:4000')  
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

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        aux_response = requests.get(f'{AUX_SERVICE_HOST}/aux_data')
        aux_data = aux_response.json()

        # Example: Read from main bucket
        main_data = read_from_s3(MAIN_BUCKET, 'main-data.txt') 
        if main_data:
            print(f"Data from main bucket: {main_data}")

        # Example: Write to auxiliary bucket
        write_to_s3(AUX_BUCKET, 'api-data.txt', str(aux_data)) 

        data = {'message': 'Hello from the Main API!', 'aux_data': aux_data, 'main_s3_data': main_data}
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        return jsonify({'error': f"S3 Error: {str(e)}"}), 500

if __name__ == '__main__':
    print("AWS_ROLE_ARN: " + os.environ.get("AWS_ROLE_ARN", "Not Set"))
    print("AWS_WEB_IDENTITY_TOKEN_FILE: " + os.environ.get("AWS_WEB_IDENTITY_TOKEN_FILE", "Not Set"))
    app.run(host='0.0.0.0', port=3000, debug=True)
