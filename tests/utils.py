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

__author__ = "EUROCONTROL (SWIM)"

from typing import Tuple, Dict, Any

from geofencing_service_client.models import UASZonesFilter, UASZone, GenericReply, UASZoneFilterReply, \
    UASZoneCreateReply, SubscribeToUASZonesUpdatesReply, UASZoneSubscriptionReplyObject, UASZoneSubscriptionReply, \
    UASZoneSubscriptionsReply


def make_uas_zones_filter() -> Tuple[Dict[str, Any], UASZonesFilter]:
    usa_zones_filter_dict = {
        'airspaceVolume': {
            "lowerLimit": 0,
            "lowerVerticalReference": "AGL",
            "polygon": [
                {
                    "LAT": "50.862525",
                    "LON": "4.32812"
                },
                {
                    "LAT": "50.865502",
                    "LON": "4.329257"
                },
                {
                    "LAT": "50.865468",
                    "LON": "4.323686"
                },
                {
                    "LAT": "50.862525",
                    "LON": "4.32812"
                }
            ],
            "upperLimit": 0,
            "upperVerticalReference": "AGL"
        },
        'regions': [1],
        'requestID': 'request',
        'startDateTime': '2020-01-01T00:00:00+00:00',
        'endDateTime': '2020-02-01T00:00:00+00:00',
        'updatedAfterDateTime': '2020-01-15T00:00:00+00:00',
    }

    uas_zones_filter = UASZonesFilter.from_json(usa_zones_filter_dict)

    return usa_zones_filter_dict, uas_zones_filter


def make_uas_zone() -> Tuple[Dict[str, Any], UASZone]:
    uas_zone_dict = {
        'airspaceVolume': {
            "lowerLimit": 0,
            "lowerVerticalReference": "AGL",
            "polygon": [
                {
                    "LAT": "50.862525",
                    "LON": "4.32812"
                },
                {
                    "LAT": "50.865502",
                    "LON": "4.329257"
                },
                {
                    "LAT": "50.865468",
                    "LON": "4.323686"
                },
                {
                    "LAT": "50.862525",
                    "LON": "4.32812"
                }
            ],
            "upperLimit": 0,
            "upperVerticalReference": "AGL"
        },
        'applicableTimePeriod': {
            'dailySchedule': [{
                'day': 'MON',
                'endTime': '18:00:00+00:00',
                'startTime': '12:00:00+00:00'
            }, {
                'day': 'SAT',
                'endTime': '15:00:00+00:00',
                'startTime': '09:00:00+00:00'
            }],
            'endDateTime': '2021-01-01T00:00:00+00:00',
            'permanent': 'YES',
            'startDateTime': '2020-01-01T00:00:00+00:00',
        },
        'authority': {
            'requiresAuthorizationFrom': {
                'authority': {
                    'contactName': 'AuthorityEntity manager',
                    'email': 'auth@autority.be',
                    'name': '175d280099fb48eea5da490ac12f816a',
                    'phone': '234234234',
                    'service': 'AuthorityEntity service',
                    'siteURL': 'http://www.autority.be'
                }
            },
            'requiresNotificationTo': {
                'authority': {
                    'contactName': 'AuthorityEntity manager',
                    'email': 'auth@autority.be',
                    'name': '175d280099fb48eea5da490ac12f816a',
                    'phone': '234234234',
                    'service': 'AuthorityEntity service',
                    'siteURL': 'http://www.autority.be'
                },
                'intervalBefore': 'P1D'
            }
        },
        'country': 'BEL',
        'dataCaptureProhibition': 'YES',
        'dataSource': {
            'author': 'Author',
            'creationDateTime': '2019-01-01T00:00:00+00:00',
            'updateDateTime': '2019-01-02T00:00:00+00:00'
        },
        'extendedProperties': {},
        'identifier': "zsdffgs",
        'message': 'message',
        'name': "",
        'reason': [],
        'region': 1,
        'restriction': 'NO_RESTRICTION',
        'restrictionConditions': [],
        'type': 'COMMON',
        'uSpaceClass': 'EUROCONTROL',
    }

    uas_zone = UASZone.from_json(uas_zone_dict)

    return uas_zone_dict, uas_zone


