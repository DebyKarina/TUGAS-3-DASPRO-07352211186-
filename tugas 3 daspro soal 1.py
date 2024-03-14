# Data login yang disimpan dalam bentuk nested dictionary
data_login = {
    'mahasiswa1': {
        'password': 'mahasiswa1',
        'email': 'mahasiswa1@example.com'
    },
    'mahasiswa2': {
        'password': 'mahasiswa2',
        'email': 'mahasiswa2@example.com'
    },
    'mahasiswa3': {
        'password': 'mahasiswa3',
        'email': 'mahasiswa3@example.com'
    },
    'mahasiswa4': {
        'password': 'mahasiswa4',
        'email': 'mahasiswa4@example.com'
    },
    'mahasiswa5': {
        'password': 'mahasiswa5',
        'email': 'mahasiswa5@example.com'
    },
    'mahasiswa6': {
        'password': 'mahasiswa6',
        'email': 'mahasiswa6@example.com'
    },
    'mahasiswa7': {
        'password': 'mahasiswa7',
        'email': 'mahasiswa7@example.com'
    },
    'mahasiswa8': {
        'password': 'mahasiswa8',
        'email': 'mahasiswa8@example.com'
    },
    'mahasiswa9': {
        'password': 'mahasiswa9',
        'email': 'mahasiswa9@example.com'
    },
    'mahasiswa10': {
        'password': 'mahasiswa10',
        'email': 'mahasiswa10@example.com'
    }
}

def login(username, password):
    if username in data_login and data_login[username]['password'] == password:
        print("Login berhasil.")
        print("Email yang terdaftar:", data_login[username]['email'])
    else:
        print("Login gagal. Periksa kembali username dan password Anda.")

# Contoh penggunaan
username_input = input("Masukkan username: ")
password_input = input("Masukkan password: ")
login(username_input, password_input)

