# coding: utf-8

"""
    An API to insert and retrieve metadata on cloud artifacts.

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiSource(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'storage_source': 'ApiStorageSource',
        'repo_source': 'ApiRepoSource',
        'artifact_storage_source': 'ApiStorageSource',
        'file_hashes': 'dict(str, ApiFileHashes)',
        'context': 'ApiSourceContext',
        'additional_contexts': 'list[ApiSourceContext]'
    }

    attribute_map = {
        'storage_source': 'storage_source',
        'repo_source': 'repo_source',
        'artifact_storage_source': 'artifact_storage_source',
        'file_hashes': 'file_hashes',
        'context': 'context',
        'additional_contexts': 'additional_contexts'
    }

    def __init__(self, storage_source=None, repo_source=None, artifact_storage_source=None, file_hashes=None, context=None, additional_contexts=None):  # noqa: E501
        """ApiSource - a model defined in Swagger"""  # noqa: E501

        self._storage_source = None
        self._repo_source = None
        self._artifact_storage_source = None
        self._file_hashes = None
        self._context = None
        self._additional_contexts = None
        self.discriminator = None

        if storage_source is not None:
            self.storage_source = storage_source
        if repo_source is not None:
            self.repo_source = repo_source
        if artifact_storage_source is not None:
            self.artifact_storage_source = artifact_storage_source
        if file_hashes is not None:
            self.file_hashes = file_hashes
        if context is not None:
            self.context = context
        if additional_contexts is not None:
            self.additional_contexts = additional_contexts

    @property
    def storage_source(self):
        """Gets the storage_source of this ApiSource.  # noqa: E501

        If provided, get the source from this location in in Google Cloud Storage.  # noqa: E501

        :return: The storage_source of this ApiSource.  # noqa: E501
        :rtype: ApiStorageSource
        """
        return self._storage_source

    @storage_source.setter
    def storage_source(self, storage_source):
        """Sets the storage_source of this ApiSource.

        If provided, get the source from this location in in Google Cloud Storage.  # noqa: E501

        :param storage_source: The storage_source of this ApiSource.  # noqa: E501
        :type: ApiStorageSource
        """

        self._storage_source = storage_source

    @property
    def repo_source(self):
        """Gets the repo_source of this ApiSource.  # noqa: E501

        If provided, get source from this location in a Cloud Repo.  # noqa: E501

        :return: The repo_source of this ApiSource.  # noqa: E501
        :rtype: ApiRepoSource
        """
        return self._repo_source

    @repo_source.setter
    def repo_source(self, repo_source):
        """Sets the repo_source of this ApiSource.

        If provided, get source from this location in a Cloud Repo.  # noqa: E501

        :param repo_source: The repo_source of this ApiSource.  # noqa: E501
        :type: ApiRepoSource
        """

        self._repo_source = repo_source

    @property
    def artifact_storage_source(self):
        """Gets the artifact_storage_source of this ApiSource.  # noqa: E501

        If provided, the input binary artifacts for the build came from this location.  # noqa: E501

        :return: The artifact_storage_source of this ApiSource.  # noqa: E501
        :rtype: ApiStorageSource
        """
        return self._artifact_storage_source

    @artifact_storage_source.setter
    def artifact_storage_source(self, artifact_storage_source):
        """Sets the artifact_storage_source of this ApiSource.

        If provided, the input binary artifacts for the build came from this location.  # noqa: E501

        :param artifact_storage_source: The artifact_storage_source of this ApiSource.  # noqa: E501
        :type: ApiStorageSource
        """

        self._artifact_storage_source = artifact_storage_source

    @property
    def file_hashes(self):
        """Gets the file_hashes of this ApiSource.  # noqa: E501

        Hash(es) of the build source, which can be used to verify that the original source integrity was maintained in the build.  The keys to this map are file paths used as build source and the values contain the hash values for those files.  If the build source came in a single package such as a gzipped tarfile (.tar.gz), the FileHash will be for the single path to that file.  # noqa: E501

        :return: The file_hashes of this ApiSource.  # noqa: E501
        :rtype: dict(str, ApiFileHashes)
        """
        return self._file_hashes

    @file_hashes.setter
    def file_hashes(self, file_hashes):
        """Sets the file_hashes of this ApiSource.

        Hash(es) of the build source, which can be used to verify that the original source integrity was maintained in the build.  The keys to this map are file paths used as build source and the values contain the hash values for those files.  If the build source came in a single package such as a gzipped tarfile (.tar.gz), the FileHash will be for the single path to that file.  # noqa: E501

        :param file_hashes: The file_hashes of this ApiSource.  # noqa: E501
        :type: dict(str, ApiFileHashes)
        """

        self._file_hashes = file_hashes

    @property
    def context(self):
        """Gets the context of this ApiSource.  # noqa: E501

        If provided, the source code used for the build came from this location.  # noqa: E501

        :return: The context of this ApiSource.  # noqa: E501
        :rtype: ApiSourceContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ApiSource.

        If provided, the source code used for the build came from this location.  # noqa: E501

        :param context: The context of this ApiSource.  # noqa: E501
        :type: ApiSourceContext
        """

        self._context = context

    @property
    def additional_contexts(self):
        """Gets the additional_contexts of this ApiSource.  # noqa: E501

        If provided, some of the source code used for the build may be found in these locations, in the case where the source repository had multiple remotes or submodules. This list will not include the context specified in the context field.  # noqa: E501

        :return: The additional_contexts of this ApiSource.  # noqa: E501
        :rtype: list[ApiSourceContext]
        """
        return self._additional_contexts

    @additional_contexts.setter
    def additional_contexts(self, additional_contexts):
        """Sets the additional_contexts of this ApiSource.

        If provided, some of the source code used for the build may be found in these locations, in the case where the source repository had multiple remotes or submodules. This list will not include the context specified in the context field.  # noqa: E501

        :param additional_contexts: The additional_contexts of this ApiSource.  # noqa: E501
        :type: list[ApiSourceContext]
        """

        self._additional_contexts = additional_contexts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ApiSource, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
