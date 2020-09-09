#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
from test_framework.page.base_page import BasePage


class LoginPage(BasePage):
    def login_by_password(self, username, password):
        self.po_runSteps("login_by_password", username = username, password = password)