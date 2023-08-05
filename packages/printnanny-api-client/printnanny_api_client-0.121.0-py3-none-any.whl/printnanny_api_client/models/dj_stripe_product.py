# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.121.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from printnanny_api_client.configuration import Configuration


class DjStripeProduct(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'djstripe_id': 'int',
        'djstripe_created': 'datetime',
        'djstripe_updated': 'datetime',
        'id': 'str',
        'livemode': 'bool',
        'created': 'datetime',
        'metadata': 'dict(str, object)',
        'description': 'str',
        'name': 'str',
        'type': 'StripeProductType',
        'active': 'bool',
        'attributes': 'dict(str, object)',
        'caption': 'str',
        'deactivate_on': 'dict(str, object)',
        'images': 'dict(str, object)',
        'package_dimensions': 'dict(str, object)',
        'shippable': 'bool',
        'url': 'str',
        'statement_descriptor': 'str',
        'unit_label': 'str',
        'djstripe_owner_account': 'str'
    }

    attribute_map = {
        'djstripe_id': 'djstripe_id',
        'djstripe_created': 'djstripe_created',
        'djstripe_updated': 'djstripe_updated',
        'id': 'id',
        'livemode': 'livemode',
        'created': 'created',
        'metadata': 'metadata',
        'description': 'description',
        'name': 'name',
        'type': 'type',
        'active': 'active',
        'attributes': 'attributes',
        'caption': 'caption',
        'deactivate_on': 'deactivate_on',
        'images': 'images',
        'package_dimensions': 'package_dimensions',
        'shippable': 'shippable',
        'url': 'url',
        'statement_descriptor': 'statement_descriptor',
        'unit_label': 'unit_label',
        'djstripe_owner_account': 'djstripe_owner_account'
    }

    def __init__(self, djstripe_id=None, djstripe_created=None, djstripe_updated=None, id=None, livemode=None, created=None, metadata=None, description=None, name=None, type=None, active=None, attributes=None, caption=None, deactivate_on=None, images=None, package_dimensions=None, shippable=None, url=None, statement_descriptor=None, unit_label=None, djstripe_owner_account=None, local_vars_configuration=None):  # noqa: E501
        """DjStripeProduct - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._djstripe_id = None
        self._djstripe_created = None
        self._djstripe_updated = None
        self._id = None
        self._livemode = None
        self._created = None
        self._metadata = None
        self._description = None
        self._name = None
        self._type = None
        self._active = None
        self._attributes = None
        self._caption = None
        self._deactivate_on = None
        self._images = None
        self._package_dimensions = None
        self._shippable = None
        self._url = None
        self._statement_descriptor = None
        self._unit_label = None
        self._djstripe_owner_account = None
        self.discriminator = None

        self.djstripe_id = djstripe_id
        self.djstripe_created = djstripe_created
        self.djstripe_updated = djstripe_updated
        self.id = id
        self.livemode = livemode
        self.created = created
        self.metadata = metadata
        self.description = description
        self.name = name
        self.type = type
        self.active = active
        self.attributes = attributes
        if caption is not None:
            self.caption = caption
        self.deactivate_on = deactivate_on
        self.images = images
        self.package_dimensions = package_dimensions
        self.shippable = shippable
        self.url = url
        if statement_descriptor is not None:
            self.statement_descriptor = statement_descriptor
        if unit_label is not None:
            self.unit_label = unit_label
        self.djstripe_owner_account = djstripe_owner_account

    @property
    def djstripe_id(self):
        """Gets the djstripe_id of this DjStripeProduct.  # noqa: E501


        :return: The djstripe_id of this DjStripeProduct.  # noqa: E501
        :rtype: int
        """
        return self._djstripe_id

    @djstripe_id.setter
    def djstripe_id(self, djstripe_id):
        """Sets the djstripe_id of this DjStripeProduct.


        :param djstripe_id: The djstripe_id of this DjStripeProduct.  # noqa: E501
        :type djstripe_id: int
        """
        if self.local_vars_configuration.client_side_validation and djstripe_id is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_id`, must not be `None`")  # noqa: E501

        self._djstripe_id = djstripe_id

    @property
    def djstripe_created(self):
        """Gets the djstripe_created of this DjStripeProduct.  # noqa: E501


        :return: The djstripe_created of this DjStripeProduct.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_created

    @djstripe_created.setter
    def djstripe_created(self, djstripe_created):
        """Sets the djstripe_created of this DjStripeProduct.


        :param djstripe_created: The djstripe_created of this DjStripeProduct.  # noqa: E501
        :type djstripe_created: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_created is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_created`, must not be `None`")  # noqa: E501

        self._djstripe_created = djstripe_created

    @property
    def djstripe_updated(self):
        """Gets the djstripe_updated of this DjStripeProduct.  # noqa: E501


        :return: The djstripe_updated of this DjStripeProduct.  # noqa: E501
        :rtype: datetime
        """
        return self._djstripe_updated

    @djstripe_updated.setter
    def djstripe_updated(self, djstripe_updated):
        """Sets the djstripe_updated of this DjStripeProduct.


        :param djstripe_updated: The djstripe_updated of this DjStripeProduct.  # noqa: E501
        :type djstripe_updated: datetime
        """
        if self.local_vars_configuration.client_side_validation and djstripe_updated is None:  # noqa: E501
            raise ValueError("Invalid value for `djstripe_updated`, must not be `None`")  # noqa: E501

        self._djstripe_updated = djstripe_updated

    @property
    def id(self):
        """Gets the id of this DjStripeProduct.  # noqa: E501


        :return: The id of this DjStripeProduct.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DjStripeProduct.


        :param id: The id of this DjStripeProduct.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 255):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501

        self._id = id

    @property
    def livemode(self):
        """Gets the livemode of this DjStripeProduct.  # noqa: E501

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :return: The livemode of this DjStripeProduct.  # noqa: E501
        :rtype: bool
        """
        return self._livemode

    @livemode.setter
    def livemode(self, livemode):
        """Sets the livemode of this DjStripeProduct.

        Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.  # noqa: E501

        :param livemode: The livemode of this DjStripeProduct.  # noqa: E501
        :type livemode: bool
        """

        self._livemode = livemode

    @property
    def created(self):
        """Gets the created of this DjStripeProduct.  # noqa: E501

        The datetime this object was created in stripe.  # noqa: E501

        :return: The created of this DjStripeProduct.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DjStripeProduct.

        The datetime this object was created in stripe.  # noqa: E501

        :param created: The created of this DjStripeProduct.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def metadata(self):
        """Gets the metadata of this DjStripeProduct.  # noqa: E501

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :return: The metadata of this DjStripeProduct.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DjStripeProduct.

        A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.  # noqa: E501

        :param metadata: The metadata of this DjStripeProduct.  # noqa: E501
        :type metadata: dict(str, object)
        """

        self._metadata = metadata

    @property
    def description(self):
        """Gets the description of this DjStripeProduct.  # noqa: E501

        A description of this object.  # noqa: E501

        :return: The description of this DjStripeProduct.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DjStripeProduct.

        A description of this object.  # noqa: E501

        :param description: The description of this DjStripeProduct.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this DjStripeProduct.  # noqa: E501

        The product's name, meant to be displayable to the customer. Applicable to both `service` and `good` types.  # noqa: E501

        :return: The name of this DjStripeProduct.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DjStripeProduct.

        The product's name, meant to be displayable to the customer. Applicable to both `service` and `good` types.  # noqa: E501

        :param name: The name of this DjStripeProduct.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 5000):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `5000`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this DjStripeProduct.  # noqa: E501

        The type of the product. The product is either of type `good`, which is eligible for use with Orders and SKUs, or `service`, which is eligible for use with Subscriptions and Plans.  # noqa: E501

        :return: The type of this DjStripeProduct.  # noqa: E501
        :rtype: StripeProductType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DjStripeProduct.

        The type of the product. The product is either of type `good`, which is eligible for use with Orders and SKUs, or `service`, which is eligible for use with Subscriptions and Plans.  # noqa: E501

        :param type: The type of this DjStripeProduct.  # noqa: E501
        :type type: StripeProductType
        """

        self._type = type

    @property
    def active(self):
        """Gets the active of this DjStripeProduct.  # noqa: E501

        Whether the product is currently available for purchase. Only applicable to products of `type=good`.  # noqa: E501

        :return: The active of this DjStripeProduct.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this DjStripeProduct.

        Whether the product is currently available for purchase. Only applicable to products of `type=good`.  # noqa: E501

        :param active: The active of this DjStripeProduct.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def attributes(self):
        """Gets the attributes of this DjStripeProduct.  # noqa: E501

        A list of up to 5 attributes that each SKU can provide values for (e.g., `[\"color\", \"size\"]`). Only applicable to products of `type=good`.  # noqa: E501

        :return: The attributes of this DjStripeProduct.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this DjStripeProduct.

        A list of up to 5 attributes that each SKU can provide values for (e.g., `[\"color\", \"size\"]`). Only applicable to products of `type=good`.  # noqa: E501

        :param attributes: The attributes of this DjStripeProduct.  # noqa: E501
        :type attributes: dict(str, object)
        """

        self._attributes = attributes

    @property
    def caption(self):
        """Gets the caption of this DjStripeProduct.  # noqa: E501

        A short one-line description of the product, meant to be displayableto the customer. Only applicable to products of `type=good`.  # noqa: E501

        :return: The caption of this DjStripeProduct.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this DjStripeProduct.

        A short one-line description of the product, meant to be displayableto the customer. Only applicable to products of `type=good`.  # noqa: E501

        :param caption: The caption of this DjStripeProduct.  # noqa: E501
        :type caption: str
        """
        if (self.local_vars_configuration.client_side_validation and
                caption is not None and len(caption) > 5000):
            raise ValueError("Invalid value for `caption`, length must be less than or equal to `5000`")  # noqa: E501

        self._caption = caption

    @property
    def deactivate_on(self):
        """Gets the deactivate_on of this DjStripeProduct.  # noqa: E501

        An array of connect application identifiers that cannot purchase this product. Only applicable to products of `type=good`.  # noqa: E501

        :return: The deactivate_on of this DjStripeProduct.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._deactivate_on

    @deactivate_on.setter
    def deactivate_on(self, deactivate_on):
        """Sets the deactivate_on of this DjStripeProduct.

        An array of connect application identifiers that cannot purchase this product. Only applicable to products of `type=good`.  # noqa: E501

        :param deactivate_on: The deactivate_on of this DjStripeProduct.  # noqa: E501
        :type deactivate_on: dict(str, object)
        """

        self._deactivate_on = deactivate_on

    @property
    def images(self):
        """Gets the images of this DjStripeProduct.  # noqa: E501

        A list of up to 8 URLs of images for this product, meant to be displayable to the customer. Only applicable to products of `type=good`.  # noqa: E501

        :return: The images of this DjStripeProduct.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this DjStripeProduct.

        A list of up to 8 URLs of images for this product, meant to be displayable to the customer. Only applicable to products of `type=good`.  # noqa: E501

        :param images: The images of this DjStripeProduct.  # noqa: E501
        :type images: dict(str, object)
        """

        self._images = images

    @property
    def package_dimensions(self):
        """Gets the package_dimensions of this DjStripeProduct.  # noqa: E501

        The dimensions of this product for shipping purposes. A SKU associated with this product can override this value by having its own `package_dimensions`. Only applicable to products of `type=good`.  # noqa: E501

        :return: The package_dimensions of this DjStripeProduct.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._package_dimensions

    @package_dimensions.setter
    def package_dimensions(self, package_dimensions):
        """Sets the package_dimensions of this DjStripeProduct.

        The dimensions of this product for shipping purposes. A SKU associated with this product can override this value by having its own `package_dimensions`. Only applicable to products of `type=good`.  # noqa: E501

        :param package_dimensions: The package_dimensions of this DjStripeProduct.  # noqa: E501
        :type package_dimensions: dict(str, object)
        """

        self._package_dimensions = package_dimensions

    @property
    def shippable(self):
        """Gets the shippable of this DjStripeProduct.  # noqa: E501

        Whether this product is a shipped good. Only applicable to products of `type=good`.  # noqa: E501

        :return: The shippable of this DjStripeProduct.  # noqa: E501
        :rtype: bool
        """
        return self._shippable

    @shippable.setter
    def shippable(self, shippable):
        """Sets the shippable of this DjStripeProduct.

        Whether this product is a shipped good. Only applicable to products of `type=good`.  # noqa: E501

        :param shippable: The shippable of this DjStripeProduct.  # noqa: E501
        :type shippable: bool
        """

        self._shippable = shippable

    @property
    def url(self):
        """Gets the url of this DjStripeProduct.  # noqa: E501

        A URL of a publicly-accessible webpage for this product. Only applicable to products of `type=good`.  # noqa: E501

        :return: The url of this DjStripeProduct.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DjStripeProduct.

        A URL of a publicly-accessible webpage for this product. Only applicable to products of `type=good`.  # noqa: E501

        :param url: The url of this DjStripeProduct.  # noqa: E501
        :type url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) > 799):
            raise ValueError("Invalid value for `url`, length must be less than or equal to `799`")  # noqa: E501

        self._url = url

    @property
    def statement_descriptor(self):
        """Gets the statement_descriptor of this DjStripeProduct.  # noqa: E501

        Extra information about a product which will appear on your customer's credit card statement. In the case that multiple products are billed at once, the first statement descriptor will be used. Only available on products of type=`service`.  # noqa: E501

        :return: The statement_descriptor of this DjStripeProduct.  # noqa: E501
        :rtype: str
        """
        return self._statement_descriptor

    @statement_descriptor.setter
    def statement_descriptor(self, statement_descriptor):
        """Sets the statement_descriptor of this DjStripeProduct.

        Extra information about a product which will appear on your customer's credit card statement. In the case that multiple products are billed at once, the first statement descriptor will be used. Only available on products of type=`service`.  # noqa: E501

        :param statement_descriptor: The statement_descriptor of this DjStripeProduct.  # noqa: E501
        :type statement_descriptor: str
        """
        if (self.local_vars_configuration.client_side_validation and
                statement_descriptor is not None and len(statement_descriptor) > 22):
            raise ValueError("Invalid value for `statement_descriptor`, length must be less than or equal to `22`")  # noqa: E501

        self._statement_descriptor = statement_descriptor

    @property
    def unit_label(self):
        """Gets the unit_label of this DjStripeProduct.  # noqa: E501


        :return: The unit_label of this DjStripeProduct.  # noqa: E501
        :rtype: str
        """
        return self._unit_label

    @unit_label.setter
    def unit_label(self, unit_label):
        """Sets the unit_label of this DjStripeProduct.


        :param unit_label: The unit_label of this DjStripeProduct.  # noqa: E501
        :type unit_label: str
        """
        if (self.local_vars_configuration.client_side_validation and
                unit_label is not None and len(unit_label) > 12):
            raise ValueError("Invalid value for `unit_label`, length must be less than or equal to `12`")  # noqa: E501

        self._unit_label = unit_label

    @property
    def djstripe_owner_account(self):
        """Gets the djstripe_owner_account of this DjStripeProduct.  # noqa: E501

        The Stripe Account this object belongs to.  # noqa: E501

        :return: The djstripe_owner_account of this DjStripeProduct.  # noqa: E501
        :rtype: str
        """
        return self._djstripe_owner_account

    @djstripe_owner_account.setter
    def djstripe_owner_account(self, djstripe_owner_account):
        """Sets the djstripe_owner_account of this DjStripeProduct.

        The Stripe Account this object belongs to.  # noqa: E501

        :param djstripe_owner_account: The djstripe_owner_account of this DjStripeProduct.  # noqa: E501
        :type djstripe_owner_account: str
        """

        self._djstripe_owner_account = djstripe_owner_account

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DjStripeProduct):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DjStripeProduct):
            return True

        return self.to_dict() != other.to_dict()
