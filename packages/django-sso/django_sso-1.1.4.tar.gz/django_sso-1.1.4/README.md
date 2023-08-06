# Django SSO (Single Sign-On) [Beta]

Realization of Single Sign-On for Django.

Supported Django versions:

- `3.*`
- `4.*`

*Recommended to force specify package version while installing package, this is for security and compatibility reasons.*



## How it works?

You should install this library to Django-project, that you planning will the authorization gateway (will keep all user accounts). Then add this library to services wich you wanna to authenticate via SSO gateway and thats all!



## Installation

### Server side

1) Add to `INSTALLED_APPS` variable the module named `django_sso`.`gateway`

```python
# project/settings.py
INSTALLED_APPS = [
    # ...
    'django_sso.sso_gateway',
]
```



2) Migrate the gateway models

```python
./manage.py migrate sso_gateway
```



3) Add urls to project:

```python
# project/urls.py

urlpatterns = [
	# ...,
	path('', include('django_sso.sso_gateway.urls')),
]
```



4) In the admin panel you can see now new section, named `SINGLE SIGN-ON`. And in `Subordinated services` you should be create new. With next fields:

- `Name` - Human name of service
- `Base url` - URL for redirects and access to service endpoints from server side. (Like https://your-service.example).
- `Enabled` - Are Subordinated service active. (Inactive services can’t communicate with server side and server side can’t communicate with it)
- `Token` - Automatically generated token you should past to `settings.py ` to your service to `SSO_TOKEN` variable.

Then server side is ready to use!



##### Optional settings

You also can provide the timeout of communication with subordinated services via variable in **settings.py**  named as `SSO_SUBORDINATE_COMMUNICATION_TIMEOUT`. This is timeout in seconds. Default value is 0.1s (100ms) per one service.



### Client side

When library attached to client side project. Admin login form will overridden with same view as `login/` in client side.

1) Add `django_sso`.`sso_service` to `INSTALLED_APPS` 

```python
# project/settings.py
INSTALLED_APPS = [
    # ...
    'django_sso.sso_service',
]
```



2) Add urls to service application

```python
# project/urls.py

urlpatterns = [
    # ...,
    path('', include('django_sso.sso_service.urls')),    
]
```



3) Setup settings variables

```python
# project/settings.py

# Django variable. URL for unlogged users. We redirect it to our view.
LOGIN_URL = '/login/'

# Specify SSO server base url
SSO_ROOT = 'https://sso.project.test'

# Specify application token obtained in SSO server in the admin panel
SSO_TOKEN = 'reej8Vt5kbCPJM9mZQqYsvfxC...'

# Overriding event acceptor class (OPTIONAL). For more details read "Overriding event acceptor in subordinated service" partition
SSO_EVENT_ACCEPTOR_CLASS = 'project.my_overrides.MySSOEventAcceptor'
```



## Structure

#### Server side urls

- `login/` - central login form (you can override template `django_sso/login.html`) 
- `logout/` - central logout view. Clear all sessions on all resources for user

Internal library urls (endpoints for services):

- `sso/obtain/` - obtain <u>authorization request</u>
- `sso/get/` - get SSO token information. (Is authorized for this token? Get user identity from token. etc..)
- `sso/make_used/` - after successful authentication on client side need to mark authorization request as used.
- `sso/deauthenticate/` - services sends deauthentication requests to SSO-server. SSO server broadcasts all services to deauthenticate user
- `__welcome/` - sample view for testing. For logged and unlogged users.



#### Client side urls

- `login/` - login form. Intermediate form. Obtains authentication request, and redirects to SSO server `/login`. 
- `logout/` - Does deauthenticate user and cast deauthentication event to SSO-server (to `sso/deauthenticate/` on server side).
- `sso/test/` - Page for test SSO mechanism immediately after install `django_sso`. When you open it in browser: If user are logged in - shows his name or redirect to SSO server and comes back after successful authentication.

Library urls for internal usage (endpoints for SSO-server side)

- `sso/event/` - Event acceptor from SSO server. Look to “**SSO with non-Django project / Accepting events**” section

