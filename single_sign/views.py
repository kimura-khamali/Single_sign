# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as auth_login
# from django.contrib.auth.models import User
# from django.contrib import messages
# import json
# from authlib.integrations.django_client import OAuth
# from django.conf import settings
# from django.urls import reverse
# from urllib.parse import quote_plus, urlencode


# oauth = OAuth()
# oauth.register(
#     "auth0",
#     client_id=settings.AUTH0_CLIENT_ID,
#     client_secret=settings.AUTH0_CLIENT_SECRET,
#     client_kwargs={
#         "scope": "openid profile email",
#     },
#     server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
# )

# def auth_login_view(request):
#     """Redirects the user to the Auth0 login page."""
#     return oauth.auth0.authorize_redirect(
#         request, request.build_absolute_uri(reverse("callback"))
#     )

# # def callback(request):
# #     """Handles the callback from Auth0 after the user logs in."""
# #     token = oauth.auth0.authorize_access_token(request)
# #     user_info = token.get("userinfo")
    
# #     # Check if the user already exists
# #     user = User.objects.filter(email=user_info["email"]).first()
# #     if user:
# #         auth_login(request, user)  # Use the imported auth_login function
# #         return redirect(request.build_absolute_uri(reverse("index")))
# #     else:
# #         messages.error(request, "Account does not exist. Do you want to sign up?")
# #         return redirect("register")

# def callback(request):
#     """Handles the callback from Auth0 after the user logs in."""
#     token = oauth.auth0.authorize_access_token(request)
#     user_info = token.get("userinfo")
    
#     user = User.objects.filter(email=user_info["email"]).first()
#     if user:
#         auth_login(request, user)  
#         return redirect(request.build_absolute_uri(reverse("index")))
#     else:
#         messages.error(request, "Account does not exist. Do you want to sign up?")
#         return redirect("register")

# def register(request):
#     """Handles user registration."""
#     user_info = request.session.get("user_info")

    
#     if request.method == "POST":
#         username = user_info["email"]
#         password = User.objects.make_random_password()
        
       
#         user, created = User.objects.get_or_create(username=username, email=user_info["email"])
#         if created:
#             user.set_password(password)  
#             user.save()
#             auth_login(request, user)  
#             return redirect("index")
#         else:
#             messages.error(request, "User already exists.")
#             return redirect("login")
    
#     return render(request, "registration/register.html", {"user_info": user_info})

# def logout(request):
#     """Logs the user out and redirects to Auth0 logout."""
#     request.session.clear()
#     return redirect(
#         f"http://{settings.AUTH0_DOMAIN}/v2/logout?"
#         + urlencode(
#             {
#                 "returnTo": request.build_absolute_uri(reverse("index")),
#                 "client_id": settings.AUTH0_CLIENT_ID,
#             },
#             quote_via=quote_plus,
#         ),
#     )

# def index(request):
#     """Renders the index page."""
#     return render(
#         request,
#         "registration/index.html",
#         context={
#             "session": request.session.get("user"),
#             "pretty": json.dumps(request.session.get("user"), indent=4),
#         },
#     )




# # from django.shortcuts import render

# # # Create your views here.
# # from django.contrib.auth.forms import UserCreationForm
# # from django.urls import reverse_lazy
# # from django.views.generic import CreateView

# # class SignUpView(CreateView):
# #     form_class = UserCreationForm
# #     success_url = reverse_lazy('login')
# #     template_name = 'registration/signup.html'


# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as auth_login
# from django.contrib.auth.models import User
# from django.contrib import messages
# import json
# from authlib.integrations.django_client import OAuth
# from django.conf import settings
# from django.urls import reverse
# from urllib.parse import quote_plus, urlencode
# import logging

# # Set up logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# oauth = OAuth()
# oauth.register(
#     "auth0",
#     client_id=settings.AUTH0_CLIENT_ID,
#     client_secret=settings.AUTH0_CLIENT_SECRET,
#     client_kwargs={
#         "scope": "openid profile email",
#     },
#     server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
# )

# def auth_login_view(request):
#     """Redirects the user to the Auth0 login page."""
#     redirect_uri = request.build_absolute_uri(reverse("callback"))
#     return oauth.auth0.authorize_redirect(request, redirect_uri)

