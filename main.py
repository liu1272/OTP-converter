import pyotp

# 设置服务端密钥
secret_key = "KEY"

# 使用密钥和时间间隔（默认为 30 秒）创建一个 TOTP 对象
totp = pyotp.TOTP(secret_key)

# 生成当前的 OTP
current_otp = totp.now()
print(f"当前OTP: {current_otp}")