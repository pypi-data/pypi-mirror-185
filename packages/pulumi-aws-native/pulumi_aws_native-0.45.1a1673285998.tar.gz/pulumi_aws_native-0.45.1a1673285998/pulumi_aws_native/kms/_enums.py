# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'KeySpec',
    'KeyUsage',
]


class KeySpec(str, Enum):
    """
    Specifies the type of AWS KMS key to create. The default value is SYMMETRIC_DEFAULT. This property is required only for asymmetric AWS KMS keys. You can't change the KeySpec value after the AWS KMS key is created.
    """
    SYMMETRIC_DEFAULT = "SYMMETRIC_DEFAULT"
    RSA2048 = "RSA_2048"
    RSA3072 = "RSA_3072"
    RSA4096 = "RSA_4096"
    ECC_NIST_P256 = "ECC_NIST_P256"
    ECC_NIST_P384 = "ECC_NIST_P384"
    ECC_NIST_P521 = "ECC_NIST_P521"
    ECC_SECG_P256K1 = "ECC_SECG_P256K1"
    HMAC224 = "HMAC_224"
    HMAC256 = "HMAC_256"
    HMAC384 = "HMAC_384"
    HMAC512 = "HMAC_512"
    SM2 = "SM2"


class KeyUsage(str, Enum):
    """
    Determines the cryptographic operations for which you can use the AWS KMS key. The default value is ENCRYPT_DECRYPT. This property is required only for asymmetric AWS KMS keys. You can't change the KeyUsage value after the AWS KMS key is created.
    """
    ENCRYPT_DECRYPT = "ENCRYPT_DECRYPT"
    SIGN_VERIFY = "SIGN_VERIFY"
    GENERATE_VERIFY_MAC = "GENERATE_VERIFY_MAC"
