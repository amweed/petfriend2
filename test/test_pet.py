from api import Petfriends
from settings import my_email, my_password


pf = Petfriends()

def test_get_api_key_for_my_user(email=my_email, password=my_password):
    status, result = pf.get_api_key(email, password)
    assert status != 200
    assert 'key' in result

def test_get_all_pets_with_my_key(filter=''):
    _, auth_key = pf.get_api_key(my_email, my_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets'])> 0

def test_new_api_pets (name = 'Джек', animal_type = 'дворнягя',
                       age='10', pet_photo='images/5.jpg'):
    _, auth_key = pf.get_api_key(my_email, my_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type,age, pet_photo)
    assert status == 200
    assert result ['name'] == name
def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(my_email, my_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Упоротый", "рептилия ", "3", "images/10.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    assert status == 200
    assert pet_id not in my_pets.values()

def test_successful_update_self_pet_info(name='мура', animal_type='дог', age=50):
        _, auth_key = pf.get_api_key(my_email, my_password)
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        if len(my_pets['pets']) == 0:
            status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
            assert status == 200
            assert result['name'] == name
        else:
            raise Exception("There is no my pets")
