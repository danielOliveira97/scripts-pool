locals {
  origin_list = [
    {
      origin_id = "example-origin-1",
      origin_path = "/example-origin-1",
      origin_domain_name = "example-origin-1.s3.amazonaws.com"
    },
    {
      origin_id = "example-origin-2",
      origin_path = "/example-origin-2",
      origin_domain_name = "example-origin-2.s3.amazonaws.com"
    }
  ]
}

resource "aws_cloudfront_distribution" "example" {
  enabled = true

  # other properties for the distribution
  
  origin {
    domain_name = local.origin_list[0].origin_domain_name
    origin_id   = local.origin_list[0].origin_id
    custom_origin_config {
      origin_path = local.origin_list[0].origin_path
    }
  }
  
  # use for_each to create origins
  origin {
    for_each = local.origin_list[1:]
    domain_name = each.value.origin_domain_name
    origin_id   = each.value.origin_id
    custom_origin_config {
      origin_path = each.value.origin_path
    }
  }
}