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

from geofencing_service_client.models import AirspaceVolume, DailyPeriod, CodeWeekDay, TimePeriod, \
    CodeYesNoType, Authority, UASZone, CodeRestrictionType, CodeUSpaceClassType, CodeZoneType, \
    UASZonesFilter, GenericReply, RequestStatus, UASZoneFilterReply, UASZoneCreateReply, \
    SubscribeToUASZonesUpdatesReply, UASZoneSubscriptionReplyObject, UASZoneSubscriptionReply, \
    UASZoneSubscriptionsReply, Polygon, CodeAuthorityRole, Circle


@pytest.mark.parametrize('polygon_json, expected_object', [
    (
        {
            "type": "Polygon",
            "coordinates": [[
                [2.485866, 49.029301],
                [2.604141, 49.034704],
                [2.631263, 48.987301],
                [2.510414, 48.983358],
                [2.485866, 49.029301]
            ]]
        },
        Polygon(coordinates=[[
                [2.485866, 49.029301],
                [2.604141, 49.034704],
                [2.631263, 48.987301],
                [2.510414, 48.983358],
                [2.485866, 49.029301]
            ]]
        )
    )
])
def test_polygon__from_json(polygon_json, expected_object):
    assert expected_object == Polygon.from_json(polygon_json)


@pytest.mark.parametrize('polygon, expected_json', [
    (
        Polygon(coordinates=[[
                [2.485866, 49.029301],
                [2.604141, 49.034704],
                [2.631263, 48.987301],
                [2.510414, 48.983358],
                [2.485866, 49.029301]
            ]]
        ),
        {
            "type": "Polygon",
            "coordinates": [[
                [2.485866, 49.029301],
                [2.604141, 49.034704],
                [2.631263, 48.987301],
                [2.510414, 48.983358],
                [2.485866, 49.029301]
            ]]
        }
    )
])
def test_polygon__to_json(polygon, expected_json):
    assert expected_json == polygon.to_json()


@pytest.mark.parametrize('circle_json, expected_object', [
    (
        {
            "type": "Circle",
            "center": [2.485866, 49.029301],
            "radius": 7000
        },
        Circle(
            center=[2.485866, 49.029301],
            radius=7000
        )
    )
])
def test_circle__from_json(circle_json, expected_object):
    assert expected_object == Circle.from_json(circle_json)


@pytest.mark.parametrize('circle, expected_json', [
    (
        Circle(
            center=[2.485866, 49.029301],
            radius=7000
        ),
        {
            "type": "Circle",
            "center": [2.485866, 49.029301],
            "radius": 7000
        }
    )
])
def test_circle__to_json(circle, expected_json):
    assert expected_json == circle.to_json()


@pytest.mark.parametrize('airspace_volume_json, expected_object', [
    (
        {
            "lowerLimit": 0,
            "lowerVerticalReference": "AGL",
            "horizontalProjection": {
                "type": "Polygon",
                "coordinates": [[
                    [2.485866, 49.029301],
                    [2.604141, 49.034704],
                    [2.631263, 48.987301],
                    [2.510414, 48.983358],
                    [2.485866, 49.029301]
                ]]
            },
            "uomDimensions": "M",
            "upperLimit": 0,
            "upperVerticalReference": "AGL"
        },
        AirspaceVolume(
            uom_dimensions="M",
            lower_limit=0,
            lower_vertical_reference="AGL",
            upper_limit=0,
            upper_vertical_reference="AGL",
            horizontal_projection=Polygon(coordinates=[[
                    [2.485866, 49.029301],
                    [2.604141, 49.034704],
                    [2.631263, 48.987301],
                    [2.510414, 48.983358],
                    [2.485866, 49.029301]
                ]]
            )
        )
    ),
    (
        {
            "lowerLimit": 0,
            "lowerVerticalReference": "AGL",
            "horizontalProjection": {
                "type": "Circle",
                "center": [2.485866, 49.029301],
                "radius": 7000
            },
            "uomDimensions": "M",
            "upperLimit": 0,
            "upperVerticalReference": "AGL"
        },
        AirspaceVolume(
            uom_dimensions="M",
            lower_limit=0,
            lower_vertical_reference="AGL",
            upper_limit=0,
            upper_vertical_reference="AGL",
            horizontal_projection=Circle(
               center=[2.485866, 49.029301],
               radius=7000
            )
        )
    )
])
def test_airspace_volume__from_json(airspace_volume_json, expected_object):
    assert expected_object == AirspaceVolume.from_json(airspace_volume_json)


