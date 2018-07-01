from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from models import Authenticate

def authenticate(function):
    def authenticate_wrap(request):
        userName = request.GET.get("user","")
        token = request.GET.get("token","")
        try:
            exist = Authenticate.objects.get(userName=userName,token = token,isActive=1)
            return function(request,exist)
        except ObjectDoesNotExist:
            return HttpResponse(' Unauthorized User or Token ', status=403)
    return authenticate_wrap