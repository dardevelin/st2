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

from st2common import transport
from st2common.models import db
from st2common.models.db import workflow as wf_db_models
from st2common.persistence import base as persistence


__all__ = [
    'WorkflowExecution',
    'TaskExecution'
]


class WorkflowExecution(persistence.StatusBasedResource):
    impl = db.ChangeRevisionMongoDBAccess(wf_db_models.WorkflowExecutionDB)
    publisher = None

    @classmethod
    def _get_impl(cls):
        return cls.impl

    @classmethod
    def _get_publisher(cls):
        if not cls.publisher:
            cls.publisher = transport.workflow.WorkflowExecutionPublisher()

        return cls.publisher


class TaskExecution(persistence.StatusBasedResource):
    impl = db.ChangeRevisionMongoDBAccess(wf_db_models.TaskExecutionDB)
    publisher = None

    @classmethod
    def _get_impl(cls):
        return cls.impl
