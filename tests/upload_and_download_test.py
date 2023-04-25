import allure
from pages.upload_and_download_page import UploadAndDownloadPage


@allure.feature('Upload and Download page')
class TestUploadAndDownload:
    @allure.title('Check upload file')
    def test_upload_file(self, driver):
        upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
        upload_download_page.open()
        file_name, result = upload_download_page.upload_file()
        assert file_name == result, "the file has not been uploaded"

    @allure.title('Check download file')
    def test_download_file(self, driver):
        upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
        upload_download_page.open()
        check = upload_download_page.download_file()
        assert check is True, "the file has not been downloaded"
