from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import get_coin_data_task

class CoinDataView(APIView):
    def post(self, request, *args, **kwargs):
        coin_acronyms = request.data.get('coins', [])
        if not coin_acronyms:
            return Response({"error": "No coin acronyms provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        task = get_coin_data_task.delay(coin_acronyms)
        return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)

    def get(self, request, *args, **kwargs):
        task_id = request.query_params.get('task_id', None)
        if not task_id:
            return Response({"error": "No task ID provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        task_result = get_coin_data_task.AsyncResult(task_id)
        if task_result.state == 'PENDING':
            return Response({"status": "Task is still running."}, status=status.HTTP_200_OK)
        elif task_result.state == 'SUCCESS':
            return Response({"status": "Task completed.", "data": task_result.result}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "Task failed."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
