from .classes import APIKeyData, APINicknameResponse, APIPlayerData, APIPunishmentData, APIResponseTypes, APIStaffTracker, FilterType

from requests import get
from json import loads

from typing import Any

API = "https://hypixel.cactive.network/api/v3"

class Client:
    def __init__(self, key: str, cache: bool = False) -> None:
        self.__key = key
        self.__cache = cache

    def __map_external_error(self, json: APIResponseTypes) -> APIResponseTypes:
        return {
            "success": False,
            "id": json.id,
            "errors": map(lambda err: {"type": err.type, "code": err.code, "message": err.message, "internal": False}, json.errors),
        }

    def __map_internal_error(self, reason: Any) -> APIResponseTypes:
        return {
            "success": False,
            "errors": [
                {
                    "type": "failed-api-request",
                    "code": 500,
                    "message": str(reason),
                    "internal": True,
                }
            ]
        }

    def nickname_history(self, nickname: str) -> APINicknameResponse:
        try:
            req = get(f"{API}/nickname-history?key={self.__key}&cache={self.__cache}&nickname={nickname}")
            json: APINicknameResponse = APINicknameResponse(*loads(req.text).values())
        except Exception as reason:
            raise Exception(self.__map_internal_error(reason))

        if json.success: return json
        else: raise Exception(self.__map_external_error(json))

    def player_data(self, uuid: str) -> APIPlayerData:
        try:
            req = get(f"{API}/player-data?key={self.__key}&cache={self.__cache}&uuid={uuid}")
            json: APIPlayerData = APIPlayerData(*loads(req.text).values())
        except Exception as reason:
            raise Exception(self.__map_internal_error(reason))

        if json.success: return json
        else: raise Exception(self.__map_external_error(json))

    def staff_tracker(self, filter: FilterType) -> APIStaffTracker:
        try:
            req = get(f"{API}/staff-tracker?key={self.__key}&cache={self.__cache}&filter={filter}")
            json: APIStaffTracker = APIStaffTracker(*loads(req.text).values())
        except Exception as reason:
            raise Exception(self.__map_internal_error(reason))

        if json.success: return json
        else: raise Exception(self.__map_external_error(json))

    def punishment_data(self, id: str) -> APIPunishmentData:
        try:
            req = get(f"{API}/punishment-data?key={self.__key}&cache={self.__cache}&id={id}")
            json: APIPunishmentData = APIPunishmentData(*loads(req.text).values())
        except Exception as reason:
            raise Exception(self.__map_internal_error(reason))

        if json.success: return json
        else: raise Exception(self.__map_external_error(json))

    def key_data(self) -> APIKeyData:
        try:
            req = get(f"{API}/key?key={self.__key}")
            json: APIKeyData = APIKeyData(*loads(req.text).values())
        except Exception as reason:
            raise Exception(self.__map_internal_error(reason))

        if json.success: return json
        else: raise Exception(self.__map_external_error(json))