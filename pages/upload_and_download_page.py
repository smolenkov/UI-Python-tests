import base64
import os
import random

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from supplier.supplier import generated_file


class UploadAndDownloadPage(BasePage):
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')
    DOWNLOAD_FILE = (By.CSS_SELECTOR, 'a[id="downloadButton"]')

    @allure.step('upload file')
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.UPLOADED_RESULT).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    @allure.step('download file')
    def download_file(self):
        link = self.element_is_present(self.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'E:\automation_qa_course\filetest{random.randint(0, 999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file