@pytest.mark.parametrize('airspace_volume, expected_json', [
    (
        AirspaceVolume(
            uom_dimensions="M",
            lower_limit=0,
            lower_vertical_reference="AGL",
            upper_limit=0,
            upper_vertical_reference="AGL",
            horizontal_projection=Polygon(coordinates=[[
                [2.485866, 49.029301],
                [2.604141, 49.034704],
                [2.631263, 48.987301],
                [2.510414, 48.983358],
                [2.485866, 49.029301]
            ]]
            )
        ),
        {
            "lowerLimit": 0,
            "lowerVerticalReference": "AGL",
            "horizontalProjection": {
                "type": "Polygon",
                "coordinates": [[
                    [2.485866, 49.029301],
                    [2.604141, 49.034704],
                    [2.631263, 48.987301],
                    [2.510414, 48.983358],
                    [2.485866, 49.029301]
                ]]
            },
            "uomDimensions": "M",
            "upperLimit": 0,
            "upperVerticalReference": "AGL"
        },
    ),
    (
        (
            AirspaceVolume(
                uom_dimensions="M",
                lower_limit=0,
                lower_vertical_reference="AGL",
                upper_limit=0,
                upper_vertical_reference="AGL",
                horizontal_projection=Circle(
                    center=[2.485866, 49.029301],
                    radius=7000
                )
            ),
            {
                "lowerLimit": 0,
                "lowerVerticalReference": "AGL",
                "horizontalProjection": {
                    "type": "Circle",
                    "center": [2.485866, 49.029301],
                    "radius": 7000
                },
                "uomDimensions": "M",
                "upperLimit": 0,
                "upperVerticalReference": "AGL"
            },
        )
    )
])
def test_airspace_volume__to_json(airspace_volume, expected_json):
    assert expected_json == airspace_volume.to_json()


@pytest.mark.parametrize('daily_period_json, expected_object', [
    (
        {
            'day': 'MON',
            'endTime': '18:00:00+00:00',
            'startTime': '12:00:00+00:00'
        },
        DailyPeriod(
            day=CodeWeekDay.MON,
            start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
            end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
        )
    )
])
def test_daily_period__from_json(daily_period_json, expected_object):
    assert expected_object == DailyPeriod.from_json(daily_period_json)


