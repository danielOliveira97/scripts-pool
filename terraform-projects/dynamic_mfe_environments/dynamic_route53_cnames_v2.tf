locals {
  cname_list = [
    {
      name = "example-cname-1",
      cloudfront_distribution_id = "XXXXXXXXXXXX"
    },
    {
      name = "example-cname-2",
      cloudfront_distribution_id = "XXXXXXXXXXXX"
    }
  ]
}

resource "aws_route53_record" "example" {
  count = length(local.cname_list)
  for_each = local.cname_list

  name = "${each.value.name}.example.com"
  type = "A"
  zone_id = "ZXXXXXXXXXXXXX"
  alias {
    name = "dualstack.${each.value.cloudfront_distribution_id}.cloudfront.net."
    zone_
