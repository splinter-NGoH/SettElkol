from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _




User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    
    class Meta(admin_forms.UserChangeForm):
        model = User
        fields = "__all__"


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm):
        model = User
        fields = "__all__"
        error_messages = {
            "username": {
                "unique": _("This username has already taken"),
            },
        }
class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
