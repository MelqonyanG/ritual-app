from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from algebraic_operations.operations.models import Operation
from algebraic_operations.operations.serializers import (
    OperationSerializer,
    HistoryRequestSerializer,
    HistorySerializer,
)
from algebraic_operations.operations.utils.evaluator import evaluate_expression 


class OperationsHistoryView(APIView):

    def get(self, request, *args, **kwargs):
        params = HistoryRequestSerializer(data=request.query_params)
        params.is_valid(raise_exception=True)

        page_size = params.validated_data.get('page_size')
        page_number = params.validated_data.get('page_number')

        operations_history = Operation.objects.all()

        if page_number and page_size:
            paginator = Paginator(operations_history, page_size)
            
            if page_number <= paginator.num_pages:
                operations_history = paginator.get_page(page_number).object_list
            else:
                operations_history = []

        response_data = HistorySerializer(operations_history, many=True)
        return Response(
            {
                'history': response_data.data,
            }
        )


class EvaluateOperationView(APIView):

    def post(self, request, *args, **kwargs):
        params = OperationSerializer(data=request.data)
        params.is_valid(raise_exception=True)

        expression = params.validated_data.get('expression', '')
        result = evaluate_expression(expression)
        history = Operation.objects.create(expression=expression, result=result)
        return Response({'result': result}, status=status.HTTP_201_CREATED)
