resource "aws_s3_bucket" "test" {
  bucket = "public-bucket-test-ai"
  acl    = "public-read"
}
