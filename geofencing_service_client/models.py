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

from rest_client import BaseModel

__author__ = "EUROCONTROL (SWIM)"

from rest_client.typing import JSONType

from geofencing_service_client.utils import get_time_from_datetime_iso

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


class Point(BaseModel):

    def __init__(self, lat: float, lon: float) -> None:
        """

        :param lat:
        :param lon:
        """
        self.lat = lat
        self.lon = lon

    @classmethod
    def from_json(cls, object_dict):
        return cls(
            lat=float(object_dict['LAT']),
            lon=float(object_dict['LON']),
        )

    def to_json(self) -> Dict[str, str]:
        return {
            "LAT": str(self.lat),
            "LON": str(self.lon)
        }


class AirspaceVolume(BaseModel):

    def __init__(self,
                 polygon: List[Point],
                 upper_limit_in_m: int,
                 lower_limit_in_m: int,
                 upper_vertical_reference: Union[CodeVerticalReferenceType, str],
                 lower_vertical_reference: Union[CodeVerticalReferenceType, str]) -> None:
        """

        :param polygon:
        :param upper_limit_in_m:
        :param lower_limit_in_m:
        :param upper_vertical_reference:
        :param lower_vertical_reference:
        """
        self.polygon = polygon
        self.upper_limit_in_m = upper_limit_in_m
        self.lower_limit_in_m = lower_limit_in_m
        self.upper_vertical_reference = CodeVerticalReferenceType(upper_vertical_reference)
        self.lower_vertical_reference = CodeVerticalReferenceType(lower_vertical_reference)

    @classmethod
    def from_json(cls, object_dict):
        return cls(
            polygon=[Point.from_json(coords) for coords in object_dict['polygon']],
            upper_limit_in_m=object_dict.get("upperLimit"),
            lower_limit_in_m=object_dict.get("lowerLimit"),
            upper_vertical_reference=object_dict.get("upperVerticalReference"),
            lower_vertical_reference=object_dict.get("lowerVerticalReference"),
        )

    def to_json(self) -> Dict[str, Any]:
        return {
            "polygon": [point.to_json() for point in self.polygon],
            "upperLimit": self.upper_limit_in_m,
            "lowerLimit": self.lower_limit_in_m,
            "upperVerticalReference": self.upper_vertical_reference.value,
            "lowerVerticalReference": self.lower_vertical_reference.value
        }


class DailySchedule(BaseModel):

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
            start_time=datetime.fromisoformat(start_time),
            end_time=datetime.fromisoformat(end_time),
        )

    def to_json(self) -> JSONType:
        return {
            'day': self.day.value,
            'startTime': get_time_from_datetime_iso(self.start_time.isoformat()),
            'endTime': get_time_from_datetime_iso(self.end_time.isoformat())
        }


class ApplicableTimePeriod(BaseModel):

    def __init__(self,
                 permanent: Union[str, CodeYesNoType],
                 start_date_time: datetime,
                 end_date_time: datetime,
                 daily_schedule: List[DailySchedule]):
        """

        :param permanent:
        :param start_date_time:
        :param end_date_time:
        :param daily_schedule:
        """
        self.permanent = permanent if isinstance(permanent, CodeYesNoType) else CodeYesNoType(permanent)
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.daily_schedule = daily_schedule

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            permanent=object_dict['permanent'],
            start_date_time=datetime.fromisoformat(object_dict['startDateTime']),
            end_date_time=datetime.fromisoformat(object_dict['endDateTime']),
            daily_schedule=[DailySchedule.from_json(daily_schedule) for daily_schedule in object_dict['dailySchedule']]
        )

    def to_json(self) -> JSONType:
        return {
            'permanent': self.permanent.value,
            'startDateTime': self.start_date_time.isoformat(),
            'endDateTime': self.end_date_time.isoformat(),
            'dailySchedule': [daily_schedule.to_json() for daily_schedule in self.daily_schedule]
        }


class AuthorityEntity(BaseModel):

    def __init__(self,
                 name: Optional[str] = None,
                 contact_name: Optional[str] = None,
                 service: Optional[str] = None,
                 email: Optional[str] = None,
                 site_url: Optional[str] = None,
                 phone: Optional[str] = None) -> None:
        """

        :param name:
        :param contact_name:
        :param service:
        :param email:
        :param site_url:
        :param phone:
        """
        self.name = name
        self.contact_name = contact_name
        self.service = service
        self.email = email
        self.site_url = site_url
        self.phone = phone

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            name=object_dict['name'],
            contact_name=object_dict['contactName'],
            service=object_dict['service'],
            email=object_dict['email'],
            site_url=object_dict['siteURL'],
            phone=object_dict['phone']
        )

    def to_json(self) -> JSONType:
        return {
            'name': self.name,
            'contactName': self.contact_name,
            'service': self.service,
            'email': self.email,
            'siteURL': self.site_url,
            'phone': self.phone
        }


