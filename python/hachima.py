import base64

HACHIMA = '哈、基、米、南、北、绿、豆、阿、西、噶、压、库、那、鲁、曼、波、欧、马、自、立、悠、嗒、步、诺、斯、哇、嗷、冰、踩、背、叮、咚、鸡、大、狗、叫、袋、鼠、兴、奋、剂、出、示、健、康、码、楼、上、下、来、带、一、段、小、白、手、套、胖、宝、牛、魔、呵、嘿、喔'.split('、')
BASE64 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')

H2B = {}
B2H = {}

for i in range(len(HACHIMA)):
    H2B[HACHIMA[i]] = BASE64[i]
    B2H[BASE64[i]] = HACHIMA[i]

def encode(data):
    s = base64.b64encode(data)
    s = s.decode('ascii')
    r = ''
    for c in s:
        if c == '=':
            continue
        r += B2H[c]
    return r

def decode(r):
    s = ''
    for c in r:
        s += H2B[c]
    padding = 4 - (len(s) % 4)
    if padding != 4:
        s += '=' * padding
    return base64.b64decode(s)

"""
if __name__ == '__main__':
    import os
    #create folder under ./audioClips/HACHIMA.each()
    for i in range(len(HACHIMA)):
        os.makedirs('./audioClips/' + HACHIMA[i], exist_ok=True)
"""
