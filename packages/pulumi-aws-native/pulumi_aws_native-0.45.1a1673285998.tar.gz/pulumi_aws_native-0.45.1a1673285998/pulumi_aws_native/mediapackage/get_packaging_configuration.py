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
    'GetPackagingConfigurationResult',
    'AwaitableGetPackagingConfigurationResult',
    'get_packaging_configuration',
    'get_packaging_configuration_output',
]

@pulumi.output_type
class GetPackagingConfigurationResult:
    def __init__(__self__, arn=None, cmaf_package=None, dash_package=None, hls_package=None, mss_package=None, packaging_group_id=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if cmaf_package and not isinstance(cmaf_package, dict):
            raise TypeError("Expected argument 'cmaf_package' to be a dict")
        pulumi.set(__self__, "cmaf_package", cmaf_package)
        if dash_package and not isinstance(dash_package, dict):
            raise TypeError("Expected argument 'dash_package' to be a dict")
        pulumi.set(__self__, "dash_package", dash_package)
        if hls_package and not isinstance(hls_package, dict):
            raise TypeError("Expected argument 'hls_package' to be a dict")
        pulumi.set(__self__, "hls_package", hls_package)
        if mss_package and not isinstance(mss_package, dict):
            raise TypeError("Expected argument 'mss_package' to be a dict")
        pulumi.set(__self__, "mss_package", mss_package)
        if packaging_group_id and not isinstance(packaging_group_id, str):
            raise TypeError("Expected argument 'packaging_group_id' to be a str")
        pulumi.set(__self__, "packaging_group_id", packaging_group_id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the PackagingConfiguration.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="cmafPackage")
    def cmaf_package(self) -> Optional['outputs.PackagingConfigurationCmafPackage']:
        """
        A CMAF packaging configuration.
        """
        return pulumi.get(self, "cmaf_package")

    @property
    @pulumi.getter(name="dashPackage")
    def dash_package(self) -> Optional['outputs.PackagingConfigurationDashPackage']:
        """
        A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
        """
        return pulumi.get(self, "dash_package")

    @property
    @pulumi.getter(name="hlsPackage")
    def hls_package(self) -> Optional['outputs.PackagingConfigurationHlsPackage']:
        """
        An HTTP Live Streaming (HLS) packaging configuration.
        """
        return pulumi.get(self, "hls_package")

    @property
    @pulumi.getter(name="mssPackage")
    def mss_package(self) -> Optional['outputs.PackagingConfigurationMssPackage']:
        """
        A Microsoft Smooth Streaming (MSS) PackagingConfiguration.
        """
        return pulumi.get(self, "mss_package")

    @property
    @pulumi.getter(name="packagingGroupId")
    def packaging_group_id(self) -> Optional[str]:
        """
        The ID of a PackagingGroup.
        """
        return pulumi.get(self, "packaging_group_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.PackagingConfigurationTag']]:
        """
        A collection of tags associated with a resource
        """
        return pulumi.get(self, "tags")


class AwaitableGetPackagingConfigurationResult(GetPackagingConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPackagingConfigurationResult(
            arn=self.arn,
            cmaf_package=self.cmaf_package,
            dash_package=self.dash_package,
            hls_package=self.hls_package,
            mss_package=self.mss_package,
            packaging_group_id=self.packaging_group_id,
            tags=self.tags)


def get_packaging_configuration(id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPackagingConfigurationResult:
    """
    Resource schema for AWS::MediaPackage::PackagingConfiguration


    :param str id: The ID of the PackagingConfiguration.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:mediapackage:getPackagingConfiguration', __args__, opts=opts, typ=GetPackagingConfigurationResult).value

    return AwaitableGetPackagingConfigurationResult(
        arn=__ret__.arn,
        cmaf_package=__ret__.cmaf_package,
        dash_package=__ret__.dash_package,
        hls_package=__ret__.hls_package,
        mss_package=__ret__.mss_package,
        packaging_group_id=__ret__.packaging_group_id,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_packaging_configuration)
def get_packaging_configuration_output(id: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPackagingConfigurationResult]:
    """
    Resource schema for AWS::MediaPackage::PackagingConfiguration


    :param str id: The ID of the PackagingConfiguration.
    """
    ...
