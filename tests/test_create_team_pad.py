#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.signup import SignupPage
from pages.teampad import TeamPad
from restmail.restmail import RestmailInbox
from unittestzero import Assert
from mocks.mock_user import MockUser

import pytest
import time


class TestCreateTeamPad:

    @pytest.mark.destructive
    def test_that_user_can_create_team_pad(self, mozwebqa):
        user = MockUser()
        signup_pg = SignupPage(mozwebqa)

        teampad = 'webqatest_%s' % repr(time.time()).replace('.','')
        fullname = 'Testy Testington'

        signup_pg.go_to_signup_page()
        browserid = signup_pg.create_team_pad(teampad, fullname)
        browserid.sign_in_new_user(user['email'], user['password'])

        # Open restmail inbox, find the email
        inbox = RestmailInbox(user['email'])
        email = inbox.find_by_sender('BrowserID@browserid.org')

        # Load the BrowserID link from the email in the browser
        mozwebqa.selenium.get(email.verify_user_link)
        from browserid.pages.webdriver.complete_registration import CompleteRegistration
        CompleteRegistration(mozwebqa.selenium, mozwebqa.timeout)

        signup_pg.go_to_signup_page()
        browserid = signup_pg.create_team_pad(teampad, fullname, expect='returning')
        browserid.click_sign_in_returning_user()

        Assert.true(signup_pg.is_created)

        teampad_pg = TeamPad(mozwebqa)
        teampad_pg.go_to_teampad_page(teampad)
        browserid = teampad_pg.sign_in(expect='returning')
        browserid.click_sign_in_returning_user()

        Assert.true(teampad_pg.is_logged_in)

        mozwebqa.selenium.get(teampad_pg.logout_link)
        teampad_pg.go_to_teampad_page(teampad)

        Assert.true(teampad_pg.is_logged_out)
