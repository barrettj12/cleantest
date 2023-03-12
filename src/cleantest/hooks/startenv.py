# Copyright 2023 Jason C. Nucciarone
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Hook run when test environment instance starts."""

from dataclasses import dataclass
from typing import List

from cleantest.meta.objects import injectable


@dataclass(frozen=True)
class StartEnvHook:
    """Hook run at the start of the test environment.

    Args:
        name: Unique name of hook.
        packages: Packages to inject into test environment.
        upload: Artifacts to upload into test environment.
    """

    name: str
    packages: List[injectable.Injectable] = None
    upload: List[injectable.Injectable] = None
