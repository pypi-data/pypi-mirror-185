# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ConnectAttachmentOptionsArgs',
    'ConnectAttachmentTagArgs',
    'ConnectPeerBgpOptionsArgs',
    'ConnectPeerTagArgs',
    'CoreNetworkTagArgs',
    'DeviceLocationArgs',
    'DeviceTagArgs',
    'GlobalNetworkTagArgs',
    'LinkBandwidthArgs',
    'LinkTagArgs',
    'SiteLocationArgs',
    'SiteTagArgs',
    'SiteToSiteVpnAttachmentTagArgs',
    'VpcAttachmentTagArgs',
    'VpcAttachmentVpcOptionsArgs',
]

@pulumi.input_type
class ConnectAttachmentOptionsArgs:
    def __init__(__self__, *,
                 protocol: Optional[pulumi.Input[str]] = None):
        """
        Connect attachment options for protocol
        :param pulumi.Input[str] protocol: Tunnel protocol for connect attachment
        """
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        Tunnel protocol for connect attachment
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)


@pulumi.input_type
class ConnectAttachmentTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ConnectPeerBgpOptionsArgs:
    def __init__(__self__, *,
                 peer_asn: Optional[pulumi.Input[float]] = None):
        """
        Bgp options
        """
        if peer_asn is not None:
            pulumi.set(__self__, "peer_asn", peer_asn)

    @property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "peer_asn")

    @peer_asn.setter
    def peer_asn(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "peer_asn", value)


@pulumi.input_type
class ConnectPeerTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class CoreNetworkTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class DeviceLocationArgs:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None,
                 latitude: Optional[pulumi.Input[str]] = None,
                 longitude: Optional[pulumi.Input[str]] = None):
        """
        The site location.
        :param pulumi.Input[str] address: The physical address.
        :param pulumi.Input[str] latitude: The latitude.
        :param pulumi.Input[str] longitude: The longitude.
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if latitude is not None:
            pulumi.set(__self__, "latitude", latitude)
        if longitude is not None:
            pulumi.set(__self__, "longitude", longitude)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        """
        The physical address.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def latitude(self) -> Optional[pulumi.Input[str]]:
        """
        The latitude.
        """
        return pulumi.get(self, "latitude")

    @latitude.setter
    def latitude(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "latitude", value)

    @property
    @pulumi.getter
    def longitude(self) -> Optional[pulumi.Input[str]]:
        """
        The longitude.
        """
        return pulumi.get(self, "longitude")

    @longitude.setter
    def longitude(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "longitude", value)


@pulumi.input_type
class DeviceTagArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        A key-value pair to associate with a device resource.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class GlobalNetworkTagArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        A key-value pair to associate with a global network resource.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class LinkBandwidthArgs:
    def __init__(__self__, *,
                 download_speed: Optional[pulumi.Input[int]] = None,
                 upload_speed: Optional[pulumi.Input[int]] = None):
        """
        The bandwidth for the link.
        :param pulumi.Input[int] download_speed: Download speed in Mbps.
        :param pulumi.Input[int] upload_speed: Upload speed in Mbps.
        """
        if download_speed is not None:
            pulumi.set(__self__, "download_speed", download_speed)
        if upload_speed is not None:
            pulumi.set(__self__, "upload_speed", upload_speed)

    @property
    @pulumi.getter(name="downloadSpeed")
    def download_speed(self) -> Optional[pulumi.Input[int]]:
        """
        Download speed in Mbps.
        """
        return pulumi.get(self, "download_speed")

    @download_speed.setter
    def download_speed(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "download_speed", value)

    @property
    @pulumi.getter(name="uploadSpeed")
    def upload_speed(self) -> Optional[pulumi.Input[int]]:
        """
        Upload speed in Mbps.
        """
        return pulumi.get(self, "upload_speed")

    @upload_speed.setter
    def upload_speed(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "upload_speed", value)


@pulumi.input_type
class LinkTagArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        A key-value pair to associate with a link resource.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class SiteLocationArgs:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None,
                 latitude: Optional[pulumi.Input[str]] = None,
                 longitude: Optional[pulumi.Input[str]] = None):
        """
        The location of the site
        :param pulumi.Input[str] address: The physical address.
        :param pulumi.Input[str] latitude: The latitude.
        :param pulumi.Input[str] longitude: The longitude.
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if latitude is not None:
            pulumi.set(__self__, "latitude", latitude)
        if longitude is not None:
            pulumi.set(__self__, "longitude", longitude)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        """
        The physical address.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def latitude(self) -> Optional[pulumi.Input[str]]:
        """
        The latitude.
        """
        return pulumi.get(self, "latitude")

    @latitude.setter
    def latitude(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "latitude", value)

    @property
    @pulumi.getter
    def longitude(self) -> Optional[pulumi.Input[str]]:
        """
        The longitude.
        """
        return pulumi.get(self, "longitude")

    @longitude.setter
    def longitude(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "longitude", value)


@pulumi.input_type
class SiteTagArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        A key-value pair to associate with a site resource.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class SiteToSiteVpnAttachmentTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class VpcAttachmentTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class VpcAttachmentVpcOptionsArgs:
    def __init__(__self__, *,
                 appliance_mode_support: Optional[pulumi.Input[bool]] = None,
                 ipv6_support: Optional[pulumi.Input[bool]] = None):
        """
        Vpc options of the attachment.
        :param pulumi.Input[bool] appliance_mode_support: Indicates whether to enable ApplianceModeSupport Support for Vpc Attachment. Valid Values: true | false
        :param pulumi.Input[bool] ipv6_support: Indicates whether to enable Ipv6 Support for Vpc Attachment. Valid Values: enable | disable
        """
        if appliance_mode_support is not None:
            pulumi.set(__self__, "appliance_mode_support", appliance_mode_support)
        if ipv6_support is not None:
            pulumi.set(__self__, "ipv6_support", ipv6_support)

    @property
    @pulumi.getter(name="applianceModeSupport")
    def appliance_mode_support(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether to enable ApplianceModeSupport Support for Vpc Attachment. Valid Values: true | false
        """
        return pulumi.get(self, "appliance_mode_support")

    @appliance_mode_support.setter
    def appliance_mode_support(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "appliance_mode_support", value)

    @property
    @pulumi.getter(name="ipv6Support")
    def ipv6_support(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether to enable Ipv6 Support for Vpc Attachment. Valid Values: enable | disable
        """
        return pulumi.get(self, "ipv6_support")

    @ipv6_support.setter
    def ipv6_support(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ipv6_support", value)


