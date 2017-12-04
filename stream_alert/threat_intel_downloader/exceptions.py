"""
Copyright 2017-present, Airbnb Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


class ThreatStreamException(Exception):
    """Base exception class ThreatStream Error"""

class ThreatStreamCredsError(ThreatStreamException):
    """Class for API Credential errors"""

class ThreatStreamConfigError(ThreatStreamException):
    """Class for Configuration errors"""

class ThreatStreamLambdaInvokeError(ThreatStreamException):
    """Class for Lambda Invoke Error"""

class ThreatStreamRequestsError(ThreatStreamException):
    """Classe for requests return code errors"""