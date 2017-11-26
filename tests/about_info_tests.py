# -*- coding: utf-8 -*-

from tests.main import Tests


class AboutInfoTests(Tests):
    NAME = 'testName'
    BDAY = '7'
    GENDER_M = 'Родился'
    GENDER_F = 'Родилась'
    CITY_LIPETSK_EN = 'Lipetsk'
    CITY_MOSCOW_EN = 'Moscow'
    CITY_LIPETSK_RUS = 'Липецк'
    CITY_MOSCOW_RUS = 'Москва'
    MUSIC = 'latina'

    def test_change_name(self):
        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        user_name_before = about_info_component.get_user_name()
        edit_profile_frame = about_info_component.edit_profile()
        edit_profile_frame.change_user_name(self.NAME)
        edit_profile_frame.confirm_changes()

        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        user_name_after = about_info_component.get_user_name()
        self.assertEqual(user_name_after, self.NAME)

        edit_profile_frame = about_info_component.edit_profile()  # возвращаем имя обратно
        edit_profile_frame.change_user_name(user_name_before)
        edit_profile_frame.confirm_changes()

    def test_change_without_confirm(self):
        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        user_name_before = about_info_component.get_user_name()
        edit_profile_frame = about_info_component.edit_profile()
        edit_profile_frame.change_user_name(self.NAME)
        edit_profile_frame.cancel_changes()

        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        user_name_after = about_info_component.get_user_name()
        self.assertEqual(user_name_after, user_name_before)

    def test_change_date_of_birth(self):
        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        birth_date_before = about_info_component.get_user_birth_date()
        edit_profile_frame = about_info_component.edit_profile()
        edit_profile_frame.change_user_bday(self.BDAY)
        edit_profile_frame.confirm_changes()

        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        birth_date_after = about_info_component.get_user_birth_date()
        self.assertEqual(birth_date_after, self.BDAY)

        edit_profile_frame = about_info_component.edit_profile()  # возвращаем имя обратно
        edit_profile_frame.change_user_bday(birth_date_before)
        edit_profile_frame.confirm_changes()

    def test_change_gender(self):
        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        edit_profile_frame = about_info_component.edit_profile()
        edit_profile_frame.set_gender_f()
        edit_profile_frame.confirm_changes()

        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        gender_string = about_info_component.get_gender_string()
        self.assertEqual(gender_string.encode('utf-8'), self.GENDER_F)

        # для чистоты эксперимента пробуем поставить другой пол
        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        edit_profile_frame = about_info_component.edit_profile()
        edit_profile_frame.set_gender_m()
        edit_profile_frame.confirm_changes()

        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        gender_string = about_info_component.get_gender_string()
        self.assertEqual(gender_string.encode('utf-8'), self.GENDER_M)

    def test_change_city(self):
        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        edit_profile_frame = about_info_component.edit_profile()
        edit_profile_frame.change_birth_city(self.CITY_LIPETSK_EN)
        edit_profile_frame.confirm_changes()

        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        birth_city_curr = about_info_component.get_birth_city()
        self.assertEqual(birth_city_curr.encode('utf-8'), self.CITY_LIPETSK_RUS)

        # повторяем ещё раз с другим городом
        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        edit_profile_frame = about_info_component.edit_profile()
        edit_profile_frame.change_birth_city(self.CITY_MOSCOW_EN)
        edit_profile_frame.confirm_changes()

        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        birth_city_curr = about_info_component.get_birth_city()
        self.assertEqual(birth_city_curr.encode('utf-8'), self.CITY_MOSCOW_RUS)

    def test_add_favourite_music(self):
        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        about_info_component.fav_music_section.add_fav_music(self.MUSIC)

        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        last_added_music = about_info_component.fav_music_section.get_last_added_music_string()
        self.assertEqual(last_added_music, self.MUSIC)

    def test_del_favourite_music(self):
        # сначала добавляем музыку, которую собираемся удалять
        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        about_info_component.fav_music_section.add_fav_music(self.MUSIC)

        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        about_info_component.fav_music_section.del_last_added_music()

        about_page = self._to_about_page()
        about_info_component = about_page.get_about_info_component()
        last_added_music = about_info_component.fav_music_section.get_last_added_music_string()
        self.assertNotEqual(last_added_music, self.MUSIC)
