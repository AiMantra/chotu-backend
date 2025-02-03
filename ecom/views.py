from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class SocietyAPI(APIView):
    def get(self, request):
        try:
            query = Society.objects.all()
            serializer = SocietySerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = SocietySerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SocietyUpdateAPI(APIView):
    def put(self, request, pk):
        data = request.data
        query = Society.objects.get(pk=pk)
        serializer = SocietySerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = Society.objects.get(pk=pk)
        query.delete()
        return Response(f"Society {query} Deleted")


class VendorAPI(APIView):
    def get(self, request):
        try:
            query = Vendors.objects.all()
            serializer = VendorSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        data = request.data
        serializer = VendorSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class VendorUpdateAPI(APIView):
    def put(self, request, pk):
        data = request.data
        query = Vendors.objects.get(pk=pk)
        serializer = VendorSerializer(query, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        query = Vendors.objects.get(pk=pk)
        query.delete()
        return Response(f"Vendor {query} Deleted")


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


class AllCustomerDataAPI(APIView):
    def get(self, request):
        try:
            query = Customer.objects.all()
            serializer = AllCustomerDataSerializer(query, many=True)
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
    def get(self, request, vendors):
        query = Product.objects.all()

        if vendors != "null":
            query = query.filter(vendors=vendors)

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


# Ledger CRUD API
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
