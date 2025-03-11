output "main_api_bucket_arn" {
  description = "ARN of the Main API S3 bucket"
  value       = aws_s3_bucket.main_api_bucket.arn
}

output "auxiliary_bucket_arn" {
  description = "ARN of the Auxiliary Service S3 bucket"
  value       = aws_s3_bucket.auxiliary_bucket.arn
}

output "main_api_param_arn" {
  description = "ARN of the Main API Parameter Store parameter"
  value       = aws_ssm_parameter.main_api_param.arn
}

output "auxiliary_param_arn" {
  description = "ARN of the Auxiliary Service Parameter Store parameter"
  value       = aws_ssm_parameter.auxiliary_param.arn
}

output "s3_access_policy_arn" {
  description = "ARN of the S3 access IAM policy"
  value       = aws_iam_policy.s3_access_policy.arn
}

output "ssm_access_policy_arn" {
  description = "ARN of the SSM access IAM policy"
  value       = aws_iam_policy.ssm_access_policy.arn
}