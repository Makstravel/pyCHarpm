class MediaPlayer:

    def open(file, filename):
        file.filename = filename

    def play(file, filename):
        file.filename = filename
        print('Воспроизведение', filename)


media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open('filemedia1')
media2.open('filemedia2')
media1.play('filemedia1')
media2.play('filemedia2')