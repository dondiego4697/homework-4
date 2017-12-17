# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from tests.Component.Component import Component


class AboutInfoComponent(Component):
    XPATH = '//div[contains(@class, "wide-profile")]'

    def __init__(self, driver, element):
        super(AboutInfoComponent, self).__init__(driver)
        self._element = element
        self._link_to_edit_profile = self._get_link_to_edit_profile()
        fav_music_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, FavouriteMusicSection.XPATH))
        )
        self.fav_music_section = FavouriteMusicSection(self.driver, fav_music_elem)

    def edit_profile(self):
        self._link_to_edit_profile.click()
        edit_profile_frame_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, EditProfileFrame.XPATH))
        )
        return EditProfileFrame(self.driver, edit_profile_frame_elem)

    def get_user_name(self):
        name_xpath = '//div[contains(@class, "compact-profile")]'
        return self._get_element_by_xpath(name_xpath).text.split()[0]

    def get_user_birth_date(self):
        date_xpath = '//div[@data-type="AGE"]'
        return self._get_element_by_xpath(date_xpath).text.split()[0]

    def get_gender_string(self):
        gender_xpath = '//span[contains(@class, "user-profile_i_t_inner")]'
        return self._get_element_by_xpath(gender_xpath).text

    def get_birth_city(self):
        city_xpath = '//div[@data-type="TEXT"]'
        return self._get_element_by_xpath(city_xpath).text

    def _get_link_to_edit_profile(self):
        link_xpath = '//a[contains(@class, "user-profile_lk-o")]'
        return self._get_element_by_xpath(link_xpath)


class EditProfileFrame(Component):
    XPATH = '//div[contains(@class, "modal-new_cnt")]'

    def __init__(self, driver, element):
        super(EditProfileFrame, self).__init__(driver)
        self._element = element
        self._input_name_field = self._get_input_name_field()
        self._save_confirm_btn = self._get_save_confirm_btn()
        self._cancel_btn = self._get_cancel_btn()
        self._bday_selector = self._get_bday_selector()
        self._gender_radio_m = self._get_mgender_radio_btn()
        self._gender_radio_f = self._get_fgender_radio_btn()
        self._birth_city_input = self._get_birth_city_input()

    def change_user_name(self, text):
        self._input_name_field.clear()
        self._input_name_field.send_keys(text)

    def change_user_bday(self, day):
        select = Select(self._bday_selector)
        select.select_by_visible_text(day)

    def change_birth_city(self, text):
        self._birth_city_input.clear()
        self._birth_city_input.send_keys(text)
        suggestion_xpath = '//ul[contains(@id, "citySugg_SuggestItems")]/li[1]'
        suggestion = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, suggestion_xpath))
        )
        suggestion.click()

    def cancel_changes(self):
        self._cancel_btn.click()

    def confirm_changes(self):
        self._save_confirm_btn.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.XPATH))
        )

    def set_gender_m(self):
        self._gender_radio_m.click()

    def set_gender_f(self):
        self._gender_radio_f.click()

    def _get_input_name_field(self):
        input_xpath = '//input[contains(@name, "fr.name")]'
        return self._get_element_by_xpath(input_xpath)

    def _get_save_confirm_btn(self):
        btn_xpath = '//input[contains(@name, "button_savePopLayerEditUserProfileNew")]'
        return self._get_element_by_xpath(btn_xpath)

    def _get_cancel_btn(self):
        btn_cancel_xpath = '//a[@id = "nohook_modal_close"]'
        return self._get_element_by_xpath(btn_cancel_xpath)

    def _get_bday_selector(self):
        selector_xpath = '//select[contains(@name, "fr.bday")]'
        return self._get_element_by_xpath(selector_xpath)

    def _get_mgender_radio_btn(self):
        mbtn_xpath = '//input[contains(@id, "field_gender_1")]'
        return self._get_element_by_xpath(mbtn_xpath)

    def _get_fgender_radio_btn(self):
        fbtn_xpath = '//input[contains(@id, "field_gender_2")]'
        return self._get_element_by_xpath(fbtn_xpath)

    def _get_birth_city_input(self):
        input_xpath = '//input[contains(@name, "fr.citySugg_SearchInput")]'
        return self._get_element_by_xpath(input_xpath)


class FavouriteMusicSection(Component):
    XPATH = '//div[contains(@id, "hook_Block_UserProfileInterests")]/div[2]'

    def __init__(self, driver, element):
        super(FavouriteMusicSection, self).__init__(driver)
        self._element = element
        self._music_input_field = self._get_music_input_field()

    def add_fav_music(self, text):
        actions = ActionChains(self.driver)
        actions.move_to_element(self._music_input_field)
        actions.click(self._music_input_field)
        actions.send_keys(text)
        actions.perform()
        add_btn_xpath = '//input[contains(@name, "btnSubmitMusic")]'
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, add_btn_xpath))
        )
        add_btn.click()

    def del_last_added_music(self):
        del_btn_xpath = '//ul[contains(@class, "interests_ul")]/li[1]/div/a'
        del_btn = self._get_element_by_xpath(del_btn_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(del_btn).click().perform()

    def get_last_added_music_string(self):
        return self._get_last_added_music().text

    def _get_music_input_field(self):
        input_xpath = '//div[contains(@id, "_intSuggCntMusic")]'
        return self._get_element_by_xpath(input_xpath)

    def _get_add_btn(self):
        input_xpath = '//input[contains(@name, "btnSubmitMusic")]'
        return self._get_element_by_xpath(input_xpath)

    def _get_last_added_music(self):
        music_xpath = '//ul[contains(@class, "interests_ul")]/li[1]/a'
        return self._get_element_by_xpath(music_xpath)
