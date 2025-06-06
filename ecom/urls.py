from django.urls import path
from .views import *
from .views import SendOTPView, VerifyOTPView

urlpatterns = [
    # ************************ Society Url ************************
    path("society/", SocietyAPI.as_view()),
    path("society/<uuid:pk>/", SocietyUpdateAPI.as_view()),


    # ************************ Vendor Url ************************
    path("vendor/", VendorAPI.as_view()),
    path("vendor/<str:pk>/", VendorUpdateAPI.as_view()),
    path("vendorproduct/",VendorProductsAPI.as_view()),
    path("vendorproduct/<uuid:pk>/", VendorProductUpdate.as_view()),
    path("vendorprice/",Vendor_Product_PriceAPI.as_view()),
    path("vendorprice/<uuid:pk>/", Vendor_Product_PriceUpdateAPI.as_view()),
    



    # ************************ Contact Form Url ************************
    path("contactform/", ContactFormAPI.as_view()),
    path("contactform/<str:pk>/", ContactFormUpdateAPI.as_view()),
    path("contactformfilter/<str:start_date>/<str:end_date>/<str:replied>/",ContactFormFilterAPI.as_view(),),


    # ? ************************ Address Url ************************
    path("address/", AddressAPI.as_view()),
    path("addressaddmany/", AddressAddMultiple.as_view()),
    path("addressupdate/<str:pk>/", AddressUpdateAPI.as_view()),


    #  ************************ Customer Url ************************
    path("customer/", CustomerAPI.as_view()),
    path("allcustomer/", AllCustomerDataAPI.as_view()),
    path("customerupdate/<str:pk>/", CustomerUpdateAPI.as_view()),   
    
    #  ************************ CustomerSupport******************
    path("customersupport/", CustomerSupportAPI.as_view()),
    path("customersupportupdate/<str:pk>/", CustomerSupportUpdateAPI.as_view()),



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
    path("subcategory/", SubCategoryAPI.as_view()),
    path("subcategory/<uuid:pk>/", SubCategoryUpdateAPI.as_view()),


    # ************************ Product Url ************************
    path("product/", ProductAPI.as_view()),
    path("product/<uuid:pk>/", ProductUpdateAPI.as_view()),
    path("productbyid/<uuid:pk>/", ProductGetbyIDAPI.as_view()),
    path("product/<str:vendors>/<str:category>/", ProductFilterAPI.as_view()),
    path("productimage/", ProductImageAPI.as_view()),
    path("productimageupdate/<uuid:pk>/", ProductImageUpdateAPI.as_view()),
    path("productimageview/<uuid:pk>/", ProductDetailView.as_view()),
    path("productvariant/", ProductVariantAPI.as_view()),
    path("productvariant/<uuid:pk>/",ProductVariantUpdateAPI.as_view()),


    # ************************ Order Url ************************
    path("order/", OrderAPI.as_view()),
    path("order/<uuid:pk>/", OrderUpdateAPI.as_view()),


    # ************************ Order Item Url ************************
    path("orderitem/", OrderItemAPI.as_view()),
    path("orderitem/<uuid:pk>/", OrderItemUpdateAPI.as_view()),


    # ************************ Ledger Url ************************
    path("ledger/", LedgerAPI.as_view()),
    path("ledger/<uuid:pk>/", LedgerUpdateAPI.as_view()),


    # ************************ Wallet Url ************************
    path("wallet/", WalletAPI.as_view()),
    path("wallet/<uuid:pk>/", WalletUpdateAPI.as_view()),  


    # ************************ Bank Details ************************
    path("bankdetails/",BankDetailsAPI.as_view()),
    path("bankdetails/<uuid:pk>/",BankDetailsUpdate.as_view()),
    
    # ************************ Inventory API ************************
    path("inventory/",InventoryAPI.as_view()),
    path("inventory/<uuid:pk>/",InventoryUpdate.as_view()),



    # ************************  Delivery API ************************    
    path("delivery/",DeliveryAPI.as_view()),
    path("delivery/<uuid:pk>/",DeliveryUpdateAPI.as_view()),
    
    # ************************  Delivery Agent API ************************    
    path("deliveryagent/",DeliveryAgentAPI.as_view()),
    path("deliveryagent/<uuid:pk>/",DeliveryAgentUpdateAPI.as_view()),


   #**********************PincodeServiceability**************************
    path("PincodeServiceability/",PincodeserviceabilityAPI.as_view()),
    path("PincodeServiceability/<uuid:pk>/",PincodeServiceabilityUpdateAPI.as_view()),
    


    #********************** CART **************************
    path("Cart/",CartAPI.as_view()),
    path("cart/<uuid:pk>/",CartUpdateAPI.as_view()),
    path("cartitem/",CartItemAPI.as_view()),
    path("cartitem/<uuid:pk>/",CartItemUpdateAPI.as_view()),



    #**********************Payment**************************
    path("payment/",PaymentAPI.as_view()),
    path("payment/<uuid:pk>/",PaymentUpdateAPI.as_view()),


    #**********************LiveOrderTrackingAPI**************************
    path("liveordertracking/",LiveOrderTrackingAPI.as_view()),
    path("liveordertracking/<uuid:pk>/",LiveOrderTrackingUpdateAPI.as_view()),


    #**********************Rating**************************
    path("rating/",RatingAPI.as_view()),
    path("rating/<uuid:pk>/",RatingUpdateAPI.as_view()),
    
    #**********************ReviewAPI**************************
    path("review/",ReviewAPI.as_view()),
    path("review/<uuid:pk>/",ReviewUpdateAPI.as_view()),
    
         

    #***********************Return System***********************
    path("returnsystem/",ReturnSystemAPI.as_view()),
    path("returnsystem/<uuid:pk>/",ReturnSystemUpdateAPI.as_view()),


    #*****************ProductCoinsAPI*************************
    path("productcoins/",ProductCoinsAPI.as_view()),
    path("productcoins/<uuid:pk>/",ProductCoinsUpdateAPI.as_view()),


    
    
    #***********************VoiceOrderRequestAPI*********************
    path("voiceorderrequest/",VoiceOrderRequestAPI.as_view()),
    path("voiceorderrequest/<uuid:pk>/",VoiceOrderRequestUpdateAPI.as_view()),



    # **************************Referral*****************************
    path("referral/",ReferralAPI.as_view()),
    path("referral/<uuid:pk>/",ReferralUpdateAPI.as_view()),


    #**********************otp verify***********************************
    path('send-otp/', SendOTPView.as_view()),
    path('verify-otp/', VerifyOTPView.as_view()),

    # ***************************userapi*******************************
    path('users/', UserAPI.as_view()),
    path('users/<uuid:pk>/', UserDetailAPI.as_view()),
    
]


