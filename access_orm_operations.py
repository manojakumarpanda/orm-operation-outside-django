from orm_operations import settings

from orm_operations_app.models import City


# django_orm_settings(settings)
def City_Entry():
    try:
        city=City.objects.filter(id=1).values()
        return city
    except Exception as e:
        print('ERROR is-->'+str(e))
        return str(e)
    
if __name__ == "__main__":
    city=City_Entry()
    print(city)