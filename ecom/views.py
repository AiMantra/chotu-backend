from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid 
from datetime import datetime
from .models import User, OTP
from .serializers import SendOTPSerializer, VerifyOTPSerializer


# Create your views here.

# *************************Society*******************************
class SocietyAPI(APIView):
    def get(self, request):
            query = Society.objects.all()
            serializer = SocietySerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
              

    def post(self, request):
        data = request.data
        serializer = SocietySerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SocietyUpdateAPI(APIView):
    def get(self, request, pk):
        try:
            query = Society.objects.get(id=pk)
            serializer = SocietySerializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Society.DoesNotExist:
            return Response({"error": "Society not found"}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk):
        data = request.data
        query = Society.objects.get(id=pk)
        serializer = SocietySerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = Society.objects.get(id=pk)
        query.delete()
        return Response(f"Society {query} Deleted")



# ***************user api****************

class UserAPI(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

    def put(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

    def delete(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            user.delete()
            return Response({"message": "User deleted"}, status=204)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

# *************************Vendor*******************************

class VendorAPI(APIView):
    def get(self, request):
        try:
            query = Vendors.objects.all()
            serializer = VendorSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Error occurred due to {e}"}, status=status.HTTP_400_BAD_REQUEST)
            

    def post(self, request):
        data = request.data
        serializer = VendorSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class VendorUpdateAPI(APIView):
    def get(self, request, pk):
        try:
            query = Vendors.objects.get(id=pk)
            serializer = VendorSerializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Vendors.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk):
        data = request.data
        query = Vendors.objects.get(id=pk)
        serializer = VendorSerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = Vendors.objects.get(pk=pk)
        query.delete()
        return Response(f"Vendor {query} Deleted")

    


#*********************************Vendorsproduct*************************************#
class VendorProductsAPI(APIView):
    def get(self, request):
        query = VendorProduct.objects.all()
        serializer = VendorProductSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = VendorProductSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class VendorProductUpdate(APIView):
    def get(self, request, pk):
        try:
            vendor = VendorProduct.objects.get(id=pk)
            serializer = VendorProductSerializer(vendor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Vendors.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk):
        try:
            query = VendorProduct.objects.get(id=pk)
            data = request.data
            serializer = VendorProductSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            vendorsproduct = VendorProduct.objects.get(id=pk)
            vendorsproduct.delete()
            return Response({"VendorsProduct Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )    
    
    


#***************************Vendor price****************************#


class Vendor_Product_PriceAPI(APIView):
    def get(self, request):
        queryset = Vendor_Product_Price.objects.all()
        serializer = Vendor_Product_PriceSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Vendor_Product_PriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Vendor_Product_PriceUpdateAPI(APIView):
    def get_object(self, pk):
        try:
            return Vendor_Product_Price.objects.get(pk=pk)
        except Vendor_Product_Price.DoesNotExist:
            return None

    def get(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({"error": "VendorProductPrice not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = Vendor_Product_PriceSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({"error": "VendorProductPrice not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = Vendor_Product_PriceSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({"error": "VendorProductPrice not found"}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"message": "VendorProductPrice deleted successfully"}, status=status.HTTP_200_OK)





#***************************BANK DETAILS API*******************#

class BankDetailsAPI(APIView):
    def get(self, request):
        query = BankDetails.objects.all()
        serializer = BankDetailsSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = BankDetailsSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class BankDetailsUpdate(APIView):
    def put(self, request, pk):
        try:
            query = BankDetails.objects.get(id=pk)
            data = request.data
            serializer = BankDetailsSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            bankDetails = BankDetails.objects.get(id=pk)
            bankDetails.delete()
            return Response({"BankDetails Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )




#*********************CONTACT FORM API******************************#


class ContactFormAPI(APIView):
    def get(self, request):
        try:

            query = ContactForm.objects.all()
            serializer = ContactFormSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occured Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = ContactFormSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactFormUpdateAPI(APIView):
    def put(self, request, pk):
        data = request.data
        query = ContactForm.objects.get(pk=pk)
        serializer = ContactFormSerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = ContactForm.objects.get(pk=pk)
        query.delete()
        return Response(f"ContactForm with ID {query} Deleted")


class ContactFormFilterAPI(APIView):
    def get(self, request, start_date, end_date, replied):
        query = ContactForm.objects.all()

        if start_date != "null":
            query = query.filter(reply_date__gte=start_date)

        if end_date != "null":
            query = query.filter(reply_date__lte=end_date)

        if replied != "null":
            query = query.filter(replied=replied)

        serializer = ContactFormSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#***************************************Address API***************************************************#
class AddressAPI(APIView):
    def get(self, request):
        try:
            query = Address.objects.all()
            serializer = AddressSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occured Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = AddressSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddressUpdateAPI(APIView):
    def put(self, request, pk):
        data = request.data
        query = Address.objects.get(pk=pk)
        serializer = AddressSerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = Address.objects.get(pk=pk)
        query.delete()
        return Response(f"Address {query} Deleted")


class AddressAddMultiple(APIView):
    def post(self, request):
        data = request.data
        serializer = AddressSerializer(data=data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

#**********************************************Customer API*****************************************#
class AllCustomerDataAPI(APIView):
    def get(self, request):
        try:
            query = Customer.objects.all()
            serializer = AllCustomerDataSerializer(Customer, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occured Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )
 

class CustomerAPI(APIView):
    def get(self, request):
        try:
            query = Customer.objects.all()
            serializer = CustomerSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occured Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = CustomerSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerUpdateAPI(APIView):
    def put(self, request, pk):
        data = request.data
        query = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = Customer.objects.get(pk=pk)
        query.delete()
        return Response(f"Customer {query} Deleted")

#**********************************Services API****************************************#

class ServicesAPI(APIView):
    def get(self, request):
        try:
            query = Services.objects.all()
            serializer = ServicesSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occured Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = ServicesSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServicesUpdateAPI(APIView):
    def put(self, request, pk):
        data = request.data
        query = Services.objects.get(pk=pk)
        serializer = ServicesSerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = Services.objects.get(pk=pk)
        query.delete()
        return Response(f"Services with ID {query} Deleted")
    




#********************************Coupon ***********************************#
class AllCouponDataAPI(APIView):
    def get(self, request):
        try:
            query = Coupon.objects.all()
            serializer = AllCouponDataSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occured Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )


class CouponAPI(APIView):
    def get(self, request):
        try:
            query = Coupon.objects.all()
            serializer = CouponSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occured Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = CouponSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CouponUpdateAPI(APIView):
    def put(self, request, pk):
        data = request.data
        query = Coupon.objects.get(pk=pk)
        serializer = CouponSerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = Coupon.objects.get(pk=pk)
        query.delete()
        return Response(f"Coupon {query} Deleted")


# Category CRUD APIs
class CategoryAPI(APIView):
    def get(self, request):
        try:
            query = Category.objects.all()
            serializer = CategorySerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryUpdateAPI(APIView):
    def put(self, request, pk):
        data = request.data
        query = Category.objects.get(pk=pk)
        serializer = CategorySerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = Category.objects.get(pk=pk)
        query.delete()
        return Response(f"Category {query} Deleted")
        
class SubCategoryAPI(APIView):
    def get(self, request):
        try:
            query = SubCategory.objects.all()
            serializer = SubCategorySerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = SubCategorySerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubCategoryUpdateAPI(APIView):
    def put(self, request, pk):
        data = request.data
        query = SubCategory.objects.get(pk=pk)
        serializer = SubCategorySerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = SubCategory.objects.get(pk=pk)
        query.delete()
        return Response(f"SubCategory {query} Deleted")
        


# Product CRUD APIs
class ProductAPI(APIView):
    def get(self, request):
        try:
            query = Product.objects.all()
            serializer = ProductSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = ProductSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductUpdateAPI(APIView):
    def put(self, request, pk):
        data = request.data
        query = Product.objects.get(pk=pk)
        serializer = ProductSerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = Product.objects.get(pk=pk)
        query.delete()
        return Response(f"Product {query} Deleted")
        


class ProductGetbyIDAPI(APIView):
    def get(self, request, pk):
        query = Product.objects.get(id=pk)
        serializer = ProductSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductFilterAPI(APIView):
    def get(self, request, vendors, category):
        query = Product.objects.all()

        if vendors != "null":
            query = query.filter(vendors=vendors)

        if category != "null":
            query = query.filter(category=category)

        serializer = ProductSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductImageAPI(APIView):
    def get(self, request):
        try:
            query = ProductImage.objects.all()
            serializer = ProductImageSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occured Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = ProductImageSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductImageUpdateAPI(APIView):
    def put(self, request, pk):
        data = request.data
        query = ProductImage.objects.get(pk=pk)
        serializer = ProductImageSerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = ProductImage.objects.get(pk=pk)
        query.delete()
        return Response(f"ProductImage with ID {query} Deleted")


class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.prefetch_related("product_images_product").get(
                pk=pk
            )

            serializer = ProductByProductSerializer(product)
            return Response(serializer.data)

        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
#CRUD OF PRODUCT VARIANT
class ProductVariantAPI(APIView):
    def get(self, request):
        try:
            query = ProductVariant.objects.all()
            serializer = ProductVariantSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = ProductVariantSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductVariantUpdateAPI(APIView):
    def put(self, request, pk):
        data = request.data
        query = ProductVariant.objects.get(pk=pk)
        serializer = ProductVariantSerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = ProductVariant.objects.get(pk=pk)
        query.delete()
        return Response(f"ProductVariant {query} Deleted")
    

# *******************Inventory********************

class InventoryAPI(APIView):
    def get(self, request):
        query = Inventory.objects.all()
        serializer = InventorySerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = InventorySerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class InventoryUpdate(APIView):
    def put(self, request, pk):
        try:
            query = Inventory.objects.get(id=pk)
            data = request.data
            serializer = InventorySerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            esslDetails = Inventory.objects.get(id=pk)
            esslDetails.delete()
            return Response({"Inventory Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

# *******************OrderAPI********************


class OrderAPI(APIView):
    def get(self, request):
        try:
            query = Order.objects.all()
            serializer = OrderSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = OrderSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            data = request.data
            query = Order.objects.get(pk=pk)
            serializer = OrderSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response("Order not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            query = Order.objects.get(pk=pk)
            query.delete()
            return Response(f"Order {query} Deleted", status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response("Order not found", status=status.HTTP_404_NOT_FOUND)

# *******************OrderItemAPI********************

class OrderItemAPI(APIView):
    def get(self, request):
        try:
            query = OrderItem.objects.all()
            serializer = OrderItemSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = OrderItemSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderItemUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            data = request.data
            query = OrderItem.objects.get(pk=pk)
            serializer = OrderItemSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except OrderItem.DoesNotExist:
            return Response("OrderItem not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            query = OrderItem.objects.get(pk=pk)
            query.delete()
            return Response(f"OrderItem {query} Deleted", status=status.HTTP_200_OK)
        except OrderItem.DoesNotExist:
            return Response("OrderItem not found", status=status.HTTP_404_NOT_FOUND)


# **************************Ledger CRUD API*****************************
class LedgerAPI(APIView):
    def get(self, request):
        try:
            query = Ledger.objects.all()
            serializer = LedgerSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = LedgerSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class LedgerUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            data = request.data
            query = Ledger.objects.get(pk=pk)
            serializer = LedgerSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Ledger.DoesNotExist:
            return Response("Ledger not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            query = Ledger.objects.get(pk=pk)
            query.delete()
            return Response(f"Ledger {query} Deleted", status=status.HTTP_200_OK)
        except Ledger.DoesNotExist:
            return Response("Ledger not found", status=status.HTTP_404_NOT_FOUND)

class WalletAPI(APIView):
    def get(self, request):
        try:
            wallets = Wallet.objects.all()
            serializer = WalletSerializer(wallets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        data = request.data
        serializer = WalletSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class WalletUpdateAPI(APIView):
    def put(self, request, pk):
        data = request.data
        try:
            wallet = Wallet.objects.get(pk=pk)
        except Wallet.DoesNotExist:
            return Response(f"Wallet with id {pk} does not exist.", status=status.HTTP_404_NOT_FOUND)

        serializer = WalletSerializer(wallet, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            wallet = Wallet.objects.get(pk=pk)
        except Wallet.DoesNotExist:
            return Response(f"Wallet with id {pk} does not exist.", status=status.HTTP_404_NOT_FOUND)
        wallet.delete()
        return Response(f"Wallet {pk} Deleted", status=status.HTTP_200_OK)





# **************************************Delivery API****************************************************** #  
class DeliveryAPI(APIView):
    def get(self, request):
        query = Delivery.objects.all()
        serializer = DeliverySerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = DeliverySerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeliveryUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = Delivery.objects.get(id=pk)
            data = request.data
            serializer = DeliverySerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            delivery = Delivery.objects.get(id=pk)
            delivery.delete()
            return Response({"Delivery Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )     
        
#***********************************Delivery-Agent*********************************************#


class DeliveryAgentAPI(APIView):
    def get(self, request):
        query = DeliveryAgent.objects.all()
        serializer = DeliveryAgentSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = DeliveryAgentSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeliveryAgentUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = DeliveryAgent.objects.get(id=pk)
            data = request.data
            serializer = DeliveryAgentSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            deliveryagent = DeliveryAgent.objects.get(id=pk)
            deliveryagent.delete()
            return Response({"DeliveryAgent Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )     
        

#***********************************PincodeServiceability*********************************************#
class PincodeserviceabilityAPI(APIView):
    def get(self, request):
        query = PincodeServiceability.objects.all()
        serializer = PincodeServiceabilitySerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = PincodeServiceabilitySerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class PincodeServiceabilityUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = PincodeServiceability.objects.get(id=pk)
            data = request.data
            serializer = PincodeServiceabilitySerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            pincodeserviceability = PincodeServiceability.objects.get(id=pk)
            pincodeserviceability.delete()
            return Response({"PincodeServiceability Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )     
        
# **********************************Cart*****************************************?


class CartAPI(APIView):
    def get(self, request):
        query = Cart.objects.all()
        serializer = CartSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = CartSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = Cart.objects.get(id=pk)
            data = request.data
            serializer = CartSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            cart = Cart.objects.get(id=pk)
            cart.delete()
            return Response({"Cart Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )     
# *************************CartItem*********************************

class CartItemAPI(APIView):
    def get(self, request):
        query = CartItem.objects.all()
        serializer = CartItemSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = CartItemSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartItemUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = CartItem.objects.get(id=pk)
            data = request.data
            serializer = CartItemSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            cartitem = CartItem.objects.get(id=pk)
            cartitem.delete()
            return Response({"CartItem Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )     
        



# *************************Payment*********************************
   

class PaymentAPI(APIView):
    def get(self, request):
        query = Payment.objects.all()
        serializer = PaymentSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = PaymentSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class PaymentUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = Payment.objects.get(id=pk)
            data = request.data
            serializer = PaymentSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            payment = CartItem.objects.get(id=pk)
            payment.delete()
            return Response({"Payment Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )             
        
        
        
# *************************LiveOrderTracking*********************************




class LiveOrderTrackingAPI(APIView):
    def get(self, request):
        query = LiveOrderTracking.objects.all()
        serializer =LiveOrderTrackingSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = LiveOrderTrackingSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class LiveOrderTrackingUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = LiveOrderTracking.objects.get(id=pk)
            data = request.data
            serializer = LiveOrderTrackingSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            liveordertracking = LiveOrderTracking.objects.get(id=pk)
            liveordertracking.delete()
            return Response({"LiveOrderTracking Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )             
        
        

        
# *************************Rating*********************************
   

class RatingAPI(APIView):
    def get(self, request):
        query = Rating.objects.all()
        serializer = RatingSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = RatingSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class RatingUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = Rating.objects.get(id=pk)
            data = request.data
            serializer = RatingSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            rating = Rating.objects.get(id=pk)
            rating.delete()
            return Response({"Rating Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )             
        
                
#**************************************************Review*************************************************
class ReviewAPI(APIView):
    def get(self, request):
        query = Review.objects.all()
        serializer = ReviewSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = ReviewSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = Review.objects.get(id=pk)
            data = request.data
            serializer = ReviewSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            review = Review.objects.get(id=pk)
            review.delete()
            return Response({"Review Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )        
    
#**************************************************CustomerSupport*************************************************
class CustomerSupportAPI(APIView):
    def get(self, request):
        query = CustomerSupport.objects.all()
        serializer = CustomerSupportSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = CustomerSupportSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerSupportUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = CustomerSupport.objects.get(id=pk)
            data = request.data
            serializer = CustomerSupportSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            customersupport = CustomerSupport.objects.get(id=pk)
            customersupport.delete()
            return Response({"CustomerSupport Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )                
            




#***********************************Return System**************************************

class ReturnSystemAPI(APIView):
    def get(self, request):
        query = ReturnSystem.objects.all()
        serializer = ReturnSystemSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = ReturnSystemSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReturnSystemUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = ReturnSystem.objects.get(id=pk)
            data = request.data
            serializer =ReturnSystem(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            returnsystem = ReturnSystem.objects.get(id=pk)
            returnsystem.delete()
            return Response({"ReturnSystem Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )                
            

#**********************************Product_Coin***************************************


class ProductCoinsAPI(APIView):
    def get(self, request):
        query = ProductCoins.objects.all()
        serializer = ProductCoinsSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = ProductCoinsSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCoinsUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = ProductCoins.objects.get(id=pk)
            data = request.data
            serializer = ProductCoinsSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            productcoin = ProductCoins.objects.get(id=pk)
            productcoin.delete()
            return Response({"ProductCoin Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        
#***************************************Voice Order Request**********************************************
class VoiceOrderRequestAPI(APIView):
    def get(self, request):
        query = VoiceOrderRequest.objects.all()
        serializer = VoiceOrderRequestSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = VoiceOrderRequestSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class VoiceOrderRequestUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = VoiceOrderRequest.objects.get(id=pk)
            data = request.data
            serializer =VoiceOrderRequestSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST, 
            )

    def delete(self, request, pk):
        try:
          voiceorderrequest= VoiceOrderRequest.objects.get(id=pk)
          voiceorderrequest .delete()
          return Response({"Voice Order Request Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )                
        
        
        
        
 # ***********************************Referral*****************************************************


class ReferralAPI(APIView):
    def get(self, request):
        query = Referral.objects.all()
        serializer = ReferralSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = ReferralSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReferralUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            query = Referral.objects.get(id=pk)
            data = request.data
            serializer = ReferralSerializer(query, data=data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        try:
            referral = Referral.objects.get(id=pk)
            referral.delete()
            return Response({"Referral Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": f"something went wrong, {e}",
                },
                status=status.HTTP_400_BAD_REQUEST,

            )
        



#**********************************OTP created and verify****************************
class SendOTPView(APIView):
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone_number']
            role = serializer.validated_data['role']

            user, created = User.objects.get_or_create(phone_number=phone, defaults={'user_roles': role})
            if not created and user.user_roles != role:
                return Response({'error': 'Role mismatch for this phone number.'}, status=status.HTTP_400_BAD_REQUEST)


            otp_instance = OTP.generate_otp(user)
            # In production, don't return OTP in response, send via SMS instead
            return Response({'message': 'OTP sent', 'otp': otp_instance.otp_code},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone_number']
            otp_input = serializer.validated_data['otp']

            try:
                user = User.objects.get(phone_number=phone)
            except User.DoesNotExist:
                return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

            latest_otp = user.otps.order_by('-created_at').first()
            # print(otp_input, latest_otp)
            if latest_otp and latest_otp.is_valid(otp_input):
                user.is_verified = True
                user.save()
                return Response({'message': 'OTP verified. Login successful.', 'user_id': user.id},status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid or expired OTP.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