- `sso/accept/` - User after successful authentication comes back. SSO-server redirect it to this URL for make Django authorization. Then after session is up - browser will redirect to the next URL.



## Overriding

### User and session storage

This library based on Django user subsystem and Django session subsystem. Also supports custom classes, but he must be based on classical Django classes (AbstractUser / AbstractBaseUser, etc..). This means that you have two ways. One: Do nothing, just install library to gateway/services and just use it. Two: Just pick own classes of user/session with based Django`s mechanisms.



### Overriding event acceptor in subordinated service

For event processing you must declare own class and inherit it from base class located in `django_sso.sso_service.backends.EventAcceptor`. Inheritance are necessary. Arguments must  absolutely matches for overridden methods. 

```python
# project/my_overrides.py
from django_sso.sso_service.backends import EventAcceptor

# In case, when you need to do something after deauthentication
class MyEventAcceptor(EventAcceptor):
    def deauthenticate(self, username):
        super().deauthenticate(usernmae)
        # Here you can do own actions after deauthentication

        
# In other case, when you need to override default behavior of class
class MyHardEventAcceptor(EventAcceptor):
    def deauthenticate(self, username):
        # Here you do own actions
```



Then next put path to this class to `settings.py`:

```python
SSO_EVENT_ACCEPTOR_CLASS = 'project.my_overrides.MySSOEventAcceptor'
```



## Debug & develop letter

All exceptions in SSO mechanism will be logged in console.



Often occurs error, when developer running gateway and services on same host that is unworkable situation. When it's happens - one service drops others cookies. For developing/runing on one machine multiple services you should separate by hosts. Write in your **hosts file** lines like next:

```hosts
127.0.0.1	sso_gateway
127.0.0.1	my_sso_service_1
127.0.0.1	my_sso_service_2
```
If after success authentication on the SSO-gateway system can't send event to subordinated service



If after redirect back to service after authorization in gateway occurs any error, user will redirected url `/?sso_broken_token=true` on subordinated service. 



If user redirected from subordinated service to gateway and successfully authorized on it but the gateway catch error while casting event - user will redirect to gateway page with url `/__welcome/fallback=true`.

# SSO with non-Django project

### Basics

Any external service must be registered in SSO server in admin panel section named  `SINGLE SIGN-ON / Subordinated services`. Then obtained token put to your script for next calls. And make service available directly for SSO server.

In next examples i’ll use sso_server.test meaning SSO server.

### Login page

When unlogged user visit login page. In backend need to requests SSO token from SSO server.

Fields:

`token` - obtained from first step from SSO server

`next_url` - relative URL, for redirect after successful authentication. (SSO will generate `Basic URL + Next URL` string and will forward user to it)

```bash
curl --request POST \
  --url http://sso_server.test/sso/obtain/ \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'X-Token: IJj42agKd231SzinVYqJMqq0buinM0wU' \
  --data token=AhTu1Un5zef3eRMGsL3y7AbDt2213123123f \
  --data next_url=/successful/page/
```



If all success, server will send to you authentication request token in JSON.

```json
{
	"token": "NmyWRItAye0gDxX7CZhOFs2HKZtT3xyfdrq14TU"
}
```

Then

1) Write token to session. (In PHP - $_SESSION.)

2) Redirect user to http://sso_server.test/login/?sso=NmyWRItAye0gDxX7CZhOFs2HKZtT3xyfdrq14TU. You should put obtained token to URL to “sso” parameter. User will be redirected to SSO login page. 

On SSO login page next:

If user successful logged on SSO, SSO sends to your event endpoint basic information about user. You should be it write to your authentication system. Then SSO server redirects user back to http://your_service.test/sso/accept/ where script recover SSO token from session and request information from SSO:

`token` - Service token.

`authentication_token` - SSO token, obtained in last step.

```bash
curl --request POST \
  --url http://sso_server.test/sso/get/ \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'X-Token: IJj42agKdp31SzinVYqJMqq0buinM0wU' \
  --data token=AhTu1Un5zef3eRMGsL3y7AbDt2213123123f \
  --data authentication_token=NmyWRItAye0gDxX7CZhOFs2HKZtT3xyfdrq14TU
