# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ArrayOfNumberOnly(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, array_number: List[float]=None):  # noqa: E501
        """ArrayOfNumberOnly - a model defined in Swagger

        :param array_number: The array_number of this ArrayOfNumberOnly.  # noqa: E501
        :type array_number: List[float]
        """
        self.swagger_types = {
            'array_number': List[float]
        }

        self.attribute_map = {
            'array_number': 'ArrayNumber'
        }
        self._array_number = array_number

    @classmethod
    def from_dict(cls, dikt) -> 'ArrayOfNumberOnly':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ArrayOfNumberOnly of this ArrayOfNumberOnly.  # noqa: E501
        :rtype: ArrayOfNumberOnly
        """
        return util.deserialize_model(dikt, cls)

    @property
    def array_number(self) -> List[float]:
        """Gets the array_number of this ArrayOfNumberOnly.


        :return: The array_number of this ArrayOfNumberOnly.
        :rtype: List[float]
        """
        return self._array_number

    @array_number.setter
    def array_number(self, array_number: List[float]):
        """Sets the array_number of this ArrayOfNumberOnly.


        :param array_number: The array_number of this ArrayOfNumberOnly.
        :type array_number: List[float]
        """

        self._array_number = array_number
