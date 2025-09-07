const H2B = {}
const B2H = {}

const HACHIMA = '哈、基、米、南、北、绿、豆、阿、西、噶、压、库、那、鲁、曼、波、欧、马、自、立、悠、嗒、步、诺、斯、哇、嗷、冰、踩、背、叮、咚、鸡、大、狗、叫、袋、鼠、兴、奋、剂、出、示、健、康、码、楼、上、下、来、带、一、段、小、白、手、套、胖、宝、牛、魔、呵、嘿、喔'.split('、')
const BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'.split('')

for (let i = 0; i < HACHIMA.length; ++i) {
    H2B[HACHIMA[i]] = BASE64[i]
    B2H[BASE64[i]] = HACHIMA[i]
}

export function encode(data) {
    let s = btoa(data);
    let r = ''
    for (let c of s) {
        if (c == '=') {
            continue
        }
        r += B2H[c]
    }
    return r
}

export function decode(r) {
    let s = ''
    for (let c of r) {
        let x = H2B[c]
        if (!x) {
            throw new Exception('unexpected char: ' + c)
        }
        s += x
    }
    let padding = 4 - (s.length % 4)
    if (padding != 4) {
        s += '='.repeat(padding)
    }
    return atob(s)
}

export default { encode, decode }
