from aws_cdk import (
    aws_s3 as s3,
    aws_lambda as lamb,
    core
)
import inspect

class SiteSnapshotsAwsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create an s3 bucket to store snapshots, if one doesn't already exist
        s3.Bucket(self, 'site-snapshots-bucket', bucket_name='site-snapshots-bucket')

        # retrieve the s3 bucket
        bucket = s3.Bucket.from_bucket_name(self, 'BucketByName', 'site-snapshots-bucket')

        