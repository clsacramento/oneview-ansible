#!/usr/bin/python

###
# Copyright (2016) Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###

from ansible.module_utils.basic import *

try:
    from hpOneView.oneview_client import OneViewClient

    HAS_HPE_ONEVIEW = True
except ImportError:
    HAS_HPE_ONEVIEW = False

DOCUMENTATION = '''
---
module: oneview_sas_logical_interconnect_group_facts
short_description: Retrieve facts about one or more of the OneView SAS Logical Interconnect Groups.
description:
    - Retrieve facts about one or more of the SAS Logical Interconnect Groups from OneView.
requirements:
    - "python >= 2.7.9"
    - "hpOneView >= 3.0"
author: "Camila Balestrin (@balestrinc)"
options:
    config:
      description:
        - Path to a .json configuration file containing the OneView client configuration.
          The configuration file is optional. If the file path is not provided, the configuration will be loaded from
          environment variables.
      required: false
    name:
      description:
        - Name of the SAS Logical Interconnect Group.
      required: false
notes:
    - "A sample configuration file for the config parameter can be found at:
       https://github.hpe.com/Rainforest/oneview-ansible/blob/master/examples/oneview_config.json"
    - "Check how to use environment variables for configuration at:
       https://github.com/HewlettPackard/oneview-ansible#environment-variables"
'''

EXAMPLES = '''
- name: Gather facts about all SAS Logical Interconnect Groups
    oneview_sas_logical_interconnect_group_facts:
    config: "{{ config_path }}"

- debug: var=sas_logical_interconnect_groups

- name: Gather facts about a SAS Logical Interconnect Group by name
    oneview_sas_logical_interconnect_group_facts:
    config: "{{ config_path }}"
    name: "LIG-SLJA-1"

- debug: var=sas_logical_interconnect_groups
'''

RETURN = '''
sas_logical_interconnect_groups:
    description: Has all the OneView facts about the SAS Logical Interconnect Groups.
    returned: Always, but can be null.
    type: complex
'''
HPE_ONEVIEW_SDK_REQUIRED = 'HPE OneView Python SDK is required for this module.'


class SasLogicalInterconnectGroupFactsModule(object):
    argument_spec = dict(
        config=dict(required=False, type='str'),
        name=dict(required=False, type='str')
    )

    def __init__(self):
        self.module = AnsibleModule(argument_spec=self.argument_spec, supports_check_mode=False)
        if not HAS_HPE_ONEVIEW:
            self.module.fail_json(msg=HPE_ONEVIEW_SDK_REQUIRED)

        if not self.module.params['config']:
            self.oneview_client = OneViewClient.from_environment_variables()
        else:
            self.oneview_client = OneViewClient.from_json_file(self.module.params['config'])

    def run(self):
        try:
            if self.module.params['name']:
                name = self.module.params['name']
                resources = self.oneview_client.sas_logical_interconnect_groups.get_by('name', name)
            else:
                resources = self.oneview_client.sas_logical_interconnect_groups.get_all()

            self.module.exit_json(changed=False, ansible_facts=dict(sas_logical_interconnect_groups=resources))

        except Exception as exception:
            self.module.fail_json(msg='; '.join(str(e) for e in exception.args))


def main():
    SasLogicalInterconnectGroupFactsModule().run()


if __name__ == '__main__':
    main()