class NotificationRequirement(BaseModel):

    def __init__(self, authority: AuthorityEntity, interval_before: str) -> None:
        """

        :param authority:
        :param interval_before:
        """
        self.authority = authority
        self.interval_before = interval_before

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            authority=AuthorityEntity.from_json(object_dict['authority']),
            interval_before=object_dict['intervalBefore']
        )

    def to_json(self) -> JSONType:
        return {
            'authority': self.authority.to_json(),
            'intervalBefore': self.interval_before
        }


class AuthorizationRequirement(BaseModel):

    def __init__(self, authority: AuthorityEntity) -> None:
        """

        :param authority:
        """
        self.authority = authority

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            authority=AuthorityEntity.from_json(object_dict['authority'])
        )

    def to_json(self) -> JSONType:
        return {
            'authority': self.authority.to_json()
        }


class Authority(BaseModel):

    def __init__(self,
                 requires_notification_to: Optional[NotificationRequirement] = None,
                 requires_authorization_from: Optional[AuthorizationRequirement] = None) -> None:
        """

        :param requires_notification_to:
        :param requires_authorization_from:
        """
        self.requires_notification_to = requires_notification_to
        self.requires_authorization_from = requires_authorization_from

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            requires_notification_to=NotificationRequirement.from_json(object_dict['requiresNotificationTo']),
            requires_authorization_from=AuthorizationRequirement.from_json(object_dict['requiresAuthorizationFrom'])
        )

    def to_json(self) -> JSONType:
        return {
            'requiresNotificationTo': self.requires_notification_to.to_json(),
            'requiresAuthorizationFrom': self.requires_authorization_from.to_json()
        }


class DataSource(BaseModel):

    def __init__(self, creation_date_time: datetime, update_date_time: datetime, author: Optional[str] = None) -> None:
        self.creation_date_time = creation_date_time
        self.update_date_time = update_date_time
        self.author = author

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            creation_date_time=datetime.fromisoformat(object_dict['creationDateTime']),
            update_date_time=datetime.fromisoformat(object_dict['updateDateTime']),
            author=object_dict['author']
        )

    def to_json(self) -> JSONType:
        return {
            'creationDateTime': self.creation_date_time.isoformat(),
            'updateDateTime': self.update_date_time.isoformat(),
            'author': self.author
        }


class UASZone(BaseModel):
    def __init__(self,
                 identifier: str,
                 name: str,
                 type: Union[str, CodeZoneType],
                 restriction: Union[str, CodeRestrictionType],
                 restriction_conditions: List[str],
                 region: int,
                 data_capture_prohibition: Union[str, CodeYesNoType],
                 u_space_class: Union[str, CodeUSpaceClassType],
                 message: str,
                 reason: List[CodeZoneReasonType],
                 country: str,
                 airspace_volume: AirspaceVolume,
                 applicable_time_period: ApplicableTimePeriod,
                 data_source: DataSource,
                 authority: Optional[Authority] = None,
                 extended_properties: Optional[Dict[str, Any]] = None) -> None:
        """

        :param identifier:
        :param name:
        :param type:
        :param restriction:
        :param restriction_conditions:
        :param region:
        :param data_capture_prohibition:
        :param u_space_class:
        :param message:
        :param reason:
        :param country:
        :param airspace_volume:
        :param applicable_time_period:
        :param data_source:
        :param authority:
        :param extended_properties:
        """
        self.identifier = identifier
        self.name = name
        self.type = CodeZoneType(type)
        self.restriction = CodeRestrictionType(restriction)
        self.restriction_conditions = restriction_conditions
        self.region = region
        self.data_capture_prohibition = CodeYesNoType(data_capture_prohibition)
        self.u_space_class = CodeUSpaceClassType(u_space_class)
        self.message = message
        self.reason = reason
        self.country = country
        self.airspace_volume = airspace_volume
        self.applicable_time_period = applicable_time_period
        self.data_source = data_source
        self.authority = authority
        self.extended_properties = extended_properties

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            identifier=object_dict['identifier'],
            name=object_dict['name'],
            type=CodeZoneType(object_dict['type']),
            restriction=CodeRestrictionType(object_dict['restriction']),
            restriction_conditions=object_dict['restrictionConditions'],
            region=object_dict['region'],
            data_capture_prohibition=object_dict['dataCaptureProhibition'],
            u_space_class=CodeUSpaceClassType(object_dict['uSpaceClass']),
            message=object_dict['message'],
            reason=[CodeZoneReasonType(reason) for reason in object_dict['reason']],
            country=object_dict['country'],
            airspace_volume=AirspaceVolume.from_json(object_dict['airspaceVolume']),
            applicable_time_period=ApplicableTimePeriod.from_json(object_dict['applicableTimePeriod']),
            data_source=DataSource.from_json(object_dict['dataSource']),
            authority=Authority.from_json(object_dict['authority']),
            extended_properties=object_dict['extendedProperties'],
        )

    def to_json(self) -> JSONType:
        return {
            'identifier': self.identifier,
            'name': self.name,
            'type': self.type.value,
            'restriction': self.restriction.value,
            'restrictionConditions': self.restriction_conditions,
            'region': self.region,
            'dataCaptureProhibition': self.data_capture_prohibition.value,
            'uSpaceClass': self.u_space_class.value,
            'message': self.message,
            'reason': [reason.value for reason in self.reason],
            'country': self.country,
            'airspaceVolume': self.airspace_volume.to_json(),
            'applicableTimePeriod': self.applicable_time_period.to_json(),
            'dataSource': self.data_source.to_json(),
            'authority': self.authority.to_json(),
            'extendedProperties': self.extended_properties
        }


