alien_url = 'https://teachersandtrees.files.wordpress.com/2015/02/littlecutealien.jpg'

alien = Image(alien_url, 150, 150)
alien.width *= 0.3
alien.height *= 0.3

def onStep():
    alien.centerX += 1
    alien.centerY +=1
