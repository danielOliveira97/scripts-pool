locals {
  distribution_list = [
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
  origin {
    domain_name = local.distribution_list[0].origin_domain_name
    origin_id   = local.distribution_list[0].origin_id
    custom_origin_config {
      origin_path = local.distribution_list[0].origin_path
    }
  }

  enabled = true

  # other properties for the distribution
}

resource "aws_cloudfront_origin_group" "example" {
  count = length(local.distribution_list) - 1
  for_each = local.distribution_list[1:]

  origin_id = each.value.origin_id
  failover_criteria {
    status_codes = [404, 503]
  }
  members {
    origin_id = each.value.origin_id
    weight = 1
  }
  distribution_id = aws_cloudfront_distribution.example.id
}