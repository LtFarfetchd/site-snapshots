#!/usr/bin/env python3

from aws_cdk import core

from site_snapshots_aws.site_snapshots_aws_stack import SiteSnapshotsAwsStack


app = core.App()
SiteSnapshotsAwsStack(app, "site-snapshots-aws")

app.synth()
