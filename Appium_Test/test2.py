#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from appium import webdriver
import desired_capabilities
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

SLEEPY_TIME = 3

class FindByAccessibilityIDTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_single_element(self):
        el = self.driver.find_element_by_accessibility_id('Media')
        action = TouchAction(self.driver)
        action.tap(el).perform()
        sleep(SLEEPY_TIME)
        el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("MediaPlayer")')
        self.assertIsNotNone(el)
        sleep(SLEEPY_TIME)

class FindByAccessibilityIDTest2(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('selendroid-test-app.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_single_element(self):
        try:
                print(self.driver.find_element_by_name('EN Button').is_enabled())
                print(self.driver.find_element_by_name('EN Button').is_displayed())
                print(self.driver.find_element_by_name('EN Button').is_selected())

                if self.driver.find_element_by_name('EN Button').is_enabled():
                        sleep(SLEEPY_TIME)
                        el = self.driver.find_element_by_name('EN Button').click()
                        self.assertIsNotNone(el)
                        sleep(SLEEPY_TIME)
        except Exception as e:
                print(e)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FindByAccessibilityIDTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(FindByAccessibilityIDTest2)
    unittest.TextTestRunner(verbosity=2).run(suite)