
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from dimakis_test_registry_instance_sdk.api.admin_api import AdminApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from dimakis_test_registry_instance_sdk.api.admin_api import AdminApi
from dimakis_test_registry_instance_sdk.api.artifact_rules_api import ArtifactRulesApi
from dimakis_test_registry_instance_sdk.api.artifacts_api import ArtifactsApi
from dimakis_test_registry_instance_sdk.api.global_rules_api import GlobalRulesApi
from dimakis_test_registry_instance_sdk.api.metadata_api import MetadataApi
from dimakis_test_registry_instance_sdk.api.search_api import SearchApi
from dimakis_test_registry_instance_sdk.api.system_api import SystemApi
from dimakis_test_registry_instance_sdk.api.users_api import UsersApi
from dimakis_test_registry_instance_sdk.api.versions_api import VersionsApi
