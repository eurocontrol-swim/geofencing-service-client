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

from datetime import datetime, timezone

import pytest

from geofencing_service_client.models import Point, AirspaceVolume, DailySchedule, CodeWeekDay, ApplicableTimePeriod, \
    CodeYesNoType, AuthorityEntity, NotificationRequirement, AuthorizationRequirement, Authority, DataSource, UASZone, \
    CodeRestrictionType, CodeUSpaceClassType, CodeZoneType, UASZonesFilter, GenericReply, RequestStatus, \
    UASZoneFilterReply, UASZoneCreateReply, SubscribeToUASZonesUpdatesReply, UASZoneSubscriptionReplyObject, \
    UASZoneSubscriptionReply, UASZoneSubscriptionsReply


@pytest.mark.parametrize('point_json, expected_object', [
    (
        {"LON": "54.234234", "LAT": "4.123423"}, Point(54.234234, 4.123423)
    )
])
def test_point__from_json(point_json, expected_object):
    return expected_object == Point.from_json(point_json)


@pytest.mark.parametrize('point, expected_json', [
    (
        Point(54.234234, 4.123423), {"LON": "54.234234", "LAT": "4.123423"}
    )

])
def test_to_json(point, expected_json):
    assert expected_json == point.to_json()


@pytest.mark.parametrize('airspace_volume_json, expected_object', [
    (
        {
            "lowerLimit": 0,
            "lowerVerticalReference": "AGL",
            "polygon": [
                {
                    "LON": "50.862525",
                    "LAT": "4.328120"
                },
                {
                    "LON": "50.865502",
                    "LAT": "4.329257"
                },
                {
                    "LON": "50.865468",
                    "LAT": "4.323686"
                },
                {
                    "LON": "50.862525",
                    "LAT": "4.328120"
                }
            ],
            "upperLimit": 0,
            "upperVerticalReference": "AGL"
        },
        AirspaceVolume(
            lower_limit_in_m=0,
            lower_vertical_reference="AGL",
            upper_limit_in_m=0,
            upper_vertical_reference="AGL",
            polygon=[
                Point(lon=50.862525, lat=4.328120),
                Point(lon=50.865502, lat=4.329257),
                Point(lon=50.865468, lat=4.323686),
                Point(lon=50.862525, lat=4.328120)
            ]
        )
    )
])
def test_airspace_volume__from_json(airspace_volume_json, expected_object):
    assert expected_object == AirspaceVolume.from_json(airspace_volume_json)


@pytest.mark.parametrize('airspace_volume, expected_json', [
    (
        AirspaceVolume(
            lower_limit_in_m=0,
            lower_vertical_reference="AGL",
            upper_limit_in_m=0,
            upper_vertical_reference="AGL",
            polygon=[
                Point(lon=50.862525, lat=4.328120),
                Point(lon=50.865502, lat=4.329257),
                Point(lon=50.865468, lat=4.323686),
                Point(lon=50.862525, lat=4.328120)
            ]
        ),
        {
            "lowerLimit": 0,
            "lowerVerticalReference": "AGL",
            "polygon": [
                {
                    "LON": "50.862525",
                    "LAT": "4.32812"
                },
                {
                    "LON": "50.865502",
                    "LAT": "4.329257"
                },
                {
                    "LON": "50.865468",
                    "LAT": "4.323686"
                },
                {
                    "LON": "50.862525",
                    "LAT": "4.32812"
                }
            ],
            "upperLimit": 0,
            "upperVerticalReference": "AGL"
        }
    )

])
def test_airspace_volume__to_json(airspace_volume, expected_json):
    assert expected_json == airspace_volume.to_json()


@pytest.mark.parametrize('daily_schedule_json, expected_object', [
    (
        {
            'day': 'MON',
            'endTime': '18:00:00+00:00',
            'startTime': '12:00:00+00:00'
        },
        DailySchedule(
            day=CodeWeekDay.MON,
            start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
            end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
        )
    )
])
def test_daily_schedule__from_json(daily_schedule_json, expected_object):
    assert expected_object == DailySchedule.from_json(daily_schedule_json)


@pytest.mark.parametrize('daily_schedule, expected_json', [
    (
            DailySchedule(
                day=CodeWeekDay.MON,
                start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
            ),
            {
                'day': 'MON',
                'endTime': '18:00:00+00:00',
                'startTime': '12:00:00+00:00'
            }
    )
])
def test_daily_schedule__to_json(daily_schedule, expected_json):
    assert expected_json == daily_schedule.to_json()


@pytest.mark.parametrize('applicable_time_period_json, expected_object', [
    (
        {
            'dailySchedule': [{
                'day': 'MON',
                 'endTime': '18:00:00+00:00',
                 'startTime': '12:00:00+00:00'
            },{
                'day': 'SAT',
                 'endTime': '15:00:00+00:00',
                 'startTime': '09:00:00+00:00'
            }],
            'endDateTime': '2021-01-01T00:00:00+00:00',
            'permanent': 'YES',
            'startDateTime': '2020-01-01T00:00:00+00:00',
        },
        ApplicableTimePeriod(
            permanent=CodeYesNoType.YES,
            start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            end_date_time=datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            daily_schedule=[
                DailySchedule(
                    day=CodeWeekDay.MON,
                    start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                    end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
                ),
                DailySchedule(
                    day=CodeWeekDay.SAT,
                    start_time=datetime(2000, 1, 1, 9, 0, 0, tzinfo=timezone.utc),
                    end_time=datetime(2000, 1, 1, 15, 0, 0, tzinfo=timezone.utc)
                )
            ]
        )
    )
])
def test_applicable_time_period__from_json(applicable_time_period_json, expected_object):
    assert expected_object == ApplicableTimePeriod.from_json(applicable_time_period_json)


