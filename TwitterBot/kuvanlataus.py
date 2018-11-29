import urllib.request
QR_koodi = "Mattijateppo"
url = "https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl="+QR_koodi+"&choe=utf-8"
#file_name = "testia"
#file_path = 'images/'
#full_path = file_path + file_name + '.jpg'
urllib.request.urlretrieve(url, "Projects/Twitter/Images/testia.jpg")
