package main

import "fmt"
import "github.com/wkgcass/hachima/go/hachima"

func main() {
	encoded := hachima.Encode([]byte("hello, world! 你好，世界！"))
	fmt.Println(encoded)
	decoded, err := hachima.Decode(encoded)
	if err != nil {
		panic(err)
	}
	println(string(decoded))
}
