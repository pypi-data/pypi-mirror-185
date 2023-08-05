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
    'AccessPointVpcConfiguration',
    'BucketAbortIncompleteMultipartUpload',
    'BucketFilterAndOperator',
    'BucketFilterTag',
    'BucketLifecycleConfiguration',
    'BucketRule',
    'BucketRuleFilterProperties',
    'BucketTag',
    'EndpointNetworkInterface',
]

@pulumi.output_type
class AccessPointVpcConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "vpcId":
            suggest = "vpc_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccessPointVpcConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccessPointVpcConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccessPointVpcConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 vpc_id: Optional[str] = None):
        """
        :param str vpc_id: Virtual Private Cloud (VPC) Id from which AccessPoint will allow requests.
        """
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        """
        Virtual Private Cloud (VPC) Id from which AccessPoint will allow requests.
        """
        return pulumi.get(self, "vpc_id")


@pulumi.output_type
class BucketAbortIncompleteMultipartUpload(dict):
    """
    Specifies the days since the initiation of an incomplete multipart upload that Amazon S3Outposts will wait before permanently removing all parts of the upload.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "daysAfterInitiation":
            suggest = "days_after_initiation"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BucketAbortIncompleteMultipartUpload. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BucketAbortIncompleteMultipartUpload.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BucketAbortIncompleteMultipartUpload.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 days_after_initiation: int):
        """
        Specifies the days since the initiation of an incomplete multipart upload that Amazon S3Outposts will wait before permanently removing all parts of the upload.
        :param int days_after_initiation: Specifies the number of days after which Amazon S3Outposts aborts an incomplete multipart upload.
        """
        pulumi.set(__self__, "days_after_initiation", days_after_initiation)

    @property
    @pulumi.getter(name="daysAfterInitiation")
    def days_after_initiation(self) -> int:
        """
        Specifies the number of days after which Amazon S3Outposts aborts an incomplete multipart upload.
        """
        return pulumi.get(self, "days_after_initiation")


@pulumi.output_type
class BucketFilterAndOperator(dict):
    def __init__(__self__):
        pass


@pulumi.output_type
class BucketFilterTag(dict):
    """
    Tag used to identify a subset of objects for an Amazon S3Outposts bucket.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        Tag used to identify a subset of objects for an Amazon S3Outposts bucket.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class BucketLifecycleConfiguration(dict):
    def __init__(__self__, *,
                 rules: Sequence['outputs.BucketRule']):
        """
        :param Sequence['BucketRule'] rules: A list of lifecycle rules for individual objects in an Amazon S3Outposts bucket.
        """
        pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.BucketRule']:
        """
        A list of lifecycle rules for individual objects in an Amazon S3Outposts bucket.
        """
        return pulumi.get(self, "rules")


