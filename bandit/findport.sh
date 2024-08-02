#!/bin/bash

# 當前級別的密碼
current_password="kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx"

# 掃描端口並檢查 SSL
for port in {31000..32000}
do
    # 檢查端口是否開放
    (echo > /dev/tcp/localhost/$port) >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "Port $port is open"
       
        # 檢查 SSL 支持
        echo "Q" | openssl s_client -connect localhost:$port -quiet 2>/dev/null | grep -q "Verify return code: 0"
        if [ $? -eq 0 ]; then
            echo "Port $port supports SSL"
            
            # 嘗試獲取下一級憑證
            response=$(echo "$current_password" | ncat --ssl localhost:$port -quiet 2>/dev/null)
            
            # 檢查回應是否只是回顯輸入
            if [[ "$response" != *"$current_password"* ]]; then
                echo "Possible next level credentials found on port $port:"
                echo "$response"
                exit 0
            fi
        fi
    fi
done

echo "No valid port found for next level credentials."