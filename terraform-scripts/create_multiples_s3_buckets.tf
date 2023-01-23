variable "bucket_list" {
  type = list(object({
    name = string,
    acl  = string
  }))
  default = [
    {
      name = "example-bucket-1",
      acl  = "private"
    },
    {
      name = "example-bucket-2",
      acl  = "private"
    },
    {
      name = "example-bucket-3",
      acl  = "private"
    }
  ]
}

resource "aws_s3_bucket" "example" {
  count = length(var.bucket_list)
  for_each = var.bucket_list

  bucket = each.value.name
  acl    = each.value.acl
}