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
    'GetViewResult',
    'AwaitableGetViewResult',
    'get_view',
    'get_view_output',
]

@pulumi.output_type
class GetViewResult:
    def __init__(__self__, filters=None, included_properties=None, tags=None, view_arn=None):
        if filters and not isinstance(filters, dict):
            raise TypeError("Expected argument 'filters' to be a dict")
        pulumi.set(__self__, "filters", filters)
        if included_properties and not isinstance(included_properties, list):
            raise TypeError("Expected argument 'included_properties' to be a list")
        pulumi.set(__self__, "included_properties", included_properties)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if view_arn and not isinstance(view_arn, str):
            raise TypeError("Expected argument 'view_arn' to be a str")
        pulumi.set(__self__, "view_arn", view_arn)

    @property
    @pulumi.getter
    def filters(self) -> Optional['outputs.ViewFilters']:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="includedProperties")
    def included_properties(self) -> Optional[Sequence['outputs.ViewIncludedProperty']]:
        return pulumi.get(self, "included_properties")

    @property
    @pulumi.getter
    def tags(self) -> Optional['outputs.ViewTagMap']:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="viewArn")
    def view_arn(self) -> Optional[str]:
        return pulumi.get(self, "view_arn")


class AwaitableGetViewResult(GetViewResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetViewResult(
            filters=self.filters,
            included_properties=self.included_properties,
            tags=self.tags,
            view_arn=self.view_arn)


def get_view(view_arn: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetViewResult:
    """
    Definition of AWS::ResourceExplorer2::View Resource Type
    """
    __args__ = dict()
    __args__['viewArn'] = view_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:resourceexplorer2:getView', __args__, opts=opts, typ=GetViewResult).value

    return AwaitableGetViewResult(
        filters=__ret__.filters,
        included_properties=__ret__.included_properties,
        tags=__ret__.tags,
        view_arn=__ret__.view_arn)


@_utilities.lift_output_func(get_view)
def get_view_output(view_arn: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetViewResult]:
    """
    Definition of AWS::ResourceExplorer2::View Resource Type
    """
    ...
