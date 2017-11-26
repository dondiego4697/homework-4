# coding=utf-8
from tests.main import Tests


class ProfileTests(Tests):
    def test_share_now(self):
        profile_page = self._to_profile_page()
        albums_view = profile_page.get_avatar_change_view()
        photos = albums_view.get_not_selected_photos()
        photos[0].select()
        profile_page.submit_avatar_change()

    # Проверить возможность загрузки фото на страницу (не при создании записи, а по кнопке Фото)
    def test_upload_photo_by_photo_btn(self):
        profile_page = self._to_profile_page()
        profile_page.upload_photo()
        profile_page = self._to_profile_page()
        last_post = profile_page.get_last_post()
        is_contains_image = last_post.contains_image()
        self.assertTrue(is_contains_image)

    # Проверить возможность загрузки видео на страницу (не при создании записи, а по кнопке Видео)
    def test_upload_video_by_video_btn(self):
        profile_page = self._to_profile_page()
        profile_page.upload_video()
        profile_page = self._to_profile_page()
        last_post = profile_page.get_last_post()
        is_contains_video = last_post.contains_video()
        self.assertTrue(is_contains_video)
