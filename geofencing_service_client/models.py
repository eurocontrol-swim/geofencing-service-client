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
import enum
from datetime import datetime
from typing import List, Union, Dict, Optional, Any

import dateutil.parser
from rest_client import BaseModel
from rest_client.typing import JSONType

from geofencing_service_client.utils import get_time_from_datetime_iso, make_timezone_aware

__author__ = "EUROCONTROL (SWIM)"

GeoJSONPolygonCoordinates = List[List[List[Union[float, int]]]]


class CodeYesNoType(enum.Enum):
    YES = "YES"
    NO = "NO"


class CodeWeekDay(enum.Enum):
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"


class CodeZoneType(enum.Enum):
    COMMON = "COMMON"
    CUSTOMIZED = "CUSTOMIZED"


class CodeRestrictionType(enum.Enum):
    PROHIBITED = "PROHIBITED"
    REQ_AUTHORISATION = "REQ_AUTHORISATION"
    CONDITIONAL = "CONDITIONAL"
    NO_RESTRICTION = "NO_RESTRICTION"


class CodeUSpaceClassType(enum.Enum):
    EUROCONTROL = "EUROCONTROL"
    CORUS = "CORUS"


class CodeZoneReasonType(enum.Enum):
    AIR_TRAFFIC = "AIR_TRAFFIC"
    SENSITIVE = "SENSITIVE"
    PRIVACY = "PRIVACY"
    POPULATION = "POPULATION"
    NATURE = "NATURE"
    NOISE = "NOISE"
    FOREIGN_TERRITORY = "FOREIGN_TERRITORY"
    OTHER = "OTHER"


class CodeVerticalReferenceType(enum.Enum):
    AGL = "AGL"
    AMSL = "AMSL"
    WGS84 = "WGS84"


class RequestStatus(enum.Enum):
    OK = "OK"
    NOK = "NOK"


class UomDistance(enum.Enum):
    METERS = 'M'
    FEET = 'FT'

class CodeAuthorityRole(enum.Enum):
    AUTHORIZATION = "AUTHORIZATION"
    NOTIFICATION = "NOTIFICATION"
    INFORMATION = "INFORMATION"


class Polygon(BaseModel):

    def __init__(self, coordinates: List[List[List[float]]]):
        self.type= "Polygon"
        self.coordinates = coordinates

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            coordinates=object_dict['coordinates']
        )

    def to_json(self) -> JSONType:
        return {
            "type": self.type,
            "coordinates": self.coordinates
        }


class Circle(BaseModel):

    def __init__(self, center: List[float], radius: float) -> None:
        self.type= "Circle"
        self.center = center
        self.radius = radius

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            center=object_dict['center'],
            radius=object_dict['radius']
        )

    def to_json(self) -> JSONType:
        return {
            "type": self.type,
            "center": self.center,
            "radius": self.radius
        }


class AirspaceVolume(BaseModel):

    def __init__(self,
                 horizontal_projection: Union[Polygon, Circle],
                 uom_dimensions: Union[UomDistance, str],
                 upper_limit: int,
                 lower_limit: int,
                 upper_vertical_reference: Union[CodeVerticalReferenceType, str],
                 lower_vertical_reference: Union[CodeVerticalReferenceType, str]) -> None:
        """

        :param horizontal_projection:
        :param uom_dimensions:
        :param upper_limit:
        :param lower_limit:
        :param upper_vertical_reference:
        :param lower_vertical_reference:
        """
        self.horizontal_projection = horizontal_projection
        self.uom_dimensions = uom_dimensions
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
        self.upper_vertical_reference = CodeVerticalReferenceType(upper_vertical_reference)
        self.lower_vertical_reference = CodeVerticalReferenceType(lower_vertical_reference)

    @classmethod
    def from_json(cls, object_dict):
        if object_dict['horizontalProjection']['type'] == 'Circle':
            horizontal_projection = Circle.from_json(object_dict['horizontalProjection'])
        else:
            horizontal_projection = Polygon.from_json(object_dict['horizontalProjection'])

        return cls(
            horizontal_projection=horizontal_projection,
            uom_dimensions=object_dict.get("uomDimensions"),
            upper_limit=object_dict.get("upperLimit"),
            lower_limit=object_dict.get("lowerLimit"),
            upper_vertical_reference=object_dict.get("upperVerticalReference"),
            lower_vertical_reference=object_dict.get("lowerVerticalReference"),
        )

    def to_json(self) -> Dict[str, Any]:
        if self.horizontal_projection.type == 'Circle':
            horizontal_projection = Circle.to_json(self.horizontal_projection)
        else:
            horizontal_projection = Polygon.to_json(self.horizontal_projection)

        return {
            "uomDimensions": self.uom_dimensions,
            "horizontalProjection": horizontal_projection,
            "upperLimit": self.upper_limit,
            "lowerLimit": self.lower_limit,
            "upperVerticalReference": self.upper_vertical_reference.value,
            "lowerVerticalReference": self.lower_vertical_reference.value
        }


