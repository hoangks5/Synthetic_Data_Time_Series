from instagrapi import Client

cl = Client()
cl.login('hoangkss5', 'Hoang22041999')

media_pk = cl.media_pk_from_url('https://www.instagram.com/p/CO8JG34gxc32HxGOxB-mw_FEQ59P8MbFDYTJAc0/')
media_path = cl.video_download(media_pk)




