# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Ptsv2creditsProcessingInformationElectronicBenefitsTransfer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'category': 'str'
    }

    attribute_map = {
        'category': 'category'
    }

    def __init__(self, category=None):
        """
        Ptsv2creditsProcessingInformationElectronicBenefitsTransfer - a model defined in Swagger
        """

        self._category = None

        if category is not None:
          self.category = category

    @property
    def category(self):
        """
        Gets the category of this Ptsv2creditsProcessingInformationElectronicBenefitsTransfer.
        Flag that specifies the category for the EBT transaction.  Possible values: - `CASH`: Cash benefits, which can be used to purchase any item at a participating retailer, as well as to obtain cash-back or make a cash withdrawal from a participating ATM. - `FOOD`: Food stamp benefits, which can be used only to purchase food items authorized by the USDA SNAP program. 

        :return: The category of this Ptsv2creditsProcessingInformationElectronicBenefitsTransfer.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Ptsv2creditsProcessingInformationElectronicBenefitsTransfer.
        Flag that specifies the category for the EBT transaction.  Possible values: - `CASH`: Cash benefits, which can be used to purchase any item at a participating retailer, as well as to obtain cash-back or make a cash withdrawal from a participating ATM. - `FOOD`: Food stamp benefits, which can be used only to purchase food items authorized by the USDA SNAP program. 

        :param category: The category of this Ptsv2creditsProcessingInformationElectronicBenefitsTransfer.
        :type: str
        """
        if category is not None and len(category) > 4:
            raise ValueError("Invalid value for `category`, length must be less than or equal to `4`")

        self._category = category

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Ptsv2creditsProcessingInformationElectronicBenefitsTransfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
