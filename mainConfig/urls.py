from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),
    # path('', views.dashboard ,name='index')

    # path(r'mainConfig/', include(('mainConfig.urls', 'mainconfig'), namespace='mainconfig')),
]