@pytest.mark.parametrize('applicable_time_period, expected_json', [
    (
        ApplicableTimePeriod(
            permanent=CodeYesNoType.YES,
            start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            end_date_time=datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            daily_schedule=[
                DailySchedule(
                    day=CodeWeekDay.MON,
                    start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                    end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
                ),
                DailySchedule(
                    day=CodeWeekDay.SAT,
                    start_time=datetime(2000, 1, 1, 9, 0, 0, tzinfo=timezone.utc),
                    end_time=datetime(2000, 1, 1, 15, 0, 0, tzinfo=timezone.utc)
                )
            ]
        ),
        {
            'dailySchedule': [{
                'day': 'MON',
                 'endTime': '18:00:00+00:00',
                 'startTime': '12:00:00+00:00'
            },{
                'day': 'SAT',
                 'endTime': '15:00:00+00:00',
                 'startTime': '09:00:00+00:00'
            }],
            'endDateTime': '2021-01-01T00:00:00+00:00',
            'permanent': 'YES',
            'startDateTime': '2020-01-01T00:00:00+00:00',
        }
    )
])
def test_applicable_time_period__to_json(applicable_time_period, expected_json):
    assert expected_json == applicable_time_period.to_json()


@pytest.mark.parametrize('authority_entity_json, expected_object', [
    (
        {
            'contactName': 'AuthorityEntity manager',
            'email': 'auth@autority.be',
            'name': '175d280099fb48eea5da490ac12f816a',
            'phone': '234234234',
            'service': 'AuthorityEntity service',
            'siteURL': 'http://www.autority.be'
        },
        AuthorityEntity(
            contact_name='AuthorityEntity manager',
            email='auth@autority.be',
            name='175d280099fb48eea5da490ac12f816a',
            phone='234234234',
            service='AuthorityEntity service',
            site_url='http://www.autority.be'
        )
    )
])
def test_authority_entity__from_json(authority_entity_json, expected_object):
    assert expected_object == AuthorityEntity.from_json(authority_entity_json)


@pytest.mark.parametrize('authority_entity, expected_json', [
    (
        AuthorityEntity(
            contact_name='AuthorityEntity manager',
            email='auth@autority.be',
            name='175d280099fb48eea5da490ac12f816a',
            phone='234234234',
            service='AuthorityEntity service',
            site_url='http://www.autority.be'
        ),
        {
            'contactName': 'AuthorityEntity manager',
            'email': 'auth@autority.be',
            'name': '175d280099fb48eea5da490ac12f816a',
            'phone': '234234234',
            'service': 'AuthorityEntity service',
            'siteURL': 'http://www.autority.be'
        }
    )
])
def test_authority_entity__to_json(authority_entity, expected_json):
    assert expected_json == authority_entity.to_json()


@pytest.mark.parametrize('notification_requirement_json, expected_object', [
    (
        {
            'authority': {
                'contactName': 'AuthorityEntity manager',
                'email': 'auth@autority.be',
                'name': '175d280099fb48eea5da490ac12f816a',
                'phone': '234234234',
                'service': 'AuthorityEntity service',
                'siteURL': 'http://www.autority.be'
            },
            'intervalBefore': 'P1D'
        },
        NotificationRequirement(
            authority=AuthorityEntity(
                contact_name='AuthorityEntity manager',
                email='auth@autority.be',
                name='175d280099fb48eea5da490ac12f816a',
                phone='234234234',
                service='AuthorityEntity service',
                site_url='http://www.autority.be'
            ),
            interval_before="P1D"
        )
    )
])
def test_notification_requirement__from_json(notification_requirement_json, expected_object):
    assert expected_object == NotificationRequirement.from_json(notification_requirement_json)