@pytest.mark.parametrize('daily_period, expected_json', [
    (
        DailyPeriod(
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
def test_daily_period__to_json(daily_period, expected_json):
    assert expected_json == daily_period.to_json()


@pytest.mark.parametrize('time_period_json, expected_object', [
    (
        {
            'schedule': [{
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
        TimePeriod(
            permanent=CodeYesNoType.YES,
            start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            end_date_time=datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            schedule=[
                DailyPeriod(
                    day=CodeWeekDay.MON,
                    start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                    end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
                ),
                DailyPeriod(
                    day=CodeWeekDay.SAT,
                    start_time=datetime(2000, 1, 1, 9, 0, 0, tzinfo=timezone.utc),
                    end_time=datetime(2000, 1, 1, 15, 0, 0, tzinfo=timezone.utc)
                )
            ]
        )
    )
])
def test_time_period__from_json(time_period_json, expected_object):
    assert expected_object == TimePeriod.from_json(time_period_json)


@pytest.mark.parametrize('time_period, expected_json', [
    (
            TimePeriod(
            permanent=CodeYesNoType.YES,
            start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            end_date_time=datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            schedule=[
                DailyPeriod(
                    day=CodeWeekDay.MON,
                    start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                    end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
                ),
                DailyPeriod(
                    day=CodeWeekDay.SAT,
                    start_time=datetime(2000, 1, 1, 9, 0, 0, tzinfo=timezone.utc),
                    end_time=datetime(2000, 1, 1, 15, 0, 0, tzinfo=timezone.utc)
                )
            ]
        ),
            {
            'schedule': [{
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
def test_time_period__to_json(time_period, expected_json):
    assert expected_json == time_period.to_json()


@pytest.mark.parametrize('authority_json, expected_object', [
    (
        {
            'name': '175d280099fb48eea5da490ac12f816a',
            'service': 'AuthorityEntity service',
            'purpose': 'AUTHORIZATION',
            'email': 'auth@autority.be',
            'contactName': 'AuthorityEntity manager',
            'siteURL': 'http://www.autority.be',
            'phone': '234234234',
            'intervalBefore': 'PD30'
        },
        Authority(
            name='175d280099fb48eea5da490ac12f816a',
            service='AuthorityEntity service',
            purpose=CodeAuthorityRole.AUTHORIZATION,
            email='auth@autority.be',
            contact_name='AuthorityEntity manager',
            site_url='http://www.autority.be',
            phone='234234234',
            interval_before='PD30'
        )
    )
])
def test_authority__from_json(authority_json, expected_object):
    assert expected_object == Authority.from_json(authority_json)


@pytest.mark.parametrize('authority, expected_json', [
    (
        Authority(
            name='175d280099fb48eea5da490ac12f816a',
            service='AuthorityEntity service',
            purpose=CodeAuthorityRole.AUTHORIZATION,
            email='auth@autority.be',
            contact_name='AuthorityEntity manager',
            site_url='http://www.autority.be',
            phone='234234234',
            interval_before='PD30'
        ),
        {
            'name': '175d280099fb48eea5da490ac12f816a',
            'service': 'AuthorityEntity service',
            'purpose': 'AUTHORIZATION',
            'email': 'auth@autority.be',
            'contactName': 'AuthorityEntity manager',
            'siteURL': 'http://www.autority.be',
            'phone': '234234234',
            'intervalBefore': 'PD30'
        }
    )
])
def test_authority__to_json(authority, expected_json):
    assert expected_json == authority.to_json()

@pytest.mark.parametrize('uas_zone_json, expected_object', [
    (
        {
            'geometry': [
                {
                    "lowerLimit": 0,
                    "lowerVerticalReference": "AGL",
                    "horizontalProjection": {
                        "type": "Polygon",
                        "coordinates": [[
                            [2.485866, 49.029301],
                            [2.604141, 49.034704],
                            [2.631263, 48.987301],
                            [2.510414, 48.983358],
                            [2.485866, 49.029301]
                        ]]
                    },
                    "uomDimensions": "M",
                    "upperLimit": 0,
                    "upperVerticalReference": "AGL"
                },
                {
                    "lowerLimit": 0,
                    "lowerVerticalReference": "AGL",
                    "horizontalProjection": {
                        "type": "Circle",
                        "center": [2.485866, 49.029301],
                        "radius": 7000
                    },
                    "uomDimensions": "M",
                    "upperLimit": 0,
                    "upperVerticalReference": "AGL"
                }
            ],
            'applicability': {
                'schedule': [{
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
            'zoneAuthority': {
                'name': '175d280099fb48eea5da490ac12f816a',
                'service': 'AuthorityEntity service',
                'purpose': 'AUTHORIZATION',
                'email': 'auth@autority.be',
                'contactName': 'AuthorityEntity manager',
                'siteURL': 'http://www.autority.be',
                'phone': '234234234',
                'intervalBefore': 'PD30'
            },
            'country': 'BEL',
            'regulationExemption': 'YES',
            'extendedProperties': {},
            'identifier': "zsdffgs",
            'message': 'message',
            'name': "",
            'reason': [],
            'otherReasonInfo': "",
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
            other_reason_info="",
            region=1,
            restriction=CodeRestrictionType.NO_RESTRICTION,
            restriction_conditions=[],
            type=CodeZoneType.COMMON,
            u_space_class=CodeUSpaceClassType.EUROCONTROL,
            country="BEL",
            regulation_exemption=CodeYesNoType.YES,
            geometry=[
                AirspaceVolume(
                    uom_dimensions="M",
                    lower_limit=0,
                    lower_vertical_reference="AGL",
                    upper_limit=0,
                    upper_vertical_reference="AGL",
                    horizontal_projection=Polygon(coordinates=[[
                            [2.485866, 49.029301],
                            [2.604141, 49.034704],
                            [2.631263, 48.987301],
                            [2.510414, 48.983358],
                            [2.485866, 49.029301]
                        ]]
                    )
                ),
                AirspaceVolume(
                    uom_dimensions="M",
                    lower_limit=0,
                    lower_vertical_reference="AGL",
                    upper_limit=0,
                    upper_vertical_reference="AGL",
                    horizontal_projection=Circle(
                        center=[2.485866, 49.029301],
                        radius=7000
                    )
                )
            ],
            applicability=TimePeriod(
                permanent=CodeYesNoType.YES,
                start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                end_date_time=datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                schedule=[
                    DailyPeriod(
                        day=CodeWeekDay.MON,
                        start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                        end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
                    ),
                    DailyPeriod(
                        day=CodeWeekDay.SAT,
                        start_time=datetime(2000, 1, 1, 9, 0, 0, tzinfo=timezone.utc),
                        end_time=datetime(2000, 1, 1, 15, 0, 0, tzinfo=timezone.utc)
                    )
                ]
            ),
            zone_authority=Authority(
                name='175d280099fb48eea5da490ac12f816a',
                service='AuthorityEntity service',
                purpose=CodeAuthorityRole.AUTHORIZATION,
                email='auth@autority.be',
                contact_name='AuthorityEntity manager',
                site_url='http://www.autority.be',
                phone='234234234',
                interval_before='PD30'
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
            other_reason_info="",
            region=1,
            restriction=CodeRestrictionType.NO_RESTRICTION,
            restriction_conditions=[],
            type=CodeZoneType.COMMON,
            u_space_class=CodeUSpaceClassType.EUROCONTROL,
            country="BEL",
            regulation_exemption=CodeYesNoType.YES,
            geometry=[
                AirspaceVolume(
                    uom_dimensions="M",
                    lower_limit=0,
                    lower_vertical_reference="AGL",
                    upper_limit=0,
                    upper_vertical_reference="AGL",
                    horizontal_projection=Polygon(coordinates=[[
                            [2.485866, 49.029301],
                            [2.604141, 49.034704],
                            [2.631263, 48.987301],
                            [2.510414, 48.983358],
                            [2.485866, 49.029301]
                        ]]
                    )
                ),
                AirspaceVolume(
                    uom_dimensions="M",
                    lower_limit=0,
                    lower_vertical_reference="AGL",
                    upper_limit=0,
                    upper_vertical_reference="AGL",
                    horizontal_projection=Circle(
                        center=[2.485866, 49.029301],
                        radius=7000
                    )
                )
            ],
            applicability=TimePeriod(
                permanent=CodeYesNoType.YES,
                start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                end_date_time=datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                schedule=[
                    DailyPeriod(
                        day=CodeWeekDay.MON,
                        start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                        end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
                    ),
                    DailyPeriod(
                        day=CodeWeekDay.SAT,
                        start_time=datetime(2000, 1, 1, 9, 0, 0, tzinfo=timezone.utc),
                        end_time=datetime(2000, 1, 1, 15, 0, 0, tzinfo=timezone.utc)
                    )
                ]
            ),
            zone_authority=Authority(
                name='175d280099fb48eea5da490ac12f816a',
                service='AuthorityEntity service',
                purpose=CodeAuthorityRole.AUTHORIZATION,
                email='auth@autority.be',
                contact_name='AuthorityEntity manager',
                site_url='http://www.autority.be',
                phone='234234234',
                interval_before='PD30'
            ),
            extended_properties={}
        ),
        {
            'geometry': [
                {
                    "lowerLimit": 0,
                    "lowerVerticalReference": "AGL",
                    "horizontalProjection": {
                        "type": "Polygon",
                        "coordinates": [[
                            [2.485866, 49.029301],
                            [2.604141, 49.034704],
                            [2.631263, 48.987301],
                            [2.510414, 48.983358],
                            [2.485866, 49.029301]
                        ]]
                    },
                    "uomDimensions": "M",
                    "upperLimit": 0,
                    "upperVerticalReference": "AGL"
                },
                {
                    "lowerLimit": 0,
                    "lowerVerticalReference": "AGL",
                    "horizontalProjection": {
                        "type": "Circle",
                        "center": [2.485866, 49.029301],
                        "radius": 7000
                    },
                    "uomDimensions": "M",
                    "upperLimit": 0,
                    "upperVerticalReference": "AGL"
                }
            ],
            'applicability': {
                'schedule': [{
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
            'zoneAuthority': {
                'name': '175d280099fb48eea5da490ac12f816a',
                'service': 'AuthorityEntity service',
                'purpose': 'AUTHORIZATION',
                'email': 'auth@autority.be',
                'contactName': 'AuthorityEntity manager',
                'siteURL': 'http://www.autority.be',
                'phone': '234234234',
                'intervalBefore': 'PD30'
            },
            'country': 'BEL',
            'regulationExemption': 'YES',
            'extendedProperties': {},
            'identifier': "zsdffgs",
            'message': 'message',
            'name': "",
            'reason': [],
            'otherReasonInfo': "",
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
                "horizontalProjection": {
                    "type": "Polygon",
                    "coordinates": [[
                        [2.485866, 49.029301],
                        [2.604141, 49.034704],
                        [2.631263, 48.987301],
                        [2.510414, 48.983358],
                        [2.485866, 49.029301]
                    ]]
                },
                "uomDimensions": "M",
                "upperLimit": 0,
                "upperVerticalReference": "AGL"
            },
            'regions': [1],
            'startDateTime': '2020-01-01T00:00:00+00:00',
            'endDateTime': '2020-02-01T00:00:00+00:00',
        },
        UASZonesFilter(
            airspace_volume=AirspaceVolume(
                uom_dimensions="M",
                lower_limit=0,
                lower_vertical_reference="AGL",
                upper_limit=0,
                upper_vertical_reference="AGL",
                horizontal_projection=Polygon(coordinates=[[
                        [2.485866, 49.029301],
                        [2.604141, 49.034704],
                        [2.631263, 48.987301],
                        [2.510414, 48.983358],
                        [2.485866, 49.029301]
                    ]]
                )
            ),
            regions=[1],
            start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
        )
    ),
    (
        {
            'airspaceVolume': {
                "lowerLimit": 0,
                "lowerVerticalReference": "AGL",
                "horizontalProjection": {
                    "type": "Circle",
                    "center": [2.485866, 49.029301],
                    "radius": 7000
                },
                "uomDimensions": "M",
                "upperLimit": 0,
                "upperVerticalReference": "AGL"
            },
            'regions': [1],
            'startDateTime': '2020-01-01T00:00:00+00:00',
            'endDateTime': '2020-02-01T00:00:00+00:00',
        },
        UASZonesFilter(
            airspace_volume=AirspaceVolume(
                uom_dimensions="M",
                lower_limit=0,
                lower_vertical_reference="AGL",
                upper_limit=0,
                upper_vertical_reference="AGL",
                horizontal_projection=Circle(
                    center=[2.485866, 49.029301],
                    radius=7000
                )
            ),
            regions=[1],
            start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
        )
    )
])
def test_uas_zones_filter__from_json(uas_zones_filter_json, expected_object):
    assert expected_object == UASZonesFilter.from_json(uas_zones_filter_json)


@pytest.mark.parametrize('uas_zones_filter, expected_json', [
    (
        UASZonesFilter(
            airspace_volume=AirspaceVolume(
                uom_dimensions="M",
                lower_limit=0,
                lower_vertical_reference="AGL",
                upper_limit=0,
                upper_vertical_reference="AGL",
                horizontal_projection=Circle(
                    center=[2.485866, 49.029301],
                    radius=7000
                )
            ),
            regions=[1],
            start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
        ),
        {
            'airspaceVolume': {
                "lowerLimit": 0,
                "lowerVerticalReference": "AGL",
                "horizontalProjection": {
                    "type": "Circle",
                    "center": [2.485866, 49.029301],
                    "radius": 7000
                },
                "uomDimensions": "M",
                "upperLimit": 0,
                "upperVerticalReference": "AGL"
            },
            'regions': [1],
            'startDateTime': '2020-01-01T00:00:00+00:00',
            'endDateTime': '2020-02-01T00:00:00+00:00',
        }
    ),
    (
        UASZonesFilter(
            airspace_volume=AirspaceVolume(
                uom_dimensions="M",
                lower_limit=0,
                lower_vertical_reference="AGL",
                upper_limit=0,
                upper_vertical_reference="AGL",
                horizontal_projection=Polygon(coordinates=[[
                        [2.485866, 49.029301],
                        [2.604141, 49.034704],
                        [2.631263, 48.987301],
                        [2.510414, 48.983358],
                        [2.485866, 49.029301]
                    ]]
                )
            ),
            regions=[1],
            start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
        ),
        {
            'airspaceVolume': {
                "lowerLimit": 0,
                "lowerVerticalReference": "AGL",
                "horizontalProjection": {
                    "type": "Polygon",
                    "coordinates": [[
                        [2.485866, 49.029301],
                        [2.604141, 49.034704],
                        [2.631263, 48.987301],
                        [2.510414, 48.983358],
                        [2.485866, 49.029301]
                    ]]
                },
                "uomDimensions": "M",
                "upperLimit": 0,
                "upperVerticalReference": "AGL"
            },
            'regions': [1],
            'startDateTime': '2020-01-01T00:00:00+00:00',
            'endDateTime': '2020-02-01T00:00:00+00:00',
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
                    'geometry': [
                        {
                            "lowerLimit": 0,
                            "lowerVerticalReference": "AGL",
                            "horizontalProjection": {
                                "type": "Polygon",
                                "coordinates": [[
                                    [2.485866, 49.029301],
                                    [2.604141, 49.034704],
                                    [2.631263, 48.987301],
                                    [2.510414, 48.983358],
                                    [2.485866, 49.029301]
                                ]]
                            },
                            "uomDimensions": "M",
                            "upperLimit": 0,
                            "upperVerticalReference": "AGL"
                        },
                        {
                            "lowerLimit": 0,
                            "lowerVerticalReference": "AGL",
                            "horizontalProjection": {
                                "type": "Circle",
                                "center": [2.485866, 49.029301],
                                "radius": 7000
                            },
                            "uomDimensions": "M",
                            "upperLimit": 0,
                            "upperVerticalReference": "AGL"
                        }
                    ],
                    'applicability': {
                        'schedule': [{
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
                    'zoneAuthority': {
                        'name': '175d280099fb48eea5da490ac12f816a',
                        'service': 'AuthorityEntity service',
                        'purpose': 'AUTHORIZATION',
                        'email': 'auth@autority.be',
                        'contactName': 'AuthorityEntity manager',
                        'siteURL': 'http://www.autority.be',
                        'phone': '234234234',
                        'intervalBefore': 'PD30'
                    },
                    'country': 'BEL',
                    'regulationExemption': 'YES',
                    'extendedProperties': {},
                    'identifier': "zsdffgs",
                    'message': 'message',
                    'name': "",
                    'reason': [],
                    'otherReasonInfo': "",
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
                    other_reason_info="",
                    region=1,
                    restriction=CodeRestrictionType.NO_RESTRICTION,
                    restriction_conditions=[],
                    type=CodeZoneType.COMMON,
                    u_space_class=CodeUSpaceClassType.EUROCONTROL,
                    country="BEL",
                    regulation_exemption=CodeYesNoType.YES,
                    geometry=[
                        AirspaceVolume(
                            uom_dimensions="M",
                            lower_limit=0,
                            lower_vertical_reference="AGL",
                            upper_limit=0,
                            upper_vertical_reference="AGL",
                            horizontal_projection=Polygon(coordinates=[[
                                [2.485866, 49.029301],
                                [2.604141, 49.034704],
                                [2.631263, 48.987301],
                                [2.510414, 48.983358],
                                [2.485866, 49.029301]
                            ]]
                            )
                        ),
                        AirspaceVolume(
                            uom_dimensions="M",
                            lower_limit=0,
                            lower_vertical_reference="AGL",
                            upper_limit=0,
                            upper_vertical_reference="AGL",
                            horizontal_projection=Circle(
                                center=[2.485866, 49.029301],
                                radius=7000
                            )
                        )
                    ],
                    applicability=TimePeriod(
                        permanent=CodeYesNoType.YES,
                        start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                        end_date_time=datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                        schedule=[
                            DailyPeriod(
                                day=CodeWeekDay.MON,
                                start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                                end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
                            ),
                            DailyPeriod(
                                day=CodeWeekDay.SAT,
                                start_time=datetime(2000, 1, 1, 9, 0, 0, tzinfo=timezone.utc),
                                end_time=datetime(2000, 1, 1, 15, 0, 0, tzinfo=timezone.utc)
                            )
                        ]
                    ),
                    zone_authority=Authority(
                        name='175d280099fb48eea5da490ac12f816a',
                        service='AuthorityEntity service',
                        purpose=CodeAuthorityRole.AUTHORIZATION,
                        email='auth@autority.be',
                        contact_name='AuthorityEntity manager',
                        site_url='http://www.autority.be',
                        phone='234234234',
                        interval_before='PD30'
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
                'geometry': [
                    {
                        "lowerLimit": 0,
                        "lowerVerticalReference": "AGL",
                        "horizontalProjection": {
                            "type": "Polygon",
                            "coordinates": [[
                                [2.485866, 49.029301],
                                [2.604141, 49.034704],
                                [2.631263, 48.987301],
                                [2.510414, 48.983358],
                                [2.485866, 49.029301]
                            ]]
                        },
                        "uomDimensions": "M",
                        "upperLimit": 0,
                        "upperVerticalReference": "AGL"
                    },
                    {
                        "lowerLimit": 0,
                        "lowerVerticalReference": "AGL",
                        "horizontalProjection": {
                            "type": "Circle",
                            "center": [2.485866, 49.029301],
                            "radius": 7000
                        },
                        "uomDimensions": "M",
                        "upperLimit": 0,
                        "upperVerticalReference": "AGL"
                    }
                ],
                'applicability': {
                    'schedule': [{
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
                'zoneAuthority': {
                    'name': '175d280099fb48eea5da490ac12f816a',
                    'service': 'AuthorityEntity service',
                    'purpose': 'AUTHORIZATION',
                    'email': 'auth@autority.be',
                    'contactName': 'AuthorityEntity manager',
                    'siteURL': 'http://www.autority.be',
                    'phone': '234234234',
                    'intervalBefore': 'PD30'
                },
                'country': 'BEL',
                'regulationExemption': 'YES',
                'extendedProperties': {},
                'identifier': "zsdffgs",
                'message': 'message',
                'name': "",
                'reason': [],
                'otherReasonInfo': "",
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
                other_reason_info="",
                region=1,
                restriction=CodeRestrictionType.NO_RESTRICTION,
                restriction_conditions=[],
                type=CodeZoneType.COMMON,
                u_space_class=CodeUSpaceClassType.EUROCONTROL,
                country="BEL",
                regulation_exemption=CodeYesNoType.YES,
                geometry=[
                    AirspaceVolume(
                        uom_dimensions="M",
                        lower_limit=0,
                        lower_vertical_reference="AGL",
                        upper_limit=0,
                        upper_vertical_reference="AGL",
                        horizontal_projection=Polygon(coordinates=[[
                                [2.485866, 49.029301],
                                [2.604141, 49.034704],
                                [2.631263, 48.987301],
                                [2.510414, 48.983358],
                                [2.485866, 49.029301]
                            ]]
                        )
                    ),
                    AirspaceVolume(
                        uom_dimensions="M",
                        lower_limit=0,
                        lower_vertical_reference="AGL",
                        upper_limit=0,
                        upper_vertical_reference="AGL",
                        horizontal_projection=Circle(
                            center=[2.485866, 49.029301],
                            radius=7000
                        )
                    )
                ],
                applicability=TimePeriod(
                    permanent=CodeYesNoType.YES,
                    start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    end_date_time=datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    schedule=[
                        DailyPeriod(
                            day=CodeWeekDay.MON,
                            start_time=datetime(2000, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                            end_time=datetime(2000, 1, 1, 18, 0, 0, tzinfo=timezone.utc)
                        ),
                        DailyPeriod(
                            day=CodeWeekDay.SAT,
                            start_time=datetime(2000, 1, 1, 9, 0, 0, tzinfo=timezone.utc),
                            end_time=datetime(2000, 1, 1, 15, 0, 0, tzinfo=timezone.utc)
                        )
                    ]
                ),
                zone_authority=Authority(
                    name='175d280099fb48eea5da490ac12f816a',
                    service='AuthorityEntity service',
                    purpose=CodeAuthorityRole.AUTHORIZATION,
                    email='auth@autority.be',
                    contact_name='AuthorityEntity manager',
                    site_url='http://www.autority.be',
                    phone='234234234',
                    interval_before='PD30'
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
                    "horizontalProjection": {
                        "type": "Polygon",
                        "coordinates": [[
                            [2.485866, 49.029301],
                            [2.604141, 49.034704],
                            [2.631263, 48.987301],
                            [2.510414, 48.983358],
                            [2.485866, 49.029301]
                        ]]
                    },
                    "uomDimensions": "M",
                    "upperLimit": 0,
                    "upperVerticalReference": "AGL"
                },
                'regions': [1],
                'startDateTime': '2020-01-01T00:00:00+00:00',
                'endDateTime': '2020-02-01T00:00:00+00:00',
            }
        },
        UASZoneSubscriptionReplyObject(
            subscription_id='123456',
            publication_location='location',
            active=True,
            uas_zones_filter=UASZonesFilter(
                airspace_volume=AirspaceVolume(
                    uom_dimensions="M",
                    lower_limit=0,
                    lower_vertical_reference="AGL",
                    upper_limit=0,
                    upper_vertical_reference="AGL",
                    horizontal_projection=Polygon(coordinates=[[
                            [2.485866, 49.029301],
                            [2.604141, 49.034704],
                            [2.631263, 48.987301],
                            [2.510414, 48.983358],
                            [2.485866, 49.029301]
                        ]]
                    )
                ),
                regions=[1],
                start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
            )
        )
    ),
    (
        {
            'subscriptionID': '123456',
            'publicationLocation': 'location',
            'active': True,
            'UASZonesFilter': {
                'airspaceVolume': {
                    "lowerLimit": 0,
                    "lowerVerticalReference": "AGL",
                    "horizontalProjection": {
                        "type": "Circle",
                        "center": [2.485866, 49.029301],
                        "radius": 7000
                    },
                    "uomDimensions": "M",
                    "upperLimit": 0,
                    "upperVerticalReference": "AGL"
                },
                'regions': [1],
                'startDateTime': '2020-01-01T00:00:00+00:00',
                'endDateTime': '2020-02-01T00:00:00+00:00',
            }
        },
        UASZoneSubscriptionReplyObject(
            subscription_id='123456',
            publication_location='location',
            active=True,
            uas_zones_filter=UASZonesFilter(
                airspace_volume=AirspaceVolume(
                    uom_dimensions="M",
                    lower_limit=0,
                    lower_vertical_reference="AGL",
                    upper_limit=0,
                    upper_vertical_reference="AGL",
                    horizontal_projection=Circle(
                        center=[2.485866, 49.029301],
                        radius=7000
                    )
                ),
                regions=[1],
                start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
            )
        )
    )
])
def test_uas_zone_subscription_reply_object__from_json(uas_zone_subscription_reply_object_json, expected_object):
    assert expected_object == UASZoneSubscriptionReplyObject.from_json(uas_zone_subscription_reply_object_json)
#

@pytest.mark.parametrize('uas_zone_subscription_reply_object, expected_dict', [
    (
        UASZoneSubscriptionReplyObject(
            subscription_id='123456',
            publication_location='location',
            active=True,
            uas_zones_filter=UASZonesFilter(
                airspace_volume=AirspaceVolume(
                    uom_dimensions="M",
                    lower_limit=0,
                    lower_vertical_reference="AGL",
                    upper_limit=0,
                    upper_vertical_reference="AGL",
                    horizontal_projection=Polygon(coordinates=[[
                            [2.485866, 49.029301],
                            [2.604141, 49.034704],
                            [2.631263, 48.987301],
                            [2.510414, 48.983358],
                            [2.485866, 49.029301]
                        ]]
                    )
                ),
                regions=[1],
                start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
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
                    "horizontalProjection": {
                        "type": "Polygon",
                        "coordinates": [[
                            [2.485866, 49.029301],
                            [2.604141, 49.034704],
                            [2.631263, 48.987301],
                            [2.510414, 48.983358],
                            [2.485866, 49.029301]
                        ]]
                    },
                    "uomDimensions": "M",
                    "upperLimit": 0,
                    "upperVerticalReference": "AGL"
                },
                'regions': [1],
                'startDateTime': '2020-01-01T00:00:00+00:00',
                'endDateTime': '2020-02-01T00:00:00+00:00',
            }
        }
    ),
    (
        UASZoneSubscriptionReplyObject(
            subscription_id='123456',
            publication_location='location',
            active=True,
            uas_zones_filter=UASZonesFilter(
                airspace_volume=AirspaceVolume(
                    uom_dimensions="M",
                    lower_limit=0,
                    lower_vertical_reference="AGL",
                    upper_limit=0,
                    upper_vertical_reference="AGL",
                    horizontal_projection=Circle(
                        center=[2.485866, 49.029301],
                        radius=7000
                    )
                ),
                regions=[1],
                start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
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
                    "horizontalProjection": {
                        "type": "Circle",
                        "center": [2.485866, 49.029301],
                        "radius": 7000
                    },
                    "uomDimensions": "M",
                    "upperLimit": 0,
                    "upperVerticalReference": "AGL"
                },
                'regions': [1],
                'startDateTime': '2020-01-01T00:00:00+00:00',
                'endDateTime': '2020-02-01T00:00:00+00:00',
            }
        }
    )
])
def test_uas_zone_subscription_reply_object__to_json(uas_zone_subscription_reply_object, expected_dict):
    assert expected_dict == uas_zone_subscription_reply_object.to_json()


@pytest.mark.parametrize('uas_zone_subscription_reply_json, expected_object', [
    (
        {
            'subscription': {
                'subscriptionID': '123456',
                'publicationLocation': 'location',
                'active': True,
                'UASZonesFilter': {
                    'airspaceVolume': {
                        "lowerLimit": 0,
                        "lowerVerticalReference": "AGL",
                        "horizontalProjection": {
                            "type": "Polygon",
                            "coordinates": [[
                                [2.485866, 49.029301],
                                [2.604141, 49.034704],
                                [2.631263, 48.987301],
                                [2.510414, 48.983358],
                                [2.485866, 49.029301]
                            ]]
                        },
                        "uomDimensions": "M",
                        "upperLimit": 0,
                        "upperVerticalReference": "AGL"
                    },
                    'regions': [1],
                    'startDateTime': '2020-01-01T00:00:00+00:00',
                    'endDateTime': '2020-02-01T00:00:00+00:00',
                }
            },
            'genericReply': {
                'RequestStatus': 'OK',
                'RequestExceptionDescription': 'everything ok',
                'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
            }
        },
        UASZoneSubscriptionReply(
            subscription=UASZoneSubscriptionReplyObject(
                subscription_id='123456',
                publication_location='location',
                active=True,
                uas_zones_filter=UASZonesFilter(
                    airspace_volume=AirspaceVolume(
                        uom_dimensions="M",
                        lower_limit=0,
                        lower_vertical_reference="AGL",
                        upper_limit=0,
                        upper_vertical_reference="AGL",
                        horizontal_projection=Polygon(coordinates=[[
                                [2.485866, 49.029301],
                                [2.604141, 49.034704],
                                [2.631263, 48.987301],
                                [2.510414, 48.983358],
                                [2.485866, 49.029301]
                            ]]
                        )
                    ),
                    regions=[1],
                    start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                )
            ),
            generic_reply=GenericReply(
                request_status=RequestStatus.OK,
                request_exception_description='everything ok',
                request_processed_timestamp=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
            )
        )
    ),    (
        {
            'subscription': {
                'subscriptionID': '123456',
                'publicationLocation': 'location',
                'active': True,
                'UASZonesFilter': {
                    'airspaceVolume': {
                        "lowerLimit": 0,
                        "lowerVerticalReference": "AGL",
                        "horizontalProjection": {
                        "type": "Circle",
                        "center": [2.485866, 49.029301],
                        "radius": 7000
                    },
                        "uomDimensions": "M",
                        "upperLimit": 0,
                        "upperVerticalReference": "AGL"
                    },
                    'regions': [1],
                    'startDateTime': '2020-01-01T00:00:00+00:00',
                    'endDateTime': '2020-02-01T00:00:00+00:00',
                }
            },
            'genericReply': {
                'RequestStatus': 'OK',
                'RequestExceptionDescription': 'everything ok',
                'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
            }
        },
        UASZoneSubscriptionReply(
            subscription=UASZoneSubscriptionReplyObject(
                subscription_id='123456',
                publication_location='location',
                active=True,
                uas_zones_filter=UASZonesFilter(
                    airspace_volume=AirspaceVolume(
                        uom_dimensions="M",
                        lower_limit=0,
                        lower_vertical_reference="AGL",
                        upper_limit=0,
                        upper_vertical_reference="AGL",
                        horizontal_projection=Circle(
                           center=[2.485866, 49.029301],
                            radius=7000
                        )
                    ),
                    regions=[1],
                    start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
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
            'subscriptions': [{
                'subscriptionID': '123456',
                'publicationLocation': 'location',
                'active': True,
                'UASZonesFilter': {
                    'airspaceVolume': {
                        "lowerLimit": 0,
                        "lowerVerticalReference": "AGL",
                        "horizontalProjection": {
                            "type": "Polygon",
                            "coordinates": [[
                                [2.485866, 49.029301],
                                [2.604141, 49.034704],
                                [2.631263, 48.987301],
                                [2.510414, 48.983358],
                                [2.485866, 49.029301]
                            ]]
                        },
                        "uomDimensions": "M",
                        "upperLimit": 0,
                        "upperVerticalReference": "AGL"
                    },
                    'regions': [1],
                    'startDateTime': '2020-01-01T00:00:00+00:00',
                    'endDateTime': '2020-02-01T00:00:00+00:00',
                }
            }],
            'genericReply': {
                'RequestStatus': 'OK',
                'RequestExceptionDescription': 'everything ok',
                'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
            }
        },
        UASZoneSubscriptionsReply(
            subscriptions=[UASZoneSubscriptionReplyObject(
                subscription_id='123456',
                publication_location='location',
                active=True,
                uas_zones_filter=UASZonesFilter(
                    airspace_volume=AirspaceVolume(
                        uom_dimensions="M",
                        lower_limit=0,
                        lower_vertical_reference="AGL",
                        upper_limit=0,
                        upper_vertical_reference="AGL",
                        horizontal_projection=Polygon(coordinates=[[
                                [2.485866, 49.029301],
                                [2.604141, 49.034704],
                                [2.631263, 48.987301],
                                [2.510414, 48.983358],
                                [2.485866, 49.029301]
                            ]]
                        )
                    ),
                    regions=[1],
                    start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                )
            )],
            generic_reply=GenericReply(
                request_status=RequestStatus.OK,
                request_exception_description='everything ok',
                request_processed_timestamp=datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
            )
        )
    ),
    (
        {
            'subscriptions': [{
                'subscriptionID': '123456',
                'publicationLocation': 'location',
                'active': True,
                'UASZonesFilter': {
                    'airspaceVolume': {
                        "lowerLimit": 0,
                        "lowerVerticalReference": "AGL",
                        "horizontalProjection": {
                        "type": "Circle",
                        "center": [2.485866, 49.029301],
                        "radius": 7000
                    },
                        "uomDimensions": "M",
                        "upperLimit": 0,
                        "upperVerticalReference": "AGL"
                    },
                    'regions': [1],
                    'startDateTime': '2020-01-01T00:00:00+00:00',
                    'endDateTime': '2020-02-01T00:00:00+00:00',
                }
            }],
            'genericReply': {
                'RequestStatus': 'OK',
                'RequestExceptionDescription': 'everything ok',
                'RequestProcessedTimestamp': '2019-01-01T00:00:00+00:00'
            }
        },
        UASZoneSubscriptionsReply(
            subscriptions=[UASZoneSubscriptionReplyObject(
                subscription_id='123456',
                publication_location='location',
                active=True,
                uas_zones_filter=UASZonesFilter(
                    airspace_volume=AirspaceVolume(
                        uom_dimensions="M",
                        lower_limit=0,
                        lower_vertical_reference="AGL",
                        upper_limit=0,
                        upper_vertical_reference="AGL",
                        horizontal_projection=Circle(
                           center=[2.485866, 49.029301],
                            radius=7000
                        )
                    ),
                    regions=[1],
                    start_date_time=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    end_date_time=datetime(2020, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
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
