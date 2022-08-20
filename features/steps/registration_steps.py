from behave import *

from Utilities import Configreader
from features.PageObjects.RigistrationPage import RegistrationPage as RP


@given(u'I navigate to the URL qa.way2automation.com')
def step_impl(context):
    context.reg = RP(driver=context.driver)
    context.reg.open(Configreader.config_reader("basic info","testsiteurl"))


@when(u'I enter name as "<name>"')
def step_impl(context,name):
    RP.setName(name)


@then(u'I enter phonenum as "<phonenum>"')
def step_impl(context,phonenum):
    RP.setphoneNum(phonenum)


@then(u'I enter email as "<email>"')
def step_impl(context,email):
    RP.setemail(email)


@then(u'I enter password as "<username>"')
def step_impl(context,username):
    RP.setusername()


@then(u'I enter password as "<password>"')
def step_impl(context,password):
    RP.setpassword(password)
