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
    """
    API View to retrieve the history of operations.

    Methods:
        get(self, request, *args, **kwargs): Retrieves the history of operations.
    """

    def get(self, request, *args, **kwargs):
        """
        Retrieves the history of operations based on query parameters.

        Args:
            request: Request object containing query parameters.

        Returns:
            Response: JSON response containing the history of operations.
        """

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
        return Response({'history': response_data.data})


class EvaluateOperationView(APIView):
    """
    API View to evaluate an arithmetic expression.

    Methods:
        post(self, request, *args, **kwargs): Evaluates an arithmetic expression.
    """

    def post(self, request, *args, **kwargs):
        """
        Evaluates an arithmetic expression and stores the result in the operation history.

        Args:
            request: Request object containing the expression to be evaluated.

        Returns:
            Response: JSON response containing the evaluated result or an error message.
        """

        params = OperationSerializer(data=request.data)
        params.is_valid(raise_exception=True)

        expression = params.validated_data.get('expression', '')
        try:
            result = evaluate_expression(expression)
            history = Operation.objects.create(expression=expression, result=result)
            return Response({'result': result}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
