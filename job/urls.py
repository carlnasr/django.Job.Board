from django.urls import path
from . import views

urlPatterns =[
    path('' ,views.job_list),
    path('<int=id>'. views.job_detail)

]
