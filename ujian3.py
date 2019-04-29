'''
No 3
API Berita
'''
import requests
url = 'https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey=3f9db5730444468fad1d57aeb332890d'


print('Selamat datang, mau tahu berita apa hari ini?\n'
  '[1] Berita seputar teknologi\n'
  '[2] Berita seputar bisnis\n'
  '[3] Berita seputar olahraga\n'
  '[4] Berita seputar kesehatan\n'
  '[5] Berita seputar science\n')

pilih = int(input('Ketik pilihan Anda [1/2/3/4/5] : '))
if pilih == 1:
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey=3f9db5730444468fad1d57aeb332890d'
elif pilih == 2:
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey=3f9db5730444468fad1d57aeb332890d'
elif pilih == 3:
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey=3f9db5730444468fad1d57aeb332890d'
elif pilih == 4:
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey=3f9db5730444468fad1d57aeb332890d'
elif pilih == 5:
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey=3f9db5730444468fad1d57aeb332890d'


berita = requests.get(url)


for i in range(5):
    print(i+1, ' - ', berita.json()['articles'][i+1]['title'])

print()

