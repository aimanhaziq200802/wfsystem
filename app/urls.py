from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *  


urlpatterns = [
        
    path('all_quotations/', views.all_quotations, name='all_quotations'),
    path('create_request/', views.create_request, name='create_request'),
    path('quotation_list/', views.quotation_list, name='quotation_list'),
    path('quotation/<int:qid>/', views.quotation_details, name='quotation_details'),

    path('verification_queue/', views.verification_queue, name='verification_queue'),
    path('quotation/<int:qid>/verify/', views.quotation_verify, name='quotation_verify'),
    path('verification_history/', views.verification_history, name='verification_history'),
    
    path('approval_queue/', views.approval_queue, name='approval_queue'),
    path('quotation/<int:qid>/approve/', views.quotation_approve, name='quotation_approve'),
    path('approval_history/', views.approval_history, name='approval_history'),
    
    path('final_approval_queue/', views.final_approval_queue, name='final_approval_queue'),
    path('quotation/<int:qid>/final_approve/', views.final_approve, name='final_approve'),
    path('final_approval_history/', views.final_approval_history, name='final_approval_history'),

    path('finance_queue/', views.finance_queue, name='finance_queue'),
    path('quotation/<int:qid>/finance_approve/', views.finance_approve, name='finance_approve'),
    path('finance_history/', views.finance_history, name='finance_history'),

    path('export_quotation/<int:qid>/', export_quotation_to_excel, name='export_quotation_to_excel'),

]
