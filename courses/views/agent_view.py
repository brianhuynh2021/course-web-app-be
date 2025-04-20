from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai
import os


class AgentCourseView(APIView):
    def post(self, request):
        prompt = request.data.get("goal", "Give a compliment for user")
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-search-preview-2025-03-11",
                messages=[
                    {"role": "system", "content": "You are AI assistant"},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response.choices[0].message.content.strip()
            return Response({"result": result})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
