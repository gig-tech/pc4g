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


class UtilitiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def download_csi_driver_examples(self, **kwargs):  # noqa: E501
        """download_csi_driver_examples  # noqa: E501

        download examples for using the CSI driver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_csi_driver_examples(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_csi_driver_examples_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.download_csi_driver_examples_with_http_info(**kwargs)  # noqa: E501
            return data

    def download_csi_driver_examples_with_http_info(self, **kwargs):  # noqa: E501
        """download_csi_driver_examples  # noqa: E501

        download examples for using the CSI driver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_csi_driver_examples_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method download_csi_driver_examples" % key
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
            ['application/zip'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/utilities/csi-driver/examples', 'GET',
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

    def download_kubernetes_configuration_files_example(self, **kwargs):  # noqa: E501
        """download_kubernetes_configuration_files_example  # noqa: E501

        download pre-filled examples for kubernetes configuration files  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_kubernetes_configuration_files_example(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_kubernetes_configuration_files_example_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.download_kubernetes_configuration_files_example_with_http_info(**kwargs)  # noqa: E501
            return data

    def download_kubernetes_configuration_files_example_with_http_info(self, **kwargs):  # noqa: E501
        """download_kubernetes_configuration_files_example  # noqa: E501

        download pre-filled examples for kubernetes configuration files  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_kubernetes_configuration_files_example_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method download_kubernetes_configuration_files_example" % key
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
            ['application/zip'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/utilities/examples/kubernetes-files', 'GET',
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

    def download_terraform_provider_version(self, platform, **kwargs):  # noqa: E501
        """download_terraform_provider_version  # noqa: E501

        download Terraform provider version  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_terraform_provider_version(platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str platform: platforms available i.e. windows, linux etc. (required)
        :param str x_fields: An optional fields mask
        :return: VersionInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_terraform_provider_version_with_http_info(platform, **kwargs)  # noqa: E501
        else:
            (data) = self.download_terraform_provider_version_with_http_info(platform, **kwargs)  # noqa: E501
            return data

    def download_terraform_provider_version_with_http_info(self, platform, **kwargs):  # noqa: E501
        """download_terraform_provider_version  # noqa: E501

        download Terraform provider version  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_terraform_provider_version_with_http_info(platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str platform: platforms available i.e. windows, linux etc. (required)
        :param str x_fields: An optional fields mask
        :return: VersionInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['platform', 'x_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_terraform_provider_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'platform' is set
        if self.api_client.client_side_validation and ('platform' not in params or
                                                       params['platform'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `platform` when calling `download_terraform_provider_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'platform' in params:
            query_params.append(('platform', params['platform']))  # noqa: E501

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
            '/utilities/terraform-provider/version', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VersionInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cli(self, platform, **kwargs):  # noqa: E501
        """get_cli  # noqa: E501

        Get cli  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cli(platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str platform: specific platform to download binaries for (required)
        :param str version: specific version to download (internally used by the cli update mechanism. should not be used otherwise)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cli_with_http_info(platform, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cli_with_http_info(platform, **kwargs)  # noqa: E501
            return data

    def get_cli_with_http_info(self, platform, **kwargs):  # noqa: E501
        """get_cli  # noqa: E501

        Get cli  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cli_with_http_info(platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str platform: specific platform to download binaries for (required)
        :param str version: specific version to download (internally used by the cli update mechanism. should not be used otherwise)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['platform', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cli" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'platform' is set
        if self.api_client.client_side_validation and ('platform' not in params or
                                                       params['platform'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `platform` when calling `get_cli`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'platform' in params:
            query_params.append(('platform', params['platform']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/zip'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/utilities/cli', 'GET',
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

    def get_latest_cli_version_info(self, platform, **kwargs):  # noqa: E501
        """get_latest_cli_version_info  # noqa: E501

        get latest cli version info  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_latest_cli_version_info(platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str platform: platforms available i.e. windows, linux etc. (required)
        :param str x_fields: An optional fields mask
        :return: VersionInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_latest_cli_version_info_with_http_info(platform, **kwargs)  # noqa: E501
        else:
            (data) = self.get_latest_cli_version_info_with_http_info(platform, **kwargs)  # noqa: E501
            return data

    def get_latest_cli_version_info_with_http_info(self, platform, **kwargs):  # noqa: E501
        """get_latest_cli_version_info  # noqa: E501

        get latest cli version info  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_latest_cli_version_info_with_http_info(platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str platform: platforms available i.e. windows, linux etc. (required)
        :param str x_fields: An optional fields mask
        :return: VersionInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['platform', 'x_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_latest_cli_version_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'platform' is set
        if self.api_client.client_side_validation and ('platform' not in params or
                                                       params['platform'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `platform` when calling `get_latest_cli_version_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'platform' in params:
            query_params.append(('platform', params['platform']))  # noqa: E501

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
            '/utilities/cli/version', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VersionInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_terrafom_provider(self, platform, **kwargs):  # noqa: E501
        """get_terrafom_provider  # noqa: E501

        Get terraform provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_terrafom_provider(platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str platform: specific platform to download binaries for (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_terrafom_provider_with_http_info(platform, **kwargs)  # noqa: E501
        else:
            (data) = self.get_terrafom_provider_with_http_info(platform, **kwargs)  # noqa: E501
            return data

    def get_terrafom_provider_with_http_info(self, platform, **kwargs):  # noqa: E501
        """get_terrafom_provider  # noqa: E501

        Get terraform provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_terrafom_provider_with_http_info(platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str platform: specific platform to download binaries for (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['platform']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_terrafom_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'platform' is set
        if self.api_client.client_side_validation and ('platform' not in params or
                                                       params['platform'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `platform` when calling `get_terrafom_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'platform' in params:
            query_params.append(('platform', params['platform']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/zip'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/utilities/terraform-provider', 'GET',
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

    def list_cli_platforms(self, **kwargs):  # noqa: E501
        """list_cli_platforms  # noqa: E501

        list cli platforms  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cli_platforms(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_fields: An optional fields mask
        :return: SupportedPlatforms
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_cli_platforms_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_cli_platforms_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_cli_platforms_with_http_info(self, **kwargs):  # noqa: E501
        """list_cli_platforms  # noqa: E501

        list cli platforms  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cli_platforms_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_fields: An optional fields mask
        :return: SupportedPlatforms
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
                    " to method list_cli_platforms" % key
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
            '/utilities/cli/platforms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SupportedPlatforms',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_terraform_provider_platforms(self, **kwargs):  # noqa: E501
        """list_terraform_provider_platforms  # noqa: E501

        list terraform provider platforms  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_terraform_provider_platforms(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_fields: An optional fields mask
        :return: SupportedPlatforms
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_terraform_provider_platforms_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_terraform_provider_platforms_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_terraform_provider_platforms_with_http_info(self, **kwargs):  # noqa: E501
        """list_terraform_provider_platforms  # noqa: E501

        list terraform provider platforms  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_terraform_provider_platforms_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_fields: An optional fields mask
        :return: SupportedPlatforms
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
                    " to method list_terraform_provider_platforms" % key
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
            '/utilities/terrafrom-provider/platforms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SupportedPlatforms',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)