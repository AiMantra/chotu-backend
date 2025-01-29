from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class VendorAPI(APIView):
    def get(self, request):
        try:
            query = Vendors.objects.all()
            serializer = VendorSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST)

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
            return Response(f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST)

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
            return Response(f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST)

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

class OrderAPI(APIView):
    def get(self, request):
        try:
            query = Order.objects.all()
            serializer = OrderSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST)

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
            return Response(f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST)

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
            return Response(f"Error Occurred Due to {e}", status=status.HTTP_400_BAD_REQUEST)

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
