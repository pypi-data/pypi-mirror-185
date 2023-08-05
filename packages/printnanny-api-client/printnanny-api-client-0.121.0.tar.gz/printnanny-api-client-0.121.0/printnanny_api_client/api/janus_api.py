# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.121.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from printnanny_api_client.api_client import ApiClient
from printnanny_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class JanusApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pis_webrtc_streams_create(self, pi_id, **kwargs):  # noqa: E501
        """pis_webrtc_streams_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pis_webrtc_streams_create(pi_id, async_req=True)
        >>> result = thread.get()

        :param pi_id: (required)
        :type pi_id: int
        :param webrtc_stream_request:
        :type webrtc_stream_request: WebrtcStreamRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WebrtcStream
        """
        kwargs['_return_http_data_only'] = True
        return self.pis_webrtc_streams_create_with_http_info(pi_id, **kwargs)  # noqa: E501

    def pis_webrtc_streams_create_with_http_info(self, pi_id, **kwargs):  # noqa: E501
        """pis_webrtc_streams_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pis_webrtc_streams_create_with_http_info(pi_id, async_req=True)
        >>> result = thread.get()

        :param pi_id: (required)
        :type pi_id: int
        :param webrtc_stream_request:
        :type webrtc_stream_request: WebrtcStreamRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WebrtcStream, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'pi_id',
            'webrtc_stream_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pis_webrtc_streams_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'pi_id' is set
        if self.api_client.client_side_validation and ('pi_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pi_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pi_id` when calling `pis_webrtc_streams_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pi_id' in local_var_params:
            path_params['pi_id'] = local_var_params['pi_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'webrtc_stream_request' in local_var_params:
            body_params = local_var_params['webrtc_stream_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'],
                'POST', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = ['cookieAuth', 'tokenAuth']  # noqa: E501

        response_types_map = {
            201: "WebrtcStream",
            409: "ErrorDetail",
            400: "ErrorDetail",
            401: "ErrorDetail",
            403: "ErrorDetail",
            500: "ErrorDetail",
        }

        return self.api_client.call_api(
            '/api/pis/{pi_id}/webrtc-streams/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def pis_webrtc_streams_list(self, pi_id, **kwargs):  # noqa: E501
        """pis_webrtc_streams_list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pis_webrtc_streams_list(pi_id, async_req=True)
        >>> result = thread.get()

        :param pi_id: (required)
        :type pi_id: int
        :param page: A page number within the paginated result set.
        :type page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PaginatedWebrtcStreamList
        """
        kwargs['_return_http_data_only'] = True
        return self.pis_webrtc_streams_list_with_http_info(pi_id, **kwargs)  # noqa: E501

    def pis_webrtc_streams_list_with_http_info(self, pi_id, **kwargs):  # noqa: E501
        """pis_webrtc_streams_list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pis_webrtc_streams_list_with_http_info(pi_id, async_req=True)
        >>> result = thread.get()

        :param pi_id: (required)
        :type pi_id: int
        :param page: A page number within the paginated result set.
        :type page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PaginatedWebrtcStreamList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'pi_id',
            'page'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pis_webrtc_streams_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'pi_id' is set
        if self.api_client.client_side_validation and ('pi_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pi_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pi_id` when calling `pis_webrtc_streams_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pi_id' in local_var_params:
            path_params['pi_id'] = local_var_params['pi_id']  # noqa: E501

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['cookieAuth', 'tokenAuth']  # noqa: E501

        response_types_map = {
            200: "PaginatedWebrtcStreamList",
            400: "ErrorDetail",
            401: "ErrorDetail",
            403: "ErrorDetail",
            500: "ErrorDetail",
        }

        return self.api_client.call_api(
            '/api/pis/{pi_id}/webrtc-streams/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def pis_webrtc_streams_partial_update(self, id, pi_id, **kwargs):  # noqa: E501
        """pis_webrtc_streams_partial_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pis_webrtc_streams_partial_update(id, pi_id, async_req=True)
        >>> result = thread.get()

        :param id: A unique integer value identifying this webrtc stream. (required)
        :type id: int
        :param pi_id: (required)
        :type pi_id: int
        :param patched_webrtc_stream_request:
        :type patched_webrtc_stream_request: PatchedWebrtcStreamRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WebrtcStream
        """
        kwargs['_return_http_data_only'] = True
        return self.pis_webrtc_streams_partial_update_with_http_info(id, pi_id, **kwargs)  # noqa: E501

    def pis_webrtc_streams_partial_update_with_http_info(self, id, pi_id, **kwargs):  # noqa: E501
        """pis_webrtc_streams_partial_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pis_webrtc_streams_partial_update_with_http_info(id, pi_id, async_req=True)
        >>> result = thread.get()

        :param id: A unique integer value identifying this webrtc stream. (required)
        :type id: int
        :param pi_id: (required)
        :type pi_id: int
        :param patched_webrtc_stream_request:
        :type patched_webrtc_stream_request: PatchedWebrtcStreamRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WebrtcStream, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'id',
            'pi_id',
            'patched_webrtc_stream_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pis_webrtc_streams_partial_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `pis_webrtc_streams_partial_update`")  # noqa: E501
        # verify the required parameter 'pi_id' is set
        if self.api_client.client_side_validation and ('pi_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pi_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pi_id` when calling `pis_webrtc_streams_partial_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'pi_id' in local_var_params:
            path_params['pi_id'] = local_var_params['pi_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patched_webrtc_stream_request' in local_var_params:
            body_params = local_var_params['patched_webrtc_stream_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'],
                'PATCH', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = ['cookieAuth', 'tokenAuth']  # noqa: E501

        response_types_map = {
            202: "WebrtcStream",
            409: "ErrorDetail",
            400: "ErrorDetail",
            401: "ErrorDetail",
            403: "ErrorDetail",
            500: "ErrorDetail",
        }

        return self.api_client.call_api(
            '/api/pis/{pi_id}/webrtc-streams/{id}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def pis_webrtc_streams_retrieve(self, id, pi_id, **kwargs):  # noqa: E501
        """pis_webrtc_streams_retrieve  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pis_webrtc_streams_retrieve(id, pi_id, async_req=True)
        >>> result = thread.get()

        :param id: A unique integer value identifying this webrtc stream. (required)
        :type id: int
        :param pi_id: (required)
        :type pi_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WebrtcStream
        """
        kwargs['_return_http_data_only'] = True
        return self.pis_webrtc_streams_retrieve_with_http_info(id, pi_id, **kwargs)  # noqa: E501

    def pis_webrtc_streams_retrieve_with_http_info(self, id, pi_id, **kwargs):  # noqa: E501
        """pis_webrtc_streams_retrieve  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pis_webrtc_streams_retrieve_with_http_info(id, pi_id, async_req=True)
        >>> result = thread.get()

        :param id: A unique integer value identifying this webrtc stream. (required)
        :type id: int
        :param pi_id: (required)
        :type pi_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WebrtcStream, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'id',
            'pi_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pis_webrtc_streams_retrieve" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `pis_webrtc_streams_retrieve`")  # noqa: E501
        # verify the required parameter 'pi_id' is set
        if self.api_client.client_side_validation and ('pi_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pi_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pi_id` when calling `pis_webrtc_streams_retrieve`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'pi_id' in local_var_params:
            path_params['pi_id'] = local_var_params['pi_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['cookieAuth', 'tokenAuth']  # noqa: E501

        response_types_map = {
            200: "WebrtcStream",
            404: "ErrorDetail",
            400: "ErrorDetail",
            401: "ErrorDetail",
            403: "ErrorDetail",
            500: "ErrorDetail",
        }

        return self.api_client.call_api(
            '/api/pis/{pi_id}/webrtc-streams/{id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def pis_webrtc_streams_update(self, id, pi_id, **kwargs):  # noqa: E501
        """pis_webrtc_streams_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pis_webrtc_streams_update(id, pi_id, async_req=True)
        >>> result = thread.get()

        :param id: A unique integer value identifying this webrtc stream. (required)
        :type id: int
        :param pi_id: (required)
        :type pi_id: int
        :param webrtc_stream_request:
        :type webrtc_stream_request: WebrtcStreamRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WebrtcStream
        """
        kwargs['_return_http_data_only'] = True
        return self.pis_webrtc_streams_update_with_http_info(id, pi_id, **kwargs)  # noqa: E501

    def pis_webrtc_streams_update_with_http_info(self, id, pi_id, **kwargs):  # noqa: E501
        """pis_webrtc_streams_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pis_webrtc_streams_update_with_http_info(id, pi_id, async_req=True)
        >>> result = thread.get()

        :param id: A unique integer value identifying this webrtc stream. (required)
        :type id: int
        :param pi_id: (required)
        :type pi_id: int
        :param webrtc_stream_request:
        :type webrtc_stream_request: WebrtcStreamRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WebrtcStream, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'id',
            'pi_id',
            'webrtc_stream_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pis_webrtc_streams_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `pis_webrtc_streams_update`")  # noqa: E501
        # verify the required parameter 'pi_id' is set
        if self.api_client.client_side_validation and ('pi_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pi_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pi_id` when calling `pis_webrtc_streams_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'pi_id' in local_var_params:
            path_params['pi_id'] = local_var_params['pi_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'webrtc_stream_request' in local_var_params:
            body_params = local_var_params['webrtc_stream_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'],
                'PUT', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = ['cookieAuth', 'tokenAuth']  # noqa: E501

        response_types_map = {
            202: "WebrtcStream",
            409: "ErrorDetail",
            400: "ErrorDetail",
            401: "ErrorDetail",
            403: "ErrorDetail",
            500: "ErrorDetail",
        }

        return self.api_client.call_api(
            '/api/pis/{pi_id}/webrtc-streams/{id}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
