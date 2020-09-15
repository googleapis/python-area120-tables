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


import google.api_core.grpc_helpers

from google.area120.tables_v1alpha.proto1 import tables_pb2_grpc


class TablesServiceGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.area120.tables.v1alpha1 TablesService API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = (
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive.readonly",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/spreadsheets.readonly",
    )

    def __init__(
        self, channel=None, credentials=None, address="area120tables.googleapis.com:443"
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive.",
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "tables_service_stub": tables_pb2_grpc.TablesServiceStub(channel),
        }

    @classmethod
    def create_channel(
        cls, address="area120tables.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def get_table(self):
        """Return the gRPC stub for :meth:`TablesServiceClient.get_table`.

        Gets a table. Returns NOT_FOUND if the table does not exist.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["tables_service_stub"].GetTable

    @property
    def list_tables(self):
        """Return the gRPC stub for :meth:`TablesServiceClient.list_tables`.

        Lists tables for the user.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["tables_service_stub"].ListTables

    @property
    def get_row(self):
        """Return the gRPC stub for :meth:`TablesServiceClient.get_row`.

        Gets a row. Returns NOT_FOUND if the row does not exist in the
        table.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["tables_service_stub"].GetRow

    @property
    def list_rows(self):
        """Return the gRPC stub for :meth:`TablesServiceClient.list_rows`.

        Lists rows in a table. Returns NOT_FOUND if the table does not
        exist.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["tables_service_stub"].ListRows

    @property
    def create_row(self):
        """Return the gRPC stub for :meth:`TablesServiceClient.create_row`.

        Creates a row.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["tables_service_stub"].CreateRow

    @property
    def batch_create_rows(self):
        """Return the gRPC stub for :meth:`TablesServiceClient.batch_create_rows`.

        Creates multiple rows.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["tables_service_stub"].BatchCreateRows

    @property
    def update_row(self):
        """Return the gRPC stub for :meth:`TablesServiceClient.update_row`.

        Updates a row.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["tables_service_stub"].UpdateRow

    @property
    def batch_update_rows(self):
        """Return the gRPC stub for :meth:`TablesServiceClient.batch_update_rows`.

        Updates multiple rows.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["tables_service_stub"].BatchUpdateRows

    @property
    def delete_row(self):
        """Return the gRPC stub for :meth:`TablesServiceClient.delete_row`.

        Deletes a row.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["tables_service_stub"].DeleteRow
