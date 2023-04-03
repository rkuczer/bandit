#!/usr/bin/env python
# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0
from bandit import bandit
export PATH="/opt/hostedtoolcache/Python/3.7.16/x64/bin:$PATH"

if __name__ == "__main__":
    bandit.main()
