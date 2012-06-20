#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class TeamPad(Page):

    _signinbutton_locator = (By.CSS_SELECTOR, '#signInButton')
    _success_message = (By.CSS_SELECTOR, '#welcome-msg')
    _page_title = 'MoPad: Sign In'

    def go_to_teampad_page(self, teampad):
        # FIXME where should this be configured?
        self.selenium.get('https://%s.etherpad-dev.allizom.org' % teampad)
        #self._page_title = '%s - MoPad' % teampad
        self.is_the_current_page

    def logout(self):
        self.click_logout()

    def sign_in(self, expect='new'):
        """Click the 'Sign In' button.

        Keyword arguments:
        expect -- the expected resulting page
                  'new' for user that is not currently signed in (default)
                  'returning' for users already signed in or recently verified

        """
        self.selenium.find_element(*self._signinbutton_locator).click()
        from browserid.pages.webdriver.sign_in import SignIn
        return SignIn(self.selenium, self.timeout, expect=expect)

    def click_logout(self):
        # FIXME
        # no convenient id, link is /ep/account/sign-out
        pass

    def reload(self):
        self.selenium.refresh()

    @property
    def is_logged_in(self):
        return self.is_element_visible(*self._success_message)

