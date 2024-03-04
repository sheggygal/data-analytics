from utils import unzip_with_7z

zip_file_path = 'congrats.7z'  # keep as is
dest_path = '.'  # keep as is

find_me = ''  # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW

lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

for first_letter in lowercase_letters:
    for second_letter in lowercase_letters:
        find_me = first_letter + second_letter
        secret_password = find_me + 'bcmpda'

        success = unzip_with_7z(zip_file_path, dest_path, secret_password)

        if success:
            print("Password found:", secret_password)
            break
    else:
        continue
    break
