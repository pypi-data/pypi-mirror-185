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

__all__ = ['ServerArgs', 'Server']

@pulumi.input_type
class ServerArgs:
    def __init__(__self__, *,
                 instance_profile_arn: pulumi.Input[str],
                 instance_type: pulumi.Input[str],
                 service_role_arn: pulumi.Input[str],
                 associate_public_ip_address: Optional[pulumi.Input[bool]] = None,
                 backup_id: Optional[pulumi.Input[str]] = None,
                 backup_retention_count: Optional[pulumi.Input[int]] = None,
                 custom_certificate: Optional[pulumi.Input[str]] = None,
                 custom_domain: Optional[pulumi.Input[str]] = None,
                 custom_private_key: Optional[pulumi.Input[str]] = None,
                 disable_automated_backup: Optional[pulumi.Input[bool]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 engine_attributes: Optional[pulumi.Input[Sequence[pulumi.Input['ServerEngineAttributeArgs']]]] = None,
                 engine_model: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 key_pair: Optional[pulumi.Input[str]] = None,
                 preferred_backup_window: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ServerTagArgs']]]] = None):
        """
        The set of arguments for constructing a Server resource.
        """
        pulumi.set(__self__, "instance_profile_arn", instance_profile_arn)
        pulumi.set(__self__, "instance_type", instance_type)
        pulumi.set(__self__, "service_role_arn", service_role_arn)
        if associate_public_ip_address is not None:
            pulumi.set(__self__, "associate_public_ip_address", associate_public_ip_address)
        if backup_id is not None:
            pulumi.set(__self__, "backup_id", backup_id)
        if backup_retention_count is not None:
            pulumi.set(__self__, "backup_retention_count", backup_retention_count)
        if custom_certificate is not None:
            pulumi.set(__self__, "custom_certificate", custom_certificate)
        if custom_domain is not None:
            pulumi.set(__self__, "custom_domain", custom_domain)
        if custom_private_key is not None:
            pulumi.set(__self__, "custom_private_key", custom_private_key)
        if disable_automated_backup is not None:
            pulumi.set(__self__, "disable_automated_backup", disable_automated_backup)
        if engine is not None:
            pulumi.set(__self__, "engine", engine)
        if engine_attributes is not None:
            pulumi.set(__self__, "engine_attributes", engine_attributes)
        if engine_model is not None:
            pulumi.set(__self__, "engine_model", engine_model)
        if engine_version is not None:
            pulumi.set(__self__, "engine_version", engine_version)
        if key_pair is not None:
            pulumi.set(__self__, "key_pair", key_pair)
        if preferred_backup_window is not None:
            pulumi.set(__self__, "preferred_backup_window", preferred_backup_window)
        if preferred_maintenance_window is not None:
            pulumi.set(__self__, "preferred_maintenance_window", preferred_maintenance_window)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if server_name is not None:
            pulumi.set(__self__, "server_name", server_name)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="instanceProfileArn")
    def instance_profile_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "instance_profile_arn")

    @instance_profile_arn.setter
    def instance_profile_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_profile_arn", value)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "service_role_arn")

    @service_role_arn.setter
    def service_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_role_arn", value)

    @property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "associate_public_ip_address")

    @associate_public_ip_address.setter
    def associate_public_ip_address(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "associate_public_ip_address", value)

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "backup_id")

    @backup_id.setter
    def backup_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backup_id", value)

    @property
    @pulumi.getter(name="backupRetentionCount")
    def backup_retention_count(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "backup_retention_count")

    @backup_retention_count.setter
    def backup_retention_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "backup_retention_count", value)

    @property
    @pulumi.getter(name="customCertificate")
    def custom_certificate(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "custom_certificate")

    @custom_certificate.setter
    def custom_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_certificate", value)

    @property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "custom_domain")

    @custom_domain.setter
    def custom_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_domain", value)

    @property
    @pulumi.getter(name="customPrivateKey")
    def custom_private_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "custom_private_key")

    @custom_private_key.setter
    def custom_private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_private_key", value)

    @property
    @pulumi.getter(name="disableAutomatedBackup")
    def disable_automated_backup(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "disable_automated_backup")

    @disable_automated_backup.setter
    def disable_automated_backup(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_automated_backup", value)

    @property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "engine")

    @engine.setter
    def engine(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine", value)

    @property
    @pulumi.getter(name="engineAttributes")
    def engine_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServerEngineAttributeArgs']]]]:
        return pulumi.get(self, "engine_attributes")

    @engine_attributes.setter
    def engine_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServerEngineAttributeArgs']]]]):
        pulumi.set(self, "engine_attributes", value)

    @property
    @pulumi.getter(name="engineModel")
    def engine_model(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "engine_model")

    @engine_model.setter
    def engine_model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine_model", value)

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "engine_version")

    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine_version", value)

    @property
    @pulumi.getter(name="keyPair")
    def key_pair(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key_pair")

    @key_pair.setter
    def key_pair(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_pair", value)

    @property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "preferred_backup_window")

    @preferred_backup_window.setter
    def preferred_backup_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_backup_window", value)

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "preferred_maintenance_window")

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_maintenance_window", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServerTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServerTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Server(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associate_public_ip_address: Optional[pulumi.Input[bool]] = None,
                 backup_id: Optional[pulumi.Input[str]] = None,
                 backup_retention_count: Optional[pulumi.Input[int]] = None,
                 custom_certificate: Optional[pulumi.Input[str]] = None,
                 custom_domain: Optional[pulumi.Input[str]] = None,
                 custom_private_key: Optional[pulumi.Input[str]] = None,
                 disable_automated_backup: Optional[pulumi.Input[bool]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 engine_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerEngineAttributeArgs']]]]] = None,
                 engine_model: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 instance_profile_arn: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 key_pair: Optional[pulumi.Input[str]] = None,
                 preferred_backup_window: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 service_role_arn: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::OpsWorksCM::Server

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::OpsWorksCM::Server

        :param str resource_name: The name of the resource.
        :param ServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associate_public_ip_address: Optional[pulumi.Input[bool]] = None,
                 backup_id: Optional[pulumi.Input[str]] = None,
                 backup_retention_count: Optional[pulumi.Input[int]] = None,
                 custom_certificate: Optional[pulumi.Input[str]] = None,
                 custom_domain: Optional[pulumi.Input[str]] = None,
                 custom_private_key: Optional[pulumi.Input[str]] = None,
                 disable_automated_backup: Optional[pulumi.Input[bool]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 engine_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerEngineAttributeArgs']]]]] = None,
                 engine_model: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 instance_profile_arn: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 key_pair: Optional[pulumi.Input[str]] = None,
                 preferred_backup_window: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 service_role_arn: Optional[pulumi.Input[str]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerArgs.__new__(ServerArgs)

            __props__.__dict__["associate_public_ip_address"] = associate_public_ip_address
            __props__.__dict__["backup_id"] = backup_id
            __props__.__dict__["backup_retention_count"] = backup_retention_count
            __props__.__dict__["custom_certificate"] = custom_certificate
            __props__.__dict__["custom_domain"] = custom_domain
            __props__.__dict__["custom_private_key"] = custom_private_key
            __props__.__dict__["disable_automated_backup"] = disable_automated_backup
            __props__.__dict__["engine"] = engine
            __props__.__dict__["engine_attributes"] = engine_attributes
            __props__.__dict__["engine_model"] = engine_model
            __props__.__dict__["engine_version"] = engine_version
            if instance_profile_arn is None and not opts.urn:
                raise TypeError("Missing required property 'instance_profile_arn'")
            __props__.__dict__["instance_profile_arn"] = instance_profile_arn
            if instance_type is None and not opts.urn:
                raise TypeError("Missing required property 'instance_type'")
            __props__.__dict__["instance_type"] = instance_type
            __props__.__dict__["key_pair"] = key_pair
            __props__.__dict__["preferred_backup_window"] = preferred_backup_window
            __props__.__dict__["preferred_maintenance_window"] = preferred_maintenance_window
            __props__.__dict__["security_group_ids"] = security_group_ids
            __props__.__dict__["server_name"] = server_name
            if service_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'service_role_arn'")
            __props__.__dict__["service_role_arn"] = service_role_arn
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["endpoint"] = None
        super(Server, __self__).__init__(
            'aws-native:opsworkscm:Server',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Server':
        """
        Get an existing Server resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerArgs.__new__(ServerArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["associate_public_ip_address"] = None
        __props__.__dict__["backup_id"] = None
        __props__.__dict__["backup_retention_count"] = None
        __props__.__dict__["custom_certificate"] = None
        __props__.__dict__["custom_domain"] = None
        __props__.__dict__["custom_private_key"] = None
        __props__.__dict__["disable_automated_backup"] = None
        __props__.__dict__["endpoint"] = None
        __props__.__dict__["engine"] = None
        __props__.__dict__["engine_attributes"] = None
        __props__.__dict__["engine_model"] = None
        __props__.__dict__["engine_version"] = None
        __props__.__dict__["instance_profile_arn"] = None
        __props__.__dict__["instance_type"] = None
        __props__.__dict__["key_pair"] = None
        __props__.__dict__["preferred_backup_window"] = None
        __props__.__dict__["preferred_maintenance_window"] = None
        __props__.__dict__["security_group_ids"] = None
        __props__.__dict__["server_name"] = None
        __props__.__dict__["service_role_arn"] = None
        __props__.__dict__["subnet_ids"] = None
        __props__.__dict__["tags"] = None
        return Server(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "associate_public_ip_address")

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "backup_id")

    @property
    @pulumi.getter(name="backupRetentionCount")
    def backup_retention_count(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "backup_retention_count")

    @property
    @pulumi.getter(name="customCertificate")
    def custom_certificate(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "custom_certificate")

    @property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "custom_domain")

    @property
    @pulumi.getter(name="customPrivateKey")
    def custom_private_key(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "custom_private_key")

    @property
    @pulumi.getter(name="disableAutomatedBackup")
    def disable_automated_backup(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "disable_automated_backup")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineAttributes")
    def engine_attributes(self) -> pulumi.Output[Optional[Sequence['outputs.ServerEngineAttribute']]]:
        return pulumi.get(self, "engine_attributes")

    @property
    @pulumi.getter(name="engineModel")
    def engine_model(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "engine_model")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="instanceProfileArn")
    def instance_profile_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "instance_profile_arn")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="keyPair")
    def key_pair(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "key_pair")

    @property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "preferred_backup_window")

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "server_name")

    @property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "service_role_arn")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ServerTag']]]:
        return pulumi.get(self, "tags")

