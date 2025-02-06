from django.urls import path
from .views import *

urlpatterns = [
    # ************************ Vendor Url ************************
    path("society/", SocietyAPI.as_view()),
    path("society/<uuid:pk>/", SocietyUpdateAPI.as_view()),
    # ************************ Vendor Url ************************
    path("vendor/", VendorAPI.as_view()),
    path("vendor/<uuid:pk>/", VendorUpdateAPI.as_view()),
    # ************************ Contact Us Url ************************
    path("contactform/", ContactFormAPI.as_view()),
    path("contactform/<str:pk>/", ContactFormUpdateAPI.as_view()),
    path(
        "contactformfilter/<str:start_date>/<str:end_date>/<str:replied>/",
        ContactFormFilterAPI.as_view(),
    ),
    # ? ************************ Address Url ************************
    path("address/", AddressAPI.as_view()),
    path("addressaddmany/", AddressAddMultiple.as_view()),
    path("addressupdate/<str:pk>/", AddressUpdateAPI.as_view()),
    # ? ************************ Customer Url ************************
    path("customer/", CustomerAPI.as_view()),
    path("allcustomer/", AllCustomerDataAPI.as_view()),
    path("customerupdate/<str:pk>/", CustomerUpdateAPI.as_view()),
    # ? ************************ Services Url ************************
    path("services/", ServicesAPI.as_view()),
    path("services/<str:pk>/", ServicesUpdateAPI.as_view()),
    # ? ************************ Coupon Url ************************
    path("coupon/", CouponAPI.as_view()),
    path("allcoupon/", AllCouponDataAPI.as_view()),
    path("couponupdate/<str:pk>/", CouponUpdateAPI.as_view()),
    # ************************ Category Url ************************
    path("category/", CategoryAPI.as_view()),
    path("category/<uuid:pk>/", CategoryUpdateAPI.as_view()),
    # ************************ Product Url ************************
    path("product/", ProductAPI.as_view()),
    path("product/<uuid:pk>/", ProductUpdateAPI.as_view()),
    path("productbyid/<uuid:pk>/", ProductGetbyIDAPI.as_view()),
    path("product/<str:vendors>/<str:category>/", ProductFilterAPI.as_view()),
    path("productimage/", ProductImageAPI.as_view()),
    path("productimageupdate/<uuid:pk>/", ProductImageUpdateAPI.as_view()),
    path("productimageview/<uuid:pk>/", ProductDetailView.as_view()),
    # ************************ Order Url ************************
    path("order/", OrderAPI.as_view()),
    path("order/<uuid:pk>/", OrderUpdateAPI.as_view()),
    # ************************ Order Item Url ************************
    path("orderitem/", OrderItemAPI.as_view()),
    path("orderitem/<uuid:pk>/", OrderItemUpdateAPI.as_view()),
    # ************************ Ledger Url ************************
    path("ledger/", LedgerAPI.as_view()),
    path("ledger/<uuid:pk>/", LedgerUpdateAPI.as_view()),
]
