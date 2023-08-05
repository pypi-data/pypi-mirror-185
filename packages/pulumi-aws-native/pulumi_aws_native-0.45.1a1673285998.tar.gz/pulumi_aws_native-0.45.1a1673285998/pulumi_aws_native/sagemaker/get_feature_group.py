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
from ._enums import *

__all__ = [
    'GetFeatureGroupResult',
    'AwaitableGetFeatureGroupResult',
    'get_feature_group',
    'get_feature_group_output',
]

@pulumi.output_type
class GetFeatureGroupResult:
    def __init__(__self__, feature_definitions=None):
        if feature_definitions and not isinstance(feature_definitions, list):
            raise TypeError("Expected argument 'feature_definitions' to be a list")
        pulumi.set(__self__, "feature_definitions", feature_definitions)

    @property
    @pulumi.getter(name="featureDefinitions")
    def feature_definitions(self) -> Optional[Sequence['outputs.FeatureGroupFeatureDefinition']]:
        """
        An Array of Feature Definition
        """
        return pulumi.get(self, "feature_definitions")


class AwaitableGetFeatureGroupResult(GetFeatureGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFeatureGroupResult(
            feature_definitions=self.feature_definitions)


def get_feature_group(feature_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFeatureGroupResult:
    """
    Resource Type definition for AWS::SageMaker::FeatureGroup


    :param str feature_group_name: The Name of the FeatureGroup.
    """
    __args__ = dict()
    __args__['featureGroupName'] = feature_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:sagemaker:getFeatureGroup', __args__, opts=opts, typ=GetFeatureGroupResult).value

    return AwaitableGetFeatureGroupResult(
        feature_definitions=__ret__.feature_definitions)


@_utilities.lift_output_func(get_feature_group)
def get_feature_group_output(feature_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFeatureGroupResult]:
    """
    Resource Type definition for AWS::SageMaker::FeatureGroup


    :param str feature_group_name: The Name of the FeatureGroup.
    """
    ...
