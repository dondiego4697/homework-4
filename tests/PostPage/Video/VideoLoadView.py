# -*- coding: utf-8 -*-

from tests.Component.Component import Component


class VideoLoadView(Component):
    XPATH = '//div[@class="modal-new_center"]'

    def __init__(self, driver, elem):
        super(VideoLoadView, self).__init__(driver)
        self._elem = elem
        self._first_video_cover = self._get_first_video_cover()

    def attach_first_video(self):
        self._get_first_video_cover().click()

    def _get_first_video_cover(self):
        video_xpath = '//div[@class="ugrid_cnt"]//img[@class="vid-card_img"]'
        return self._get_element_by_xpath(video_xpath)
