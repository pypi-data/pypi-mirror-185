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

__all__ = [
    'ApplicationAutoStartConfigurationArgs',
    'ApplicationAutoStopConfigurationArgs',
    'ApplicationInitialCapacityConfigKeyValuePairArgs',
    'ApplicationInitialCapacityConfigArgs',
    'ApplicationMaximumAllowedResourcesArgs',
    'ApplicationNetworkConfigurationArgs',
    'ApplicationTagArgs',
    'ApplicationWorkerConfigurationArgs',
]

@pulumi.input_type
class ApplicationAutoStartConfigurationArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None):
        """
        Configuration for Auto Start of Application
        :param pulumi.Input[bool] enabled: If set to true, the Application will automatically start. Defaults to true.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, the Application will automatically start. Defaults to true.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class ApplicationAutoStopConfigurationArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 idle_timeout_minutes: Optional[pulumi.Input[int]] = None):
        """
        Configuration for Auto Stop of Application
        :param pulumi.Input[bool] enabled: If set to true, the Application will automatically stop after being idle. Defaults to true.
        :param pulumi.Input[int] idle_timeout_minutes: The amount of time [in minutes] to wait before auto stopping the Application when idle. Defaults to 15 minutes.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if idle_timeout_minutes is not None:
            pulumi.set(__self__, "idle_timeout_minutes", idle_timeout_minutes)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, the Application will automatically stop after being idle. Defaults to true.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="idleTimeoutMinutes")
    def idle_timeout_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        The amount of time [in minutes] to wait before auto stopping the Application when idle. Defaults to 15 minutes.
        """
        return pulumi.get(self, "idle_timeout_minutes")

    @idle_timeout_minutes.setter
    def idle_timeout_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "idle_timeout_minutes", value)


@pulumi.input_type
class ApplicationInitialCapacityConfigKeyValuePairArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input['ApplicationInitialCapacityConfigArgs']):
        """
        :param pulumi.Input[str] key: Worker type for an analytics framework.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Worker type for an analytics framework.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input['ApplicationInitialCapacityConfigArgs']:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input['ApplicationInitialCapacityConfigArgs']):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ApplicationInitialCapacityConfigArgs:
    def __init__(__self__, *,
                 worker_configuration: pulumi.Input['ApplicationWorkerConfigurationArgs'],
                 worker_count: pulumi.Input[int]):
        """
        :param pulumi.Input[int] worker_count: Initial count of workers to be initialized when an Application is started. This count will be continued to be maintained until the Application is stopped
        """
        pulumi.set(__self__, "worker_configuration", worker_configuration)
        pulumi.set(__self__, "worker_count", worker_count)

    @property
    @pulumi.getter(name="workerConfiguration")
    def worker_configuration(self) -> pulumi.Input['ApplicationWorkerConfigurationArgs']:
        return pulumi.get(self, "worker_configuration")

    @worker_configuration.setter
    def worker_configuration(self, value: pulumi.Input['ApplicationWorkerConfigurationArgs']):
        pulumi.set(self, "worker_configuration", value)

    @property
    @pulumi.getter(name="workerCount")
    def worker_count(self) -> pulumi.Input[int]:
        """
        Initial count of workers to be initialized when an Application is started. This count will be continued to be maintained until the Application is stopped
        """
        return pulumi.get(self, "worker_count")

    @worker_count.setter
    def worker_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "worker_count", value)


@pulumi.input_type
class ApplicationMaximumAllowedResourcesArgs:
    def __init__(__self__, *,
                 cpu: pulumi.Input[str],
                 memory: pulumi.Input[str],
                 disk: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] cpu: Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        :param pulumi.Input[str] memory: Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        :param pulumi.Input[str] disk: Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        pulumi.set(__self__, "cpu", cpu)
        pulumi.set(__self__, "memory", memory)
        if disk is not None:
            pulumi.set(__self__, "disk", disk)

    @property
    @pulumi.getter
    def cpu(self) -> pulumi.Input[str]:
        """
        Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        """
        return pulumi.get(self, "cpu")

    @cpu.setter
    def cpu(self, value: pulumi.Input[str]):
        pulumi.set(self, "cpu", value)

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Input[str]:
        """
        Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: pulumi.Input[str]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter
    def disk(self) -> Optional[pulumi.Input[str]]:
        """
        Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        return pulumi.get(self, "disk")

    @disk.setter
    def disk(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk", value)


@pulumi.input_type
class ApplicationNetworkConfigurationArgs:
    def __init__(__self__, *,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The ID of the security groups in the VPC to which you want to connect your job or application.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The ID of the subnets in the VPC to which you want to connect your job or application.
        """
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The ID of the security groups in the VPC to which you want to connect your job or application.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The ID of the subnets in the VPC to which you want to connect your job or application.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)


@pulumi.input_type
class ApplicationTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The value for the tag. You can specify a value that is 1 to 128 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 1 to 128 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ApplicationWorkerConfigurationArgs:
    def __init__(__self__, *,
                 cpu: pulumi.Input[str],
                 memory: pulumi.Input[str],
                 disk: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] cpu: Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        :param pulumi.Input[str] memory: Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        :param pulumi.Input[str] disk: Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        pulumi.set(__self__, "cpu", cpu)
        pulumi.set(__self__, "memory", memory)
        if disk is not None:
            pulumi.set(__self__, "disk", disk)

    @property
    @pulumi.getter
    def cpu(self) -> pulumi.Input[str]:
        """
        Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        """
        return pulumi.get(self, "cpu")

    @cpu.setter
    def cpu(self, value: pulumi.Input[str]):
        pulumi.set(self, "cpu", value)

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Input[str]:
        """
        Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: pulumi.Input[str]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter
    def disk(self) -> Optional[pulumi.Input[str]]:
        """
        Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        """
        return pulumi.get(self, "disk")

    @disk.setter
    def disk(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk", value)


