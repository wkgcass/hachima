import hachima from './hachima.mjs'

const bytes = Buffer.from('hello, world! 你好，世界！', 'utf8')
let s = ''
for (const b of bytes) {
    s += String.fromCharCode(b)
}

let encoded = hachima.encode(s)
console.log(encoded)
let decoded = hachima.decode(encoded)
let output = Buffer.from(decoded, 'ascii').toString('utf8')
console.log(output)
