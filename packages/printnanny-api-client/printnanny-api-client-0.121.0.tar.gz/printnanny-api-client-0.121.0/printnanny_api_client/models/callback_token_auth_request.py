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


class CallbackTokenAuthRequest(object):
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
        'email': 'str',
        'mobile': 'str',
        'token': 'str'
    }

    attribute_map = {
        'email': 'email',
        'mobile': 'mobile',
        'token': 'token'
    }

    def __init__(self, email=None, mobile=None, token=None, local_vars_configuration=None):  # noqa: E501
        """CallbackTokenAuthRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._mobile = None
        self._token = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if mobile is not None:
            self.mobile = mobile
        self.token = token

    @property
    def email(self):
        """Gets the email of this CallbackTokenAuthRequest.  # noqa: E501


        :return: The email of this CallbackTokenAuthRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CallbackTokenAuthRequest.


        :param email: The email of this CallbackTokenAuthRequest.  # noqa: E501
        :type email: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def mobile(self):
        """Gets the mobile of this CallbackTokenAuthRequest.  # noqa: E501


        :return: The mobile of this CallbackTokenAuthRequest.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this CallbackTokenAuthRequest.


        :param mobile: The mobile of this CallbackTokenAuthRequest.  # noqa: E501
        :type mobile: str
        """
        if (self.local_vars_configuration.client_side_validation and
                mobile is not None and len(mobile) > 17):
            raise ValueError("Invalid value for `mobile`, length must be less than or equal to `17`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                mobile is not None and len(mobile) < 1):
            raise ValueError("Invalid value for `mobile`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                mobile is not None and not re.search(r'^\+[1-9]\d{1,14}$', mobile)):  # noqa: E501
            raise ValueError(r"Invalid value for `mobile`, must be a follow pattern or equal to `/^\+[1-9]\d{1,14}$/`")  # noqa: E501

        self._mobile = mobile

    @property
    def token(self):
        """Gets the token of this CallbackTokenAuthRequest.  # noqa: E501


        :return: The token of this CallbackTokenAuthRequest.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CallbackTokenAuthRequest.


        :param token: The token of this CallbackTokenAuthRequest.  # noqa: E501
        :type token: str
        """
        if self.local_vars_configuration.client_side_validation and token is None:  # noqa: E501
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                token is not None and len(token) > 6):
            raise ValueError("Invalid value for `token`, length must be less than or equal to `6`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                token is not None and len(token) < 6):
            raise ValueError("Invalid value for `token`, length must be greater than or equal to `6`")  # noqa: E501

        self._token = token

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
        if not isinstance(other, CallbackTokenAuthRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CallbackTokenAuthRequest):
            return True

        return self.to_dict() != other.to_dict()
