import hashlib

def crack_sha1_hash(hash, use_salts = False):
    pw_arr = []
    file_text_arr("top-10000-passwords.txt", pw_arr)
    for p in pw_arr:
        hash_pass = hashlib.sha1(p)
        hash_pass_line = hash_pass.hexdigest()
        if hash_pass_line == hash:
            return p.decode("utf-8")
              
    if use_salts:
        pw_salts = []
        file_text_arr("known-salts.txt", pw_salts)
        for s in pw_salts:
            for pword in pw_arr:
                prepend_salt = hashlib.sha1(s + pword).hexdigest()
                append_salt = hashlib.sha1(pword + s).hexdigest()
                prepend_append_salt = hashlib.sha1(s + pword + s).hexdigest()
                if prepend_salt == hash:
                    return pword.decode("utf-8")
                elif append_salt == hash:
                    return pword.decode("utf-8")
                elif prepend_append_salt == hash:
                    return pword.decode("utf-8")
            pw_arr.append(pword)

    return "PASSWORD NOT IN DATABASE"
def file_text_arr(file_text, array):
    with open(file_text, "rb") as file:
        text = file.readline().strip()
        while text:
            array.append(text)
            text = file.readline().strip()
    #print(array)
