#7.4(p450)
from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name  = 'photo'

# URLパターンを登録する変数
urlpatterns = [
    # photoアプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),

    # 写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post'),

    # 写真投稿ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/', 
         views.PostSuccessView.as_view(), 
         name='post_done'),

    #  photos/<Categorysテーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path('photos/<int:category>',
        views.CategoryView.as_view(),
        name = 'photos_cat'
        ),

    # ユーザーの投稿一覧ページ
    # photos/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user: id値(int)}としてCategoryViewに渡される
    path('user-list/<int:user>',
        views.UserView.as_view(),
        name = 'user_list'
        ),

    # 詳細ページ
    # photo-detail/<Photo postsテーブルのid値>にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path ('photo-detail/<int:pk>',
    	views.DetailView.as_view(),
    	name = 'photo_detail'
    ),

    #マイページ
	#mypage/へのアクセスはMypageViewを実行
	path('mypage/', views.MypageView.as_view(), name = 'mypage'),

    #投稿写真の削除
    #photo/<Photo postsテーブルのid値>/delete/にマッチング
    #<int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('photo/<int:pk>/delete/',
        views.PhotoDeleteView.as_view(),
        name = 'photo_delete'
        ),
]


# #7.6(p474)
# from django.urls import path
# from . import views

# # URLパターンを逆引きできるように名前を付ける
# app_name  = 'photo'

# # URLパターンを登録する変数
# urlpatterns = [
#     # photoアプリへのアクセスはviewsモジュールのIndexViewを実行
#     path('', views.IndexView.as_view(), name='index'),

#     # 写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
#     path('post/', views.CreatePhotoView.as_view(), name='post')
#     # 投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
#     path('post_done/', 
#         views.PostSuccessView.as_view(), 
#         name='post_done'),

#     # カテゴリ一覧ページ
#     # photos/<Categorysテーブルのid値>にマッチング
#     # <int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
#     path('photos/,<int:category>',
#         views.CategoryView.as_view(),
#         name = 'photos_cat'
#         ),
# ]


#7.7(p481)
# from django.urls import path
# from . import views

# # URLパターンを逆引きできるように名前を付ける
# app_name  = 'photo'

# # URLパターンを登録する変数
# urlpatterns = [
#     # photoアプリへのアクセスはviewsモジュールのIndexViewを実行
#     path('', views.IndexView.as_view(), name='index'),

#     # 写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
#     path('post/', views.CreatePhotoView.as_view(), name='post')
#     # 写真投稿ページへのアクセスはviewsモジュールのPostSuccessViewを実行
#     path('post_done/', 
#         views.PostSuccessView.as_view(), 
#         name='post_done'),
#     # カテゴリ一覧ページ
#     # photos/<Categorysテーブルのid値>にマッチング
#     # <int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
#     path('photos/,<int:category>',
#         views.CategoryView.as_view(),
#         name = 'photos_cat'
#         ),

#     # ユーザーの投稿一覧ページ
#     # photos/<ユーザーテーブルのid値>にマッチング
#     # <int:user>は辞書{user: id値(int)}としてCategoryViewに渡される
#     path('user-list/<int:user>',
#         views.UserView.as_view(),
#         name = 'user_list'
#         ),
# ]


#7.8 (p489) 以下を追加する
# from django.urls import path
# from . import views

# # URLパターンを逆引きできるように名前を付ける
# app_name  = 'photo'

# # URLパターンを登録する変数
# urlpatterns = [
#     # photoアプリへのアクセスはviewsモジュールのIndexViewを実行
#     path('', views.IndexView.as_view(), name='index'),

#     # 写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
#     path('post/', views.CreatePhotoView.as_view(), name='post')
#     # 写真投稿ページへのアクセスはviewsモジュールのPostSuccessViewを実行
#     path('post_done/', 
#         views.PostSuccessView.as_view(), 
#         name='post_done'),
#     # カテゴリ一覧ページ
#     # photos/<Categorysテーブルのid値>にマッチング
#     # <int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
#     path('photos/,<int:category>',
#         views.CategoryView.as_view(),
#         name = 'photos_cat'
#         ),

