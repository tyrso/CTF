# 步驟 1: 創建臨時工作目錄
WORKDIR=$(mktemp -d)
echo "工作目錄: $WORKDIR"
cd $WORKDIR

# 步驟 2: 複製數據文件
cp /path/to/data.txt ./data

# 步驟 3: 將十六進制轉儲轉換回二進制文件
xxd -r data > data.bin

# 步驟 4: 循環解壓縮
while true; do
    # 檢查文件類型
    filetype=$(file data.bin)
    echo "檔案類型: $filetype"

    if [[ $filetype == *"gzip compressed data"* ]]; then
        mv data.bin data.gz
        gzip -d data.gz
    elif [[ $filetype == *"bzip2 compressed data"* ]]; then
        mv data.bin data.bz2
        bzip2 -d data.bz2
    elif [[ $filetype == *"POSIX tar archive"* ]]; then
        mv data.bin data.tar
        tar xf data.tar
    elif [[ $filetype == *"ASCII text"* ]]; then
        echo "找到文本文件，可能包含密碼："
        cat data.bin
        break
    else
        echo "未知文件類型，無法繼續解壓"
        break
    fi

    # 如果解壓後的文件不是 data.bin，則重命名
    if [ ! -f data.bin ]; then
        mv data data.bin 2>/dev/null || true
    fi
done

# 清理（可選）
cd ..
rm -rf $WORKDIR