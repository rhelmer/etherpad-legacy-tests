#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.signup import SignupPage
from unittestzero import Assert

import pytest


class TestCreateTeamPad:

    @pytest.mark.destructive
    def test_that_user_can_create_team_pad(self, mozwebqa):
        signup_pg = SignupPage(mozwebqa)
        signup_pg.go_to_signup_page()
        signup_pg.create_team_pad()
        Assert.true(signup_pg.is_logged_in)
