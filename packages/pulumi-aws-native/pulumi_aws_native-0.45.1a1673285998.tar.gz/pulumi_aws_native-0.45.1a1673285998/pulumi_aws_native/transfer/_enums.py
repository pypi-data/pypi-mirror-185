# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AgreementStatus',
    'CertificateStatus',
    'CertificateType',
    'CertificateUsage',
    'ConnectorAs2ConfigPropertiesCompression',
    'ConnectorAs2ConfigPropertiesEncryptionAlgorithm',
    'ConnectorAs2ConfigPropertiesMdnResponse',
    'ConnectorAs2ConfigPropertiesMdnSigningAlgorithm',
    'ConnectorAs2ConfigPropertiesSigningAlgorithm',
    'ProfileType',
    'WorkflowStepCopyStepDetailsPropertiesOverwriteExisting',
    'WorkflowStepType',
]


class AgreementStatus(str, Enum):
    """
    Specifies the status of the agreement.
    """
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class CertificateStatus(str, Enum):
    """
    A status description for the certificate.
    """
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    INACTIVE = "INACTIVE"


class CertificateType(str, Enum):
    """
    Describing the type of certificate. With or without a private key.
    """
    CERTIFICATE = "CERTIFICATE"
    CERTIFICATE_WITH_PRIVATE_KEY = "CERTIFICATE_WITH_PRIVATE_KEY"


class CertificateUsage(str, Enum):
    """
    Specifies the usage type for the certificate.
    """
    SIGNING = "SIGNING"
    ENCRYPTION = "ENCRYPTION"


class ConnectorAs2ConfigPropertiesCompression(str, Enum):
    """
    Compression setting for this AS2 connector configuration.
    """
    ZLIB = "ZLIB"
    DISABLED = "DISABLED"


class ConnectorAs2ConfigPropertiesEncryptionAlgorithm(str, Enum):
    """
    Encryption algorithm for this AS2 connector configuration.
    """
    AES128_CBC = "AES128_CBC"
    AES192_CBC = "AES192_CBC"
    AES256_CBC = "AES256_CBC"
    NONE = "NONE"


class ConnectorAs2ConfigPropertiesMdnResponse(str, Enum):
    """
    MDN Response setting for this AS2 connector configuration.
    """
    SYNC = "SYNC"
    NONE = "NONE"


class ConnectorAs2ConfigPropertiesMdnSigningAlgorithm(str, Enum):
    """
    MDN Signing algorithm for this AS2 connector configuration.
    """
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"
    SHA1 = "SHA1"
    NONE = "NONE"
    DEFAULT = "DEFAULT"


class ConnectorAs2ConfigPropertiesSigningAlgorithm(str, Enum):
    """
    Signing algorithm for this AS2 connector configuration.
    """
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"
    SHA1 = "SHA1"
    NONE = "NONE"


class ProfileType(str, Enum):
    """
    Enum specifying whether the profile is local or associated with a trading partner.
    """
    LOCAL = "LOCAL"
    PARTNER = "PARTNER"


class WorkflowStepCopyStepDetailsPropertiesOverwriteExisting(str, Enum):
    """
    A flag that indicates whether or not to overwrite an existing file of the same name. The default is FALSE.
    """
    TRUE = "TRUE"
    FALSE = "FALSE"


class WorkflowStepType(str, Enum):
    COPY = "COPY"
    CUSTOM = "CUSTOM"
    DELETE = "DELETE"
    TAG = "TAG"
