from instagrapi import Client

cl = Client()
cl.login('hoangkss5', 'Hoang22041999')

media_pk = cl.media_pk_from_url('https://www.instagram.com/p/ChLtDjWjmQ9/')
media_path = cl.video_download(media_pk)




