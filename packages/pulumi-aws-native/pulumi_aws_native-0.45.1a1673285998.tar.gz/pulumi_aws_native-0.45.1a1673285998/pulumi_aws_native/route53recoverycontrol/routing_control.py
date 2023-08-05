# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['RoutingControlArgs', 'RoutingControl']

@pulumi.input_type
class RoutingControlArgs:
    def __init__(__self__, *,
                 cluster_arn: Optional[pulumi.Input[str]] = None,
                 control_panel_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RoutingControl resource.
        :param pulumi.Input[str] cluster_arn: Arn associated with Control Panel
        :param pulumi.Input[str] control_panel_arn: The Amazon Resource Name (ARN) of the control panel.
        :param pulumi.Input[str] name: The name of the routing control. You can use any non-white space character in the name.
        """
        if cluster_arn is not None:
            pulumi.set(__self__, "cluster_arn", cluster_arn)
        if control_panel_arn is not None:
            pulumi.set(__self__, "control_panel_arn", control_panel_arn)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Arn associated with Control Panel
        """
        return pulumi.get(self, "cluster_arn")

    @cluster_arn.setter
    def cluster_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_arn", value)

    @property
    @pulumi.getter(name="controlPanelArn")
    def control_panel_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the control panel.
        """
        return pulumi.get(self, "control_panel_arn")

    @control_panel_arn.setter
    def control_panel_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "control_panel_arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the routing control. You can use any non-white space character in the name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class RoutingControl(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_arn: Optional[pulumi.Input[str]] = None,
                 control_panel_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        AWS Route53 Recovery Control Routing Control resource schema .

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_arn: Arn associated with Control Panel
        :param pulumi.Input[str] control_panel_arn: The Amazon Resource Name (ARN) of the control panel.
        :param pulumi.Input[str] name: The name of the routing control. You can use any non-white space character in the name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[RoutingControlArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AWS Route53 Recovery Control Routing Control resource schema .

        :param str resource_name: The name of the resource.
        :param RoutingControlArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoutingControlArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_arn: Optional[pulumi.Input[str]] = None,
                 control_panel_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RoutingControlArgs.__new__(RoutingControlArgs)

            __props__.__dict__["cluster_arn"] = cluster_arn
            __props__.__dict__["control_panel_arn"] = control_panel_arn
            __props__.__dict__["name"] = name
            __props__.__dict__["routing_control_arn"] = None
            __props__.__dict__["status"] = None
        super(RoutingControl, __self__).__init__(
            'aws-native:route53recoverycontrol:RoutingControl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RoutingControl':
        """
        Get an existing RoutingControl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RoutingControlArgs.__new__(RoutingControlArgs)

        __props__.__dict__["cluster_arn"] = None
        __props__.__dict__["control_panel_arn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["routing_control_arn"] = None
        __props__.__dict__["status"] = None
        return RoutingControl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> pulumi.Output[Optional[str]]:
        """
        Arn associated with Control Panel
        """
        return pulumi.get(self, "cluster_arn")

    @property
    @pulumi.getter(name="controlPanelArn")
    def control_panel_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of the control panel.
        """
        return pulumi.get(self, "control_panel_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the routing control. You can use any non-white space character in the name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routingControlArn")
    def routing_control_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the routing control.
        """
        return pulumi.get(self, "routing_control_arn")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['RoutingControlStatus']:
        """
        The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.
        """
        return pulumi.get(self, "status")

