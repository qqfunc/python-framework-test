"""Get version information of Python."""

import argparse
import platform
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("mode", choices=["long", "short"])
    args = parser.parse_args()

    if args.mode == "long":
        print(platform.python_version())
    else:
        ".".join(map(lambda n: str(n), sys.version_info[0:3]))