@pytest.mark.parametrize('notification_requirement, expected_json', [
    (
        NotificationRequirement(
            authority=AuthorityEntity(
                contact_name='AuthorityEntity manager',
                email='auth@autority.be',
                name='175d280099fb48eea5da490ac12f816a',
                phone='234234234',
                service='AuthorityEntity service',
                site_url='http://www.autority.be'
            ),
            interval_before="P1D"
        ),
        {
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
    )
])
def test_notification_requirement__to_json(notification_requirement, expected_json):
    assert expected_json == notification_requirement.to_json()


@pytest.mark.parametrize('authorization_requirement_json, expected_object', [
    (
        {
            'authority': {
                'contactName': 'AuthorityEntity manager',
                'email': 'auth@autority.be',
                'name': '175d280099fb48eea5da490ac12f816a',
                'phone': '234234234',
                'service': 'AuthorityEntity service',
                'siteURL': 'http://www.autority.be'
            }
        },
        AuthorizationRequirement(
            authority=AuthorityEntity(
                contact_name='AuthorityEntity manager',
                email='auth@autority.be',
                name='175d280099fb48eea5da490ac12f816a',
                phone='234234234',
                service='AuthorityEntity service',
                site_url='http://www.autority.be'
            )
        )
    )
])
def test_authorization_requirement__from_json(authorization_requirement_json, expected_object):
    assert expected_object == AuthorizationRequirement.from_json(authorization_requirement_json)


@pytest.mark.parametrize('authorization_requirement, expected_json', [
    (
        AuthorizationRequirement(
            authority=AuthorityEntity(
                contact_name='AuthorityEntity manager',
                email='auth@autority.be',
                name='175d280099fb48eea5da490ac12f816a',
                phone='234234234',
                service='AuthorityEntity service',
                site_url='http://www.autority.be'
            )
        ),
        {
            'authority': {
                'contactName': 'AuthorityEntity manager',
                'email': 'auth@autority.be',
                'name': '175d280099fb48eea5da490ac12f816a',
                'phone': '234234234',
                'service': 'AuthorityEntity service',
                'siteURL': 'http://www.autority.be'
            }
        }
    )
])
def test_authorization_requirement__to_json(authorization_requirement, expected_json):
    assert expected_json == authorization_requirement.to_json()


@pytest.mark.parametrize('authority_json, expected_object', [
    (
        {
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
        Authority(
            requires_authorization_from=AuthorizationRequirement(
                authority=AuthorityEntity(
                    contact_name='AuthorityEntity manager',
                    email='auth@autority.be',
                    name='175d280099fb48eea5da490ac12f816a',
                    phone='234234234',
                    service='AuthorityEntity service',
                    site_url='http://www.autority.be'
                )
            ),
            requires_notification_to=NotificationRequirement(
                authority=AuthorityEntity(
                    contact_name='AuthorityEntity manager',
                    email='auth@autority.be',
                    name='175d280099fb48eea5da490ac12f816a',
                    phone='234234234',
                    service='AuthorityEntity service',
                    site_url='http://www.autority.be'
                ),
                interval_before="P1D"
            )
        )
    )
])
def test_authority__from_json(authority_json, expected_object):
    assert expected_object == Authority.from_json(authority_json)


@pytest.mark.parametrize('authority, expected_json', [
    (
        Authority(
            requires_authorization_from=AuthorizationRequirement(
                authority=AuthorityEntity(
                    contact_name='AuthorityEntity manager',
                    email='auth@autority.be',
                    name='175d280099fb48eea5da490ac12f816a',
                    phone='234234234',
                    service='AuthorityEntity service',
                    site_url='http://www.autority.be'
                )
            ),
            requires_notification_to=NotificationRequirement(
                authority=AuthorityEntity(
                    contact_name='AuthorityEntity manager',
                    email='auth@autority.be',
                    name='175d280099fb48eea5da490ac12f816a',
                    phone='234234234',
                    service='AuthorityEntity service',
                    site_url='http://www.autority.be'
                ),
                interval_before="P1D"
            )
        ),
        {
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
        }
    )
])
def test_authority__to_json(authority, expected_json):
    assert expected_json == authority.to_json()


@pytest.mark.parametrize('data_source_json, expected_object', [
    (
        {
            'author': 'Author',
            'creationDateTime': '2019-01-01T00:00:00+00:00',
            'updateDateTime': '2019-01-02T00:00:00+00:00'
        },
        DataSource(
            author='Author',
            creation_date_time=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            update_date_time=datetime(2019, 1, 2, 0, 0, 0, tzinfo=timezone.utc),
        )
    )
])
def test_data_source__from_json(data_source_json, expected_object):
    assert expected_object == DataSource.from_json(data_source_json)


@pytest.mark.parametrize('data_source, expected_json', [
    (
        DataSource(
            author='Author',
            creation_date_time=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            update_date_time=datetime(2019, 1, 2, 0, 0, 0, tzinfo=timezone.utc),
        ),
        {
            'author': 'Author',
            'creationDateTime': '2019-01-01T00:00:00+00:00',
            'updateDateTime': '2019-01-02T00:00:00+00:00'
        }
    )
])
def test_data_source__to_json(data_source, expected_json):
    assert expected_json == data_source.to_json()


@pytest.mark.parametrize('uas_zone_json, expected_object', [
    (
        {
            'airspaceVolume': {
                "lowerLimit": 0,
                "lowerVerticalReference": "AGL",
                "polygon": [
                    {
                        "LON": "50.862525",
                        "LAT": "4.32812"
                    },
                    {
                        "LON": "50.865502",
                        "LAT": "4.329257"
                    },
                    {
                        "LON": "50.865468",
                        "LAT": "4.323686"
                    },
                    {
                        "LON": "50.862525",
                        "LAT": "4.32812"
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
                },{
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
        UASZone(
            identifier="zsdffgs",
            message='message',
            name="",
            reason=[],
            region=1,
            restriction=CodeRestrictionType.NO_RESTRICTION,
            restriction_conditions=[],
            type=CodeZoneType.COMMON,
            u_space_class=CodeUSpaceClassType.EUROCONTROL,
            country="BEL",
            data_capture_prohibition=CodeYesNoType.YES,
            data_source=DataSource(
                author='Author',
                creation_date_time=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                update_date_time=datetime(2019, 1, 2, 0, 0, 0, tzinfo=timezone.utc),
            ),
            airspace_volume=AirspaceVolume(
                lower_limit_in_m=0,
                lower_vertical_reference="AGL",
                upper_limit_in_m=0,
                upper_vertical_reference="AGL",
                polygon=[
                    Point(lon=50.862525, lat=4.328120),
                    Point(lon=50.865502, lat=4.329257),
                    Point(lon=50.865468, lat=4.323686),
                    Point(lon=50.862525, lat=4.328120)
                ]
            ),
            applicable_time_period=ApplicableTimePeriod(
                permanent=CodeYesNoType.YES,
                start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                end_date_time=datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                daily_schedule=[
                    DailySchedule(
                        day=CodeWeekDay.MON,
                        start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                        end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
                    ),
                    DailySchedule(
                        day=CodeWeekDay.SAT,
                        start_time=datetime(2000, 1, 1, 9, 0, 0, tzinfo=timezone.utc),
                        end_time=datetime(2000, 1, 1, 15, 0, 0, tzinfo=timezone.utc)
                    )
                ]
            ),
            authority=Authority(
                requires_authorization_from=AuthorizationRequirement(
                    authority=AuthorityEntity(
                        contact_name='AuthorityEntity manager',
                        email='auth@autority.be',
                        name='175d280099fb48eea5da490ac12f816a',
                        phone='234234234',
                        service='AuthorityEntity service',
                        site_url='http://www.autority.be'
                    )
                ),
                requires_notification_to=NotificationRequirement(
                    authority=AuthorityEntity(
                        contact_name='AuthorityEntity manager',
                        email='auth@autority.be',
                        name='175d280099fb48eea5da490ac12f816a',
                        phone='234234234',
                        service='AuthorityEntity service',
                        site_url='http://www.autority.be'
                    ),
                    interval_before="P1D"
                )
            ),
            extended_properties={}
        )
    )
])
def test_uas_zone__from_json(uas_zone_json, expected_object):
    assert expected_object == UASZone.from_json(uas_zone_json)


@pytest.mark.parametrize('uas_zone, expected_json', [
    (
        UASZone(
            identifier="zsdffgs",
            message='message',
            name="",
            reason=[],
            region=1,
            restriction=CodeRestrictionType.NO_RESTRICTION,
            restriction_conditions=[],
            type=CodeZoneType.COMMON,
            u_space_class=CodeUSpaceClassType.EUROCONTROL,
            country="BEL",
            data_capture_prohibition=CodeYesNoType.YES,
            data_source=DataSource(
                author='Author',
                creation_date_time=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                update_date_time=datetime(2019, 1, 2, 0, 0, 0, tzinfo=timezone.utc),
            ),
            airspace_volume=AirspaceVolume(
                lower_limit_in_m=0,
                lower_vertical_reference="AGL",
                upper_limit_in_m=0,
                upper_vertical_reference="AGL",
                polygon=[
                    Point(lon=50.862525, lat=4.328120),
                    Point(lon=50.865502, lat=4.329257),
                    Point(lon=50.865468, lat=4.323686),
                    Point(lon=50.862525, lat=4.328120)
                ]
            ),
            applicable_time_period=ApplicableTimePeriod(
                permanent=CodeYesNoType.YES,
                start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                end_date_time=datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                daily_schedule=[
                    DailySchedule(
                        day=CodeWeekDay.MON,
                        start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                        end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
                    ),
                    DailySchedule(
                        day=CodeWeekDay.SAT,
                        start_time=datetime(2000, 1, 1, 9, 0, 0, tzinfo=timezone.utc),
                        end_time=datetime(2000, 1, 1, 15, 0, 0, tzinfo=timezone.utc)
                    )
                ]
            ),
            authority=Authority(
                requires_authorization_from=AuthorizationRequirement(
                    authority=AuthorityEntity(
                        contact_name='AuthorityEntity manager',
                        email='auth@autority.be',
                        name='175d280099fb48eea5da490ac12f816a',
                        phone='234234234',
                        service='AuthorityEntity service',
                        site_url='http://www.autority.be'
                    )
                ),
                requires_notification_to=NotificationRequirement(
                    authority=AuthorityEntity(
                        contact_name='AuthorityEntity manager',
                        email='auth@autority.be',
                        name='175d280099fb48eea5da490ac12f816a',
                        phone='234234234',
                        service='AuthorityEntity service',
                        site_url='http://www.autority.be'
                    ),
                    interval_before="P1D"
                )
            ),
            extended_properties={}
        ),
        {
            'airspaceVolume': {
                "lowerLimit": 0,
                "lowerVerticalReference": "AGL",
                "polygon": [
                    {
                        "LON": "50.862525",
                        "LAT": "4.32812"
                    },
                    {
                        "LON": "50.865502",
                        "LAT": "4.329257"
                    },
                    {
                        "LON": "50.865468",
                        "LAT": "4.323686"
                    },
                    {
                        "LON": "50.862525",
                        "LAT": "4.32812"
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
    )
])
def test_uas_zone__to_json(uas_zone, expected_json):
    assert expected_json == uas_zone.to_json()


@pytest.mark.parametrize('uas_zones_filter_json, expected_object', [
    (
        {
            'airspaceVolume': {
                "lowerLimit": 0,
                "lowerVerticalReference": "AGL",
                "polygon": [
                    {
                        "LON": "50.862525",
                        "LAT": "4.328120"
                    },
                    {
                        "LON": "50.865502",
                        "LAT": "4.329257"
                    },
                    {
                        "LON": "50.865468",
                        "LAT": "4.323686"
                    },
                    {
                        "LON": "50.862525",
                        "LAT": "4.328120"
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
        },
        UASZonesFilter(
            airspace_volume=AirspaceVolume(
                lower_limit_in_m=0,
                lower_vertical_reference="AGL",
                upper_limit_in_m=0,
                upper_vertical_reference="AGL",
                polygon=[
                    Point(lon=50.862525, lat=4.328120),
                    Point(lon=50.865502, lat=4.329257),
                    Point(lon=50.865468, lat=4.323686),
                    Point(lon=50.862525, lat=4.328120)
                ]
            ),
            regions=[1],
            request_id='request',
            start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
            updated_after_date_time=datetime(2020, 1, 15, 0, 0, 0, tzinfo=timezone.utc)
        )
    )
])
def test_uas_zones_filter__from_json(uas_zones_filter_json, expected_object):
    assert expected_object == UASZonesFilter.from_json(uas_zones_filter_json)


@pytest.mark.parametrize('uas_zones_filter, expected_json', [
    (
        UASZonesFilter(
            airspace_volume=AirspaceVolume(
                lower_limit_in_m=0,
                lower_vertical_reference="AGL",
                upper_limit_in_m=0,
                upper_vertical_reference="AGL",
                polygon=[
                    Point(lon=50.862525, lat=4.328120),
                    Point(lon=50.865502, lat=4.329257),
                    Point(lon=50.865468, lat=4.323686),
                    Point(lon=50.862525, lat=4.328120)
                ]
            ),
            regions=[1],
            request_id='request',
            start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
            updated_after_date_time=datetime(2020, 1, 15, 0, 0, 0, tzinfo=timezone.utc)
        ),
        {
            'airspaceVolume': {
                "lowerLimit": 0,
                "lowerVerticalReference": "AGL",
                "polygon": [
                    {
                        "LON": "50.862525",
                        "LAT": "4.32812"
                    },
                    {
                        "LON": "50.865502",
                        "LAT": "4.329257"
                    },
                    {
                        "LON": "50.865468",
                        "LAT": "4.323686"
                    },
                    {
                        "LON": "50.862525",
                        "LAT": "4.32812"
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
    ),(
        UASZonesFilter(
            airspace_volume=AirspaceVolume(
                lower_limit_in_m=0,
                lower_vertical_reference="AGL",
                upper_limit_in_m=0,
                upper_vertical_reference="AGL",
                polygon=[
                    Point(lon=50.862525, lat=4.328120),
                    Point(lon=50.865502, lat=4.329257),
                    Point(lon=50.865468, lat=4.323686),
                    Point(lon=50.862525, lat=4.328120)
                ]
            ),
            regions=[1],
            request_id='request',
            start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
        ),
        {
            'airspaceVolume': {
                "lowerLimit": 0,
                "lowerVerticalReference": "AGL",
                "polygon": [
                    {
                        "LON": "50.862525",
                        "LAT": "4.32812"
                    },
                    {
                        "LON": "50.865502",
                        "LAT": "4.329257"
                    },
                    {
                        "LON": "50.865468",
                        "LAT": "4.323686"
                    },
                    {
                        "LON": "50.862525",
                        "LAT": "4.32812"
                    }
                ],
                "upperLimit": 0,
                "upperVerticalReference": "AGL"
            },
            'regions': [1],
            'requestID': 'request',
            'startDateTime': '2020-01-01T00:00:00+00:00',
            'endDateTime': '2020-02-01T00:00:00+00:00'
        }
    )
])
def test_uas_zones_filter__to_json__(uas_zones_filter, expected_json):
    assert expected_json == uas_zones_filter.to_json()


@pytest.mark.parametrize('generic_reply_json, expected_object', [
    (
        {
            'RequestStatus': 'OK',
            'RequestExceptionDescription': 'everything ok',
            'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
        },
        GenericReply(
            request_status=RequestStatus.OK,
            request_exception_description='everything ok',
            request_processed_timestamp=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        )
    )
])
def test_generic_reply__from_json(generic_reply_json, expected_object):
    assert expected_object == GenericReply.from_json(generic_reply_json)


@pytest.mark.parametrize('uas_zones_filter_reply_json, expected_object', [
    (
        {
            'UASZoneList': [
                {
                    'airspaceVolume': {
                        "lowerLimit": 0,
                        "lowerVerticalReference": "AGL",
                        "polygon": [
                            {
                                "LON": "50.862525",
                                "LAT": "4.32812"
                            },
                            {
                                "LON": "50.865502",
                                "LAT": "4.329257"
                            },
                            {
                                "LON": "50.865468",
                                "LAT": "4.323686"
                            },
                            {
                                "LON": "50.862525",
                                "LAT": "4.32812"
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
        },
        UASZoneFilterReply(
            uas_zone_list=[
                UASZone(
                    identifier="zsdffgs",
                    message='message',
                    name="",
                    reason=[],
                    region=1,
                    restriction=CodeRestrictionType.NO_RESTRICTION,
                    restriction_conditions=[],
                    type=CodeZoneType.COMMON,
                    u_space_class=CodeUSpaceClassType.EUROCONTROL,
                    country="BEL",
                    data_capture_prohibition=CodeYesNoType.YES,
                    data_source=DataSource(
                        author='Author',
                        creation_date_time=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                        update_date_time=datetime(2019, 1, 2, 0, 0, 0, tzinfo=timezone.utc),
                    ),
                    airspace_volume=AirspaceVolume(
                        lower_limit_in_m=0,
                        lower_vertical_reference="AGL",
                        upper_limit_in_m=0,
                        upper_vertical_reference="AGL",
                        polygon=[
                            Point(lon=50.862525, lat=4.328120),
                            Point(lon=50.865502, lat=4.329257),
                            Point(lon=50.865468, lat=4.323686),
                            Point(lon=50.862525, lat=4.328120)
                        ]
                    ),
                    applicable_time_period=ApplicableTimePeriod(
                        permanent=CodeYesNoType.YES,
                        start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                        end_date_time=datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                        daily_schedule=[
                            DailySchedule(
                                day=CodeWeekDay.MON,
                                start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                                end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
                            ),
                            DailySchedule(
                                day=CodeWeekDay.SAT,
                                start_time=datetime(2000, 1, 1, 9, 0, 0, tzinfo=timezone.utc),
                                end_time=datetime(2000, 1, 1, 15, 0, 0, tzinfo=timezone.utc)
                            )
                        ]
                    ),
                    authority=Authority(
                        requires_authorization_from=AuthorizationRequirement(
                            authority=AuthorityEntity(
                                contact_name='AuthorityEntity manager',
                                email='auth@autority.be',
                                name='175d280099fb48eea5da490ac12f816a',
                                phone='234234234',
                                service='AuthorityEntity service',
                                site_url='http://www.autority.be'
                            )
                        ),
                        requires_notification_to=NotificationRequirement(
                            authority=AuthorityEntity(
                                contact_name='AuthorityEntity manager',
                                email='auth@autority.be',
                                name='175d280099fb48eea5da490ac12f816a',
                                phone='234234234',
                                service='AuthorityEntity service',
                                site_url='http://www.autority.be'
                            ),
                            interval_before="P1D"
                        )
                    ),
                    extended_properties={}
                )
            ],
            generic_reply=GenericReply(
                request_status=RequestStatus.OK,
                request_exception_description='everything ok',
                request_processed_timestamp=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
            )
        )
    )
])
def test_uas_zones_filter_reply__from_json(uas_zones_filter_reply_json, expected_object):
    assert expected_object == UASZoneFilterReply.from_json(uas_zones_filter_reply_json)


@pytest.mark.parametrize('create_uas_zone_reply_json, expected_object', [
    (
        {
            'UASZone': {
                'airspaceVolume': {
                    "lowerLimit": 0,
                    "lowerVerticalReference": "AGL",
                    "polygon": [
                        {
                            "LON": "50.862525",
                            "LAT": "4.32812"
                        },
                        {
                            "LON": "50.865502",
                            "LAT": "4.329257"
                        },
                        {
                            "LON": "50.865468",
                            "LAT": "4.323686"
                        },
                        {
                            "LON": "50.862525",
                            "LAT": "4.32812"
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
        },
        UASZoneCreateReply(
            uas_zone=UASZone(
                identifier="zsdffgs",
                message='message',
                name="",
                reason=[],
                region=1,
                restriction=CodeRestrictionType.NO_RESTRICTION,
                restriction_conditions=[],
                type=CodeZoneType.COMMON,
                u_space_class=CodeUSpaceClassType.EUROCONTROL,
                country="BEL",
                data_capture_prohibition=CodeYesNoType.YES,
                data_source=DataSource(
                    author='Author',
                    creation_date_time=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    update_date_time=datetime(2019, 1, 2, 0, 0, 0, tzinfo=timezone.utc),
                ),
                airspace_volume=AirspaceVolume(
                    lower_limit_in_m=0,
                    lower_vertical_reference="AGL",
                    upper_limit_in_m=0,
                    upper_vertical_reference="AGL",
                    polygon=[
                        Point(lon=50.862525, lat=4.328120),
                        Point(lon=50.865502, lat=4.329257),
                        Point(lon=50.865468, lat=4.323686),
                        Point(lon=50.862525, lat=4.328120)
                    ]
                ),
                applicable_time_period=ApplicableTimePeriod(
                    permanent=CodeYesNoType.YES,
                    start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    end_date_time=datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    daily_schedule=[
                        DailySchedule(
                            day=CodeWeekDay.MON,
                            start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                            end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
                        ),
                        DailySchedule(
                            day=CodeWeekDay.SAT,
                            start_time=datetime(2000, 1, 1, 9, 0, 0, tzinfo=timezone.utc),
                            end_time=datetime(2000, 1, 1, 15, 0, 0, tzinfo=timezone.utc)
                        )
                    ]
                ),
                authority=Authority(
                    requires_authorization_from=AuthorizationRequirement(
                        authority=AuthorityEntity(
                            contact_name='AuthorityEntity manager',
                            email='auth@autority.be',
                            name='175d280099fb48eea5da490ac12f816a',
                            phone='234234234',
                            service='AuthorityEntity service',
                            site_url='http://www.autority.be'
                        )
                    ),
                    requires_notification_to=NotificationRequirement(
                        authority=AuthorityEntity(
                            contact_name='AuthorityEntity manager',
                            email='auth@autority.be',
                            name='175d280099fb48eea5da490ac12f816a',
                            phone='234234234',
                            service='AuthorityEntity service',
                            site_url='http://www.autority.be'
                        ),
                        interval_before="P1D"
                    )
                ),
                extended_properties={}
            ),
            generic_reply=GenericReply(
                request_status=RequestStatus.OK,
                request_exception_description='everything ok',
                request_processed_timestamp=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
            )
        )
    )
])
def test_create_uas_zone_reply__from_json(create_uas_zone_reply_json, expected_object):
    assert expected_object == UASZoneCreateReply.from_json(create_uas_zone_reply_json)


@pytest.mark.parametrize('subscribe_to_uas_zones_updates_reply_json, expected_object', [
    (
        {
            'subscriptionID': '123456',
            'publicationLocation': 'location',
            'genericReply': {
                'RequestStatus': 'OK',
                'RequestExceptionDescription': 'everything ok',
                'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
            }
        },
        SubscribeToUASZonesUpdatesReply(
            subscription_id='123456',
            publication_location='location',
            generic_reply=GenericReply(
                request_status=RequestStatus.OK,
                request_exception_description='everything ok',
                request_processed_timestamp=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
            )
        )
    )
])
def test_subscribe_to_uas_zones_updates_reply__from_json(subscribe_to_uas_zones_updates_reply_json, expected_object):
    assert expected_object == SubscribeToUASZonesUpdatesReply.from_json(subscribe_to_uas_zones_updates_reply_json)


@pytest.mark.parametrize('uas_zone_subscription_reply_object_json, expected_object', [
    (
        {
            'subscriptionID': '123456',
            'publicationLocation': 'location',
            'active': True,
            'UASZonesFilter': {
                'airspaceVolume': {
                    "lowerLimit": 0,
                    "lowerVerticalReference": "AGL",
                    "polygon": [
                        {
                            "LON": "50.862525",
                            "LAT": "4.328120"
                        },
                        {
                            "LON": "50.865502",
                            "LAT": "4.329257"
                        },
                        {
                            "LON": "50.865468",
                            "LAT": "4.323686"
                        },
                        {
                            "LON": "50.862525",
                            "LAT": "4.328120"
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
        },
        UASZoneSubscriptionReplyObject(
            subscription_id='123456',
            publication_location='location',
            active=True,
            uas_zones_filter=UASZonesFilter(
                airspace_volume=AirspaceVolume(
                    lower_limit_in_m=0,
                    lower_vertical_reference="AGL",
                    upper_limit_in_m=0,
                    upper_vertical_reference="AGL",
                    polygon=[
                        Point(lon=50.862525, lat=4.328120),
                        Point(lon=50.865502, lat=4.329257),
                        Point(lon=50.865468, lat=4.323686),
                        Point(lon=50.862525, lat=4.328120)
                    ]
                ),
                regions=[1],
                request_id='request',
                start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                updated_after_date_time=datetime(2020, 1, 15, 0, 0, 0, tzinfo=timezone.utc)
            )
        )
    )
])
def test_uas_zone_subscription_reply_object__from_json(uas_zone_subscription_reply_object_json, expected_object):
    assert expected_object == UASZoneSubscriptionReplyObject.from_json(uas_zone_subscription_reply_object_json)


@pytest.mark.parametrize('uas_zone_subscription_reply_object, expected_dict', [
    (
        UASZoneSubscriptionReplyObject(
            subscription_id='123456',
            publication_location='location',
            active=True,
            uas_zones_filter=UASZonesFilter(
                airspace_volume=AirspaceVolume(
                    lower_limit_in_m=0,
                    lower_vertical_reference="AGL",
                    upper_limit_in_m=0,
                    upper_vertical_reference="AGL",
                    polygon=[
                        Point(lon=50.862525, lat=4.328120),
                        Point(lon=50.865502, lat=4.329257),
                        Point(lon=50.865468, lat=4.323686),
                        Point(lon=50.862525, lat=4.328120)
                    ]
                ),
                regions=[1],
                request_id='request',
                start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                updated_after_date_time=datetime(2020, 1, 15, 0, 0, 0, tzinfo=timezone.utc)
            )
        ),
        {
            'subscriptionID': '123456',
            'publicationLocation': 'location',
            'active': True,
            'UASZonesFilter': {
                'airspaceVolume': {
                    "lowerLimit": 0,
                    "lowerVerticalReference": "AGL",
                    "polygon": [
                        {
                            "LON": "50.862525",
                            "LAT": "4.32812"
                        },
                        {
                            "LON": "50.865502",
                            "LAT": "4.329257"
                        },
                        {
                            "LON": "50.865468",
                            "LAT": "4.323686"
                        },
                        {
                            "LON": "50.862525",
                            "LAT": "4.32812"
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
        }
    )
])
def test_uas_zone_subscription_reply_object__to_json(uas_zone_subscription_reply_object, expected_dict):
    assert expected_dict == uas_zone_subscription_reply_object.to_json()


@pytest.mark.parametrize('uas_zone_subscription_reply_json, expected_object', [
    (
        {
            'UASZoneSubscription': {
                'subscriptionID': '123456',
                'publicationLocation': 'location',
                'active': True,
                'UASZonesFilter': {
                    'airspaceVolume': {
                        "lowerLimit": 0,
                        "lowerVerticalReference": "AGL",
                        "polygon": [
                            {
                                "LON": "50.862525",
                                "LAT": "4.328120"
                            },
                            {
                                "LON": "50.865502",
                                "LAT": "4.329257"
                            },
                            {
                                "LON": "50.865468",
                                "LAT": "4.323686"
                            },
                            {
                                "LON": "50.862525",
                                "LAT": "4.328120"
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
            },
            'genericReply': {
                'RequestStatus': 'OK',
                'RequestExceptionDescription': 'everything ok',
                'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
            }
        },
        UASZoneSubscriptionReply(
            uas_zone_subscription=UASZoneSubscriptionReplyObject(
                subscription_id='123456',
                publication_location='location',
                active=True,
                uas_zones_filter=UASZonesFilter(
                    airspace_volume=AirspaceVolume(
                        lower_limit_in_m=0,
                        lower_vertical_reference="AGL",
                        upper_limit_in_m=0,
                        upper_vertical_reference="AGL",
                        polygon=[
                            Point(lon=50.862525, lat=4.328120),
                            Point(lon=50.865502, lat=4.329257),
                            Point(lon=50.865468, lat=4.323686),
                            Point(lon=50.862525, lat=4.328120)
                        ]
                    ),
                    regions=[1],
                    request_id='request',
                    start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                    updated_after_date_time=datetime(2020, 1, 15, 0, 0, 0, tzinfo=timezone.utc)
                )
            ),
            generic_reply=GenericReply(
                request_status=RequestStatus.OK,
                request_exception_description='everything ok',
                request_processed_timestamp=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
            )
        )
    )
])
def test_uas_zone_subscription_reply__from_json(uas_zone_subscription_reply_json, expected_object):
    assert expected_object == UASZoneSubscriptionReply.from_json(uas_zone_subscription_reply_json)


@pytest.mark.parametrize('uas_zone_subscriptions_reply_json, expected_object', [
    (
        {
            'UASZoneSubscriptions': [{
                'subscriptionID': '123456',
                'publicationLocation': 'location',
                'active': True,
                'UASZonesFilter': {
                    'airspaceVolume': {
                        "lowerLimit": 0,
                        "lowerVerticalReference": "AGL",
                        "polygon": [
                            {
                                "LON": "50.862525",
                                "LAT": "4.328120"
                            },
                            {
                                "LON": "50.865502",
                                "LAT": "4.329257"
                            },
                            {
                                "LON": "50.865468",
                                "LAT": "4.323686"
                            },
                            {
                                "LON": "50.862525",
                                "LAT": "4.328120"
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
            }],
            'genericReply': {
                'RequestStatus': 'OK',
                'RequestExceptionDescription': 'everything ok',
                'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
            }
        },
        UASZoneSubscriptionsReply(
            uas_zone_subscriptions=[UASZoneSubscriptionReplyObject(
                subscription_id='123456',
                publication_location='location',
                active=True,
                uas_zones_filter=UASZonesFilter(
                    airspace_volume=AirspaceVolume(
                        lower_limit_in_m=0,
                        lower_vertical_reference="AGL",
                        upper_limit_in_m=0,
                        upper_vertical_reference="AGL",
                        polygon=[
                            Point(lon=50.862525, lat=4.328120),
                            Point(lon=50.865502, lat=4.329257),
                            Point(lon=50.865468, lat=4.323686),
                            Point(lon=50.862525, lat=4.328120)
                        ]
                    ),
                    regions=[1],
                    request_id='request',
                    start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                    updated_after_date_time=datetime(2020, 1, 15, 0, 0, 0, tzinfo=timezone.utc)
                )
            )],
            generic_reply=GenericReply(
                request_status=RequestStatus.OK,
                request_exception_description='everything ok',
                request_processed_timestamp=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
            )
        )
    )
])
def test_uas_zone_subscriptions_reply__from_json(uas_zone_subscriptions_reply_json, expected_object):
    assert expected_object == UASZoneSubscriptionsReply.from_json(uas_zone_subscriptions_reply_json)
