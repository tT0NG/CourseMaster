from models import Account

def clean_data():
    for user in Account.objects.all():
        user.courses_pack += user.courses_used - user.courses_caught
        user.courses_used = user.courses_caught
        user.courses_list = '[]'
        user.save()