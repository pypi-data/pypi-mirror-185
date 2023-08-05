# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.714
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_scheduler.configuration import Configuration


class ImageSummary(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'name': 'str',
        'push_time': 'datetime',
        'pull_time': 'datetime',
        'digest': 'str',
        'size': 'int',
        'tags': 'list[Tag]',
        'scan_status': 'str',
        'scan_summary': 'ScanSummary',
        'link': 'Link'
    }

    attribute_map = {
        'name': 'name',
        'push_time': 'pushTime',
        'pull_time': 'pullTime',
        'digest': 'digest',
        'size': 'size',
        'tags': 'tags',
        'scan_status': 'scanStatus',
        'scan_summary': 'scanSummary',
        'link': 'link'
    }

    required_map = {
        'name': 'optional',
        'push_time': 'optional',
        'pull_time': 'optional',
        'digest': 'optional',
        'size': 'optional',
        'tags': 'optional',
        'scan_status': 'optional',
        'scan_summary': 'optional',
        'link': 'optional'
    }

    def __init__(self, name=None, push_time=None, pull_time=None, digest=None, size=None, tags=None, scan_status=None, scan_summary=None, link=None, local_vars_configuration=None):  # noqa: E501
        """ImageSummary - a model defined in OpenAPI"
        
        :param name:  Name of the image
        :type name: str
        :param push_time:  The push time of the image
        :type push_time: datetime
        :param pull_time:  The latest pull time of the image
        :type pull_time: datetime
        :param digest:  The digest of the image
        :type digest: str
        :param size:  The size of the image (in bytes)
        :type size: int
        :param tags:  The tags of the image
        :type tags: list[lusid_scheduler.Tag]
        :param scan_status:  The Scan Status of the stated image
        :type scan_status: str
        :param scan_summary: 
        :type scan_summary: lusid_scheduler.ScanSummary
        :param link: 
        :type link: lusid_scheduler.Link

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._push_time = None
        self._pull_time = None
        self._digest = None
        self._size = None
        self._tags = None
        self._scan_status = None
        self._scan_summary = None
        self._link = None
        self.discriminator = None

        self.name = name
        self.push_time = push_time
        self.pull_time = pull_time
        self.digest = digest
        self.size = size
        self.tags = tags
        self.scan_status = scan_status
        if scan_summary is not None:
            self.scan_summary = scan_summary
        if link is not None:
            self.link = link

    @property
    def name(self):
        """Gets the name of this ImageSummary.  # noqa: E501

        Name of the image  # noqa: E501

        :return: The name of this ImageSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageSummary.

        Name of the image  # noqa: E501

        :param name: The name of this ImageSummary.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def push_time(self):
        """Gets the push_time of this ImageSummary.  # noqa: E501

        The push time of the image  # noqa: E501

        :return: The push_time of this ImageSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._push_time

    @push_time.setter
    def push_time(self, push_time):
        """Sets the push_time of this ImageSummary.

        The push time of the image  # noqa: E501

        :param push_time: The push_time of this ImageSummary.  # noqa: E501
        :type push_time: datetime
        """

        self._push_time = push_time

    @property
    def pull_time(self):
        """Gets the pull_time of this ImageSummary.  # noqa: E501

        The latest pull time of the image  # noqa: E501

        :return: The pull_time of this ImageSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._pull_time

    @pull_time.setter
    def pull_time(self, pull_time):
        """Sets the pull_time of this ImageSummary.

        The latest pull time of the image  # noqa: E501

        :param pull_time: The pull_time of this ImageSummary.  # noqa: E501
        :type pull_time: datetime
        """

        self._pull_time = pull_time

    @property
    def digest(self):
        """Gets the digest of this ImageSummary.  # noqa: E501

        The digest of the image  # noqa: E501

        :return: The digest of this ImageSummary.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this ImageSummary.

        The digest of the image  # noqa: E501

        :param digest: The digest of this ImageSummary.  # noqa: E501
        :type digest: str
        """

        self._digest = digest

    @property
    def size(self):
        """Gets the size of this ImageSummary.  # noqa: E501

        The size of the image (in bytes)  # noqa: E501

        :return: The size of this ImageSummary.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ImageSummary.

        The size of the image (in bytes)  # noqa: E501

        :param size: The size of this ImageSummary.  # noqa: E501
        :type size: int
        """

        self._size = size

    @property
    def tags(self):
        """Gets the tags of this ImageSummary.  # noqa: E501

        The tags of the image  # noqa: E501

        :return: The tags of this ImageSummary.  # noqa: E501
        :rtype: list[lusid_scheduler.Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ImageSummary.

        The tags of the image  # noqa: E501

        :param tags: The tags of this ImageSummary.  # noqa: E501
        :type tags: list[lusid_scheduler.Tag]
        """

        self._tags = tags

    @property
    def scan_status(self):
        """Gets the scan_status of this ImageSummary.  # noqa: E501

        The Scan Status of the stated image  # noqa: E501

        :return: The scan_status of this ImageSummary.  # noqa: E501
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        """Sets the scan_status of this ImageSummary.

        The Scan Status of the stated image  # noqa: E501

        :param scan_status: The scan_status of this ImageSummary.  # noqa: E501
        :type scan_status: str
        """

        self._scan_status = scan_status

    @property
    def scan_summary(self):
        """Gets the scan_summary of this ImageSummary.  # noqa: E501


        :return: The scan_summary of this ImageSummary.  # noqa: E501
        :rtype: lusid_scheduler.ScanSummary
        """
        return self._scan_summary

    @scan_summary.setter
    def scan_summary(self, scan_summary):
        """Sets the scan_summary of this ImageSummary.


        :param scan_summary: The scan_summary of this ImageSummary.  # noqa: E501
        :type scan_summary: lusid_scheduler.ScanSummary
        """

        self._scan_summary = scan_summary

    @property
    def link(self):
        """Gets the link of this ImageSummary.  # noqa: E501


        :return: The link of this ImageSummary.  # noqa: E501
        :rtype: lusid_scheduler.Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ImageSummary.


        :param link: The link of this ImageSummary.  # noqa: E501
        :type link: lusid_scheduler.Link
        """

        self._link = link

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageSummary):
            return True

        return self.to_dict() != other.to_dict()
