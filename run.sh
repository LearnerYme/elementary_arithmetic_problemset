if [ $1 = "zh" -o $1 = "CN" -o $1 = "ZH" -o $1 = "Chinese" ];then
    python3 run_zh.py
elif [ $1 = "en" -o $1 = "EN" -o $1 = "English" ];then
    python3 run_en.py
else
    echo "invalid argument"
fi
