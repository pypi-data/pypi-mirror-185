# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.121.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.paginated_product_list import PaginatedProductList  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPaginatedProductList(unittest.TestCase):
    """PaginatedProductList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedProductList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.paginated_product_list.PaginatedProductList()  # noqa: E501
        if include_optional :
            return PaginatedProductList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    printnanny_api_client.models.product.Product(
                        id = '', 
                        djstripe_product = printnanny_api_client.models.dj_stripe_product.DjStripeProduct(
                            djstripe_id = 56, 
                            djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = '', 
                            livemode = True, 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            metadata = {
                                'key' : null
                                }, 
                            description = '', 
                            name = '', 
                            type = null, 
                            active = True, 
                            attributes = {
                                'key' : null
                                }, 
                            caption = '', 
                            deactivate_on = {
                                'key' : null
                                }, 
                            images = {
                                'key' : null
                                }, 
                            package_dimensions = {
                                'key' : null
                                }, 
                            shippable = True, 
                            url = '', 
                            statement_descriptor = '', 
                            unit_label = '', 
                            djstripe_owner_account = '', ), 
                        prices = [
                            printnanny_api_client.models.dj_stripe_price.DjStripePrice(
                                djstripe_id = 56, 
                                billing_scheme = 'per_unit', 
                                human_readable_price = '', 
                                tiers_mode = 'graduated', 
                                djstripe_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                djstripe_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                id = '', 
                                livemode = True, 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                description = '', 
                                active = True, 
                                currency = '', 
                                nickname = '', 
                                recurring = {
                                    'key' : null
                                    }, 
                                type = null, 
                                unit_amount = -9223372036854775808, 
                                unit_amount_decimal = '-8072888', 
                                lookup_key = '', 
                                tiers = {
                                    'key' : null
                                    }, 
                                transform_quantity = {
                                    'key' : null
                                    }, 
                                djstripe_owner_account = '', 
                                product = '', )
                            ], 
                        deleted = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sku = '', 
                        slug = '', 
                        unit_label = '', 
                        name = '', 
                        description = '', 
                        statement_descriptor = '', 
                        images = [
                            ''
                            ], 
                        is_active = True, 
                        is_shippable = True, 
                        is_preorder = True, 
                        is_subscription = True, 
                        stripe_price_lookup_key = '', 
                        stripe_product_id = '', )
                    ]
            )
        else :
            return PaginatedProductList(
        )

    def testPaginatedProductList(self):
        """Test PaginatedProductList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
