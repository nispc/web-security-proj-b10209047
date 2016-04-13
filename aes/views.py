from pyramid.view import (
    view_config,
    view_defaults
    )

from .aes import AESCipher

@view_defaults(renderer='templates/mytemplate.jinja2')
class Views:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        post = self.request.POST
        if post:
            aesCipher = AESCipher('1111111199999999')
            raw =  post['raw']
            encrypted = post['encrypted']
            mode =  post['mode']
            
            if post['mode'] == 'encrypted':
                return {'raw': '', 'encrypted': aesCipher.encrypt(raw), 'mode': mode}
            else:
                return {'raw': aesCipher.decrypt(encrypted), 'encrypted': '', 'mode': mode}
                print(encrypted)
                # return {'raw': aesCipher.decrypt(encrypted), 'encrypted': encrypted}
        else:
            return {}
