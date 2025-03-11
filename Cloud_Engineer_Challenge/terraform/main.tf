provider "aws" {
  region = var.aws_region
}

# S3 Buckets
resource "aws_s3_bucket" "main_api_bucket" {
  bucket = var.main_api_bucket_name # Use variable
}

resource "aws_s3_bucket" "auxiliary_bucket" {
  bucket = var.auxiliary_bucket_name # Use variable
}

# AWS Parameter Store Parameters
resource "aws_ssm_parameter" "main_api_param" {
  name  = "main-api-param"
  type  = "String"
  value = "Main API Parameter Value"
}

resource "aws_ssm_parameter" "auxiliary_param" {
  name  = "auxiliary-param"
  type  = "String"
  value = "Auxiliary Parameter Value"
}

# IAM Policies for S3 Access
resource "aws_iam_policy" "s3_access_policy" {
  name        = "s3-access-policy"
  description = "IAM policy to allow access to S3 buckets"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow",
        Action   = ["s3:*"],
        Resource = [aws_s3_bucket.main_api_bucket.arn, "${aws_s3_bucket.main_api_bucket.arn}/*", aws_s3_bucket.auxiliary_bucket.arn, "${aws_s3_bucket.auxiliary_bucket.arn}/*"]
      }
    ]
  })
}

# IAM Policies for Parameter Store Access
resource "aws_iam_policy" "ssm_access_policy" {
  name        = "ssm-access-policy"
  description = "IAM policy to allow access to Parameter Store parameters"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow",
        Action   = ["ssm:GetParameter", "ssm:GetParameters"],
        Resource = [aws_ssm_parameter.main_api_param.arn, aws_ssm_parameter.auxiliary_param.arn]
      }
    ]
  })
}

# Attach IAM Policies to Node Group Role (or other relevant role)
resource "aws_iam_role_policy_attachment" "s3_policy_attachment" {
  policy_arn = aws_iam_policy.s3_access_policy.arn
  role       = var.node_role_name # Ensure this variable holds the correct role name
}

resource "aws_iam_role_policy_attachment" "ssm_policy_attachment" {
  policy_arn = aws_iam_policy.ssm_access_policy.arn
  role       = var.node_role_name # Ensure this variable holds the correct role name
}

resource "aws_iam_role" "eks_nodegroup_role" {
  name = "eks-nodegroup-role-andrew"
  assume_role_policy = jsonencode({
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com" # Or eks.amazonaws.com, depending on your use case
      }
    }]
    Version = "2012-10-17"
  })
}