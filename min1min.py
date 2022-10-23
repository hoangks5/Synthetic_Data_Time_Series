from instagrapi import Client

cl = Client()
cl.login('hoangkss5', 'Hoang22041999')

user_id = cl.user_id_from_username("nobita_mi")
medias = cl.user_medias(user_id, 20)