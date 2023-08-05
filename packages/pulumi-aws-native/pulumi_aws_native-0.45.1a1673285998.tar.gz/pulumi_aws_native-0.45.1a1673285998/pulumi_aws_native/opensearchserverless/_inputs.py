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
    'CollectionTagArgs',
    'SecurityConfigSamlConfigOptionsArgs',
]

@pulumi.input_type
class CollectionTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair metadata associated with resource
        :param pulumi.Input[str] key: The key in the key-value pair
        :param pulumi.Input[str] value: The value in the key-value pair
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key in the key-value pair
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value in the key-value pair
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class SecurityConfigSamlConfigOptionsArgs:
    def __init__(__self__, *,
                 metadata: pulumi.Input[str],
                 group_attribute: Optional[pulumi.Input[str]] = None,
                 session_timeout: Optional[pulumi.Input[int]] = None,
                 user_attribute: Optional[pulumi.Input[str]] = None):
        """
        Describes saml options in form of key value map
        :param pulumi.Input[str] metadata: The XML saml provider metadata document that you want to use
        :param pulumi.Input[str] group_attribute: Group attribute for this saml integration
        :param pulumi.Input[int] session_timeout: Defines the session timeout in minutes
        :param pulumi.Input[str] user_attribute: Custom attribute for this saml integration
        """
        pulumi.set(__self__, "metadata", metadata)
        if group_attribute is not None:
            pulumi.set(__self__, "group_attribute", group_attribute)
        if session_timeout is not None:
            pulumi.set(__self__, "session_timeout", session_timeout)
        if user_attribute is not None:
            pulumi.set(__self__, "user_attribute", user_attribute)

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Input[str]:
        """
        The XML saml provider metadata document that you want to use
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: pulumi.Input[str]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="groupAttribute")
    def group_attribute(self) -> Optional[pulumi.Input[str]]:
        """
        Group attribute for this saml integration
        """
        return pulumi.get(self, "group_attribute")

    @group_attribute.setter
    def group_attribute(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_attribute", value)

    @property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Defines the session timeout in minutes
        """
        return pulumi.get(self, "session_timeout")

    @session_timeout.setter
    def session_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "session_timeout", value)

    @property
    @pulumi.getter(name="userAttribute")
    def user_attribute(self) -> Optional[pulumi.Input[str]]:
        """
        Custom attribute for this saml integration
        """
        return pulumi.get(self, "user_attribute")

    @user_attribute.setter
    def user_attribute(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_attribute", value)