def test_make_generic_reply() -> Tuple[Dict[str, Any], GenericReply]:
    generic_reply_dict = {
        'RequestStatus': 'OK',
        'RequestExceptionDescription': 'everything ok',
        'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
    }

    generic_reply = GenericReply.from_json(generic_reply_dict)

    return generic_reply_dict, generic_reply


def make_uas_zones_filter_reply() -> Tuple[Dict[str, Any], UASZoneFilterReply]:
    uas_zones_filter_reply_dict = {
            'UASZoneList': [
                {
                    'airspaceVolume': {
                        "lowerLimit": 0,
                        "lowerVerticalReference": "AGL",
                        "polygon": [
                            {
                                "LAT": "50.862525",
                                "LON": "4.32812"
                            },
                            {
                                "LAT": "50.865502",
                                "LON": "4.329257"
                            },
                            {
                                "LAT": "50.865468",
                                "LON": "4.323686"
                            },
                            {
                                "LAT": "50.862525",
                                "LON": "4.32812"
                            }
                        ],
                        "upperLimit": 0,
                        "upperVerticalReference": "AGL"
                    },
                    'applicableTimePeriod': {
                        'dailySchedule': [{
                            'day': 'MON',
                            'endTime': '18:00:00+00:00',
                            'startTime': '12:00:00+00:00'
                        }, {
                            'day': 'SAT',
                            'endTime': '15:00:00+00:00',
                            'startTime': '09:00:00+00:00'
                        }],
                        'endDateTime': '2021-01-01T00:00:00+00:00',
                        'permanent': 'YES',
                        'startDateTime': '2020-01-01T00:00:00+00:00',
                    },
                    'authority': {
                        'requiresAuthorizationFrom': {
                            'authority': {
                                'contactName': 'AuthorityEntity manager',
                                'email': 'auth@autority.be',
                                'name': '175d280099fb48eea5da490ac12f816a',
                                'phone': '234234234',
                                'service': 'AuthorityEntity service',
                                'siteURL': 'http://www.autority.be'
                            }
                        },
                        'requiresNotificationTo': {
                            'authority': {
                                'contactName': 'AuthorityEntity manager',
                                'email': 'auth@autority.be',
                                'name': '175d280099fb48eea5da490ac12f816a',
                                'phone': '234234234',
                                'service': 'AuthorityEntity service',
                                'siteURL': 'http://www.autority.be'
                            },
                            'intervalBefore': 'P1D'
                        }
                    },
                    'country': 'BEL',
                    'dataCaptureProhibition': 'YES',
                    'dataSource': {
                        'author': 'Author',
                        'creationDateTime': '2019-01-01T00:00:00+00:00',
                        'updateDateTime': '2019-01-02T00:00:00+00:00'
                    },
                    'extendedProperties': {},
                    'identifier': "zsdffgs",
                    'message': 'message',
                    'name': "",
                    'reason': [],
                    'region': 1,
                    'restriction': 'NO_RESTRICTION',
                    'restrictionConditions': [],
                    'type': 'COMMON',
                    'uSpaceClass': 'EUROCONTROL',
                }
            ],
            'genericReply': {
                'RequestStatus': 'OK',
                'RequestExceptionDescription': 'everything ok',
                'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
            }
        }

    uas_zones_filter_reply = UASZoneFilterReply.from_json(uas_zones_filter_reply_dict)

    return uas_zones_filter_reply_dict, uas_zones_filter_reply


