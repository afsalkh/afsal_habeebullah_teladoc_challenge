from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddUser:
	def __init__(self,driver):
		self.txt_firstname="//input[@name='FirstName']"
		self.txt_lastname = "//input[@name='LastName']"
		self.txt_username = "//input[@name='UserName']"
		self.txt_password = "//input[@name='Password']"
		self.radio_customer = "//input[@type='radio'and @value={}]"
		self.drp_role = "//select[@name='RoleId']"

		self.txt_email = "//input[@name='Email']"
		self.txt_phone = "//input[@name='Mobilephone']"
		self.btn_save = "//button[normalize-space()='Save']"
		self.driver=driver

	def set_firstname(self,value):
		self.driver.find_element(By.XPATH, self.txt_firstname).send_keys(value)

	def set_lastname(self,value):
		self.driver.find_element(By.XPATH, self.txt_lastname).send_keys(value)

	def set_username(self,value):
		self.driver.find_element(By.XPATH, self.txt_username).send_keys(value)

	def set_password(self,value):
		self.driver.find_element(By.XPATH, self.txt_password).send_keys(value)

	def set_customer(self,value):
		if value == "Company AAA":
			self.driver.find_element(By.XPATH, self.radio_customer.format("15")).click()
		elif value == "Company BBB":
			self.driver.find_element(By.XPATH, self.radio_customer.format("16")).click()

	def set_role(self,value):
		drop = self.driver.find_element(By.XPATH, self.drp_role)
		dropvalues = Select(drop)
		dropvalues.select_by_visible_text(value)

	def set_email(self,value):
		self.driver.find_element(By.XPATH, self.txt_email).send_keys(value)

	def set_phone(self,value):
		self.driver.find_element(By.XPATH, self.txt_phone).send_keys(value)

	def click_btn_save(self):
		self.driver.find_element(By.XPATH, self.btn_save).click()