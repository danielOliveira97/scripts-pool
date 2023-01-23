locals {
  cname_list = [
    {
      name = "example-cname-1",
      domain_name = "example-cname-1.com"
    },
    {
      name = "example-cname-2",
      domain_name = "example-cname-2.com"
    }
  ]
}

resource "aws_route53_record" "example" {
  count = length(local.cname_list)
  for_each = local.cname_list

  name = "${each.value.name}.example.com"
  type = "CNAME"
  zone_id = "ZXXXXXXXXXXXXX"
  ttl = "300"
  records = [each.value.domain_name]
}
