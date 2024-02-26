from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user_data = request.user.oidc_profile.id_data
    prompt_passkeys = user_data and not user_data.get("webauthn_passwordless", False)

    return render(request, "portal/index.html", {
        "prompt_passkeys": prompt_passkeys,
    })
