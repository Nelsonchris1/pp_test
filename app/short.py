import random
import string



class URLShortner:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.chars = string.ascii_letters + string.digits
        self.base_url = "http://your_shortened_url.com/"

    def generate_unique_code(self, lenght):
        while True:
            code = ''.join(random.choice(self.chars) for _ in range(lenght))
            if code not in self.code_to_url:
                return code

    def shorten_url(self, long_url, lenght=6):
        if long_url in self.url_to_code:
            return self.base_url + self.url_to_code[long_url]
        
        code = self.generate_unique_code(lenght)
        self.url_to_code[long_url] = code
        self.code_to_url[code] = long_url

        return self.base_url + code

    def swap_letters(self,char, lenght=5):
        if lenght == 0:
            return "INVALID"
        
        swap = char[-lenght:] + char[lenght: len(char)-lenght] + char[:lenght]
        return swap        