class UASZonesFilter(BaseModel):

    def __init__(self,
                 airspace_volume: AirspaceVolume,
                 regions: List[int],
                 request_id: str,
                 start_date_time: datetime,
                 end_date_time: datetime,
                 updated_after_date_time: Optional[datetime] = None) -> None:
        """

        :param airspace_volume:
        :param request_id:
        :param regions:
        :param start_date_time:
        :param end_date_time:
        :param updated_after_date_time:
        """
        self.airspace_volume = airspace_volume
        self.regions = regions
        self.request_id = request_id
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.updated_after_date_time = updated_after_date_time

    @classmethod
    def from_json(cls, object_dict):
        updated_after_date_time = object_dict.get('updatedAfterDateTime')

        if updated_after_date_time is not None:
            updated_after_date_time = datetime.fromisoformat(updated_after_date_time)

        return cls(
            airspace_volume=AirspaceVolume.from_json(object_dict["airspaceVolume"]),
            regions=object_dict['regions'],
            start_date_time=datetime.fromisoformat(object_dict['startDateTime']),
            end_date_time=datetime.fromisoformat(object_dict['endDateTime']),
            updated_after_date_time=updated_after_date_time,
            request_id=object_dict.get('requestID')
        )

    def to_json(self) -> Dict[str, Any]:
        result = {
            "airspaceVolume": self.airspace_volume.to_json(),
            "regions": self.regions,
            "startDateTime": self.start_date_time.isoformat(),
            "endDateTime": self.end_date_time.isoformat(),
            "requestID": self.request_id
        }

        if self.updated_after_date_time:
            result["updatedAfterDateTime"] = self.updated_after_date_time.isoformat()

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
            request_status=object_dict['requestStatus'],
            request_exception_description=object_dict['requestExceptionDescription'],
            request_processed_timestamp=datetime.fromisoformat(object_dict['requestProcessedTimestamp'])
        )


class UASZoneFilterReply(BaseModel):

    def __init__(self, uas_zones: List[UASZone], generic_reply: GenericReply):
        self.uas_zones = uas_zones
        self.generic_reply = generic_reply

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            uas_zones=[UASZone.from_json(uas_zone_object) for uas_zone_object in object_dict['UASZoneList']],
            generic_reply=GenericReply.from_json(object_dict['genericReply'])
        )


class UASZoneCreateReply(BaseModel):

    def __init__(self, uas_zone: UASZone, generic_reply: GenericReply):
        super().__init__()
        self.uas_zone = uas_zone
        self.generic_reply = generic_reply

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            uas_zone=UASZone.from_json(object_dict['UASZone']),
            generic_reply=GenericReply.from_json(object_dict['genericReply'])
        )


class SubscribeToUASZonesUpdatesReply(BaseModel):

    def __init__(self, subscription_id: str, publication_location: str, generic_reply: GenericReply):
        super().__init__()
        self.subscription_id = subscription_id
        self.publication_location = publication_location
        self.generic_reply = generic_reply

    @classmethod
    def from_json(cls, object_dict: JSONType):
        return cls(
            subscription_id=object_dict['subscriptionID'],
            publication_location=object_dict['publicationLocation'],
            generic_reply=GenericReply.from_json(object_dict['genericReply'])
        )
