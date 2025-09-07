package hachima

import (
	"encoding/base64"
	"fmt"
)
import "strings"

var h2b = map[string]byte{}
var b2h = map[byte]string{}

func init() {
	hachima := strings.Split("哈、基、米、南、北、绿、豆、阿、西、噶、压、库、那、鲁、曼、波、欧、马、自、立、悠、嗒、步、诺、斯、哇、嗷、冰、踩、背、叮、咚、鸡、大、狗、叫、袋、鼠、兴、奋、剂、出、示、健、康、码、楼、上、下、来、带、一、段、小、白、手、套、胖、宝、牛、魔、呵、嘿、喔", "、")
	b64 := []byte("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
	for i := 0; i < len(hachima); i += 1 {
		h2b[hachima[i]] = b64[i]
		b2h[b64[i]] = hachima[i]
	}
}

func Encode(data []byte) string {
	s := base64.StdEncoding.EncodeToString(data)
	r := strings.Builder{}
	for _, c := range s {
		if c == '=' {
			continue
		}
		r.WriteString(b2h[byte(c)])
	}
	return r.String()
}

func Decode(r string) ([]byte, error) {
	rs := strings.Split(r, "")
	sb := strings.Builder{}
	for _, c := range rs {
		cc := h2b[c]
		if cc == 0 {
			return nil, fmt.Errorf("unexpected char: %c", cc)
		}
		sb.WriteByte(cc)
	}
	padding := 4 - (len(rs) % 4)
	if padding != 4 {
		for i := 0; i < padding; i += 1 {
			sb.WriteString("=")
		}
	}
	s := sb.String()
	return base64.StdEncoding.DecodeString(s)
}
