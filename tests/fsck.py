#!/usr/bin/env python
#
#    Copyright (C) 2008  Nikolaus Rath <Nikolaus@rath.org>
#
#    This program can be distributed under the terms of the GNU LGPL.
#

from tests import TestCase, assert_true, assert_equals, assert_raises

class fsck(TestCase):
    """Tests s3ql.fsck module
    """

    def __init__(self, cb):
        self.cb = cb
