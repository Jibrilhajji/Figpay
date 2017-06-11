"""figpay_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
# from drf_auto_endpoint.router import router
from rest_framework.routers import DefaultRouter
from facing.views import UploadList

from payments.endpoints import ConsumerPaymentEndpoint, VendorPaymentEndpoint
from payments.views import ConsumerPaymentViewset, VendorPaymentViewset
from signup.views import signup, SignupSuccess

router = DefaultRouter()
# router.register(endpoint=ConsumerPaymentEndpoint, url='payments/consumers')
# router.register(endpoint=VendorPaymentEndpoint, url='payments/vendors')
router.register("consumer/payments", ConsumerPaymentViewset, base_name='consumer_payments')
router.register("vendor/payments", VendorPaymentViewset, base_name='vendor_payments')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/token-auth/', views.obtain_auth_token),
    url(r'^api/', include(router.urls)),
    url(r'^api/recognize', UploadList.as_view()),

    url(r'^signup/success$', SignupSuccess.as_view(), name='signup-success'),
    url(r'^$', signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL_LOCAL,
                                                                       document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'FigPay Backend'

import kairos_face

kairos_face.settings.app_id = settings.KAIROS_APP_ID
kairos_face.settings.app_key = settings.KAIROS_APP_KEY
