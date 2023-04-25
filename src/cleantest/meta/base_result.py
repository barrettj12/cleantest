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

"""Result object for cleantest methods that return some form of result."""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Result:
    """Result containing exit code, stdout, and stderr.

    Args:
        exit_code (int): Captured exit code.
        stdout (Any): Captured data printed to standard output.
        stderr (Any): Captured data printed to standard error.
    """

    exit_code: int
    stdout: Optional[str] = None
    stderr: Optional[str] = None