class DailyPeriod(BaseModel):

    _default_date = "2000-01-01"

    def __init__(self, day: Union[str, CodeWeekDay], start_time: datetime, end_time: datetime) -> None:
        """

        :param day:
        :param start_time:
        :param end_time:
        """
        self.day = day if isinstance(day, CodeWeekDay) else CodeWeekDay(day)
        self.start_time = start_time
        self.end_time = end_time

    @classmethod
    def from_json(cls, object_dict: JSONType):
        start_time = f"{cls._default_date}T{object_dict['startTime']}"
        end_time = f"{cls._default_date}T{object_dict['endTime']}"

        return cls(
            day=object_dict['day'],
            start_time=dateutil.parser.parse(start_time),
            end_time=dateutil.parser.parse(end_time),
        )

    def to_json(self) -> JSONType:
        return {
            'day': self.day.value,
            'startTime': get_time_from_datetime_iso(self.start_time.isoformat()),
            'endTime': get_time_from_datetime_iso(self.end_time.isoformat())
        }


class TimePeriod(BaseModel):

    def __init__(self,
                 permanent: Union[str, CodeYesNoType],
                 start_date_time: datetime,
                 end_date_time: datetime,
                 schedule: List[DailyPeriod]):
        """

        :param permanent:
        :param start_date_time:
        :param end_date_time:
        :param schedule:
        """
        self.permanent = CodeYesNoType(permanent)
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.schedule = schedule

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            permanent=object_dict['permanent'],
            start_date_time=dateutil.parser.parse(object_dict['startDateTime']),
            end_date_time=dateutil.parser.parse(object_dict['endDateTime']),
            schedule=[DailyPeriod.from_json(s) for s in object_dict['schedule']]
        )

    def to_json(self) -> JSONType:
        return {
            'permanent': self.permanent.value,
            'startDateTime': self.start_date_time.isoformat(),
            'endDateTime': self.end_date_time.isoformat(),
            'schedule': [s.to_json() for s in self.schedule]
        }


class Authority(BaseModel):

    def __init__(self,
                 name: str,
                 service: str,
                 purpose: Union[str, CodeAuthorityRole],
                 email: Optional[str] = None,
                 contact_name: Optional[str] = None,
                 site_url: Optional[str] = None,
                 phone: Optional[str] = None,
                 interval_before: Optional[str] = None) -> None:
        """

        :param name:
        :param service:
        :param purpose:
        :param email:
        :param contact_name:
        :param site_url:
        :param phone:
        :param interval_before:
        """
        self.name = name
        self.service = service
        self.purpose = CodeAuthorityRole(purpose)
        self.email = email
        self.contact_name = contact_name
        self.site_url = site_url
        self.phone = phone
        self.interval_before = interval_before

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            name=object_dict.get('name'),
            service=object_dict.get('service'),
            purpose=object_dict.get('purpose'),
            email=object_dict.get('email'),
            contact_name=object_dict.get('contactName'),
            site_url=object_dict.get('siteURL'),
            phone=object_dict.get('phone'),
            interval_before=object_dict.get('intervalBefore')
        )

    def to_json(self) -> JSONType:
        return {
            'name': self.name,
            'service': self.service,
            'purpose': self.purpose.value,
            'email': self.email,
            'contactName': self.contact_name,
            'siteURL': self.site_url,
            'phone': self.phone,
            'intervalBefore': self.interval_before
        }


