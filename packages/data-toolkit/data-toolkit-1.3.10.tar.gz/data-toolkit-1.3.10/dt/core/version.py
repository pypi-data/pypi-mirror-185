
from cement.utils.version import get_version as cement_get_version

VERSION = (1, 3, 10, 'final', 1)

def get_version(version=VERSION):
    return cement_get_version(version)