#     # ユーザーの投稿一覧ページ
#     # photos/<ユーザーテーブルのid値>にマッチング
#     # <int:user>は辞書{user: id値(int)}としてCategoryViewに渡される
#     path('user-list/<int:user>',
#         views.UserView.as_view(),
#         name = 'user_list'
#         ),

    #詳細ページ
    # photo-detail/<Photo postsテーブルのid値>にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    # path ('photo-detail/<int:pk>',
    # 	views.DetailView.as_view(),
    # 	name = 'photo_detail'
    # ),
    # ]


# #7.9(p497)
# from django.urls import path
# from . improt views

# #URLパターンを逆引きできるように名前を付ける
# app_name = 'photo'

# #URLパターンを登録する変数
# urlpatterns = [
# 	#photoアプリへのアクセスはviewsモジュールのIndexViewを実行
# 	path('',views.IndexView.as_view(), name = 'index'),

# 	#写真投稿ページへのアクセスはviewモジュールのCreatePhotoViewを実行
# 	path('post/', views.CreatePhotoView.as_view(), name = 'post'),

# 	#投稿完了ページへのアクセスはviewsモジュールのpostSuccessViewを実行
# 	path('post done/', views.PostSuccessView.as_view(), name = 'post_done'),
	
# 	#カテゴリー一覧ページ
# 	#photo/<Categorysテーブルのid値>にマッチング
# 	#<int:category>は辞書{category:id値(int)}としてCategoryViewに渡される
# 	path('photos/<int:category>', views.CategoryView.as_view(), name = 'photos_cat'),

# 	#ユーザーの投稿一覧ページ
# 	#photos/<ユーザーテーブルのid値>にマッチング
# 	#<int.user>は辞書{user:id値(int)}としてCategoryViewに渡される
# 	path('user-list/<int:user>',
#        views.DatailView.as_view(),
#        name = 'photos_detail'
#        ),
# 	#マイページ
# 	#mypage/へのアクセスはMypageViewを実行
# 	path('mypage/', views.MypageView.as_view(), name = 'mypage'),
# ]


#7.10 p505
# from django.urls import path
# from . improt views

# #URLパターンを逆引きできるように名前を付ける
# app_name = 'photo'

# #URLパターンを登録する変数
# urlpatterns = [
# 	#photoアプリへのアクセスはviewsモジュールのIndexViewを実行
# 	path('',views.IndexView.as_view(), name = 'index'),

# 	#写真投稿ページへのアクセスはviewモジュールのCreatePhotoViewを実行
# 	path('post/', views.CreatePhotoView.as_view(), name = 'post'),

# 	#投稿完了ページへのアクセスはviewsモジュールのpostSuccessViewを実行
# 	path('post done/', views.PostSuccessView.as_view(), name = 'post_done'),
	
# 	#カテゴリー一覧ページ
# 	#photo/<Categorysテーブルのid値>にマッチング
# 	#<int:category>は辞書{category:id値(int)}としてCategoryViewに渡される
# 	path('photos/<int:category>', views.CategoryView.as_view(), name = 'photos_cat'),

# 	#ユーザーの投稿一覧ページ
# 	#photos/<ユーザーテーブルのid値>にマッチング
# 	#<int.user>は辞書{user:id値(int)}としてCategoryViewに渡される
# 	path('user-list/<int:user>', views.DatailView.as_view(), name = 'photos_detail'),
# 	#マイページ
# 	#mypage/へのアクセスはMypageViewを実行
# 	path('mypage/', 
#        views.MypageView.as_view(),
#        name = 'mypage'
#        ),
#   #投稿写真の削除
#   #photo/<Photo postsテーブルのid値>/delete/にマッチング
#   #<int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
#   path('photo/<int:pk>/delete/',
#       views.PhotoDeleteView.as_view(),
#       name = 'photo_delete'
#       ),
# ]