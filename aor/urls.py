from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.generic.base import TemplateView
from pybb.views import ProfileEditView
from registration.views import register
from aor.forms import AORProfileForm, RegistrationFormCaptcha
from aor.views import Search
from profiles.views import UserTopics, UserPosts

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'),
        name='home'),
    #    url(r'^accounts/login/$', login, name="auth_login",
    #        kwargs=dict(authentication_form=AuthenticationFormCaptcha)),
    url(r'^accounts/register/$', register,
        kwargs=dict(form_class=RegistrationFormCaptcha,
            backend='registration.backends.default.DefaultBackend'),
        name="registration_register"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^forum/profile/edit/$',
        ProfileEditView.as_view(form_class=AORProfileForm),
        name='pybb:edit_profile'),
    url(r'^forum/users/(?P<username>[^/]+)/topics/$', UserTopics.as_view(),
        name='user_topics'),
    url(r'^forum/users/(?P<username>[^/]+)/posts/$', UserPosts.as_view(),
        name='user_posts'),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),
#    url(r'^search/$', Search.as_view(), name='search'),
    url(r'^news/', include('pybb4news.urls', namespace='news')),
    url(r'^blogs/', include('pybb4blogs.urls', namespace='blogs')),
    #    url(r'^comments/', include('django.contrib.comments.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots.txt$', include('robots.urls')),
    url(r'^captcha/', include('captcha.urls')),
    # IRC Mibbit widget
    url(r'^irc/$',
        TemplateView.as_view(template_name='irc_mibbit_widget.html'),
        name='irc'),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
