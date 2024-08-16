"""Get a download URL for an installed version of Python"""

import platform
import sys

version1 = ".".join(map(lambda n: str(n), sys.version_info[0:3]))
version2 = platform.python_version()

print(f"https://www.python.org/ftp/python/{version1}/Python-{version2}.tgz")
