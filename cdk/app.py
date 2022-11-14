
#!/usr/bin/env python3

from aws_cdk import core

from cdk.vpc_base.vpc import CdkVpcStack
from cdk.pipeline.pipeline import CdkPipelineStack


class AwsEnvParity(core.App):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.stack_name = "yolo-application"
            self.base_module = CdkVpcStack(self, self.stack_name + "-base")
            self.pipeline_module = CdkPipelineStack(self, self.stack_name + "-pipeline", self.base_module.vpc)
            
if __name__ == '__main__':
    app = AwsEnvParity()
    app.synth()
