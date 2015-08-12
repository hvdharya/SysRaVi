#!/usr/bin/env python

# this file has been modified for testing
# second test

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ravi.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