@pulumi.output_type
class BucketRule(dict):
    """
    Specifies lifecycle rules for an Amazon S3Outposts bucket. You must specify at least one of the following: AbortIncompleteMultipartUpload, ExpirationDate, ExpirationInDays.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "abortIncompleteMultipartUpload":
            suggest = "abort_incomplete_multipart_upload"
        elif key == "expirationDate":
            suggest = "expiration_date"
        elif key == "expirationInDays":
            suggest = "expiration_in_days"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BucketRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BucketRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BucketRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 abort_incomplete_multipart_upload: Optional['outputs.BucketAbortIncompleteMultipartUpload'] = None,
                 expiration_date: Optional[str] = None,
                 expiration_in_days: Optional[int] = None,
                 filter: Optional['outputs.BucketRuleFilterProperties'] = None,
                 id: Optional[str] = None,
                 status: Optional['BucketRuleStatus'] = None):
        """
        Specifies lifecycle rules for an Amazon S3Outposts bucket. You must specify at least one of the following: AbortIncompleteMultipartUpload, ExpirationDate, ExpirationInDays.
        :param 'BucketAbortIncompleteMultipartUpload' abort_incomplete_multipart_upload: Specifies a lifecycle rule that stops incomplete multipart uploads to an Amazon S3Outposts bucket.
        :param str expiration_date: Indicates when objects are deleted from Amazon S3Outposts. The date value must be in ISO 8601 format. The time is always midnight UTC.
        :param int expiration_in_days: Indicates the number of days after creation when objects are deleted from Amazon S3Outposts.
        :param 'BucketRuleFilterProperties' filter: The container for the filter of the lifecycle rule.
        :param str id: Unique identifier for the lifecycle rule. The value can't be longer than 255 characters.
        """
        if abort_incomplete_multipart_upload is not None:
            pulumi.set(__self__, "abort_incomplete_multipart_upload", abort_incomplete_multipart_upload)
        if expiration_date is not None:
            pulumi.set(__self__, "expiration_date", expiration_date)
        if expiration_in_days is not None:
            pulumi.set(__self__, "expiration_in_days", expiration_in_days)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="abortIncompleteMultipartUpload")
    def abort_incomplete_multipart_upload(self) -> Optional['outputs.BucketAbortIncompleteMultipartUpload']:
        """
        Specifies a lifecycle rule that stops incomplete multipart uploads to an Amazon S3Outposts bucket.
        """
        return pulumi.get(self, "abort_incomplete_multipart_upload")

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[str]:
        """
        Indicates when objects are deleted from Amazon S3Outposts. The date value must be in ISO 8601 format. The time is always midnight UTC.
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter(name="expirationInDays")
    def expiration_in_days(self) -> Optional[int]:
        """
        Indicates the number of days after creation when objects are deleted from Amazon S3Outposts.
        """
        return pulumi.get(self, "expiration_in_days")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.BucketRuleFilterProperties']:
        """
        The container for the filter of the lifecycle rule.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Unique identifier for the lifecycle rule. The value can't be longer than 255 characters.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def status(self) -> Optional['BucketRuleStatus']:
        return pulumi.get(self, "status")


@pulumi.output_type
class BucketRuleFilterProperties(dict):
    """
    The container for the filter of the lifecycle rule.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "andOperator":
            suggest = "and_operator"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BucketRuleFilterProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BucketRuleFilterProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BucketRuleFilterProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 and_operator: Optional['outputs.BucketFilterAndOperator'] = None,
                 prefix: Optional[str] = None,
                 tag: Optional['outputs.BucketFilterTag'] = None):
        """
        The container for the filter of the lifecycle rule.
        :param 'BucketFilterAndOperator' and_operator: The container for the AND condition for the lifecycle rule. A combination of Prefix and 1 or more Tags OR a minimum of 2 or more tags.
        :param str prefix: Object key prefix that identifies one or more objects to which this rule applies.
        :param 'BucketFilterTag' tag: Specifies a tag used to identify a subset of objects for an Amazon S3Outposts bucket.
        """
        if and_operator is not None:
            pulumi.set(__self__, "and_operator", and_operator)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)
        if tag is not None:
            pulumi.set(__self__, "tag", tag)

    @property
    @pulumi.getter(name="andOperator")
    def and_operator(self) -> Optional['outputs.BucketFilterAndOperator']:
        """
        The container for the AND condition for the lifecycle rule. A combination of Prefix and 1 or more Tags OR a minimum of 2 or more tags.
        """
        return pulumi.get(self, "and_operator")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        """
        Object key prefix that identifies one or more objects to which this rule applies.
        """
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter
    def tag(self) -> Optional['outputs.BucketFilterTag']:
        """
        Specifies a tag used to identify a subset of objects for an Amazon S3Outposts bucket.
        """
        return pulumi.get(self, "tag")


@pulumi.output_type
class BucketTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class EndpointNetworkInterface(dict):
    """
    The container for the network interface.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "networkInterfaceId":
            suggest = "network_interface_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointNetworkInterface. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointNetworkInterface.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointNetworkInterface.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 network_interface_id: str):
        """
        The container for the network interface.
        """
        pulumi.set(__self__, "network_interface_id", network_interface_id)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> str:
        return pulumi.get(self, "network_interface_id")


