"""sendmail2github URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url('', include('sendmail2github.apps.core.urls')),
    url('admin/', include('sendmail2github.apps.administration.urls')),
    url('account/', include('sendmail2github.apps.authentication.urls')),
    url('ticket/', include('sendmail2github.apps.ticket.urls')),
    url('mail/', include('sendmail2github.apps.mail.urls')),
]

print(settings.STATIC_URL)
print(settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
