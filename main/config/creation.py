#!/usr/bin/env python

# Copyright (c) 2016 Hewlett Packard Enterprise Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not used this file except in compliance with the License. You may obtain
# a copy of the License at:
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging

from main.config import validation
from main.util import common_util

logger = logging.getLogger(__name__)


def create_components(_config):
    """Creates the components defined by the configuration

    :param _config: dict -- configuration containing components
    :returns: dict -- created components indexed by type and ID
    """
    components = {}
    for component_type in validation.valid_connection_types.keys():
        components[component_type] = \
            _create_comps_by_module(component_type, _config)
    return components


def _create_comps_by_module(comp_type, _config):
    """Instantiates all the components of a type defined in the configuration

    :param comp_type: string -- type of the components to be deployed
    (e.g. source, ingestor, ...)
    :type _config: dictionary -- configuration containing components
    :returns: dictionary -- deployed components, keyed by ID
    :raises: MonanasNoSuchSourceError -- if no source class found.
    """
    logger.debug("Creating components of type : " + comp_type)
    ret = {}
    for comp_id, comp_config in _config[comp_type].iteritems():
        comp = _create_component_by_module(
            comp_id, comp_config, comp_type)
        ret[comp_id] = comp
    return ret


def _create_component_by_module(comp_id, comp_config, comp_type):
    """Create a single component matching the past configuration.

    The id assigned to that component will be comp_id.

    :param comp_id: str -- ID of the component to create
    :param comp_config: dict -- configuration of the component to create
    :param comp_type: str -- type of component to create
    :returns: Object -- instantiated component object
    """
    logger.debug("deploying " + comp_config["module"] + " object")
    clazz = common_util.get_class_by_name(comp_config["module"],
                                          comp_type)
    _comp = clazz(comp_id, comp_config)
    return _comp