class UASZone(BaseModel):
    def __init__(self,
                 identifier: str,
                 country: str,
                 type: Union[str, CodeZoneType],
                 restriction: Union[str, CodeRestrictionType],
                 zone_authority: Authority,
                 geometry: List[AirspaceVolume],
                 name: Optional[str] = None,
                 restriction_conditions: Optional[List[str]] = None,
                 region: Optional[int] = None,
                 reason: Optional[List[CodeZoneReasonType]] = None,
                 other_reason_info: Optional[str] = None,
                 regulation_exemption: Optional[Union[str, CodeYesNoType]] = None,
                 u_space_class: Optional[Union[str, CodeUSpaceClassType]] = None,
                 message: Optional[str] = None,
                 applicability: Optional[TimePeriod] = None,
                 extended_properties: Optional[Dict[str, Any]] = None) -> None:
        """

        :param identifier:
        :param country:
        :param type:
        :param restriction:
        :param zone_authority:
        :param geometry:
        :param name:
        :param restriction_conditions:
        :param region:
        :param reason:
        :param other_reason_info:
        :param regulation_exemption:
        :param u_space_class:
        :param message:
        :param applicability:
        :param extended_properties:
        """
        self.identifier = identifier
        self.country = country
        self.type = CodeZoneType(type)
        self.restriction = CodeRestrictionType(restriction)
        self.zone_authority = zone_authority
        self.geometry = geometry
        self.name = name
        self.restriction_conditions = restriction_conditions
        self.region = region
        self.reason = [CodeZoneReasonType(r) for r in reason if r is not None]
        self.other_reason_info = other_reason_info
        self.regulation_exemption = CodeYesNoType(regulation_exemption) if regulation_exemption \
            else None
        self.u_space_class = CodeUSpaceClassType(u_space_class) if u_space_class else None
        self.message = message
        self.applicability = applicability
        self.extended_properties = extended_properties

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            identifier=object_dict['identifier'],
            country=object_dict['country'],
            type=CodeZoneType(object_dict['type']),
            restriction=object_dict['restriction'],
            zone_authority=Authority.from_json(object_dict['zoneAuthority']),
            geometry=[AirspaceVolume.from_json(geo) for geo in object_dict['geometry']],
            name=object_dict['name'],
            restriction_conditions=object_dict['restrictionConditions'],
            region=object_dict['region'],
            reason=object_dict['reason'],
            other_reason_info=object_dict['otherReasonInfo'],
            regulation_exemption=object_dict['regulationExemption'],
            u_space_class=object_dict['uSpaceClass'],
            message=object_dict['message'],
            applicability=TimePeriod.from_json(object_dict['applicability']),
            extended_properties=object_dict['extendedProperties'],
        )

    def to_json(self) -> JSONType:
        return {
            'identifier': self.identifier,
            'country': self.country,
            'type': self.type.value,
            'restriction': self.restriction.value,
            'zoneAuthority': self.zone_authority.to_json(),
            'geometry': [geo.to_json() for geo in self.geometry],
            'name': self.name,
            'restrictionConditions': self.restriction_conditions,
            'region': self.region,
            'reason': [r.value for r in self.reason],
            'otherReasonInfo': self.other_reason_info,
            'regulationExemption': self.regulation_exemption.value,
            'uSpaceClass': self.u_space_class.value,
            'message': self.message,
            'applicability': self.applicability.to_json(),
            'extendedProperties': self.extended_properties
        }


class UASZonesFilter(BaseModel):

    def __init__(self,
                 airspace_volume: AirspaceVolume,
                 regions: List[int],
                 start_date_time: datetime,
                 end_date_time: datetime) -> None:
        """

        :param airspace_volume:
        :param regions:
        :param start_date_time:
        :param end_date_time:
        """
        self.airspace_volume = airspace_volume
        self.regions = regions
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time

    @classmethod
    def from_json(cls, object_dict):

        return cls(
            airspace_volume=AirspaceVolume.from_json(object_dict["airspaceVolume"]),
            regions=object_dict['regions'],
            start_date_time=dateutil.parser.parse(object_dict['startDateTime']),
            end_date_time=dateutil.parser.parse(object_dict['endDateTime']),
        )

    def to_json(self) -> Dict[str, Any]:
        result = {
            "airspaceVolume": self.airspace_volume.to_json(),
            "regions": self.regions,
            "startDateTime": make_timezone_aware(self.start_date_time).isoformat(),
            "endDateTime": make_timezone_aware(self.end_date_time).isoformat(),
        }

        return result