def make_uas_zone_create_reply():
    uas_zone_create_reply_dict = {
        'UASZone': {
            'airspaceVolume': {
                "lowerLimit": 0,
                "lowerVerticalReference": "AGL",
                "polygon": [
                    {
                        "LAT": "50.862525",
                        "LON": "4.32812"
                    },
                    {
                        "LAT": "50.865502",
                        "LON": "4.329257"
                    },
                    {
                        "LAT": "50.865468",
                        "LON": "4.323686"
                    },
                    {
                        "LAT": "50.862525",
                        "LON": "4.32812"
                    }
                ],
                "upperLimit": 0,
                "upperVerticalReference": "AGL"
            },
            'applicableTimePeriod': {
                'dailySchedule': [{
                    'day': 'MON',
                    'endTime': '18:00:00+00:00',
                    'startTime': '12:00:00+00:00'
                }, {
                    'day': 'SAT',
                    'endTime': '15:00:00+00:00',
                    'startTime': '09:00:00+00:00'
                }],
                'endDateTime': '2021-01-01T00:00:00+00:00',
                'permanent': 'YES',
                'startDateTime': '2020-01-01T00:00:00+00:00',
            },
            'authority': {
                'requiresAuthorizationFrom': {
                    'authority': {
                        'contactName': 'AuthorityEntity manager',
                        'email': 'auth@autority.be',
                        'name': '175d280099fb48eea5da490ac12f816a',
                        'phone': '234234234',
                        'service': 'AuthorityEntity service',
                        'siteURL': 'http://www.autority.be'
                    }
                },
                'requiresNotificationTo': {
                    'authority': {
                        'contactName': 'AuthorityEntity manager',
                        'email': 'auth@autority.be',
                        'name': '175d280099fb48eea5da490ac12f816a',
                        'phone': '234234234',
                        'service': 'AuthorityEntity service',
                        'siteURL': 'http://www.autority.be'
                    },
                    'intervalBefore': 'P1D'
                }
            },
            'country': 'BEL',
            'dataCaptureProhibition': 'YES',
            'dataSource': {
                'author': 'Author',
                'creationDateTime': '2019-01-01T00:00:00+00:00',
                'updateDateTime': '2019-01-02T00:00:00+00:00'
            },
            'extendedProperties': {},
            'identifier': "zsdffgs",
            'message': 'message',
            'name': "",
            'reason': [],
            'region': 1,
            'restriction': 'NO_RESTRICTION',
            'restrictionConditions': [],
            'type': 'COMMON',
            'uSpaceClass': 'EUROCONTROL',
        },
        'genericReply': {
            'RequestStatus': 'OK',
            'RequestExceptionDescription': 'everything ok',
            'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
        }
    }

    uas_zone_create_reply = UASZoneCreateReply.from_json(uas_zone_create_reply_dict)

    return uas_zone_create_reply_dict, uas_zone_create_reply


def make_subscribe_to_uas_zones_updates_reply():
    subscribe_to_uas_zones_updates_reply_dict = {
        'subscriptionID': '123456',
        'publicationLocation': 'location',
        'genericReply': {
            'RequestStatus': 'OK',
            'RequestExceptionDescription': 'everything ok',
            'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
        }
    }
    subscribe_to_uas_zones_updates_reply = SubscribeToUASZonesUpdatesReply.from_json(
        subscribe_to_uas_zones_updates_reply_dict)

    return subscribe_to_uas_zones_updates_reply_dict, subscribe_to_uas_zones_updates_reply


def make_uas_zone_subscription_reply_object():
    uas_zones_filter_dict, _ = make_uas_zones_filter()

    uas_zone_subscription_reply_object_dict = {
        'subscriptionID': '123456',
        'publicationLocation': 'location',
        'active': True,
        'UASZonesFilter': uas_zones_filter_dict
    }
    uas_zone_subscription_object_reply = UASZoneSubscriptionReplyObject.from_json(
        uas_zone_subscription_reply_object_dict)

    return uas_zone_subscription_reply_object_dict, uas_zone_subscription_object_reply


def make_uas_zone_subscription_reply():
    uas_zone_subscription_reply_object_dict, _ = make_uas_zone_subscription_reply_object()

    uas_zone_subscription_reply_dict = {
        'UASZoneSubscription': uas_zone_subscription_reply_object_dict,
        'genericReply': {
            'RequestStatus': 'OK',
            'RequestExceptionDescription': 'everything ok',
            'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
        }
    }

    uas_zone_subscription_reply = UASZoneSubscriptionReply.from_json(uas_zone_subscription_reply_dict)

    return uas_zone_subscription_reply_dict, uas_zone_subscription_reply


def make_uas_zone_subscriptions_reply():
    uas_zone_subscription_reply_object_dict, _ = make_uas_zone_subscription_reply_object()

    uas_zone_subscriptions_reply_dict = {
        'UASZoneSubscriptions': [uas_zone_subscription_reply_object_dict],
        'genericReply': {
            'RequestStatus': 'OK',
            'RequestExceptionDescription': 'everything ok',
            'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
        }
    }

    uas_zone_subscriptions_reply = UASZoneSubscriptionsReply.from_json(uas_zone_subscriptions_reply_dict)

    return uas_zone_subscriptions_reply_dict, uas_zone_subscriptions_reply
