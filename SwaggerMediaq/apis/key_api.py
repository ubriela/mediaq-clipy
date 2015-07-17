#!/usr/bin/env python
# coding: utf-8

"""
KeyApi.py
Copyright 2015 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from .. import configuration
from ..api_client import ApiClient

class KeyApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('http://localhost/MediaQ_MVC_V3/api')
            self.api_client = configuration.api_client
    
    
    def create(self, level, **kwargs):
        """
        Generate an API key
        Generate an API key

        :param int level: Level (required)
        
        :return: str
        """
        
        # verify the required parameter 'level' is set
        if level is None:
            raise ValueError("Missing the required parameter `level` when calling `create`")
        
        all_params = ['level']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method create" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/key/create'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'level' in params:
            form_params['level'] = params['level']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='str', auth_settings=auth_settings)
        
        return response
        
    def regenerate(self, key, **kwargs):
        """
        Regenerate Key
        Remove a key from the database to stop it working

        :param str key: Key (required)
        
        :return: str
        """
        
        # verify the required parameter 'key' is set
        if key is None:
            raise ValueError("Missing the required parameter `key` when calling `regenerate`")
        
        all_params = ['key']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method regenerate" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/key/regenerate'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'key' in params:
            form_params['key'] = params['key']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='str', auth_settings=auth_settings)
        
        return response
        
    def remove(self, key, **kwargs):
        """
        Delete an API key
        Delete an API key

        :param str key: Key (required)
        
        :return: str
        """
        
        # verify the required parameter 'key' is set
        if key is None:
            raise ValueError("Missing the required parameter `key` when calling `remove`")
        
        all_params = ['key']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method remove" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/key/remove'.replace('{format}', 'json')
        method = 'DELETE'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'key' in params:
            form_params['key'] = params['key']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='str', auth_settings=auth_settings)
        
        return response
        
    def suspend(self, key, **kwargs):
        """
        Suspend an API key
        Set key level to 0

        :param str key: Key (required)
        
        :return: str
        """
        
        # verify the required parameter 'key' is set
        if key is None:
            raise ValueError("Missing the required parameter `key` when calling `suspend`")
        
        all_params = ['key']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method suspend" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/key/suspend'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'key' in params:
            form_params['key'] = params['key']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='str', auth_settings=auth_settings)
        
        return response
        
    def update(self, key, level, **kwargs):
        """
        Update API key level
        Update API key level

        :param str key: Key (required)
        :param int level: Level (required)
        
        :return: str
        """
        
        # verify the required parameter 'key' is set
        if key is None:
            raise ValueError("Missing the required parameter `key` when calling `update`")
        
        # verify the required parameter 'level' is set
        if level is None:
            raise ValueError("Missing the required parameter `level` when calling `update`")
        
        all_params = ['key', 'level']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method update" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/key/update'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'key' in params:
            form_params['key'] = params['key']
        
        if 'level' in params:
            form_params['level'] = params['level']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='str', auth_settings=auth_settings)
        
        return response
        









