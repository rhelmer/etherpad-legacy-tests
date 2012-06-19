#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home import HomePage
from unittestzero import Assert

import pytest


class TestSignIn:

    @pytest.mark.nondestructive
    def test_that_user_can_sign_in(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.sign_in()
        Assert.true(home_pg.is_logged_in)
