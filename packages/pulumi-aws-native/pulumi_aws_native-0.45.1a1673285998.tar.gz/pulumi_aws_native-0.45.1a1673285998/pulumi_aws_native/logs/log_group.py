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

__all__ = ['LogGroupArgs', 'LogGroup']

@pulumi.input_type
class LogGroupArgs:
    def __init__(__self__, *,
                 data_protection_policy: Optional[Any] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 log_group_name: Optional[pulumi.Input[str]] = None,
                 retention_in_days: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['LogGroupTagArgs']]]] = None):
        """
        The set of arguments for constructing a LogGroup resource.
        :param Any data_protection_policy: The body of the policy document you want to use for this topic.
               
               You can only add one policy per topic.
               
               The policy must be in JSON string format.
               
               Length Constraints: Maximum length of 30720
        :param pulumi.Input[str] kms_key_id: The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
        :param pulumi.Input[str] log_group_name: The name of the log group. If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.
        :param pulumi.Input[int] retention_in_days: The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.
        :param pulumi.Input[Sequence[pulumi.Input['LogGroupTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        if data_protection_policy is not None:
            pulumi.set(__self__, "data_protection_policy", data_protection_policy)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if log_group_name is not None:
            pulumi.set(__self__, "log_group_name", log_group_name)
        if retention_in_days is not None:
            pulumi.set(__self__, "retention_in_days", retention_in_days)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dataProtectionPolicy")
    def data_protection_policy(self) -> Optional[Any]:
        """
        The body of the policy document you want to use for this topic.

        You can only add one policy per topic.

        The policy must be in JSON string format.

        Length Constraints: Maximum length of 30720
        """
        return pulumi.get(self, "data_protection_policy")

    @data_protection_policy.setter
    def data_protection_policy(self, value: Optional[Any]):
        pulumi.set(self, "data_protection_policy", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the log group. If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.
        """
        return pulumi.get(self, "log_group_name")

    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_group_name", value)

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.
        """
        return pulumi.get(self, "retention_in_days")

    @retention_in_days.setter
    def retention_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_in_days", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LogGroupTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LogGroupTagArgs']]]]):
        pulumi.set(self, "tags", value)


class LogGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_protection_policy: Optional[Any] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 log_group_name: Optional[pulumi.Input[str]] = None,
                 retention_in_days: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogGroupTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::Logs::LogGroup

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any data_protection_policy: The body of the policy document you want to use for this topic.
               
               You can only add one policy per topic.
               
               The policy must be in JSON string format.
               
               Length Constraints: Maximum length of 30720
        :param pulumi.Input[str] kms_key_id: The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
        :param pulumi.Input[str] log_group_name: The name of the log group. If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.
        :param pulumi.Input[int] retention_in_days: The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogGroupTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[LogGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::Logs::LogGroup

        :param str resource_name: The name of the resource.
        :param LogGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LogGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_protection_policy: Optional[Any] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 log_group_name: Optional[pulumi.Input[str]] = None,
                 retention_in_days: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogGroupTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LogGroupArgs.__new__(LogGroupArgs)

            __props__.__dict__["data_protection_policy"] = data_protection_policy
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["log_group_name"] = log_group_name
            __props__.__dict__["retention_in_days"] = retention_in_days
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(LogGroup, __self__).__init__(
            'aws-native:logs:LogGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LogGroup':
        """
        Get an existing LogGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LogGroupArgs.__new__(LogGroupArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["data_protection_policy"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["log_group_name"] = None
        __props__.__dict__["retention_in_days"] = None
        __props__.__dict__["tags"] = None
        return LogGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The CloudWatch log group ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="dataProtectionPolicy")
    def data_protection_policy(self) -> pulumi.Output[Optional[Any]]:
        """
        The body of the policy document you want to use for this topic.

        You can only add one policy per topic.

        The policy must be in JSON string format.

        Length Constraints: Maximum length of 30720
        """
        return pulumi.get(self, "data_protection_policy")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the log group. If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.
        """
        return pulumi.get(self, "log_group_name")

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> pulumi.Output[Optional[int]]:
        """
        The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.
        """
        return pulumi.get(self, "retention_in_days")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.LogGroupTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

