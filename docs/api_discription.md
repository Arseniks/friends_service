# Api description
## Endpoints:
### /swagger/
OpenAPI с swagger-ом
![swagger_endpoint_works.png](swagger_endpoint_works.png)
### /redoc/
OpenAPI с redoc-ом
![redos_endpoint_works.png](redos_endpoint_works.png)
### /api/v1/friend_list/
Список всех друзей пользователя
![friend_list_endpoint_works.png](friend_list_endpoint_works.png)
### /api/v1/friend_list/delete/{id}/
Удаление дружбы с пользователем
![friend_list_delete_endpoint_works.png](friend_list_delete_endpoint_works.png)
### /api/v1/pending_list/
Список всех отправленных и полученных запросов в друзья
![pending_list_endpoint_works.png](pending_list_endpoint_works.png)
### /api/v1/pending_list/accept/{id}
Одобрение входящей заявки в друзья и добавление дружбы с соответствующим пользователем
### /api/v1/pending_list/delete/{id}
Отклонение входящей заявки в друзья
![pending_list_delete_endpoint_works.png](pending_list_delete_endpoint_works.png)
### /api/v1/user_list/
Список всех пользователей с возможностью отправить им заявку в друзья
![user_list_e ndpoint_works.png](user_list_endpoint_works.png)
![user_list_endpoint_post_works.png](user_list_endpoint_post_works.png)
### /auth/.../
Стандартная регистрация, активации аккаунта, смена пароля и т.д.
![auth_endpoint_works.png](auth_endpoint_works.png)