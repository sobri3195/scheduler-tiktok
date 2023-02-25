from TikTokApi import TikTokApi
import datetime
import time

# login ke akun TikTok
api = TikTokApi.get_instance()
api.login(username='your_username', password='your_password')

# informasi video yang akan diposting
video_path = 'path/to/video.mp4'
caption = 'Ini adalah caption untuk video'
music_id = 'music_id_of_your_choice'

# waktu untuk posting video
scheduled_time = datetime.datetime(2023, 3, 1, 10, 30)  # contoh: 1 Maret 2023 jam 10:30 pagi

# tunggu hingga waktu posting tiba
while datetime.datetime.now() < scheduled_time:
    time.sleep(1)

# post video ke TikTok
api.upload_video(video_path, caption=caption, music_id=music_id)

# logout dari akun TikTok
api.logout()
