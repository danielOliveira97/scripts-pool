locals {
  cname_list = [
    {
      name = "example-cname-1",
      distribution_id = "EXAMPLEID1"
    },
    {
      name = "example-cname-2",
      distribution_id = "EXAMPLEID2"
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
  alias {
    name = aws_cloudfront_distribution.example[each.value.distribution_id].domain_name
   
