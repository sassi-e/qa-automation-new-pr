from behave import *

@given(u'user connected and elements displayed')
def user_connected_to_site(context):
    context.login_page.is_user_connected()
    context.product_page.is_product_displayed()

@when(u'user chooses product from page')
def product_chosen(context):
    context.product_page.scroll_to_product(context.product_name)

@when(u'user clicks on button to add product to cart')
def product_to_cart(context):
    context.product_page.click_on_add_product_to_cart(context.product_name)

# @then (u'button changes')
# def button_text_changed(context)