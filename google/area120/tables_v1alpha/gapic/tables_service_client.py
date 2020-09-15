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

"""Accesses the google.area120.tables.v1alpha1 TablesService API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.area120.tables_v1alpha.gapic import enums
from google.area120.tables_v1alpha.gapic import tables_service_client_config
from google.area120.tables_v1alpha.gapic.transports import tables_service_grpc_transport
from google.area120.tables_v1alpha.proto1 import tables_pb2
from google.area120.tables_v1alpha.proto1 import tables_pb2_grpc
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-area120-tables",
).version


class TablesServiceClient(object):
    """
    The Tables Service provides an API for reading and updating tables.
    It defines the following resource model:

    -  The API has a collection of ``Table`` resources, named ``tables/*``

    -  Each Table has a collection of ``Row`` resources, named
       ``tables/*/rows/*``
    """

    SERVICE_ADDRESS = "area120tables.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.area120.tables.v1alpha1.TablesService"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TablesServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def row_path(cls, table, row):
        """Return a fully-qualified row string."""
        return google.api_core.path_template.expand(
            "tables/{table}/rows/{row}", table=table, row=row,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.TablesServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.TablesServiceGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = tables_service_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=tables_service_grpc_transport.TablesServiceGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = tables_service_grpc_transport.TablesServiceGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials,
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION,
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME],
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def get_table(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a table. Returns NOT_FOUND if the table does not exist.

        Example:
            >>> from google.area120 import tables_v1alpha
            >>>
            >>> client = tables_v1alpha.TablesServiceClient()
            >>>
            >>> # TODO: Initialize `name`:
            >>> name = ''
            >>>
            >>> response = client.get_table(name)

        Args:
            name (str): Required. The name of the table to retrieve.
                Format: tables/{table}
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.area120.tables_v1alpha.types.Table` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_table" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_table"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_table,
                default_retry=self._method_configs["GetTable"].retry,
                default_timeout=self._method_configs["GetTable"].timeout,
                client_info=self._client_info,
            )

        request = tables_pb2.GetTableRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_table"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_tables(
        self,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists tables for the user.

        Example:
            >>> from google.area120 import tables_v1alpha
            >>>
            >>> client = tables_v1alpha.TablesServiceClient()
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_tables():
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_tables().pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.area120.tables_v1alpha.types.Table` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_tables" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_tables"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_tables,
                default_retry=self._method_configs["ListTables"].retry,
                default_timeout=self._method_configs["ListTables"].timeout,
                client_info=self._client_info,
            )

        request = tables_pb2.ListTablesRequest(page_size=page_size,)
        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_tables"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="tables",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def get_row(
        self,
        name,
        view=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a row. Returns NOT_FOUND if the row does not exist in the
        table.

        Example:
            >>> from google.area120 import tables_v1alpha
            >>>
            >>> client = tables_v1alpha.TablesServiceClient()
            >>>
            >>> # TODO: Initialize `name`:
            >>> name = ''
            >>>
            >>> response = client.get_row(name)

        Args:
            name (str): Required. The name of the row to retrieve.
                Format: tables/{table}/rows/{row}
            view (~google.area120.tables_v1alpha.types.View): Optional. Column key to use for values in the row.
                Defaults to user entered name.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.area120.tables_v1alpha.types.Row` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_row" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_row"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_row,
                default_retry=self._method_configs["GetRow"].retry,
                default_timeout=self._method_configs["GetRow"].timeout,
                client_info=self._client_info,
            )

        request = tables_pb2.GetRowRequest(name=name, view=view,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_row"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_rows(
        self,
        parent,
        page_size=None,
        view=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists rows in a table. Returns NOT_FOUND if the table does not
        exist.

        Example:
            >>> from google.area120 import tables_v1alpha
            >>>
            >>> client = tables_v1alpha.TablesServiceClient()
            >>>
            >>> # TODO: Initialize `parent`:
            >>> parent = ''
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_rows(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_rows(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The parent table.
                Format: tables/{table}
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            view (~google.area120.tables_v1alpha.types.View): Optional. Column key to use for values in the row.
                Defaults to user entered name.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.area120.tables_v1alpha.types.Row` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_rows" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_rows"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_rows,
                default_retry=self._method_configs["ListRows"].retry,
                default_timeout=self._method_configs["ListRows"].timeout,
                client_info=self._client_info,
            )

        request = tables_pb2.ListRowsRequest(
            parent=parent, page_size=page_size, view=view,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_rows"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="rows",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def create_row(
        self,
        parent,
        row,
        view=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a row.

        Example:
            >>> from google.area120 import tables_v1alpha
            >>>
            >>> client = tables_v1alpha.TablesServiceClient()
            >>>
            >>> # TODO: Initialize `parent`:
            >>> parent = ''
            >>>
            >>> # TODO: Initialize `row`:
            >>> row = {}
            >>>
            >>> response = client.create_row(parent, row)

        Args:
            parent (str): Required. The parent table where this row will be created.
                Format: tables/{table}
            row (Union[dict, ~google.area120.tables_v1alpha.types.Row]): Required. The row to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.area120.tables_v1alpha.types.Row`
            view (~google.area120.tables_v1alpha.types.View): Optional. Column key to use for values in the row.
                Defaults to user entered name.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.area120.tables_v1alpha.types.Row` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_row" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_row"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_row,
                default_retry=self._method_configs["CreateRow"].retry,
                default_timeout=self._method_configs["CreateRow"].timeout,
                client_info=self._client_info,
            )

        request = tables_pb2.CreateRowRequest(parent=parent, row=row, view=view,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_row"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def batch_create_rows(
        self,
        parent,
        requests,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates multiple rows.

        Example:
            >>> from google.area120 import tables_v1alpha
            >>>
            >>> client = tables_v1alpha.TablesServiceClient()
            >>>
            >>> # TODO: Initialize `parent`:
            >>> parent = ''
            >>>
            >>> # TODO: Initialize `requests`:
            >>> requests = []
            >>>
            >>> response = client.batch_create_rows(parent, requests)

        Args:
            parent (str): Required. The parent table where the rows will be created.
                Format: tables/{table}
            requests (list[Union[dict, ~google.area120.tables_v1alpha.types.CreateRowRequest]]): Required. The request message specifying the rows to create.

                A maximum of 500 rows can be created in a single batch.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.area120.tables_v1alpha.types.CreateRowRequest`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.area120.tables_v1alpha.types.BatchCreateRowsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "batch_create_rows" not in self._inner_api_calls:
            self._inner_api_calls[
                "batch_create_rows"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.batch_create_rows,
                default_retry=self._method_configs["BatchCreateRows"].retry,
                default_timeout=self._method_configs["BatchCreateRows"].timeout,
                client_info=self._client_info,
            )

        request = tables_pb2.BatchCreateRowsRequest(parent=parent, requests=requests,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["batch_create_rows"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_row(
        self,
        row,
        update_mask=None,
        view=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates a row.

        Example:
            >>> from google.area120 import tables_v1alpha
            >>>
            >>> client = tables_v1alpha.TablesServiceClient()
            >>>
            >>> # TODO: Initialize `row`:
            >>> row = {}
            >>>
            >>> response = client.update_row(row)

        Args:
            row (Union[dict, ~google.area120.tables_v1alpha.types.Row]): Required. The row to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.area120.tables_v1alpha.types.Row`
            update_mask (Union[dict, ~google.area120.tables_v1alpha.types.FieldMask]): The list of fields to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.area120.tables_v1alpha.types.FieldMask`
            view (~google.area120.tables_v1alpha.types.View): Optional. Column key to use for values in the row.
                Defaults to user entered name.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.area120.tables_v1alpha.types.Row` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_row" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_row"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_row,
                default_retry=self._method_configs["UpdateRow"].retry,
                default_timeout=self._method_configs["UpdateRow"].timeout,
                client_info=self._client_info,
            )

        request = tables_pb2.UpdateRowRequest(
            row=row, update_mask=update_mask, view=view,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("row.name", row.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_row"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def batch_update_rows(
        self,
        parent,
        requests,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates multiple rows.

        Example:
            >>> from google.area120 import tables_v1alpha
            >>>
            >>> client = tables_v1alpha.TablesServiceClient()
            >>>
            >>> # TODO: Initialize `parent`:
            >>> parent = ''
            >>>
            >>> # TODO: Initialize `requests`:
            >>> requests = []
            >>>
            >>> response = client.batch_update_rows(parent, requests)

        Args:
            parent (str): Required. The parent table shared by all rows being updated.
                Format: tables/{table}
            requests (list[Union[dict, ~google.area120.tables_v1alpha.types.UpdateRowRequest]]): Required. The request messages specifying the rows to update.

                A maximum of 500 rows can be modified in a single batch.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.area120.tables_v1alpha.types.UpdateRowRequest`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.area120.tables_v1alpha.types.BatchUpdateRowsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "batch_update_rows" not in self._inner_api_calls:
            self._inner_api_calls[
                "batch_update_rows"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.batch_update_rows,
                default_retry=self._method_configs["BatchUpdateRows"].retry,
                default_timeout=self._method_configs["BatchUpdateRows"].timeout,
                client_info=self._client_info,
            )

        request = tables_pb2.BatchUpdateRowsRequest(parent=parent, requests=requests,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["batch_update_rows"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_row(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a row.

        Example:
            >>> from google.area120 import tables_v1alpha
            >>>
            >>> client = tables_v1alpha.TablesServiceClient()
            >>>
            >>> name = client.row_path('[TABLE]', '[ROW]')
            >>>
            >>> client.delete_row(name)

        Args:
            name (str): Required. The name of the row to delete.
                Format: tables/{table}/rows/{row}
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_row" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_row"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_row,
                default_retry=self._method_configs["DeleteRow"].retry,
                default_timeout=self._method_configs["DeleteRow"].timeout,
                client_info=self._client_info,
            )

        request = tables_pb2.DeleteRowRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_row"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
