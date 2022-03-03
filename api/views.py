from django.http import Http404
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import IngredientSerializer
from .models import Ingredient
import openai


def gpt3(stext):
    stext = f'Full description of {stext}?'
    openai.api_key = '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'
    gpt_response = openai.Completion.create(
        engine='text-curie-001',
        prompt=stext,
            temperature=0.9,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    )
    description = gpt_response.choices[0]['text']
    return description


class IngredientsView(APIView):

    def get_object(self, name):
        try:
            if Ingredient.objects.get(name=name).description == "":
                description = gpt3(name)[2:]
                Ingredient.objects.filter(name=name).update(description=description)
                return Ingredient.objects.get(name=name)
            return Ingredient.objects.get(name=name)
        except Ingredient.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        ingredient = self.get_object(name=name)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)


