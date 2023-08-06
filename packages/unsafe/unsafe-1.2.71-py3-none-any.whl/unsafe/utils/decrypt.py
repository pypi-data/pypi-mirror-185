import base64
from unsafe.utils.encrypt import Encryptor
from unsafe.utils.strings import wordlist
from typing import Optional, Union


class Decrypter:
    """
    This is abc Class for Text/File Decryption.
    """

    def __init__(self) -> None:
        ...

    def text_decrypt(self, hash: Optional[str | bytes], word: Optional[str | list] = wordlist,
                     encode: Optional[str] = None, hash_method: str = "MD5", **kwargs) -> Union[str, bytes]:
        """
        function to return encrypted string.
        """

        hash_method = hash_method.lower()

        if kwargs == {} and hash_method == 'caesar':
            count = 1
        elif kwargs != {} and hash_method == 'caesar':
            if 'count' in kwargs:
                try:
                    count = int(kwargs['count'])
                except:
                    raise ValueError('count must be integer !')
            else:
                raise ValueError(
                    f'The argument(s) {[i for i in kwargs.keys()]} not defined !')

        if kwargs != {} and hash_method != 'caesar':
            raise ValueError('This Hash Method Have Not Kwargs...')

        if type(word) in [int, float, bool, bytes]:
            word = str(word)

        if hash_method in ['shake128', 'shake256']:
            count = len(hash)

        encryptor = Encryptor()

        if type(word) == str:
            if hash_method == 'md5':
                if encode:
                    if str(encryptor.text_encrypt(word, encode, "MD5")) == hash:
                        return True
                    else:
                        return False
                else:
                    if str(encryptor.text_encrypt(words=word, hash_method="MD5")) == hash:
                        return True
                    else:
                        return False
            elif hash_method == 'sha1':
                if encode:
                    if str(encryptor.text_encrypt(word, encode, "SHA1")) == hash:
                        return True
                    else:
                        return False
                else:
                    if str(encryptor.text_encrypt(words=word, hash_method="SHA1")) == hash:
                        return True
                    else:
                        return False
            elif hash_method == 'sha256':
                if encode:
                    if str(encryptor.text_encrypt(word, encode, "SHA256")) == hash:
                        return True
                    else:
                        return False
                else:
                    if str(encryptor.text_encrypt(words=word, hash_method="SHA256")) == hash:
                        return True
                    else:
                        return False
            elif hash_method == 'sha224':
                if encode:
                    if str(encryptor.text_encrypt(word, encode, "SHA224")) == hash:
                        return True
                    else:
                        return False
                else:
                    if str(encryptor.text_encrypt(words=word, hash_method="SHA224")) == hash:
                        return True
                    else:
                        return False
            elif hash_method == 'sha384':
                if encode:
                    if str(encryptor.text_encrypt(word, encode, "SHA384")) == hash:
                        return True
                    else:
                        return False
                else:
                    if str(encryptor.text_encrypt(words=word, hash_method="SHA384")) == hash:
                        return True
                    else:
                        return False
            elif hash_method == 'sha512':
                if encode:
                    if str(encryptor.text_encrypt(word, encode, "SHA512")) == hash:
                        return True
                    else:
                        return False
                else:
                    if str(encryptor.text_encrypt(words=word, hash_method="SHA512")) == hash:
                        return True
                    else:
                        return False
            elif hash_method == 'sha3-224':
                if encode:
                    if str(encryptor.text_encrypt(word, encode, "SHA3-224")) == hash:
                        return True
                    else:
                        return False
                else:
                    if str(encryptor.text_encrypt(words=word, hash_method="SHA3-224")) == hash:
                        return True
                    else:
                        return False
            elif hash_method == 'sha3-256':
                if encode:
                    if str(encryptor.text_encrypt(word, encode, "SHA3-256")) == hash:
                        return True
                    else:
                        return False
                else:
                    if str(encryptor.text_encrypt(words=word, hash_method="SHA3-256")) == hash:
                        return True
                    else:
                        return False
            elif hash_method == 'sha3-384':
                if encode:
                    if str(encryptor.text_encrypt(word, encode, "SHA3-384")) == hash:
                        return True
                    else:
                        return False
                else:
                    if str(encryptor.text_encrypt(words=word, hash_method="SHA3-384")) == hash:
                        return True
                    else:
                        return False
            elif hash_method == 'sha3-512':
                if encode:
                    if str(encryptor.text_encrypt(word, encode, "SHA3-512")) == hash:
                        return True
                    else:
                        return False
                else:
                    if str(encryptor.text_encrypt(words=word, hash_method="SHA3-512")) == hash:
                        return True
                    else:
                        return False
            elif hash_method == 'shake128':
                if encode:
                    if str(encryptor.text_encrypt(word, encode, "SHAKE128", count=str(count))) == hash:
                        return True
                    else:
                        return False
                else:
                    if str(encryptor.text_encrypt(words=word, hash_method="SHAKE128", count=str(count))) == hash:
                        return True
                    else:
                        return False
            elif hash_method == 'shake256':
                if encode:
                    if str(encryptor.text_encrypt(word, encode, "SHAKE256", count=str(count))) == hash:
                        return True
                    else:
                        return False
                else:
                    if str(encryptor.text_encrypt(words=word, hash_method="SHAKE256", count=str(count))) == hash:
                        return True
                    else:
                        return False
            elif hash_method == 'base85':
                return base64.b85decode(hash)
            elif hash_method == 'base64':
                return base64.b64decode(hash)
            elif hash_method == 'base32':
                return base64.b32decode(str(hash))
            elif hash_method == 'base16':
                return base64.b16decode(hash)
            elif hash_method == 'ascii85':
                return base64.a85decode(hash)
            elif hash_method == 'caesar':
                if (type(count) is not int) or (count not in range(1, 27)):
                    raise ValueError(
                        "the key must be an integer between: 1 and 26")
                if (not hash) or (len(hash) == 0):
                    raise ValueError("You must provide data")
                abc = "abcdefghijklmnopqrstuvwxyz"
                ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                c = ""
                for i in hash:
                    if i in abc:
                        c += abc[(abc.index(i) - count) % 26]
                    elif i in ABC:
                        c += ABC[(ABC.index(i) - count) % 26]
                    else:
                        c += i
                return c
            else:
                raise ValueError('This Hash Method Not Available !')
        elif type(word) == list:
            if hash_method == 'base85':
                return base64.b85decode(hash)
            elif hash_method == 'base64':
                return base64.b64decode(hash)
            elif hash_method == 'base32':
                return base64.b32decode(str(hash))
            elif hash_method == 'base16':
                return base64.b16decode(hash)
            elif hash_method == 'ascii85':
                return base64.a85decode(hash)
            elif hash_method == 'md5':
                for i in word:
                    if encode:
                        if str(encryptor.text_encrypt(i, encode, "MD5")) == hash:
                            return i
                        else:
                            ...
                    else:
                        if str(encryptor.text_encrypt(words=i, hash_method="MD5")) == hash:
                            return i
                        else:
                            ...
                return ""
            elif hash_method == 'sha1':
                for i in word:
                    if encode:
                        if str(encryptor.text_encrypt(i, encode, "SHA1")) == hash:
                            return i
                        else:
                            ...
                    else:
                        if str(encryptor.text_encrypt(words=i, hash_method="SHA1")) == hash:
                            return i
                        else:
                            ...
                return ""
            elif hash_method == 'sha256':
                for i in word:
                    if encode:
                        if str(encryptor.text_encrypt(i, encode, "SHA256")) == hash:
                            return i
                        else:
                            ...
                    else:
                        if str(encryptor.text_encrypt(words=i, hash_method="SHA256")) == hash:
                            return i
                        else:
                            ...
                return ""
            elif hash_method == 'sha224':
                for i in word:
                    if encode:
                        if str(encryptor.text_encrypt(i, encode, "SHA224")) == hash:
                            return i
                        else:
                            ...
                    else:
                        if str(encryptor.text_encrypt(words=i, hash_method="SHA224")) == hash:
                            return i
                        else:
                            ...
                return ""
            elif hash_method == 'sha384':
                for i in word:
                    if encode:
                        if str(encryptor.text_encrypt(i, encode, "SHA384")) == hash:
                            return i
                        else:
                            ...
                    else:
                        if str(encryptor.text_encrypt(words=i, hash_method="SHA384")) == hash:
                            return i
                        else:
                            ...
                return ""
            elif hash_method == 'sha512':
                for i in word:
                    if encode:
                        if str(encryptor.text_encrypt(i, encode, "SHA512")) == hash:
                            return i
                        else:
                            ...
                    else:
                        if str(encryptor.text_encrypt(words=i, hash_method="SHA512")) == hash:
                            return i
                        else:
                            ...
                return ""
            elif hash_method == 'sha3-224':
                for i in word:
                    if encode:
                        if str(encryptor.text_encrypt(i, encode, "SHA3-224")) == hash:
                            return i
                        else:
                            ...
                    else:
                        if str(encryptor.text_encrypt(words=i, hash_method="SHA3-224")) == hash:
                            return i
                        else:
                            ...
                return ""
            elif hash_method == 'sha3-256':
                for i in word:
                    if encode:
                        if str(encryptor.text_encrypt(i, encode, "SHA3-256")) == hash:
                            return i
                        else:
                            ...
                    else:
                        if str(encryptor.text_encrypt(words=i, hash_method="SHA3-256")) == hash:
                            return i
                        else:
                            ...
                return ""
            elif hash_method == 'sha3-384':
                for i in word:
                    if encode:
                        if str(encryptor.text_encrypt(i, encode, "SHA3-384")) == hash:
                            return i
                        else:
                            ...
                    else:
                        if str(encryptor.text_encrypt(words=i, hash_method="SHA3-384")) == hash:
                            return i
                        else:
                            ...
                return ""
            elif hash_method == 'sha3-512':
                for i in word:
                    if encode:
                        if str(encryptor.text_encrypt(i, encode, "SHA3-512")) == hash:
                            return i
                        else:
                            ...
                    else:
                        if str(encryptor.text_encrypt(words=i, hash_method="SHA3-512")) == hash:
                            return i
                        else:
                            ...
                return ""
            elif hash_method == 'shake128':
                for i in word:
                    if encode:
                        if str(encryptor.text_encrypt(word, encode, "SHAKE128", count=str(count))) == hash:
                            return word
                        else:
                            ...
                    else:
                        if str(encryptor.text_encrypt(words=word, hash_method="SHAKE128", count=str(count))) == hash:
                            return word
                        else:
                            ...
                return ""
            elif hash_method == 'shake256':
                if encode:
                    if str(encryptor.text_encrypt(word, encode, "SHAKE256", count=str(count))) == hash:
                        return word
                    else:
                        return ""
                else:
                    if str(encryptor.text_encrypt(words=word, hash_method="SHAKE256", count=str(count))) == hash:
                        return word
                    else:
                        return ""
            elif hash_method == 'caesar':
                if (type(count) is not int) or (count not in range(1, 27)):
                    raise ValueError(
                        "the key must be an integer between: 1 and 26")
                if (not hash) or (len(hash) == 0):
                    raise ValueError("You must provide data")
                abc = "abcdefghijklmnopqrstuvwxyz"
                ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                hash = ""
                for i in hash:
                    if i in abc:
                        hash += abc[(abc.index(i) - count) % 26]
                    elif i in ABC:
                        hash += ABC[(ABC.index(i) - count) % 26]
                    else:
                        hash += i
                return hash
            else:
                raise ValueError('This Hash Method Not Available !')
        else:
            raise TypeError('"word" Argument Type Must be : str or list')
