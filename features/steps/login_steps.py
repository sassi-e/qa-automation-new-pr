from behave import *

@given(u'login page displayed')
def login_page_loaded(context):
    context.login_page.load_page()

@when(u'user enter {username} and {password}')
def enter_username_input(context,username,password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when(u'user clicks on login button')
def click_login(context):
    context.login_page.click_login()

@then(u'{page} displayed')
def verify_page_display(context,page):
    if page=='overview':
        context.login_page.is_user_connected()
    else:
        context.login_page.is_user_connection_refused()