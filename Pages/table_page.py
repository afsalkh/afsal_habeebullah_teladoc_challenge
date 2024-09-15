from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TablePage:
	def __init__(self,driver):
		self.btn_adduser="//button[normalize-space()='Add User' and @type='add']"
		self.tr_table = "//tbody/tr"
		self.td_table = "//tbody/tr[1]/td"
		self.td_username="//tbody/tr[{}]/td[3]"
		self.td_delete = "//tbody/tr[{}]/td[11]/button"
		self.delete_OK = "//button[normalize-space()='OK']"
		self.driver=driver
		self.wait=WebDriverWait(self.driver,10)

	def click_btn_adduser(self):
		#self.wait.until(expect)
		self.wait.until(EC.presence_of_element_located((By.XPATH, self.btn_adduser))).click()
		#self.driver.find_element(By.XPATH, self.btn_adduser).click()

	def get_table_rows_count(self):
		return len(self.driver.find_elements(By.XPATH,self.tr_table))

	def get_table_columns_count(self):
		return len(self.driver.find_elements(By.XPATH,self.td_table))

	def search_user(self,username=""):
		found=False
		row_count=self.get_table_rows_count()
		for row in range(1,row_count+1):
			if self.driver.find_element(By.XPATH, self.td_username.format(str(row))).text == username:
				found=True
				break
		return found

	def delete_user(self,username):
		found_and_deleted=False
		row_count=self.get_table_rows_count()
		for row in range(1,row_count+1):
			if self.driver.find_element(By.XPATH, self.td_username.format(str(row))).text == username:
				time.sleep(2)
				self.driver.find_element(By.XPATH, self.td_delete.format(str(row))).click()
				time.sleep(2)
				self.driver.find_element(By.XPATH, self.delete_OK).click()
				found_and_deleted=True
				break
		return found_and_deleted

