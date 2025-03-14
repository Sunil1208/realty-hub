from django.urls import path

from apps.properties.views import (
    ListAgentsPropertiesApiView,
    ListAllPropertyApiView,
    PropertyDetailView,
    PropertySearchApiView,
    PropertyViewsApiView,
    create_property_api_view,
    delete_property_api_view,
    update_property_api_view,
    uploadPropertyImage,
)

urlpatterns = [
    path("all/", ListAllPropertyApiView.as_view(), name="all-properties"),
    path("agents/", ListAgentsPropertiesApiView.as_view(), name="agents-properties"),
    path("create/", create_property_api_view, name="property-create"),
    path("details/<slug:slug>/", PropertyDetailView.as_view(), name="property-detail"),
    path("update/<slug:slug>/", update_property_api_view, name="property-update"),
    path("delete/<slug:slug>/", delete_property_api_view, name="property-delete"),
    path("upload-image/", uploadPropertyImage, name="upload-image"),
    path("search/", PropertySearchApiView.as_view(), name="property-search"),
]
