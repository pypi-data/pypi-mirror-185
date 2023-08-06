aiapi.pro 官方SDK包

- 使用方式
- 在 http://aiapi.pro 注册一个账户拿到一个Token后

```
from aiapi import request_api

authorization = "您的Token"
api_name = "api名称"
api_action = "api动作名称"
api_params = "参数"

# 使用API接口
request_api(authorization, api_name, api_action, api_params)

# KEY错误提交接口
authorization = "您的Token"
bot_uuid = "request_api 返回的数据中的 key_uuid"
error_data = "request_api 返回的所有数据, 如果数据敏感, 可以去掉 敏感数据"
error_api(authorization, bot_uuid, error_data)
```
