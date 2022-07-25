from django.urls import path

from . import views


app_name = "polls"
urlpatterns= [
     #ex: /polls/
    path("" , views.IndexViews.as_view() , name="index"),
#ex: /polls/detail
    path("<int:pk>/detail" , views.DetailView.as_view() , name="detail"),
#ex: /polls/results
    path("<int:pk>/results/" , views.ResultView.as_view() , name="results"),
#ex: /polls/vote
    path("<int:question_id>/vote/" , views.vote , name="vote")

]