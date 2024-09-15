import pytest
import time


from conftest import env_to_run
from Utils.utils import ConfigLaunch
from Pages.add_user import AddUser
from Pages.table_page import TablePage

testdata=ConfigLaunch.get_test_data(env_to_run)['table_page']
endpoint="/angularjs-protractor/webtables/"


class TestTablePage:

    @pytest.mark.addgroup
    @pytest.mark.parametrize("userdata, found",testdata['add_user'])
    def test_table_add_and_search(self,conf,userdata,found):
        driver=conf.driver
        obj_adduser = AddUser(driver)
        obj_tablepage = TablePage(driver)

        driver.get(conf.base_url+endpoint)
        driver.maximize_window()
        obj_tablepage.click_btn_adduser()
        time.sleep(3)

        obj_adduser.set_firstname(userdata['firstname'])
        obj_adduser.set_lastname(userdata['lastname'])
        obj_adduser.set_username(userdata['username'])
        obj_adduser.set_password(userdata['password'])
        obj_adduser.set_customer(userdata['customer'])
        obj_adduser.set_role(userdata['role'])
        obj_adduser.set_email(userdata['email'])
        obj_adduser.set_phone(userdata['phone'])
        obj_adduser.click_btn_save()

        search_result=obj_tablepage.search_user(username=userdata['username'])
        assert search_result==found, "Did not find user:{} with email {} on search".format(userdata['username'],userdata['email'])

        time.sleep(3)
        driver.close()

    @pytest.mark.deletegroup
    @pytest.mark.parametrize("deleteuser, deleted", testdata['delete_user'])
    def test_table_delete_and_search(self,conf,deleteuser, deleted):
        driver = conf.driver
        obj_tablepage = TablePage(driver)

        driver.get(conf.base_url + endpoint)
        driver.maximize_window()
        time.sleep(3)

        user_deleted=obj_tablepage.delete_user(deleteuser)
        assert user_deleted, "User Not found/Not deleted:{}".format(deleteuser)

        search_result = obj_tablepage.search_user(username=deleteuser)
        assert search_result == False, "Deleted user {} still exist".format(deleteuser)

        time.sleep(3)
        driver.close()