from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextInputSerializer
from .lda_utils import get_topic_distribution

class LDATopicView(APIView):
    def post(self, request):
        serializer = TextInputSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            topic_probs = get_topic_distribution(text)
            response = [
                {"topic": topic + 1, "probability": round(prob * 100, 2)}
                for topic, prob in topic_probs
            ]
            return Response({"topics": response})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
