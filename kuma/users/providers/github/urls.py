from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from .provider import KumaGitHubProvider

urlpatterns = default_urlpatterns(KumaGitHubProvider)
