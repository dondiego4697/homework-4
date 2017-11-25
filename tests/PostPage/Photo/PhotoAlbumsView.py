# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.Component.Component import Component
from tests.PostPage.Photo.PhotoAlbum import PhotoAlbumView


class PhotoAlbumsView(Component):
    XPATH = '//div[@class = "modal-new_center"]'

    def __init__(self, driver, elem):
        super(PhotoAlbumsView, self).__init__(driver)
        self._elem = elem
        self._first_album_cover = self._get_first_album_cover()

    def open_first_album(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self._first_album_cover)
        )
        self._first_album_cover.click()
        album_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PhotoAlbumView.XPATH))
        )
        return PhotoAlbumView(self.driver, album_elem)

    def _get_first_album_cover(self):
        album_cover_xpath = '//img[@class="photo-sc_i_cnt_a_img va_target"]'
        return self._get_element_by_xpath(album_cover_xpath)