# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from tests.MainPage.Feeling.Feeling import FeelingsListView
from tests.MainPage.Post.Post import Post
from tests.Page.Page import Page
from tests.ProfilePage.ProfilePage import ProfilePage
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(Page):
    PATH = 'feed'

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    def has_feeling(self):
        try:
            self.get_feeling_btn()
            return True
        except TimeoutException:
            return False

    def get_feeling_btn(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="ust_a"]'))
        )

    def remove_feeling_btn(self):
        delete_feeling_btn_xpath = '//i[@class="tico_img ic12 ic12_close-g"]'

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, delete_feeling_btn_xpath))
            ).click()
        except TimeoutException:
            return

        confirm_btn_xpath = '//input[@class="button-pro form-actions_yes"]'
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, confirm_btn_xpath))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[@id="popLayer_mo"]'))
        )

    def get_feelings_list_view(self):
        self._get_feeling_btn().click()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, FeelingsListView.XPATH))
        )
        return FeelingsListView(self.driver, element)

    def get_profile_page(self):
        profile_href_xpath = '//div[@class="mctc_nameAndOnline"]//a'

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, profile_href_xpath))
        )
        profile_path = element.get_attribute('pathname')
        return ProfilePage(self.driver, profile_path)

    def get_last_post(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Post.XPATH))
        )
        return Post(self.driver, element)

    def _get_feeling_btn(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="pform_ac __feeling"]'))
        )

    def add_recommended_friend(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class = 'button-pro __sec __small js-entity-accept']"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class = 'entity-item_status __success lstp-t ellip']"))
        )
        return True

    def add_recommended_group(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//div[@class="caption"]//div'
                                            '//div[@class="hookBlock join-group-link js-groupJoinButton"]//a['
                                            '@class="al"]'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="tico c-green join-group-result"]'))
        )
        return True

    def delete_recommended_group(self):
        delete_clickable = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@class = "recommended-group_close foh-s"]'))
        )
        self.driver.execute_script('arguments[0].click()', delete_clickable)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class = "recommended-group_stub_tx"]'))
        )
        return True

    def delete_recommended_friend(self):
        friend_xpath = '//*[@class = "button-pro __sec __small js-entity-accept"]'
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            friend_xpath))
        )
        friends = self.driver.find_elements_by_xpath(friend_xpath)

        decline_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class = "tico_img ic10 ic10_close-g js-entity-decline"]'))
        )
        self.driver.execute_script('arguments[0].click()', decline_element)

        WebDriverWait(self.driver, 10).until(
            WaitItemDecrease(friend_xpath, len(friends), self.driver)
        )
        return True

    def refresh_page_recommended_friend(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//div[@class="caption"]//div'
                                            '//div[@class="hookBlock join-group-link js-groupJoinButton"]'))
        )

        id = el.get_attribute("id")
        self.driver.refresh()

        refresh_el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//div[@class="caption"]//div'
                                            '//div[@class="hookBlock join-group-link js-groupJoinButton"]'))
        )
        return refresh_el.get_attribute('id') != id

    def refresh_btn_recommended_friend(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//div[@class="caption"]//div'
                                            '//div[@class="hookBlock join-group-link js-groupJoinButton"]'))
        )
        id = el.get_attribute('id')
        click_el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class = "portlet_h_ac"]'))
        )
        self.driver.execute_script('arguments[0].click()', click_el)

        WebDriverWait(self.driver, 10).until(
            EC.staleness_of(el)
        )

        refresh_el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//div[@class="caption"]//div'
                                            '//div[@class="hookBlock join-group-link js-groupJoinButton"]'))
        )
        return refresh_el.get_attribute('id') != id

    def hint_search(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[@id = "hook_Block_ContentSearchWrapper"]'))
        )
        click_el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class = "h-mod filter_i"]'))
        )
        self.driver.execute_script('arguments[0].click()', click_el)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id = "hook_Block_ContentSearchWrapper"]'))
        )
        return True

    def hint_date_post(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//span[@class = "feed_date"]'))
        )
        el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class = "feed h-mod"]'))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(el).perform()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//span[@class = "feed_date"]'))
        )
        return True

    def exit(self):
        menu = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class = "ucard-mini_cnt_i ellip"]'))
        )
        self.driver.execute_script('arguments[0].click()', menu)

        exit_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@data-l="t,logoutCurrentUser"]'))
        )
        self.driver.execute_script('arguments[0].click()', exit_btn)

        confirm_exit_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@data-l="t,confirm"]'))
        )
        self.driver.execute_script('arguments[0].click()', confirm_exit_btn)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@class="button-pro __wide"]'))
        )
        return True

    def example_hash_tag(self):
        click_el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class = "h-mod filter_i"]'))
        )
        self.driver.execute_script('arguments[0].click()', click_el)

        hash_tag = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class = "h-mod tag"]'))
        )
        value = hash_tag.get_attribute("data-query")
        self.driver.execute_script('arguments[0].click()', hash_tag)

        WebDriverWait(self.driver, 10).until(
            EC.staleness_of(hash_tag)
        )

        input_hash_tag = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@class = "it search-input_it h-mod"]'))
        )
        return value == input_hash_tag.get_attribute("value")


class WaitItemDecrease(object):
    def __init__(self, xpath, init_cnt, driver):
        self._xpath = xpath
        self._init_cnt = init_cnt
        self._driver = driver

    def __call__(self, *args, **kwargs):
        try:
            cnt = len(self._driver.find_elements_by_xpath(self._xpath))
            return cnt != self._init_cnt - 1
        except StaleElementReferenceException:
            return False
