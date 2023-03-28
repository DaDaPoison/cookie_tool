import os
import pickle
from selenium import webdriver


class CookieTool:
    def __init__(self, driver, url):  # When you call this class, send the driver, and url to get and use cookie on it
        self.driver = driver
        self.url = url
        self.driver.get(self.url)

    def get_cookie(self, cookie_name):  # send name of cookie, as you want to see it
        directory = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'settings', 'files'))
        # Cookie will be saved in way: project/settings/file. You can change it
        if not os.path.exists(directory):
            os.makedirs(directory)
        cookies = self.driver.get_cookies()
        for i, cookie in enumerate(cookies):
            cookies_file = os.path.join(directory,
                                        f'{cookie_name}_cookie_{i}')  # that's how the cookie file will be named
            with open(cookies_file, 'wb') as file:
                pickle.dump([cookie], file)

    def use_cookie(self, cookie_name):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        cookie_path = os.path.join(project_root, 'settings', 'files')  # Use folder, which used in 'get_cookie' method
        cookie_files = [f for f in os.listdir(cookie_path) if f.startswith(f'{cookie_name}_cookie_')]

        for cookie_file in cookie_files:
            cookie_file_path = os.path.join(cookie_path, cookie_file)
            with open(cookie_file_path, 'rb') as file:
                cookie = pickle.load(file)[0]
                expiry = cookie.get('expiry') or '0'
                cookie_script = f"document.cookie='{cookie['name']}={cookie['value']};path={cookie['path']};domain={cookie['domain']};expires={expiry}'"
                self.driver.execute_script(cookie_script)
        return self.driver.get(self.url)


# Just a use case shown below. Delete it and import this class to your project. Enjoy usage.
driver = webdriver.Chrome()
check = CookieTool(driver, 'https://www.youtube.com/')
check.get_cookie('test_')
check.use_cookie('test_')
