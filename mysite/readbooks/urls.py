from django.conf.urls import url
from readbooks import views

urlpatterns	= [
	url(r'^$', views.sitelogin, name='login_url'),
	url(r'^$', views.sitelogout, name='logout_url'),
	url(r'^register/$', views.register, name='signup_url'),
	url(r'^add/$', views.add, name='add_url'),
	url(r'^add_book/$', views.add_book, name='add_book_url'),
	url(r'^add_publisher/$', views.add_publisher, name='add_publisher_url'),
	url(r'^add_genre/$', views.add_genre, name='add_genre_url'),
	url(r'^add_group/$', views.add_group, name='add_group_url'),
	url(r'^add_author/$', views.add_author, name='add_author_url'),
	url(r'^settings/$', views.update_userinfo, name='user_settings_url'),
	url(r'^messages/$', views.messages, name='messages_url'),
	url(r'^add_review/$', views.add_review, name='add_review_url'), 
	url(r'^edit_review/$', views.edit_review, name='edit_review_url'),
	url(r'^home/$', views.readbooks_index, name='readbooks_index_url'),
	url(r'^search/$', views.search,	name='search_url'),
	url(r'^new/$', views.list_recent_models, name='list_recent_models_url'),
	url(r'^book/(?P<book_id>[0-9]+)/$', views.show_book_by_id, name='book_byID_url'),
	url(r'^author/(?P<author_id>[0-9]+)/$', views.show_author_by_id, name='author_byID_url'),
	url(r'^publisher/(?P<publisher_id>[0-9]+)/$', views.show_publisher_by_id, name='publisher_byID_url'),
	url(r'^reader/(?P<reader_id>[0-9]+)/$', views.show_reader_by_id, name='reader_byID_url'),
	url(r'^critic/(?P<critic_id>[0-9]+)/$', views.show_critic_by_id, name='critic_byID_url'),
	url(r'^group/(?P<group_id>[0-9]+)/$', views.show_group_by_id, name='group_byID_url'),
	url(r'^topic/(?P<topic_id>[0-9]+)/$', views.show_topic_by_id, name='topic_byID_url'),
	url(r'^review/(?P<review_id>[0-9]+)/$', views.show_review_by_id, name='review_byID_url'),
	url(r'^genre/(?P<genre_id>[0-9]+)/$', views.show_genre_by_id, name='genre_byID_url'),

]
