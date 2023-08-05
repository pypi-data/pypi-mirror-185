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
from ._inputs import *

__all__ = ['FormArgs', 'Form']

@pulumi.input_type
class FormArgs:
    def __init__(__self__, *,
                 data_type: pulumi.Input['FormDataTypeConfigArgs'],
                 fields: pulumi.Input['FormFieldsMapArgs'],
                 form_action_type: pulumi.Input['FormActionType'],
                 schema_version: pulumi.Input[str],
                 sectional_elements: pulumi.Input['FormSectionalElementMapArgs'],
                 style: pulumi.Input['FormStyleArgs'],
                 app_id: Optional[pulumi.Input[str]] = None,
                 cta: Optional[pulumi.Input['FormCTAArgs']] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input['FormTagsArgs']] = None):
        """
        The set of arguments for constructing a Form resource.
        """
        pulumi.set(__self__, "data_type", data_type)
        pulumi.set(__self__, "fields", fields)
        pulumi.set(__self__, "form_action_type", form_action_type)
        pulumi.set(__self__, "schema_version", schema_version)
        pulumi.set(__self__, "sectional_elements", sectional_elements)
        pulumi.set(__self__, "style", style)
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if cta is not None:
            pulumi.set(__self__, "cta", cta)
        if environment_name is not None:
            pulumi.set(__self__, "environment_name", environment_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input['FormDataTypeConfigArgs']:
        return pulumi.get(self, "data_type")

    @data_type.setter
    def data_type(self, value: pulumi.Input['FormDataTypeConfigArgs']):
        pulumi.set(self, "data_type", value)

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Input['FormFieldsMapArgs']:
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: pulumi.Input['FormFieldsMapArgs']):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter(name="formActionType")
    def form_action_type(self) -> pulumi.Input['FormActionType']:
        return pulumi.get(self, "form_action_type")

    @form_action_type.setter
    def form_action_type(self, value: pulumi.Input['FormActionType']):
        pulumi.set(self, "form_action_type", value)

    @property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> pulumi.Input[str]:
        return pulumi.get(self, "schema_version")

    @schema_version.setter
    def schema_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "schema_version", value)

    @property
    @pulumi.getter(name="sectionalElements")
    def sectional_elements(self) -> pulumi.Input['FormSectionalElementMapArgs']:
        return pulumi.get(self, "sectional_elements")

    @sectional_elements.setter
    def sectional_elements(self, value: pulumi.Input['FormSectionalElementMapArgs']):
        pulumi.set(self, "sectional_elements", value)

    @property
    @pulumi.getter
    def style(self) -> pulumi.Input['FormStyleArgs']:
        return pulumi.get(self, "style")

    @style.setter
    def style(self, value: pulumi.Input['FormStyleArgs']):
        pulumi.set(self, "style", value)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter
    def cta(self) -> Optional[pulumi.Input['FormCTAArgs']]:
        return pulumi.get(self, "cta")

    @cta.setter
    def cta(self, value: Optional[pulumi.Input['FormCTAArgs']]):
        pulumi.set(self, "cta", value)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input['FormTagsArgs']]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input['FormTagsArgs']]):
        pulumi.set(self, "tags", value)


class Form(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 cta: Optional[pulumi.Input[pulumi.InputType['FormCTAArgs']]] = None,
                 data_type: Optional[pulumi.Input[pulumi.InputType['FormDataTypeConfigArgs']]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[pulumi.InputType['FormFieldsMapArgs']]] = None,
                 form_action_type: Optional[pulumi.Input['FormActionType']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema_version: Optional[pulumi.Input[str]] = None,
                 sectional_elements: Optional[pulumi.Input[pulumi.InputType['FormSectionalElementMapArgs']]] = None,
                 style: Optional[pulumi.Input[pulumi.InputType['FormStyleArgs']]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['FormTagsArgs']]] = None,
                 __props__=None):
        """
        Definition of AWS::AmplifyUIBuilder::Form Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FormArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::AmplifyUIBuilder::Form Resource Type

        :param str resource_name: The name of the resource.
        :param FormArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FormArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 cta: Optional[pulumi.Input[pulumi.InputType['FormCTAArgs']]] = None,
                 data_type: Optional[pulumi.Input[pulumi.InputType['FormDataTypeConfigArgs']]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[pulumi.InputType['FormFieldsMapArgs']]] = None,
                 form_action_type: Optional[pulumi.Input['FormActionType']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema_version: Optional[pulumi.Input[str]] = None,
                 sectional_elements: Optional[pulumi.Input[pulumi.InputType['FormSectionalElementMapArgs']]] = None,
                 style: Optional[pulumi.Input[pulumi.InputType['FormStyleArgs']]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['FormTagsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FormArgs.__new__(FormArgs)

            __props__.__dict__["app_id"] = app_id
            __props__.__dict__["cta"] = cta
            if data_type is None and not opts.urn:
                raise TypeError("Missing required property 'data_type'")
            __props__.__dict__["data_type"] = data_type
            __props__.__dict__["environment_name"] = environment_name
            if fields is None and not opts.urn:
                raise TypeError("Missing required property 'fields'")
            __props__.__dict__["fields"] = fields
            if form_action_type is None and not opts.urn:
                raise TypeError("Missing required property 'form_action_type'")
            __props__.__dict__["form_action_type"] = form_action_type
            __props__.__dict__["name"] = name
            if schema_version is None and not opts.urn:
                raise TypeError("Missing required property 'schema_version'")
            __props__.__dict__["schema_version"] = schema_version
            if sectional_elements is None and not opts.urn:
                raise TypeError("Missing required property 'sectional_elements'")
            __props__.__dict__["sectional_elements"] = sectional_elements
            if style is None and not opts.urn:
                raise TypeError("Missing required property 'style'")
            __props__.__dict__["style"] = style
            __props__.__dict__["tags"] = tags
        super(Form, __self__).__init__(
            'aws-native:amplifyuibuilder:Form',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Form':
        """
        Get an existing Form resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FormArgs.__new__(FormArgs)

        __props__.__dict__["app_id"] = None
        __props__.__dict__["cta"] = None
        __props__.__dict__["data_type"] = None
        __props__.__dict__["environment_name"] = None
        __props__.__dict__["fields"] = None
        __props__.__dict__["form_action_type"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["schema_version"] = None
        __props__.__dict__["sectional_elements"] = None
        __props__.__dict__["style"] = None
        __props__.__dict__["tags"] = None
        return Form(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def cta(self) -> pulumi.Output[Optional['outputs.FormCTA']]:
        return pulumi.get(self, "cta")

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Output['outputs.FormDataTypeConfig']:
        return pulumi.get(self, "data_type")

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "environment_name")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output['outputs.FormFieldsMap']:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter(name="formActionType")
    def form_action_type(self) -> pulumi.Output['FormActionType']:
        return pulumi.get(self, "form_action_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "schema_version")

    @property
    @pulumi.getter(name="sectionalElements")
    def sectional_elements(self) -> pulumi.Output['outputs.FormSectionalElementMap']:
        return pulumi.get(self, "sectional_elements")

    @property
    @pulumi.getter
    def style(self) -> pulumi.Output['outputs.FormStyle']:
        return pulumi.get(self, "style")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional['outputs.FormTags']]:
        return pulumi.get(self, "tags")

