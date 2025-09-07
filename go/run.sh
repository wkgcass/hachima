#!/bin/bash

set -e

go build -o hachima-test ./main.go
./hachima-test
