#!/bin/bash

encodedSecret="3d3d516343746d4d6d6c315669563362"
decoded=$(echo "$encodedSecret" | xxd -r -p | rev | base64 -d)
echo "$decoded" > natas8_pass.txt
