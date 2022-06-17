# coding: utf-8

"""
    Python client for GIG based clouds (pc4g)

    RESTful api client to a GIG based cloud.  # noqa: E501

    OpenAPI spec version: v1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pc4g.api_client import ApiClient


class MeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_current_user_info(self, **kwargs):  # noqa: E501
        """get_current_user_info  # noqa: E501

        Gets current user info  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_user_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_fields: An optional fields mask
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_current_user_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_current_user_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_current_user_info_with_http_info(self, **kwargs):  # noqa: E501
        """get_current_user_info  # noqa: E501

        Gets current user info  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_user_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_fields: An optional fields mask
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_current_user_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_fields' in params:
            header_params['X-Fields'] = params['x_fields']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/me', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_current_user_jwt(self, **kwargs):  # noqa: E501
        """get_current_user_jwt  # noqa: E501

        Gets current user JWT token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_user_jwt(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_current_user_jwt_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_current_user_jwt_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_current_user_jwt_with_http_info(self, **kwargs):  # noqa: E501
        """get_current_user_jwt  # noqa: E501

        Gets current user JWT token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_user_jwt_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_current_user_jwt" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/me/jwt', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_email_subscriptions(self, **kwargs):  # noqa: E501
        """get_email_subscriptions  # noqa: E501

        Gets Email Subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_email_subscriptions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_fields: An optional fields mask
        :return: UserEmailSubscriptionConfigEmailPreferences
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_email_subscriptions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_email_subscriptions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_email_subscriptions_with_http_info(self, **kwargs):  # noqa: E501
        """get_email_subscriptions  # noqa: E501

        Gets Email Subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_email_subscriptions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_fields: An optional fields mask
        :return: UserEmailSubscriptionConfigEmailPreferences
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_email_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_fields' in params:
            header_params['X-Fields'] = params['x_fields']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/me/email-subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserEmailSubscriptionConfigEmailPreferences',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_new_email_subscriptions(self, **kwargs):  # noqa: E501
        """get_new_email_subscriptions  # noqa: E501

        Gets new email subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_new_email_subscriptions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_fields: An optional fields mask
        :return: UserEmailSubscriptionConfigEmailPreferences
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_new_email_subscriptions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_new_email_subscriptions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_new_email_subscriptions_with_http_info(self, **kwargs):  # noqa: E501
        """get_new_email_subscriptions  # noqa: E501

        Gets new email subscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_new_email_subscriptions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_fields: An optional fields mask
        :return: UserEmailSubscriptionConfigEmailPreferences
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_new_email_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_fields' in params:
            header_params['X-Fields'] = params['x_fields']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/me/new-email-subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserEmailSubscriptionConfigEmailPreferences',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_user_notifications(self, **kwargs):  # noqa: E501
        """list_user_notifications  # noqa: E501

        get email notifications  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_notifications(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool include_past: include past maintenance notifications
        :param str notification_type: notification type
        :param str status: notification status
        :param str x_fields: An optional fields mask
        :return: list[NotificationConfig]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_notifications_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_user_notifications_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_user_notifications_with_http_info(self, **kwargs):  # noqa: E501
        """list_user_notifications  # noqa: E501

        get email notifications  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_notifications_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool include_past: include past maintenance notifications
        :param str notification_type: notification type
        :param str status: notification status
        :param str x_fields: An optional fields mask
        :return: list[NotificationConfig]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include_past', 'notification_type', 'status', 'x_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_notifications" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_past' in params:
            query_params.append(('include_past', params['include_past']))  # noqa: E501
        if 'notification_type' in params:
            query_params.append(('notification_type', params['notification_type']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

        header_params = {}
        if 'x_fields' in params:
            header_params['X-Fields'] = params['x_fields']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/me/email-notifications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[NotificationConfig]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_email_subscription(self, payload, **kwargs):  # noqa: E501
        """update_email_subscription  # noqa: E501

        update Email Subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_email_subscription(payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserEmailSubscriptionConfigEmailPreferences payload: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_email_subscription_with_http_info(payload, **kwargs)  # noqa: E501
        else:
            (data) = self.update_email_subscription_with_http_info(payload, **kwargs)  # noqa: E501
            return data

    def update_email_subscription_with_http_info(self, payload, **kwargs):  # noqa: E501
        """update_email_subscription  # noqa: E501

        update Email Subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_email_subscription_with_http_info(payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserEmailSubscriptionConfigEmailPreferences payload: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_email_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payload' is set
        if self.api_client.client_side_validation and ('payload' not in params or
                                                       params['payload'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `payload` when calling `update_email_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payload' in params:
            body_params = params['payload']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/me/email-subscriptions', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
