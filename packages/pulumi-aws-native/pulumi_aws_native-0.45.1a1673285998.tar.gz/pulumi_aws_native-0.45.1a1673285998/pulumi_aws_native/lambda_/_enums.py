# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CodeSigningConfigCodeSigningPoliciesUntrustedArtifactOnDeployment',
    'EventSourceMappingFunctionResponseTypesItem',
    'EventSourceMappingSourceAccessConfigurationType',
    'FunctionArchitecturesItem',
    'FunctionPackageType',
    'FunctionSnapStartApplyOn',
    'FunctionSnapStartResponseApplyOn',
    'FunctionSnapStartResponseOptimizationStatus',
    'FunctionTracingConfigMode',
    'UrlAllowMethodsItem',
    'UrlAuthType',
    'UrlInvokeMode',
]


class CodeSigningConfigCodeSigningPoliciesUntrustedArtifactOnDeployment(str, Enum):
    """
    Indicates how Lambda operations involve updating the code artifact will operate. Default to Warn if not provided
    """
    WARN = "Warn"
    ENFORCE = "Enforce"


class EventSourceMappingFunctionResponseTypesItem(str, Enum):
    REPORT_BATCH_ITEM_FAILURES = "ReportBatchItemFailures"


class EventSourceMappingSourceAccessConfigurationType(str, Enum):
    """
    The type of source access configuration.
    """
    BASIC_AUTH = "BASIC_AUTH"
    VPC_SUBNET = "VPC_SUBNET"
    VPC_SECURITY_GROUP = "VPC_SECURITY_GROUP"
    SASL_SCRAM512_AUTH = "SASL_SCRAM_512_AUTH"
    SASL_SCRAM256_AUTH = "SASL_SCRAM_256_AUTH"
    VIRTUAL_HOST = "VIRTUAL_HOST"
    CLIENT_CERTIFICATE_TLS_AUTH = "CLIENT_CERTIFICATE_TLS_AUTH"
    SERVER_ROOT_CA_CERTIFICATE = "SERVER_ROOT_CA_CERTIFICATE"


class FunctionArchitecturesItem(str, Enum):
    X8664 = "x86_64"
    ARM64 = "arm64"


class FunctionPackageType(str, Enum):
    """
    PackageType.
    """
    IMAGE = "Image"
    ZIP = "Zip"


class FunctionSnapStartApplyOn(str, Enum):
    """
    Applying SnapStart setting on function resource type.
    """
    PUBLISHED_VERSIONS = "PublishedVersions"
    NONE = "None"


class FunctionSnapStartResponseApplyOn(str, Enum):
    """
    Applying SnapStart setting on function resource type.
    """
    PUBLISHED_VERSIONS = "PublishedVersions"
    NONE = "None"


class FunctionSnapStartResponseOptimizationStatus(str, Enum):
    """
    Indicates whether SnapStart is activated for the specified function version.
    """
    ON = "On"
    OFF = "Off"


class FunctionTracingConfigMode(str, Enum):
    """
    The tracing mode.
    """
    ACTIVE = "Active"
    PASS_THROUGH = "PassThrough"


class UrlAllowMethodsItem(str, Enum):
    GET = "GET"
    PUT = "PUT"
    HEAD = "HEAD"
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"
    ASTERISK = "*"


class UrlAuthType(str, Enum):
    """
    Can be either AWS_IAM if the requests are authorized via IAM, or NONE if no authorization is configured on the Function URL.
    """
    AWS_IAM = "AWS_IAM"
    NONE = "NONE"


class UrlInvokeMode(str, Enum):
    """
    The invocation mode for the function’s URL. Set to BUFFERED if you want to buffer responses before returning them to the client. Set to RESPONSE_STREAM if you want to stream responses, allowing faster time to first byte and larger response payload sizes. If not set, defaults to BUFFERED.
    """
    BUFFERED = "BUFFERED"
    RESPONSE_STREAM = "RESPONSE_STREAM"
