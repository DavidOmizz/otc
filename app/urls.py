from django.urls import path
from .views import CohortInfoListCreate, CohortInfoDetail

from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Cohort API",
        default_version='v1',
        description="API for managing cohort information",
    ),
    public=True,
)


urlpatterns = [
    path('api/cohort/', CohortInfoListCreate.as_view(), name='cohort-list-create'),
    path('api/cohort/<int:pk>/', CohortInfoDetail.as_view(), name='cohort-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]