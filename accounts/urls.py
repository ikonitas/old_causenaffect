from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^login/$','django.contrib.auth.views.login',{'template_name':'accounts/login.html'}),
    url(r'^logout/$','django.contrib.auth.views.logout', name="auth_logout"),
    url(r'^register/$','accounts.views.register',name="auth_register"),
    url(r'^profile/$','accounts.views.profile',name="profile"),
    )
