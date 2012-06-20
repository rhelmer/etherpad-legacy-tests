#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class SignupPage(Page):

    _page_title = ''

    _subdomain_locator = (By.CSS_SELECTOR, '#subdomain')
    _fullname_locator = (By.CSS_SELECTOR, '#fullName')
    _createbutton_locator = (By.CSS_SELECTOR, '#createbutton')
    _success_message = (By.XPATH, "//p[contains(text(), 'Success!')]")

    def go_to_signup_page(self):
        self.selenium.get(self.base_url + '/ep/pro-signup/')
        self.is_the_current_page

    def create_team_pad(self, teampad=None, fullname=None, expect='new'):

        self.selenium.find_element(*self._subdomain_locator).send_keys(teampad)
        self.selenium.find_element(*self._fullname_locator).send_keys(fullname)

        browserid = self.click_create_team_site(expect)
        return browserid

    def click_create_team_site(self, expect='new'):
        """Click the 'Create team site now' button.

        Keyword arguments:
        expect -- the expected resulting page
                  'new' for user that is not currently signed in (default)
                  'returning' for users already signed in or recently verified

        """
        self.selenium.find_element(*self._createbutton_locator).click()
        from browserid.pages.webdriver.sign_in import SignIn
        return SignIn(self.selenium, self.timeout, expect=expect)

    @property
    def is_created(self):
        return self.is_element_visible(*self._success_message)

