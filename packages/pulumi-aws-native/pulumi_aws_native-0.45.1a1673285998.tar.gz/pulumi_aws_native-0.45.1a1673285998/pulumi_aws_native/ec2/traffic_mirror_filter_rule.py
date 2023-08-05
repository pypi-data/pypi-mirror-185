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
from ._inputs import *

__all__ = ['TrafficMirrorFilterRuleArgs', 'TrafficMirrorFilterRule']

@pulumi.input_type
class TrafficMirrorFilterRuleArgs:
    def __init__(__self__, *,
                 destination_cidr_block: pulumi.Input[str],
                 rule_action: pulumi.Input[str],
                 rule_number: pulumi.Input[int],
                 source_cidr_block: pulumi.Input[str],
                 traffic_direction: pulumi.Input[str],
                 traffic_mirror_filter_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 destination_port_range: Optional[pulumi.Input['TrafficMirrorFilterRuleTrafficMirrorPortRangeArgs']] = None,
                 protocol: Optional[pulumi.Input[int]] = None,
                 source_port_range: Optional[pulumi.Input['TrafficMirrorFilterRuleTrafficMirrorPortRangeArgs']] = None):
        """
        The set of arguments for constructing a TrafficMirrorFilterRule resource.
        """
        pulumi.set(__self__, "destination_cidr_block", destination_cidr_block)
        pulumi.set(__self__, "rule_action", rule_action)
        pulumi.set(__self__, "rule_number", rule_number)
        pulumi.set(__self__, "source_cidr_block", source_cidr_block)
        pulumi.set(__self__, "traffic_direction", traffic_direction)
        pulumi.set(__self__, "traffic_mirror_filter_id", traffic_mirror_filter_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if destination_port_range is not None:
            pulumi.set(__self__, "destination_port_range", destination_port_range)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if source_port_range is not None:
            pulumi.set(__self__, "source_port_range", source_port_range)

    @property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> pulumi.Input[str]:
        return pulumi.get(self, "destination_cidr_block")

    @destination_cidr_block.setter
    def destination_cidr_block(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination_cidr_block", value)

    @property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> pulumi.Input[str]:
        return pulumi.get(self, "rule_action")

    @rule_action.setter
    def rule_action(self, value: pulumi.Input[str]):
        pulumi.set(self, "rule_action", value)

    @property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> pulumi.Input[int]:
        return pulumi.get(self, "rule_number")

    @rule_number.setter
    def rule_number(self, value: pulumi.Input[int]):
        pulumi.set(self, "rule_number", value)

    @property
    @pulumi.getter(name="sourceCidrBlock")
    def source_cidr_block(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source_cidr_block")

    @source_cidr_block.setter
    def source_cidr_block(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_cidr_block", value)

    @property
    @pulumi.getter(name="trafficDirection")
    def traffic_direction(self) -> pulumi.Input[str]:
        return pulumi.get(self, "traffic_direction")

    @traffic_direction.setter
    def traffic_direction(self, value: pulumi.Input[str]):
        pulumi.set(self, "traffic_direction", value)

    @property
    @pulumi.getter(name="trafficMirrorFilterId")
    def traffic_mirror_filter_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "traffic_mirror_filter_id")

    @traffic_mirror_filter_id.setter
    def traffic_mirror_filter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "traffic_mirror_filter_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> Optional[pulumi.Input['TrafficMirrorFilterRuleTrafficMirrorPortRangeArgs']]:
        return pulumi.get(self, "destination_port_range")

    @destination_port_range.setter
    def destination_port_range(self, value: Optional[pulumi.Input['TrafficMirrorFilterRuleTrafficMirrorPortRangeArgs']]):
        pulumi.set(self, "destination_port_range", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> Optional[pulumi.Input['TrafficMirrorFilterRuleTrafficMirrorPortRangeArgs']]:
        return pulumi.get(self, "source_port_range")

    @source_port_range.setter
    def source_port_range(self, value: Optional[pulumi.Input['TrafficMirrorFilterRuleTrafficMirrorPortRangeArgs']]):
        pulumi.set(self, "source_port_range", value)


warnings.warn("""TrafficMirrorFilterRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class TrafficMirrorFilterRule(pulumi.CustomResource):
    warnings.warn("""TrafficMirrorFilterRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_cidr_block: Optional[pulumi.Input[str]] = None,
                 destination_port_range: Optional[pulumi.Input[pulumi.InputType['TrafficMirrorFilterRuleTrafficMirrorPortRangeArgs']]] = None,
                 protocol: Optional[pulumi.Input[int]] = None,
                 rule_action: Optional[pulumi.Input[str]] = None,
                 rule_number: Optional[pulumi.Input[int]] = None,
                 source_cidr_block: Optional[pulumi.Input[str]] = None,
                 source_port_range: Optional[pulumi.Input[pulumi.InputType['TrafficMirrorFilterRuleTrafficMirrorPortRangeArgs']]] = None,
                 traffic_direction: Optional[pulumi.Input[str]] = None,
                 traffic_mirror_filter_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::TrafficMirrorFilterRule

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TrafficMirrorFilterRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::TrafficMirrorFilterRule

        :param str resource_name: The name of the resource.
        :param TrafficMirrorFilterRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TrafficMirrorFilterRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_cidr_block: Optional[pulumi.Input[str]] = None,
                 destination_port_range: Optional[pulumi.Input[pulumi.InputType['TrafficMirrorFilterRuleTrafficMirrorPortRangeArgs']]] = None,
                 protocol: Optional[pulumi.Input[int]] = None,
                 rule_action: Optional[pulumi.Input[str]] = None,
                 rule_number: Optional[pulumi.Input[int]] = None,
                 source_cidr_block: Optional[pulumi.Input[str]] = None,
                 source_port_range: Optional[pulumi.Input[pulumi.InputType['TrafficMirrorFilterRuleTrafficMirrorPortRangeArgs']]] = None,
                 traffic_direction: Optional[pulumi.Input[str]] = None,
                 traffic_mirror_filter_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""TrafficMirrorFilterRule is deprecated: TrafficMirrorFilterRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TrafficMirrorFilterRuleArgs.__new__(TrafficMirrorFilterRuleArgs)

            __props__.__dict__["description"] = description
            if destination_cidr_block is None and not opts.urn:
                raise TypeError("Missing required property 'destination_cidr_block'")
            __props__.__dict__["destination_cidr_block"] = destination_cidr_block
            __props__.__dict__["destination_port_range"] = destination_port_range
            __props__.__dict__["protocol"] = protocol
            if rule_action is None and not opts.urn:
                raise TypeError("Missing required property 'rule_action'")
            __props__.__dict__["rule_action"] = rule_action
            if rule_number is None and not opts.urn:
                raise TypeError("Missing required property 'rule_number'")
            __props__.__dict__["rule_number"] = rule_number
            if source_cidr_block is None and not opts.urn:
                raise TypeError("Missing required property 'source_cidr_block'")
            __props__.__dict__["source_cidr_block"] = source_cidr_block
            __props__.__dict__["source_port_range"] = source_port_range
            if traffic_direction is None and not opts.urn:
                raise TypeError("Missing required property 'traffic_direction'")
            __props__.__dict__["traffic_direction"] = traffic_direction
            if traffic_mirror_filter_id is None and not opts.urn:
                raise TypeError("Missing required property 'traffic_mirror_filter_id'")
            __props__.__dict__["traffic_mirror_filter_id"] = traffic_mirror_filter_id
        super(TrafficMirrorFilterRule, __self__).__init__(
            'aws-native:ec2:TrafficMirrorFilterRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TrafficMirrorFilterRule':
        """
        Get an existing TrafficMirrorFilterRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TrafficMirrorFilterRuleArgs.__new__(TrafficMirrorFilterRuleArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["destination_cidr_block"] = None
        __props__.__dict__["destination_port_range"] = None
        __props__.__dict__["protocol"] = None
        __props__.__dict__["rule_action"] = None
        __props__.__dict__["rule_number"] = None
        __props__.__dict__["source_cidr_block"] = None
        __props__.__dict__["source_port_range"] = None
        __props__.__dict__["traffic_direction"] = None
        __props__.__dict__["traffic_mirror_filter_id"] = None
        return TrafficMirrorFilterRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> pulumi.Output[str]:
        return pulumi.get(self, "destination_cidr_block")

    @property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> pulumi.Output[Optional['outputs.TrafficMirrorFilterRuleTrafficMirrorPortRange']]:
        return pulumi.get(self, "destination_port_range")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> pulumi.Output[str]:
        return pulumi.get(self, "rule_action")

    @property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> pulumi.Output[int]:
        return pulumi.get(self, "rule_number")

    @property
    @pulumi.getter(name="sourceCidrBlock")
    def source_cidr_block(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source_cidr_block")

    @property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> pulumi.Output[Optional['outputs.TrafficMirrorFilterRuleTrafficMirrorPortRange']]:
        return pulumi.get(self, "source_port_range")

    @property
    @pulumi.getter(name="trafficDirection")
    def traffic_direction(self) -> pulumi.Output[str]:
        return pulumi.get(self, "traffic_direction")

    @property
    @pulumi.getter(name="trafficMirrorFilterId")
    def traffic_mirror_filter_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "traffic_mirror_filter_id")

