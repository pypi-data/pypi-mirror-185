#  Copyright (c) 2021.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
from multiprocessing import Queue

STARTED = False
HOST = os.getenv("PY_HEALTH_CHECK_HOST", "0.0.0.0")
PORT = os.getenv("PY_HEALTH_CHECK_PORT", "8080")

TEST_MODE = os.getenv("PY_HEALTH_TEST_MODE", None) is not None

if isinstance(PORT, str) and PORT.isdecimal() and 1 < int(PORT) < 65535:
	PORT = int(PORT)
else:
	PORT = 8080

if not TEST_MODE:
	message_queue = Queue()
	process_queue = Queue()
	status_queue = Queue()
