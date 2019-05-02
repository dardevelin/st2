# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import


APACHE_20_LICENSE = """
# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""

APACHE_20_LICENSE = APACHE_20_LICENSE.strip('\n')


class ApacheLicenseChecker(object):
    name = 'check-apache-license-plugin'
    version = '0.1.0'
    off_by_default = False

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    def run(self):
        """Check for Apache 2.0 license.

        H101 Apache 2.0 license header not found
        """
        with open(self.filename, 'r') as f:
            content = f.read()

        empty_init_py = self.filename.endswith('__init__.py') and len(content) == 0

        if not empty_init_py and APACHE_20_LICENSE not in content:
            yield 1, 0, 'H101 Apache 2.0 license header not found', type(self)
