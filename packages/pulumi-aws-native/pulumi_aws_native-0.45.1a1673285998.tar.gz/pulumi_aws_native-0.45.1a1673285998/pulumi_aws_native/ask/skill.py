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

__all__ = ['SkillArgs', 'Skill']

@pulumi.input_type
class SkillArgs:
    def __init__(__self__, *,
                 authentication_configuration: pulumi.Input['SkillAuthenticationConfigurationArgs'],
                 skill_package: pulumi.Input['SkillPackageArgs'],
                 vendor_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a Skill resource.
        """
        pulumi.set(__self__, "authentication_configuration", authentication_configuration)
        pulumi.set(__self__, "skill_package", skill_package)
        pulumi.set(__self__, "vendor_id", vendor_id)

    @property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> pulumi.Input['SkillAuthenticationConfigurationArgs']:
        return pulumi.get(self, "authentication_configuration")

    @authentication_configuration.setter
    def authentication_configuration(self, value: pulumi.Input['SkillAuthenticationConfigurationArgs']):
        pulumi.set(self, "authentication_configuration", value)

    @property
    @pulumi.getter(name="skillPackage")
    def skill_package(self) -> pulumi.Input['SkillPackageArgs']:
        return pulumi.get(self, "skill_package")

    @skill_package.setter
    def skill_package(self, value: pulumi.Input['SkillPackageArgs']):
        pulumi.set(self, "skill_package", value)

    @property
    @pulumi.getter(name="vendorId")
    def vendor_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "vendor_id")

    @vendor_id.setter
    def vendor_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vendor_id", value)


warnings.warn("""Skill is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Skill(pulumi.CustomResource):
    warnings.warn("""Skill is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_configuration: Optional[pulumi.Input[pulumi.InputType['SkillAuthenticationConfigurationArgs']]] = None,
                 skill_package: Optional[pulumi.Input[pulumi.InputType['SkillPackageArgs']]] = None,
                 vendor_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for Alexa::ASK::Skill

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SkillArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for Alexa::ASK::Skill

        :param str resource_name: The name of the resource.
        :param SkillArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SkillArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_configuration: Optional[pulumi.Input[pulumi.InputType['SkillAuthenticationConfigurationArgs']]] = None,
                 skill_package: Optional[pulumi.Input[pulumi.InputType['SkillPackageArgs']]] = None,
                 vendor_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Skill is deprecated: Skill is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SkillArgs.__new__(SkillArgs)

            if authentication_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'authentication_configuration'")
            __props__.__dict__["authentication_configuration"] = authentication_configuration
            if skill_package is None and not opts.urn:
                raise TypeError("Missing required property 'skill_package'")
            __props__.__dict__["skill_package"] = skill_package
            if vendor_id is None and not opts.urn:
                raise TypeError("Missing required property 'vendor_id'")
            __props__.__dict__["vendor_id"] = vendor_id
        super(Skill, __self__).__init__(
            'aws-native:ask:Skill',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Skill':
        """
        Get an existing Skill resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SkillArgs.__new__(SkillArgs)

        __props__.__dict__["authentication_configuration"] = None
        __props__.__dict__["skill_package"] = None
        __props__.__dict__["vendor_id"] = None
        return Skill(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> pulumi.Output['outputs.SkillAuthenticationConfiguration']:
        return pulumi.get(self, "authentication_configuration")

    @property
    @pulumi.getter(name="skillPackage")
    def skill_package(self) -> pulumi.Output['outputs.SkillPackage']:
        return pulumi.get(self, "skill_package")

    @property
    @pulumi.getter(name="vendorId")
    def vendor_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "vendor_id")

