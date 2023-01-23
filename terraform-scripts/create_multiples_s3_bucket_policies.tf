locals {
  bucket_list = [
    {
      name = "example-bucket-1"
    },
    {
      name = "example-bucket-2"
    }
  ]
}

resource "aws_s3_bucket" "example" {
  count = length(local.bucket_list)
  for_each = local.bucket_list

  bucket = each.value.name
}

resource "template_file" "policy_template" {
  template = <<EOF
{
  "Version": "2012-10-17",
  "Id": "Policy1549475273933",
  "Statement": [
    {
      "Sid": "Stmt1549475272918",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::${var.bucket_name}/*"
    }
  ]
}
EOF
  vars {
    bucket_name = each.value.name
  }
}

resource "template_file" "example" {
  count = length(local.bucket_list)
  for_each = local.bucket_list

  template = template_file.policy_template.template
  vars {
    bucket_name = each.value.name
  }
}

resource "aws_s3_bucket_policy" "example" {
  count = length(local.bucket_list)
  for_each = local.bucket_list

  bucket = aws_s3_bucket.example[each.key].bucket
  policy = template_file.example[each.key].rendered
}
