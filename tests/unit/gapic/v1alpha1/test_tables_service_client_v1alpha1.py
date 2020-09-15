# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests."""

import mock
import pytest

from google.area120 import tables_v1alpha
from google.area120.tables_v1alpha.proto1 import tables_pb2
from google.protobuf import empty_pb2


class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""

    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response


class ChannelStub(object):
    """Stub for the grpc.Channel interface."""

    def __init__(self, responses=[]):
        self.responses = responses
        self.requests = []

    def unary_unary(self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)


class CustomException(Exception):
    pass


class TestTablesServiceClient(object):
    def test_get_table(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        expected_response = {"name": name_2, "display_name": display_name}
        expected_response = tables_pb2.Table(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup Request
        name = "name3373707"

        response = client.get_table(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = tables_pb2.GetTableRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_table_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup request
        name = "name3373707"

        with pytest.raises(CustomException):
            client.get_table(name)

    def test_list_tables(self):
        # Setup Expected Response
        next_page_token = ""
        tables_element = {}
        tables = [tables_element]
        expected_response = {"next_page_token": next_page_token, "tables": tables}
        expected_response = tables_pb2.ListTablesResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        paged_list_response = client.list_tables()
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.tables[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = tables_pb2.ListTablesRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_tables_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        paged_list_response = client.list_tables()
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_row(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        expected_response = {"name": name_2}
        expected_response = tables_pb2.Row(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup Request
        name = "name3373707"

        response = client.get_row(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = tables_pb2.GetRowRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_row_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup request
        name = "name3373707"

        with pytest.raises(CustomException):
            client.get_row(name)

    def test_list_rows(self):
        # Setup Expected Response
        next_page_token = ""
        rows_element = {}
        rows = [rows_element]
        expected_response = {"next_page_token": next_page_token, "rows": rows}
        expected_response = tables_pb2.ListRowsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup Request
        parent = "parent-995424086"

        paged_list_response = client.list_rows(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.rows[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = tables_pb2.ListRowsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_rows_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup request
        parent = "parent-995424086"

        paged_list_response = client.list_rows(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_create_row(self):
        # Setup Expected Response
        name = "name3373707"
        expected_response = {"name": name}
        expected_response = tables_pb2.Row(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup Request
        parent = "parent-995424086"
        row = {}

        response = client.create_row(parent, row)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = tables_pb2.CreateRowRequest(parent=parent, row=row)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_row_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup request
        parent = "parent-995424086"
        row = {}

        with pytest.raises(CustomException):
            client.create_row(parent, row)

    def test_batch_create_rows(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = tables_pb2.BatchCreateRowsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup Request
        parent = "parent-995424086"
        requests = []

        response = client.batch_create_rows(parent, requests)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = tables_pb2.BatchCreateRowsRequest(
            parent=parent, requests=requests
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_batch_create_rows_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup request
        parent = "parent-995424086"
        requests = []

        with pytest.raises(CustomException):
            client.batch_create_rows(parent, requests)

    def test_update_row(self):
        # Setup Expected Response
        name = "name3373707"
        expected_response = {"name": name}
        expected_response = tables_pb2.Row(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup Request
        row = {}

        response = client.update_row(row)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = tables_pb2.UpdateRowRequest(row=row)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_row_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup request
        row = {}

        with pytest.raises(CustomException):
            client.update_row(row)

    def test_batch_update_rows(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = tables_pb2.BatchUpdateRowsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup Request
        parent = "parent-995424086"
        requests = []

        response = client.batch_update_rows(parent, requests)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = tables_pb2.BatchUpdateRowsRequest(
            parent=parent, requests=requests
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_batch_update_rows_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup request
        parent = "parent-995424086"
        requests = []

        with pytest.raises(CustomException):
            client.batch_update_rows(parent, requests)

    def test_delete_row(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup Request
        name = client.row_path("[TABLE]", "[ROW]")

        client.delete_row(name)

        assert len(channel.requests) == 1
        expected_request = tables_pb2.DeleteRowRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_row_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = tables_v1alpha.TablesServiceClient()

        # Setup request
        name = client.row_path("[TABLE]", "[ROW]")

        with pytest.raises(CustomException):
            client.delete_row(name)
