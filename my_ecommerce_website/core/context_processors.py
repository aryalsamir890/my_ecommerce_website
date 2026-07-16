from cart.models import cart

def count(request):
    if request.user.is_authenticated:
        value=cart.objects.filter(user=request.user).count()
        return {'count_data':value}
    else:
        return {'count_data':0}
    