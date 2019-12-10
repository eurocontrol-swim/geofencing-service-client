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
from unittest.mock import Mock

import pytest

__author__ = "EUROCONTROL (SWIM)"

from rest_client.errors import APIError

from geofencing_service_client.geofencing_service import GeofencingServiceClient
from tests.utils import make_uas_zones_filter_reply, make_uas_zones_filter, make_uas_zone, make_uas_zone_create_reply, \
    make_subscribe_to_uas_zones_updates_reply, test_make_generic_reply

BASE_URL = 'geofencing-service/api/1.0/'


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_filter_uas_zones__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code
    response.text = '{"genericReply": {"RequestExceptionDescription": "error"}}'

    request_handler = Mock()
    request_handler.post = Mock(return_value=response)

    client = GeofencingServiceClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.filter_uas_zones(uas_zones_filter=Mock())


def test_filter_uas_zones__proper_response_is_returned():
    _, uas_zones_filter = make_uas_zones_filter()
    uas_zones_filter_reply_dict, expected_uas_zones_filter_reply = make_uas_zones_filter_reply()

    response = Mock()
    response.status_code = 200
    response.content = uas_zones_filter_reply_dict
    response.json = Mock(return_value=uas_zones_filter_reply_dict)

    request_handler = Mock()
    request_handler.post = Mock(return_value=response)

    client = GeofencingServiceClient(request_handler=request_handler)

    uas_zones_filter_reply = client.filter_uas_zones(uas_zones_filter=uas_zones_filter)

    assert expected_uas_zones_filter_reply == uas_zones_filter_reply

    called_url = request_handler.post.call_args[0][0]
    assert BASE_URL + 'uas_zones/filter/' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_create_uas_zones__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code
    response.text = '{"genericReply": {"RequestExceptionDescription": "error"}}'

    request_handler = Mock()
    request_handler.post = Mock(return_value=response)

    client = GeofencingServiceClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.post_uas_zone(uas_zone=Mock())


def test_uas_zone_create__proper_response_is_returned():
    _, uas_zone = make_uas_zone()
    uas_zone_create_reply_dict, expected_uas_zone_create_reply = make_uas_zone_create_reply()

    response = Mock()
    response.status_code = 200
    response.content = uas_zone_create_reply_dict
    response.json = Mock(return_value=uas_zone_create_reply_dict)

    request_handler = Mock()
    request_handler.post = Mock(return_value=response)

    client = GeofencingServiceClient(request_handler=request_handler)

    uas_zone_create_reply = client.post_uas_zone(uas_zone=uas_zone)

    assert expected_uas_zone_create_reply == uas_zone_create_reply

    called_url = request_handler.post.call_args[0][0]
    assert BASE_URL + 'uas_zones/' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_delete_uas_zone_by_identifier__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code
    response.text = '{"genericReply": {"RequestExceptionDescription": "error"}}'

    request_handler = Mock()
    request_handler.delete = Mock(return_value=response)

    client = GeofencingServiceClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.delete_uas_zone_by_identifier(uas_zone_identifier=1)


def test_delete_uas_zone_by_identifier():
    response = Mock()
    response.status_code = 204
    response.content = {}
    response.json = Mock(return_value={})

    request_handler = Mock()
    request_handler.delete = Mock(return_value=response)

    client = GeofencingServiceClient(request_handler=request_handler)

    client.delete_uas_zone_by_identifier(1)

    called_url = request_handler.delete.call_args[0][0]
    assert BASE_URL + 'uas_zones/1' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_post_subscription__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code
    response.text = '{"genericReply": {"RequestExceptionDescription": "error"}}'

    request_handler = Mock()
    request_handler.post = Mock(return_value=response)

    client = GeofencingServiceClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.post_subscription(uas_zones_filter=Mock())


def test_post_subscription__proper_response_is_returned():
    _, uas_zones_filter = make_uas_zones_filter()
    subscribe_to_uas_zones_updates_reply_dict, expected_subscribe_to_uas_zones_updates_reply = \
        make_subscribe_to_uas_zones_updates_reply()

    response = Mock()
    response.status_code = 201
    response.content = subscribe_to_uas_zones_updates_reply_dict
    response.json = Mock(return_value=subscribe_to_uas_zones_updates_reply_dict)

    request_handler = Mock()
    request_handler.post = Mock(return_value=response)

    client = GeofencingServiceClient(request_handler=request_handler)

    subscribe_to_uas_zones_updates_reply = client.post_subscription(uas_zones_filter=uas_zones_filter)

    assert expected_subscribe_to_uas_zones_updates_reply == subscribe_to_uas_zones_updates_reply

    called_url = request_handler.post.call_args[0][0]
    assert BASE_URL + 'subscriptions/' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_put_subscription__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code
    response.text = '{"genericReply": {"RequestExceptionDescription": "error"}}'

    request_handler = Mock()
    request_handler.put = Mock(return_value=response)

    client = GeofencingServiceClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.put_subscription(subscription_id='sub_id', update_data=Mock())


def test_put_subscription__proper_response_is_returned():
    _, uas_zones_filter = make_uas_zones_filter()
    generic_reply_dict, expected_generic_reply = test_make_generic_reply()

    response = Mock()
    response.status_code = 200
    response.content = generic_reply_dict
    response.json = Mock(return_value=generic_reply_dict)

    request_handler = Mock()
    request_handler.put = Mock(return_value=response)

    client = GeofencingServiceClient(request_handler=request_handler)

    generic_reply = client.put_subscription(subscription_id='sub_id', update_data=Mock())

    assert expected_generic_reply == generic_reply

    called_url = request_handler.put.call_args[0][0]
    assert BASE_URL + 'subscriptions/sub_id' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_delete_subscription_by_id__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code
    response.text = '{"genericReply": {"RequestExceptionDescription": "error"}}'

    request_handler = Mock()
    request_handler.delete = Mock(return_value=response)

    client = GeofencingServiceClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.delete_subscription_by_id(subscription_id='sub_id')


def test_delete_subscription_by_id__proper_response_is_returned():
    _, uas_zones_filter = make_uas_zones_filter()
    generic_reply_dict, expected_generic_reply = test_make_generic_reply()

    response = Mock()
    response.status_code = 204
    response.content = generic_reply_dict
    response.json = Mock(return_value=generic_reply_dict)

    request_handler = Mock()
    request_handler.delete = Mock(return_value=response)

    client = GeofencingServiceClient(request_handler=request_handler)

    generic_reply = client.delete_subscription_by_id(subscription_id='sub_id')

    assert expected_generic_reply == generic_reply

    called_url = request_handler.delete.call_args[0][0]
    assert BASE_URL + 'subscriptions/sub_id' == called_url
