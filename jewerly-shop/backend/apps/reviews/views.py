from django.shortcuts import redirect
from .forms import ReviewForm
from .models import Reviews
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class ReviewCreateView(APIView):
    # def post(self, request):
    #     if request.method == 'POST':
    #         form  = ReviewForm(request.POST)
    #         if form.is_valid():
    #             form.save()

    #     # Верните ответ
    #     return Response({'message': 'Отзыв успешно создан'})
    def post(self, request):
        redirect('/admin')
        review_data = request.data

    # Создайте экземпляр модели отзыва
        review = Reviews(
            username=review_data['name'],
            text=review_data['text'],
            product=review_data['product'],
            created_at=review_data['created_at'],
            rate=review_data['rate'],
        )

    # Сохраните отзыв в базе данных
        review.save()

        return Response({'message': 'Отзыв успешно создан'})