# sttring = open('selected_movies.html', 'r+')
# print(sttring.read().replace('пїЅ',' '))
# sttring.write('banana')
# sttring.write(sttring.read().replace('пїЅ',' '))

file = 'selected_movies - на 80.html'

with open(file, "r") as f:
    file_data = f.read()
    print(file_data)
raw = open(file, "w")
raw.write(file_data.replace('пїЅ',' '))