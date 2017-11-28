# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.Component.Component import Component


class VideoLoadView(Component):
    XPATH = '//div[@class="modal-new_center"]'

    def __init__(self, driver, elem):
        super(VideoLoadView, self).__init__(driver)
        self._elem = elem
        self._first_video_cover = self._get_first_video_cover()

    def attach_first_video(self):
        video_cover = self._get_first_video_cover()
        video_cover.click()

    def _get_first_video_cover(self):
        video_xpath = '//div[@class="ugrid_cnt"]//img[@class="vid-card_img"]'
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, video_xpath))
        )
