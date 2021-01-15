from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout_then_login
from django.contrib.auth import views as auth_views
app_name = 'auctions'

urlpatterns = [
    path('create/', views.create, name='create'),
    # path('myauctions/', views.my_auctions, name='my_auctions'),
    # Example: /auctions/
    path('', views.auctions, name='auctions'),
    # Example: /auctions/5/
    path('<int:auction_id>/', views.detail, name='detail'),
    # Example: /auctions/5/results/
    # path('<int:auction_id>/results/', views.results, name='results'),
    # Example: /auctions/5/bid/
    path('<int:auction_id>/bid/', views.bid, name='bid'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='auctions/password-reset/password_reset.html',
             subject_template_name='auctions/password-reset/password_reset_subject.txt',
             email_template_name='auctions/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='auctions/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='auctions/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='auctions/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