# def callback(request):
#     """Handles the callback from Auth0 after the user logs in."""
#     try:
#         token = oauth.auth0.authorize_access_token(request)
#         logger.debug(f"Received token: {token}")
#         user_info = token.get("userinfo")
#         logger.debug(f"User info: {user_info}")
        
#         user = User.objects.filter(email=user_info["email"]).first()
#         if user:
#             auth_login(request, user)
#             logger.info(f"User {user.email} logged in successfully")
#             return redirect(request.build_absolute_uri(reverse("index")))
#         else:
#             request.session["user_info"] = user_info
#             logger.info(f"New user {user_info['email']} redirected to registration")
#             return redirect("register")
#     except Exception as e:
#         logger.error(f"Error in callback: {str(e)}")
#         messages.error(request, "An error occurred during authentication. Please try again.")
#         return redirect("login")

# def register(request):
#     """Handles user registration."""
#     user_info = request.session.get("user_info")
    
#     if user_info is None:
#         messages.error(request, "User information not available. Please log in again.")
#         return redirect("login")

#     if request.method == "POST":
#         username = user_info.get("email")
#         password = User.objects.make_random_password()
        
#         user, created = User.objects.get_or_create(username=username, email=username)
        
#         if created:
#             user.set_password(password)
#             user.save()
#             auth_login(request, user)
#             del request.session["user_info"]
#             logger.info(f"New user {username} registered and logged in")
#             return redirect("index")
#         else:
#             messages.error(request, "User already exists.")
#             logger.warning(f"Attempted to register existing user: {username}")
#             return redirect("login")
    
#     return render(request, "registration/register.html", {"user_info": user_info})

# def logout(request):
#     """Logs the user out and redirects to Auth0 logout."""
#     request.session.clear()
#     logger.info("User logged out")
#     return redirect(
#         f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
#         + urlencode(
#             {
#                 "returnTo": request.build_absolute_uri(reverse("index")),
#                 "client_id": settings.AUTH0_CLIENT_ID,
#             },
#             quote_via=quote_plus,
#         ),
#     )

# def index(request):
#     """Renders the index page."""
#     return render(
#         request,
#         "registration/index.html",
#         context={
#             "session": request.session.get("user"),
#             "pretty": json.dumps(request.session.get("user"), indent=4),
#         },
#     )




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
import logging
import secrets
import string

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

oauth = OAuth()
oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def auth_login_view(request):
    """Redirects the user to the Auth0 login page."""
    redirect_uri = request.build_absolute_uri(reverse("callback"))
    return oauth.auth0.authorize_redirect(request, redirect_uri)

def callback(request):
    """Handles the callback from Auth0 after the user logs in."""
    try:
        token = oauth.auth0.authorize_access_token(request)
        logger.debug(f"Received token: {token}")
        user_info = token.get("userinfo")
        logger.debug(f"User info: {user_info}")
        
        user = User.objects.filter(email=user_info["email"]).first()
        if user:
            auth_login(request, user)
            logger.info(f"User {user.email} logged in successfully")
            return redirect(request.build_absolute_uri(reverse("index")))
        else:
            request.session["user_info"] = user_info
            logger.info(f"New user {user_info['email']} redirected to registration")
            return redirect("register")
    except Exception as e:
        logger.error(f"Error in callback: {str(e)}")
        messages.error(request, "An error occurred during authentication. Please try again.")
        return redirect("login")

def generate_random_password(length=12):
    """Generate a random password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))

def register(request):
    """Handles user registration."""
    user_info = request.session.get("user_info")
    
    if user_info is None:
        messages.error(request, "User information not available. Please log in again.")
        return redirect("login")

    if request.method == "POST":
        username = user_info.get("email")
        password = generate_random_password()
        
        user, created = User.objects.get_or_create(username=username, email=username)
        
        if created:
            user.set_password(password)
            user.save()
            auth_login(request, user)
            del request.session["user_info"]
            logger.info(f"New user {username} registered and logged in")
            return redirect("index")
        else:
            messages.error(request, "User already exists.")
            logger.warning(f"Attempted to register existing user: {username}")
            return redirect("login")
    
    return render(request, "registration/register.html", {"user_info": user_info})

def logout(request):
    """Logs the user out and redirects to Auth0 logout."""
    request.session.clear()
    logger.info("User logged out")
    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def index(request):
    """Renders the index page."""
    return render(
        request,
        "registration/index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )