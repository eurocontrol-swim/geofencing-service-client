"""
Copyright 2019 EUROCONTROL
==========================================

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
   disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
   disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

==========================================

Editorial note: this license is an instance of the BSD license template as provided by the Open Source Initiative:
http://opensource.org/licenses/BSD-3-Clause

Details on EUROCONTROL: http://www.eurocontrol.int
"""
import typing as t

from rest_client import Requestor, ClientFactory
from rest_client.typing import RequestHandler

from geofencing_service_client.errors import handle_geofencing_service_error
from geofencing_service_client.models import UASZone, UASZonesFilter, UASZoneFilterReply, UASZoneCreateReply, \
    SubscribeToUASZonesUpdatesReply, GenericReply, UASZoneSubscriptionReply, UASZoneSubscriptionsReply

__author__ = "EUROCONTROL (SWIM)"


class GeofencingServiceClient(Requestor, ClientFactory):

    _BASE_URL = 'geofencing-service/api/1.0/'

    def __init__(self, request_handler: RequestHandler) -> None:
        """
        :param request_handler: an instance of an object capable of handling http requests, i.e. requests.session()
        """
        Requestor.__init__(self, request_handler)

        self._url_uas_zones = self._BASE_URL + 'uas_zones/'
        self._url_uas_zones_filter = self._BASE_URL + 'uas_zones/filter/'
        self._url_uas_zones_by_identifier = self._BASE_URL + 'uas_zones/{uas_zone_identifier}'
        self._url_subscriptions = self._BASE_URL + 'subscriptions/'
        self._url_subscription_by_id = self._BASE_URL + 'subscriptions/{subscription_id}'
        self._url_ping_credentials = self._BASE_URL + 'ping-credentials'

    @handle_geofencing_service_error
    def filter_uas_zones(self, uas_zones_filter: UASZonesFilter) -> UASZoneFilterReply:
        """
        Retrieves UASZones based on the provided filter criteria

        :param uas_zones_filter:
        :return:
        """
        return self.perform_request('POST',
                                    self._url_uas_zones_filter,
                                    json=uas_zones_filter.to_json(),
                                    response_class=UASZoneFilterReply)

    @handle_geofencing_service_error
    def post_uas_zone(self, uas_zone: UASZone) -> UASZoneCreateReply:
        """
        Create a new UASZone

        :param uas_zone:
        :return:
        """
        return self.perform_request('POST',
                                    self._url_uas_zones,
                                    json=uas_zone.to_json(),
                                    response_class=UASZoneCreateReply)

    @handle_geofencing_service_error
    def delete_uas_zone_by_identifier(self, uas_zone_identifier: int) -> GenericReply:
        """
        Delete an UASZone

        :param uas_zone_identifier:
        :return:
        """
        url = self._url_uas_zones_by_identifier.format(uas_zone_identifier=uas_zone_identifier)

        return self.perform_request('DELETE', url, response_class=GenericReply)

    @handle_geofencing_service_error
    def post_subscription(self, uas_zones_filter: UASZonesFilter) -> SubscribeToUASZonesUpdatesReply:
        """
        Creates a new subscription based on the provided filter criteria. The subscriber can then use the returned
        broker publication_location in order to receive updates of created or deleted UASZones that satisfy the provided
        criteria.

        :param uas_zones_filter:
        :return:
        """
        return self.perform_request('POST',
                                    self._url_subscriptions,
                                    json=uas_zones_filter.to_json(),
                                    response_class=SubscribeToUASZonesUpdatesReply)

    @handle_geofencing_service_error
    def get_subscriptions(self) -> UASZoneSubscriptionsReply:
        """
        Retrieves subscription data (id and queue)

        :param subscription_id:
        :return:
        """
        return self.perform_request('GET', self._url_subscriptions, response_class=UASZoneSubscriptionsReply)

    @handle_geofencing_service_error
    def get_subscription_by_id(self, subscription_id: str) -> UASZoneSubscriptionReply:
        """
        Retrieves subscription data (id and queue)

        :param subscription_id:
        :return:
        """
        url = self._url_subscription_by_id.format(subscription_id=subscription_id)

        return self.perform_request('GET', url, response_class=UASZoneSubscriptionReply)

    @handle_geofencing_service_error
    def put_subscription(self, subscription_id: str, update_data: t.Dict[str, bool]) -> GenericReply:
        """
        It can be used to pause/resume a subscription by updating its status.
        Example:
            {'active': false} will pause a subscription if is already active
            {'active': true} will resume a subscription if is already paused

        :param subscription_id:
        :param update_data:
        :return:
        """
        url = self._url_subscription_by_id.format(subscription_id=subscription_id)

        return self.perform_request('PUT', url, json=update_data, response_class=GenericReply)

    @handle_geofencing_service_error
    def delete_subscription_by_id(self, subscription_id: str) -> GenericReply:
        """
        Unsubscribes the subscriber from the subscription by deleting the subscription

        :param subscription_id:
        :return:
        """
        url = self._url_subscription_by_id.format(subscription_id=subscription_id)

        return self.perform_request('DELETE', url, response_class=GenericReply)

    def ping_credentials(self):

        return self.perform_request('GET', self._url_ping_credentials)