class GenericReply(BaseModel):

    def __init__(self,
                 request_status: Union[str, RequestStatus],
                 request_exception_description: Optional[str] = None,
                 request_processed_timestamp: Optional[datetime] = None):
        """
        Encapsulates general information about the result of the respective request process
        :param request_status: can be OK or NOK
        :param request_exception_description:
        :param request_processed_timestamp:
        """
        self.request_status = RequestStatus(request_status)
        self.request_exception_description = request_exception_description
        self.request_processed_timestamp = request_processed_timestamp

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            request_status=object_dict['RequestStatus'],
            request_exception_description=object_dict['RequestExceptionDescription'],
            request_processed_timestamp=dateutil.parser.parse(object_dict['RequestProcessedTimestamp'])
        )


class Reply(BaseModel):

    def __init__(self, generic_reply: GenericReply):
        """

        :param generic_reply:
        """
        self.generic_reply = generic_reply

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            generic_reply=GenericReply.from_json(object_dict['genericReply'])
        )


class UASZoneFilterReply(Reply):

    def __init__(self, uas_zone_list: List[UASZone], generic_reply: GenericReply):
        super().__init__(generic_reply)
        self.uas_zone_list = uas_zone_list

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            uas_zone_list=[UASZone.from_json(uas_zone_object) for uas_zone_object in object_dict['UASZoneList']],
            generic_reply=GenericReply.from_json(object_dict['genericReply'])
        )


class UASZoneCreateReply(Reply):

    def __init__(self, uas_zone: UASZone, generic_reply: GenericReply):
        super().__init__(generic_reply)
        self.uas_zone = uas_zone

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            uas_zone=UASZone.from_json(object_dict['UASZone']),
            generic_reply=GenericReply.from_json(object_dict['genericReply'])
        )


class SubscribeToUASZonesUpdatesReply(Reply):

    def __init__(self, subscription_id: str, publication_location: str, generic_reply: GenericReply):
        super().__init__(generic_reply)
        self.subscription_id = subscription_id
        self.publication_location = publication_location

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            subscription_id=object_dict['subscriptionID'],
            publication_location=object_dict['publicationLocation'],
            generic_reply=GenericReply.from_json(object_dict['genericReply'])
        )


class UASZoneSubscriptionReplyObject(BaseModel):

    def __init__(self, subscription_id: str, publication_location: str, active: bool, uas_zones_filter: UASZonesFilter):
        self.subscription_id = subscription_id
        self.publication_location = publication_location
        self.active = active
        self.uas_zones_filter = uas_zones_filter

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            subscription_id=object_dict['subscriptionID'],
            publication_location=object_dict['publicationLocation'],
            active=object_dict['active'],
            uas_zones_filter=UASZonesFilter.from_json(object_dict['UASZonesFilter'])
        )

    def to_json(self) -> JSONType:
        return {
            'subscriptionID': self.subscription_id,
            'publicationLocation': self.publication_location,
            'active': self.active,
            'UASZonesFilter': self.uas_zones_filter.to_json()
        }


class UASZoneSubscriptionReply(Reply):

    def __init__(self, subscription: UASZoneSubscriptionReplyObject, generic_reply: GenericReply) -> None:
        super().__init__(generic_reply)
        self.subscription = subscription

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            subscription=UASZoneSubscriptionReplyObject.from_json(object_dict['subscription']),
            generic_reply=GenericReply.from_json(object_dict['genericReply'])
        )


class UASZoneSubscriptionsReply(Reply):

    def __init__(self, subscriptions: List[UASZoneSubscriptionReplyObject], generic_reply: GenericReply) -> None:
        super().__init__(generic_reply)
        self.subscriptions = subscriptions

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            subscriptions=[
                UASZoneSubscriptionReplyObject.from_json(subscription)
                for subscription in object_dict['subscriptions']
            ],
            generic_reply=GenericReply.from_json(object_dict['genericReply'])
        )
