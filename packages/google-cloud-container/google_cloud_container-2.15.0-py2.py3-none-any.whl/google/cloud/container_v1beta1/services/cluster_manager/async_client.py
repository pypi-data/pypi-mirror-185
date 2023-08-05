# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)
import warnings

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.container_v1beta1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.rpc import status_pb2  # type: ignore

from google.cloud.container_v1beta1.services.cluster_manager import pagers
from google.cloud.container_v1beta1.types import cluster_service

from .client import ClusterManagerClient
from .transports.base import DEFAULT_CLIENT_INFO, ClusterManagerTransport
from .transports.grpc_asyncio import ClusterManagerGrpcAsyncIOTransport


class ClusterManagerAsyncClient:
    """Google Kubernetes Engine Cluster Manager v1beta1"""

    _client: ClusterManagerClient

    DEFAULT_ENDPOINT = ClusterManagerClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ClusterManagerClient.DEFAULT_MTLS_ENDPOINT

    topic_path = staticmethod(ClusterManagerClient.topic_path)
    parse_topic_path = staticmethod(ClusterManagerClient.parse_topic_path)
    common_billing_account_path = staticmethod(
        ClusterManagerClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ClusterManagerClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ClusterManagerClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ClusterManagerClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ClusterManagerClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ClusterManagerClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ClusterManagerClient.common_project_path)
    parse_common_project_path = staticmethod(
        ClusterManagerClient.parse_common_project_path
    )
    common_location_path = staticmethod(ClusterManagerClient.common_location_path)
    parse_common_location_path = staticmethod(
        ClusterManagerClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ClusterManagerAsyncClient: The constructed client.
        """
        return ClusterManagerClient.from_service_account_info.__func__(ClusterManagerAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ClusterManagerAsyncClient: The constructed client.
        """
        return ClusterManagerClient.from_service_account_file.__func__(ClusterManagerAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return ClusterManagerClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ClusterManagerTransport:
        """Returns the transport used by the client instance.

        Returns:
            ClusterManagerTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(ClusterManagerClient).get_transport_class, type(ClusterManagerClient)
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, ClusterManagerTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the cluster manager client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ClusterManagerTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = ClusterManagerClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_clusters(
        self,
        request: Optional[Union[cluster_service.ListClustersRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.ListClustersResponse:
        r"""Lists all clusters owned by a project in either the
        specified zone or all zones.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_list_clusters():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.ListClustersRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                )

                # Make the request
                response = await client.list_clusters(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.ListClustersRequest, dict]]):
                The request object. ListClustersRequest lists clusters.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the
                parent field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides, or "-" for all zones. This
                field has been deprecated and replaced by the parent
                field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.ListClustersResponse:
                ListClustersResponse is the result of
                ListClustersRequest.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.ListClustersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_clusters,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_cluster(
        self,
        request: Optional[Union[cluster_service.GetClusterRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Cluster:
        r"""Gets the details for a specific cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_get_cluster():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.GetClusterRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                )

                # Make the request
                response = await client.get_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.GetClusterRequest, dict]]):
                The request object. GetClusterRequest gets the settings
                of a cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster to retrieve. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Cluster:
                A Google Kubernetes Engine cluster.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.GetClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_cluster,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_cluster(
        self,
        request: Optional[Union[cluster_service.CreateClusterRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster: Optional[cluster_service.Cluster] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Creates a cluster, consisting of the specified number and type
        of Google Compute Engine instances.

        By default, the cluster is created in the project's `default
        network <https://cloud.google.com/compute/docs/networks-and-firewalls#networks>`__.

        One firewall is added for the cluster. After cluster creation,
        the Kubelet creates routes for each node to allow the containers
        on that node to communicate with all other instances in the
        cluster.

        Finally, an entry is added to the project's global metadata
        indicating which CIDR range the cluster is using.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_create_cluster():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.CreateClusterRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                )

                # Make the request
                response = await client.create_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.CreateClusterRequest, dict]]):
                The request object. CreateClusterRequest creates a
                cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the
                parent field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the parent field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster (:class:`google.cloud.container_v1beta1.types.Cluster`):
                Required. A `cluster
                resource <https://cloud.google.com/container-engine/reference/rest/v1beta1/projects.locations.clusters>`__

                This corresponds to the ``cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.CreateClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster is not None:
            request.cluster = cluster

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_cluster,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_cluster(
        self,
        request: Optional[Union[cluster_service.UpdateClusterRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        update: Optional[cluster_service.ClusterUpdate] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Updates the settings for a specific cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_update_cluster():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.UpdateClusterRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                )

                # Make the request
                response = await client.update_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.UpdateClusterRequest, dict]]):
                The request object. UpdateClusterRequest updates the
                settings of a cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster to upgrade. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update (:class:`google.cloud.container_v1beta1.types.ClusterUpdate`):
                Required. A description of the
                update.

                This corresponds to the ``update`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id, update])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.UpdateClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if update is not None:
            request.update = update

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_cluster,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_node_pool(
        self,
        request: Optional[Union[cluster_service.UpdateNodePoolRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Updates the version and/or image type of a specific
        node pool.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_update_node_pool():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.UpdateNodePoolRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    node_pool_id="node_pool_id_value",
                    node_version="node_version_value",
                    image_type="image_type_value",
                )

                # Make the request
                response = await client.update_node_pool(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.UpdateNodePoolRequest, dict]]):
                The request object. SetNodePoolVersionRequest updates
                the version of a node pool.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        request = cluster_service.UpdateNodePoolRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_node_pool,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_node_pool_autoscaling(
        self,
        request: Optional[
            Union[cluster_service.SetNodePoolAutoscalingRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Sets the autoscaling settings of a specific node
        pool.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_set_node_pool_autoscaling():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.SetNodePoolAutoscalingRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    node_pool_id="node_pool_id_value",
                )

                # Make the request
                response = await client.set_node_pool_autoscaling(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.SetNodePoolAutoscalingRequest, dict]]):
                The request object. SetNodePoolAutoscalingRequest sets
                the autoscaler settings of a node pool.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        request = cluster_service.SetNodePoolAutoscalingRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_node_pool_autoscaling,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_logging_service(
        self,
        request: Optional[Union[cluster_service.SetLoggingServiceRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        logging_service: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Sets the logging service for a specific cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_set_logging_service():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.SetLoggingServiceRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    logging_service="logging_service_value",
                )

                # Make the request
                response = await client.set_logging_service(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.SetLoggingServiceRequest, dict]]):
                The request object. SetLoggingServiceRequest sets the
                logging service of a cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster to upgrade. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            logging_service (:class:`str`):
                Required. The logging service the cluster should use to
                write logs. Currently available options:

                -  ``logging.googleapis.com/kubernetes`` - The Cloud
                   Logging service with a Kubernetes-native resource
                   model
                -  ``logging.googleapis.com`` - The legacy Cloud Logging
                   service (no longer available as of GKE 1.15).
                -  ``none`` - no logs will be exported from the cluster.

                If left as an empty
                string,\ ``logging.googleapis.com/kubernetes`` will be
                used for GKE 1.14+ or ``logging.googleapis.com`` for
                earlier versions.

                This corresponds to the ``logging_service`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id, logging_service])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.SetLoggingServiceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if logging_service is not None:
            request.logging_service = logging_service

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_logging_service,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_monitoring_service(
        self,
        request: Optional[
            Union[cluster_service.SetMonitoringServiceRequest, dict]
        ] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        monitoring_service: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Sets the monitoring service for a specific cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_set_monitoring_service():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.SetMonitoringServiceRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    monitoring_service="monitoring_service_value",
                )

                # Make the request
                response = await client.set_monitoring_service(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.SetMonitoringServiceRequest, dict]]):
                The request object. SetMonitoringServiceRequest sets the
                monitoring service of a cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster to upgrade. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            monitoring_service (:class:`str`):
                Required. The monitoring service the cluster should use
                to write metrics. Currently available options:

                -  "monitoring.googleapis.com/kubernetes" - The Cloud
                   Monitoring service with a Kubernetes-native resource
                   model
                -  ``monitoring.googleapis.com`` - The legacy Cloud
                   Monitoring service (no longer available as of GKE
                   1.15).
                -  ``none`` - No metrics will be exported from the
                   cluster.

                If left as an empty
                string,\ ``monitoring.googleapis.com/kubernetes`` will
                be used for GKE 1.14+ or ``monitoring.googleapis.com``
                for earlier versions.

                This corresponds to the ``monitoring_service`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id, monitoring_service])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.SetMonitoringServiceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if monitoring_service is not None:
            request.monitoring_service = monitoring_service

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_monitoring_service,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_addons_config(
        self,
        request: Optional[Union[cluster_service.SetAddonsConfigRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        addons_config: Optional[cluster_service.AddonsConfig] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Sets the addons for a specific cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_set_addons_config():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.SetAddonsConfigRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                )

                # Make the request
                response = await client.set_addons_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.SetAddonsConfigRequest, dict]]):
                The request object. SetAddonsRequest sets the addons
                associated with the cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster to upgrade. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            addons_config (:class:`google.cloud.container_v1beta1.types.AddonsConfig`):
                Required. The desired configurations
                for the various addons available to run
                in the cluster.

                This corresponds to the ``addons_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id, addons_config])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.SetAddonsConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if addons_config is not None:
            request.addons_config = addons_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_addons_config,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_locations(
        self,
        request: Optional[Union[cluster_service.SetLocationsRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        locations: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Sets the locations for a specific cluster. Deprecated. Use
        `projects.locations.clusters.update <https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/update>`__
        instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_set_locations():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.SetLocationsRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    locations=['locations_value1', 'locations_value2'],
                )

                # Make the request
                response = await client.set_locations(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.SetLocationsRequest, dict]]):
                The request object. SetLocationsRequest sets the
                locations of the cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster to upgrade. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            locations (:class:`MutableSequence[str]`):
                Required. The desired list of Google Compute Engine
                `zones <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster's nodes should be located. Changing
                the locations a cluster is in will result in nodes being
                either created or removed from the cluster, depending on
                whether locations are being added or removed.

                This list must always include the cluster's primary
                zone.

                This corresponds to the ``locations`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        warnings.warn(
            "ClusterManagerAsyncClient.set_locations is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id, locations])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.SetLocationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if locations:
            request.locations.extend(locations)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_locations,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_master(
        self,
        request: Optional[Union[cluster_service.UpdateMasterRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        master_version: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Updates the master for a specific cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_update_master():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.UpdateMasterRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    master_version="master_version_value",
                )

                # Make the request
                response = await client.update_master(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.UpdateMasterRequest, dict]]):
                The request object. UpdateMasterRequest updates the
                master of the cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster to upgrade. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            master_version (:class:`str`):
                Required. The Kubernetes version to
                change the master to.
                Users may specify either explicit
                versions offered by Kubernetes Engine or
                version aliases, which have the
                following behavior:
                - "latest": picks the highest valid
                Kubernetes version - "1.X": picks the
                highest valid patch+gke.N patch in the
                1.X version - "1.X.Y": picks the highest
                valid gke.N patch in the 1.X.Y version -
                "1.X.Y-gke.N": picks an explicit
                Kubernetes version - "-": picks the
                default Kubernetes version

                This corresponds to the ``master_version`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id, master_version])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.UpdateMasterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if master_version is not None:
            request.master_version = master_version

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_master,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_master_auth(
        self,
        request: Optional[Union[cluster_service.SetMasterAuthRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Sets master auth materials. Currently supports
        changing the admin password or a specific cluster,
        either via password generation or explicitly setting the
        password.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_set_master_auth():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.SetMasterAuthRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    action="SET_USERNAME",
                )

                # Make the request
                response = await client.set_master_auth(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.SetMasterAuthRequest, dict]]):
                The request object. SetMasterAuthRequest updates the
                admin password of a cluster.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        request = cluster_service.SetMasterAuthRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_master_auth,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_cluster(
        self,
        request: Optional[Union[cluster_service.DeleteClusterRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Deletes the cluster, including the Kubernetes
        endpoint and all worker nodes.

        Firewalls and routes that were configured during cluster
        creation are also deleted.

        Other Google Compute Engine resources that might be in
        use by the cluster, such as load balancer resources, are
        not deleted if they weren't present when the cluster was
        initially created.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_delete_cluster():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.DeleteClusterRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                )

                # Make the request
                response = await client.delete_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.DeleteClusterRequest, dict]]):
                The request object. DeleteClusterRequest deletes a
                cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster to delete. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.DeleteClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_cluster,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_operations(
        self,
        request: Optional[Union[cluster_service.ListOperationsRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.ListOperationsResponse:
        r"""Lists all operations in a project in the specified
        zone or all zones.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_list_operations():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.ListOperationsRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                )

                # Make the request
                response = await client.list_operations(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.ListOperationsRequest, dict]]):
                The request object. ListOperationsRequest lists
                operations.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the
                parent field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                to return operations for, or ``-`` for all zones. This
                field has been deprecated and replaced by the parent
                field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.ListOperationsResponse:
                ListOperationsResponse is the result
                of ListOperationsRequest.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.ListOperationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_operations,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_operation(
        self,
        request: Optional[Union[cluster_service.GetOperationRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        operation_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Gets the specified operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_get_operation():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.GetOperationRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    operation_id="operation_id_value",
                )

                # Make the request
                response = await client.get_operation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.GetOperationRequest, dict]]):
                The request object. GetOperationRequest gets a single
                operation.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            operation_id (:class:`str`):
                Required. Deprecated. The server-assigned ``name`` of
                the operation. This field has been deprecated and
                replaced by the name field.

                This corresponds to the ``operation_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, operation_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.GetOperationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if operation_id is not None:
            request.operation_id = operation_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_operation,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def cancel_operation(
        self,
        request: Optional[Union[cluster_service.CancelOperationRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        operation_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Cancels the specified operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_cancel_operation():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.CancelOperationRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    operation_id="operation_id_value",
                )

                # Make the request
                await client.cancel_operation(request=request)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.CancelOperationRequest, dict]]):
                The request object. CancelOperationRequest cancels a
                single operation.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the operation resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            operation_id (:class:`str`):
                Required. Deprecated. The server-assigned ``name`` of
                the operation. This field has been deprecated and
                replaced by the name field.

                This corresponds to the ``operation_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, operation_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.CancelOperationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if operation_id is not None:
            request.operation_id = operation_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.cancel_operation,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def get_server_config(
        self,
        request: Optional[Union[cluster_service.GetServerConfigRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.ServerConfig:
        r"""Returns configuration info about the Google
        Kubernetes Engine service.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_get_server_config():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.GetServerConfigRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                )

                # Make the request
                response = await client.get_server_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.GetServerConfigRequest, dict]]):
                The request object. Gets the current Kubernetes Engine
                service configuration.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                to return operations for. This field has been deprecated
                and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.ServerConfig:
                Kubernetes Engine service
                configuration.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.GetServerConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_server_config,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_node_pools(
        self,
        request: Optional[Union[cluster_service.ListNodePoolsRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.ListNodePoolsResponse:
        r"""Lists the node pools for a cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_list_node_pools():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.ListNodePoolsRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                )

                # Make the request
                response = await client.list_node_pools(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.ListNodePoolsRequest, dict]]):
                The request object. ListNodePoolsRequest lists the node
                pool(s) for a cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the
                parent field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the parent field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster. This field has been deprecated
                and replaced by the parent field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.ListNodePoolsResponse:
                ListNodePoolsResponse is the result
                of ListNodePoolsRequest.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.ListNodePoolsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_node_pools,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_json_web_keys(
        self,
        request: Optional[Union[cluster_service.GetJSONWebKeysRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.GetJSONWebKeysResponse:
        r"""Gets the public component of the cluster signing keys
        in JSON Web Key format.
        This API is not yet intended for general use, and is not
        available for all clusters.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_get_json_web_keys():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.GetJSONWebKeysRequest(
                )

                # Make the request
                response = await client.get_json_web_keys(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.GetJSONWebKeysRequest, dict]]):
                The request object. GetJSONWebKeysRequest gets the
                public component of the keys used by the cluster to sign
                token requests. This will be the jwks_uri for the
                discover document returned by getOpenIDConfig. See the
                OpenID Connect Discovery 1.0 specification for details.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.GetJSONWebKeysResponse:
                GetJSONWebKeysResponse is a valid
                JSON Web Key Set as specififed in rfc
                7517

        """
        # Create or coerce a protobuf request object.
        request = cluster_service.GetJSONWebKeysRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_json_web_keys,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_node_pool(
        self,
        request: Optional[Union[cluster_service.GetNodePoolRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        node_pool_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.NodePool:
        r"""Retrieves the requested node pool.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_get_node_pool():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.GetNodePoolRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    node_pool_id="node_pool_id_value",
                )

                # Make the request
                response = await client.get_node_pool(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.GetNodePoolRequest, dict]]):
                The request object. GetNodePoolRequest retrieves a node
                pool for a cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster. This field has been deprecated
                and replaced by the name field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            node_pool_id (:class:`str`):
                Required. Deprecated. The name of the
                node pool. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``node_pool_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.NodePool:
                NodePool contains the name and
                configuration for a cluster's node pool.
                Node pools are a set of nodes (i.e.
                VM's), with a common configuration and
                specification, under the control of the
                cluster master. They may have a set of
                Kubernetes labels applied to them, which
                may be used to reference them during pod
                scheduling. They may also be resized up
                or down, to accommodate the workload.
                These upgrade settings control the level
                of parallelism and the level of
                disruption caused by an upgrade.

                maxUnavailable controls the number of
                nodes that can be simultaneously
                unavailable.

                maxSurge controls the number of
                additional nodes that can be added to
                the node pool temporarily for the time
                of the upgrade to increase the number of
                available nodes.

                (maxUnavailable + maxSurge) determines
                the level of parallelism (how many nodes
                are being upgraded at the same time).
                Note: upgrades inevitably introduce some
                disruption since workloads need to be
                moved from old nodes to new, upgraded
                ones. Even if maxUnavailable=0, this
                holds true. (Disruption stays within the
                limits of PodDisruptionBudget, if it is
                configured.)
                Consider a hypothetical node pool with 5
                nodes having maxSurge=2,
                maxUnavailable=1. This means the upgrade
                process upgrades 3 nodes simultaneously.
                It creates 2 additional (upgraded)
                nodes, then it brings down 3 old (not
                yet upgraded) nodes at the same time.
                This ensures that there are always at
                least 4 nodes available.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id, node_pool_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.GetNodePoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if node_pool_id is not None:
            request.node_pool_id = node_pool_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_node_pool,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_node_pool(
        self,
        request: Optional[Union[cluster_service.CreateNodePoolRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        node_pool: Optional[cluster_service.NodePool] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Creates a node pool for a cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_create_node_pool():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.CreateNodePoolRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                )

                # Make the request
                response = await client.create_node_pool(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.CreateNodePoolRequest, dict]]):
                The request object. CreateNodePoolRequest creates a node
                pool for a cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the
                parent field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the parent field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster. This field has been deprecated
                and replaced by the parent field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            node_pool (:class:`google.cloud.container_v1beta1.types.NodePool`):
                Required. The node pool to create.
                This corresponds to the ``node_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id, node_pool])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.CreateNodePoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if node_pool is not None:
            request.node_pool = node_pool

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_node_pool,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_node_pool(
        self,
        request: Optional[Union[cluster_service.DeleteNodePoolRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        node_pool_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Deletes a node pool from a cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_delete_node_pool():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.DeleteNodePoolRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    node_pool_id="node_pool_id_value",
                )

                # Make the request
                response = await client.delete_node_pool(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.DeleteNodePoolRequest, dict]]):
                The request object. DeleteNodePoolRequest deletes a node
                pool for a cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster. This field has been deprecated
                and replaced by the name field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            node_pool_id (:class:`str`):
                Required. Deprecated. The name of the
                node pool to delete. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``node_pool_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id, node_pool_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.DeleteNodePoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if node_pool_id is not None:
            request.node_pool_id = node_pool_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_node_pool,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def complete_node_pool_upgrade(
        self,
        request: Optional[
            Union[cluster_service.CompleteNodePoolUpgradeRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""CompleteNodePoolUpgrade will signal an on-going node
        pool upgrade to complete.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_complete_node_pool_upgrade():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.CompleteNodePoolUpgradeRequest(
                )

                # Make the request
                await client.complete_node_pool_upgrade(request=request)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.CompleteNodePoolUpgradeRequest, dict]]):
                The request object. CompleteNodePoolUpgradeRequest sets
                the name of target node pool to complete upgrade.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        request = cluster_service.CompleteNodePoolUpgradeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.complete_node_pool_upgrade,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def rollback_node_pool_upgrade(
        self,
        request: Optional[
            Union[cluster_service.RollbackNodePoolUpgradeRequest, dict]
        ] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        node_pool_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Rolls back a previously Aborted or Failed NodePool
        upgrade. This makes no changes if the last upgrade
        successfully completed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_rollback_node_pool_upgrade():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.RollbackNodePoolUpgradeRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    node_pool_id="node_pool_id_value",
                )

                # Make the request
                response = await client.rollback_node_pool_upgrade(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.RollbackNodePoolUpgradeRequest, dict]]):
                The request object. RollbackNodePoolUpgradeRequest
                rollbacks the previously Aborted or Failed NodePool
                upgrade. This will be an no-op if the last upgrade
                successfully completed.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster to rollback. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            node_pool_id (:class:`str`):
                Required. Deprecated. The name of the
                node pool to rollback. This field has
                been deprecated and replaced by the name
                field.

                This corresponds to the ``node_pool_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id, node_pool_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.RollbackNodePoolUpgradeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if node_pool_id is not None:
            request.node_pool_id = node_pool_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.rollback_node_pool_upgrade,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_node_pool_management(
        self,
        request: Optional[
            Union[cluster_service.SetNodePoolManagementRequest, dict]
        ] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        node_pool_id: Optional[str] = None,
        management: Optional[cluster_service.NodeManagement] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Sets the NodeManagement options for a node pool.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_set_node_pool_management():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.SetNodePoolManagementRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    node_pool_id="node_pool_id_value",
                )

                # Make the request
                response = await client.set_node_pool_management(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.SetNodePoolManagementRequest, dict]]):
                The request object. SetNodePoolManagementRequest sets
                the node management properties of a node pool.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster to update. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            node_pool_id (:class:`str`):
                Required. Deprecated. The name of the
                node pool to update. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``node_pool_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            management (:class:`google.cloud.container_v1beta1.types.NodeManagement`):
                Required. NodeManagement
                configuration for the node pool.

                This corresponds to the ``management`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [project_id, zone, cluster_id, node_pool_id, management]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.SetNodePoolManagementRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if node_pool_id is not None:
            request.node_pool_id = node_pool_id
        if management is not None:
            request.management = management

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_node_pool_management,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_labels(
        self,
        request: Optional[Union[cluster_service.SetLabelsRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        resource_labels: Optional[MutableMapping[str, str]] = None,
        label_fingerprint: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Sets labels on a cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_set_labels():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.SetLabelsRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    label_fingerprint="label_fingerprint_value",
                )

                # Make the request
                response = await client.set_labels(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.SetLabelsRequest, dict]]):
                The request object. SetLabelsRequest sets the Google
                Cloud Platform labels on a Google Container Engine
                cluster, which will in turn set them for Google Compute
                Engine resources used by that cluster
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster. This field has been deprecated
                and replaced by the name field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            resource_labels (:class:`MutableMapping[str, str]`):
                Required. The labels to set for that
                cluster.

                This corresponds to the ``resource_labels`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            label_fingerprint (:class:`str`):
                Required. The fingerprint of the previous set of labels
                for this resource, used to detect conflicts. The
                fingerprint is initially generated by Kubernetes Engine
                and changes after every request to modify or update
                labels. You must always provide an up-to-date
                fingerprint hash when updating or changing labels. Make
                a ``get()`` request to the resource to get the latest
                fingerprint.

                This corresponds to the ``label_fingerprint`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [project_id, zone, cluster_id, resource_labels, label_fingerprint]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.SetLabelsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if label_fingerprint is not None:
            request.label_fingerprint = label_fingerprint

        if resource_labels:
            request.resource_labels.update(resource_labels)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_labels,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_legacy_abac(
        self,
        request: Optional[Union[cluster_service.SetLegacyAbacRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        enabled: Optional[bool] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Enables or disables the ABAC authorization mechanism
        on a cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_set_legacy_abac():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.SetLegacyAbacRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    enabled=True,
                )

                # Make the request
                response = await client.set_legacy_abac(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.SetLegacyAbacRequest, dict]]):
                The request object. SetLegacyAbacRequest enables or
                disables the ABAC authorization mechanism for a cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster to update. This field has been
                deprecated and replaced by the name
                field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            enabled (:class:`bool`):
                Required. Whether ABAC authorization
                will be enabled in the cluster.

                This corresponds to the ``enabled`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id, enabled])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.SetLegacyAbacRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if enabled is not None:
            request.enabled = enabled

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_legacy_abac,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def start_ip_rotation(
        self,
        request: Optional[Union[cluster_service.StartIPRotationRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Starts master IP rotation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_start_ip_rotation():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.StartIPRotationRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                )

                # Make the request
                response = await client.start_ip_rotation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.StartIPRotationRequest, dict]]):
                The request object. StartIPRotationRequest creates a new
                IP for the cluster and then performs a node upgrade on
                each node pool to point to the new IP.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster. This field has been deprecated
                and replaced by the name field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.StartIPRotationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.start_ip_rotation,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def complete_ip_rotation(
        self,
        request: Optional[
            Union[cluster_service.CompleteIPRotationRequest, dict]
        ] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Completes master IP rotation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_complete_ip_rotation():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.CompleteIPRotationRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                )

                # Make the request
                response = await client.complete_ip_rotation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.CompleteIPRotationRequest, dict]]):
                The request object. CompleteIPRotationRequest moves the
                cluster master back into single-IP mode.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster. This field has been deprecated
                and replaced by the name field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.CompleteIPRotationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.complete_ip_rotation,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_node_pool_size(
        self,
        request: Optional[Union[cluster_service.SetNodePoolSizeRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""SetNodePoolSizeRequest sets the size of a node pool. The new
        size will be used for all replicas, including future replicas
        created by modifying
        [NodePool.locations][google.container.v1beta1.NodePool.locations].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_set_node_pool_size():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.SetNodePoolSizeRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                    node_pool_id="node_pool_id_value",
                    node_count=1070,
                )

                # Make the request
                response = await client.set_node_pool_size(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.SetNodePoolSizeRequest, dict]]):
                The request object. SetNodePoolSizeRequest sets the size
                of a node pool.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        request = cluster_service.SetNodePoolSizeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_node_pool_size,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_network_policy(
        self,
        request: Optional[Union[cluster_service.SetNetworkPolicyRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        network_policy: Optional[cluster_service.NetworkPolicy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Enables or disables Network Policy for a cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_set_network_policy():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.SetNetworkPolicyRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                )

                # Make the request
                response = await client.set_network_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.SetNetworkPolicyRequest, dict]]):
                The request object. SetNetworkPolicyRequest
                enables/disables network policy for a cluster.
            project_id (:class:`str`):
                Required. Deprecated. The Google Developers Console
                `project ID or project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.
                This field has been deprecated and replaced by the name
                field.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. Deprecated. The name of the Google Compute
                Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides. This field has been
                deprecated and replaced by the name field.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. Deprecated. The name of the
                cluster. This field has been deprecated
                and replaced by the name field.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            network_policy (:class:`google.cloud.container_v1beta1.types.NetworkPolicy`):
                Required. Configuration options for
                the NetworkPolicy feature.

                This corresponds to the ``network_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id, network_policy])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.SetNetworkPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if network_policy is not None:
            request.network_policy = network_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_network_policy,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_maintenance_policy(
        self,
        request: Optional[
            Union[cluster_service.SetMaintenancePolicyRequest, dict]
        ] = None,
        *,
        project_id: Optional[str] = None,
        zone: Optional[str] = None,
        cluster_id: Optional[str] = None,
        maintenance_policy: Optional[cluster_service.MaintenancePolicy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.Operation:
        r"""Sets the maintenance policy for a cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_set_maintenance_policy():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.SetMaintenancePolicyRequest(
                    project_id="project_id_value",
                    zone="zone_value",
                    cluster_id="cluster_id_value",
                )

                # Make the request
                response = await client.set_maintenance_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.SetMaintenancePolicyRequest, dict]]):
                The request object. SetMaintenancePolicyRequest sets the
                maintenance policy for a cluster.
            project_id (:class:`str`):
                Required. The Google Developers Console `project ID or
                project
                number <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`__.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            zone (:class:`str`):
                Required. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__
                in which the cluster resides.

                This corresponds to the ``zone`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (:class:`str`):
                Required. The name of the cluster to
                update.

                This corresponds to the ``cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            maintenance_policy (:class:`google.cloud.container_v1beta1.types.MaintenancePolicy`):
                Required. The maintenance policy to
                be set for the cluster. An empty field
                clears the existing maintenance policy.

                This corresponds to the ``maintenance_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.Operation:
                This operation resource represents
                operations that may have happened or are
                happening on the cluster. All fields are
                output only.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project_id, zone, cluster_id, maintenance_policy])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.SetMaintenancePolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if zone is not None:
            request.zone = zone
        if cluster_id is not None:
            request.cluster_id = cluster_id
        if maintenance_policy is not None:
            request.maintenance_policy = maintenance_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_maintenance_policy,
            default_timeout=45.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_usable_subnetworks(
        self,
        request: Optional[
            Union[cluster_service.ListUsableSubnetworksRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListUsableSubnetworksAsyncPager:
        r"""Lists subnetworks that can be used for creating
        clusters in a project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_list_usable_subnetworks():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.ListUsableSubnetworksRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_usable_subnetworks(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.ListUsableSubnetworksRequest, dict]]):
                The request object. ListUsableSubnetworksRequest
                requests the list of usable subnetworks. available to a
                user for creating clusters.
            parent (:class:`str`):
                Required. The parent project where subnetworks are
                usable. Specified in the format ``projects/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.services.cluster_manager.pagers.ListUsableSubnetworksAsyncPager:
                ListUsableSubnetworksResponse is the
                response of
                ListUsableSubnetworksRequest.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.ListUsableSubnetworksRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_usable_subnetworks,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListUsableSubnetworksAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_locations(
        self,
        request: Optional[Union[cluster_service.ListLocationsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> cluster_service.ListLocationsResponse:
        r"""Fetches locations that offer Google Kubernetes
        Engine.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import container_v1beta1

            async def sample_list_locations():
                # Create a client
                client = container_v1beta1.ClusterManagerAsyncClient()

                # Initialize request argument(s)
                request = container_v1beta1.ListLocationsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.list_locations(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.container_v1beta1.types.ListLocationsRequest, dict]]):
                The request object. ListLocationsRequest is used to
                request the locations that offer GKE.
            parent (:class:`str`):
                Required. Contains the name of the resource requested.
                Specified in the format ``projects/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.container_v1beta1.types.ListLocationsResponse:
                ListLocationsResponse returns the
                list of all GKE locations and their
                recommendation state.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cluster_service.ListLocationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_locations,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("ClusterManagerAsyncClient",)