```

If user already authorized. It will be returned next JSON:

```json
{
    "authenticated": True, // Are successful authenticated
    "user_identy": "somebody", // User identy (login or email...)
    "next_url": "/admin/" // URL for redirect after successful auth
}
```

In any other case:

```json
{
	"error": "Authentication request token is'nt exists"
}
```

If all success. You need to notify SSO server that token is used. Do next:

`token` - Service token.

`authentication_token` - SSO token, obtained in last step.

```bash
curl --request POST \
  --url http://sso_server.test/sso/make_used/ \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'X-Token: IJj42agKdp31SzinVYqJMqq0buinM0wU' \
  --data token=AhTu1Un5zef3eRMGsL3y7AbDt2213123123f \
  --data authentication_token=NmyWRItAye0gDxX7CZhOFs2HKZtT3xyfdrq14TU
```

And you will be get reply:

```json
{
	"ok": true
}
```



### Logout page

You first purge data from session. Then send to SSO server deauthentication event.

`token` - Service token.

`user_identy` - username or email field. Same, that you obtained from http://sso_server.test/sso/get/ at login procedure.

```bash
curl --request POST \
  --url http://127.0.0.1:5000/sso/deauthenticate/ \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'X-Token: IJj42agKdp31SzinVYqJMqq0buinM0wU' \
  --data token=AhTu1Un5zef3eRMGsL3y7AbDt2213123123f \
  --data user_identy=someody
```

Will respond with

```json
{
    "ok": true
}
```

Meaning, that deauthentication completed for all services.



### Accepting events

You should create `/sso/event/` endpoint in your project.

When user does successful authentication on SSO server, when user deleted or changed on SSO server, this library will send events to all subordinated services information about it. Account was deleted or marked as superuser or something other - SSO-server will emit events to all subordinated services. 

For example. When user is marked as superuser, SSO-server will cast event to all subordinated services to `sso/event/`. Next written all possible events. `type`, `token` fields in event data are permanent.

Events sends in JSON format via POST request.

##### Create/update account

When user created or updated or disabled or marked or unmarked as superuser also every time when user sign’s-in.

```json
{
    "type": "update_account", // Event name
    "token": "kaIrVNHF4msyLBJeaD4hSO", // Service token to authenticate SSO server
    "username": "somebody", // Value from username field
    
    // Next fields may be not included in event. Because user model on SSO don't have it
    "is_active": True, // Are active user now in SSO server
    "is_staff": True, // Are user is staff member
    "is_superuser": Trie, // Are user is superuser
}
```



##### Deauthenticate

When user somewhere requested deauthentication. This event will casts to all active subordinated services.

```json
{
    "type": "deauthenticate", // Event name
    "token": "kaIrVNHF4msyLBJeaD4hSO", // Service token to authenticate SSO server
    "username": "somebody" // Value from username field
}
```



For all requests to `sso/event/` subordinated service must be return next reponses

```json
// In successful case
{
    "ok": True
}

// Else if failured
{
    "error": "Error description here"
}
```



# To do and coming fixes | roadmap

- [ ] Automatic test on all Django versions while push to master branch
- [ ] Access control to subordinated services. Possibility to set available services for single user.
- [ ] Event queue for pushing events instead of immediately pushing. For stability and efficiency.
- [ ] Integration with popular frameworks and making plug-ins for popular languages. (I can accept your code as part of project - link to repository, for example.)
- [ ] Integrate with the Sentry
- [ ] Make auto testing

# Support

This library in alpha version. Don’t panic. This are draft version. Next time will uploaded fully documented clean version. Plans - make it more better and finish. Also i wanna to make later visual illustrations of logic.

You can support me via

Ethereum: 0x2BD7aA911861029feB08430EEB9a36DC9a8A14d2 (also accept any token :-) )

BUSD/BNB or any token (**BEP20**):  0x74e47ae3A26b8C5cD84d181595cC62723A1B114E



Any thinks: me@davidhaker.ru

With love to open source!