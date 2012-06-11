from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^login/$','accounts.views.mine_login',{'template_name':'accounts/login.html'},name="login"),
    url(r'^logout/$','django.contrib.auth.views.logout', name="auth_logout"),
    url(r'^register/$','accounts.views.register',name="auth_register"),
    url(r'^profile/$','accounts.views.profile',name="profile"),
    url(r'^forget/$','accounts.views.forget',name="forget_password"),
    )
