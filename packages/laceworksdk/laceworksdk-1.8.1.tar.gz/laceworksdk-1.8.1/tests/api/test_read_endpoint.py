# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import types

from tests.api.test_base_endpoint import BaseEndpoint


class ReadEndpoint(BaseEndpoint):

    OBJECT_TYPE = None
    OBJECT_MAP = {}

    def test_object_creation(self, api_object):

        if self.OBJECT_TYPE:
            assert isinstance(api_object, self.OBJECT_TYPE)

        if len(self.OBJECT_MAP) > 0:
            for attribute, object_type in self.OBJECT_MAP.items():
                assert isinstance(getattr(api_object, attribute), object_type)

    def test_api_get(self, api_object):
        if len(self.OBJECT_MAP) > 0:
            for attribute in self.OBJECT_MAP.keys():
                response = getattr(api_object, attribute).get()
                assert "data" in response.keys()
        else:
            response = api_object.get()
            assert "data" in response.keys()

    def test_api_search(self, api_object):
        random_object_id = self._get_random_object(api_object, self.OBJECT_ID_NAME)
        assert random_object_id is not None
        if random_object_id:
            response = api_object.search(json={
                "filters": [
                    {
                        "expression": "eq",
                        "field": self.OBJECT_ID_NAME,
                        "value": random_object_id
                    }
                ],
                "returns": [
                    self.OBJECT_ID_NAME
                ]
            })

            if isinstance(response, types.GeneratorType):
                response = next(response)

            assert "data" in response.keys()
            assert len(response["data"]) == 1
            assert response["data"][0][self.OBJECT_ID_NAME] == random_object_id
