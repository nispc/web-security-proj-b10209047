import base64
from Crypto.Cipher import AES
from Crypto import Random

BS = 16
key = '1234567812345678'

from .pkcs import PKCS7Encoder



def pad(s):
    s =  s.encode('utf-8')
    len_s = len(s)
    s = s.zfill((len_s // BS + 1) * BS)
    return s
    
def unpad(s):
    return s.decode('utf-8').strip('0')

class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ).decode('utf-8')

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))
