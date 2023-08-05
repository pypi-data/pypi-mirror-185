# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetKnowledgeBaseResult',
    'AwaitableGetKnowledgeBaseResult',
    'get_knowledge_base',
    'get_knowledge_base_output',
]

@pulumi.output_type
class GetKnowledgeBaseResult:
    def __init__(__self__, knowledge_base_arn=None, knowledge_base_id=None, rendering_configuration=None):
        if knowledge_base_arn and not isinstance(knowledge_base_arn, str):
            raise TypeError("Expected argument 'knowledge_base_arn' to be a str")
        pulumi.set(__self__, "knowledge_base_arn", knowledge_base_arn)
        if knowledge_base_id and not isinstance(knowledge_base_id, str):
            raise TypeError("Expected argument 'knowledge_base_id' to be a str")
        pulumi.set(__self__, "knowledge_base_id", knowledge_base_id)
        if rendering_configuration and not isinstance(rendering_configuration, dict):
            raise TypeError("Expected argument 'rendering_configuration' to be a dict")
        pulumi.set(__self__, "rendering_configuration", rendering_configuration)

    @property
    @pulumi.getter(name="knowledgeBaseArn")
    def knowledge_base_arn(self) -> Optional[str]:
        return pulumi.get(self, "knowledge_base_arn")

    @property
    @pulumi.getter(name="knowledgeBaseId")
    def knowledge_base_id(self) -> Optional[str]:
        return pulumi.get(self, "knowledge_base_id")

    @property
    @pulumi.getter(name="renderingConfiguration")
    def rendering_configuration(self) -> Optional['outputs.KnowledgeBaseRenderingConfiguration']:
        return pulumi.get(self, "rendering_configuration")


class AwaitableGetKnowledgeBaseResult(GetKnowledgeBaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKnowledgeBaseResult(
            knowledge_base_arn=self.knowledge_base_arn,
            knowledge_base_id=self.knowledge_base_id,
            rendering_configuration=self.rendering_configuration)


def get_knowledge_base(knowledge_base_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKnowledgeBaseResult:
    """
    Definition of AWS::Wisdom::KnowledgeBase Resource Type
    """
    __args__ = dict()
    __args__['knowledgeBaseId'] = knowledge_base_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:wisdom:getKnowledgeBase', __args__, opts=opts, typ=GetKnowledgeBaseResult).value

    return AwaitableGetKnowledgeBaseResult(
        knowledge_base_arn=__ret__.knowledge_base_arn,
        knowledge_base_id=__ret__.knowledge_base_id,
        rendering_configuration=__ret__.rendering_configuration)


@_utilities.lift_output_func(get_knowledge_base)
def get_knowledge_base_output(knowledge_base_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKnowledgeBaseResult]:
    """
    Definition of AWS::Wisdom::KnowledgeBase Resource Type
    """
    ...
