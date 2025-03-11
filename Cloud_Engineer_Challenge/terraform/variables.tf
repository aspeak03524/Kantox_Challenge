variable "aws_region" {
  description = "AWS region"
  default     = "eu-south-2" # Change to your preferred region
}

variable "main_api_bucket_name" {
  description = "Name of the S3 bucket for the Main API"
  default     = "main-api-bucket-andrew" # Replace with a unique name
}

variable "auxiliary_bucket_name" {
  description = "Name of the S3 bucket for the Auxiliary Service"
  default     = "auxiliary-bucket-andrew" # Replace with a unique name
}

variable "main_api_param_name" {
  description = "Name of the Parameter Store parameter for the Main API"
  default     = "main-api-param"
}

variable "main_api_param_value" {
  description = "Value of the Parameter Store parameter for the Main API"
  default     = "Main API Parameter Value"
}

variable "auxiliary_param_name" {
  description = "Name of the Parameter Store parameter for the Auxiliary Service"
  default     = "auxiliary-param"
}

variable "auxiliary_param_value" {
  description = "Value of the Parameter Store parameter for the Auxiliary Service"
  default     = "Auxiliary Parameter Value"
}

variable "node_role_name" {
  description = "Name of the IAM role attached to the EC2 worker nodes or relevant service"
  default     = "eks-nodegroup-role-andrew" # Ensure this default value is correct.
}