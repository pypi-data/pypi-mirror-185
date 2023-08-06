# 介绍
这是一个Python库，它可以查看当前的IP地址
# 获取iPv4地址
```
import cniptest
print(cniptest.ip())
```
# 获取ipv6地址
```
import cniptest
print(cniptest.ipv6())
```
# 检测是否有ipv6，如果有那么就返回ipv6，如果没有就返回iPv4
```
import cniptest
print(cniptest.test())
```
# 获取北京出口ipv4地址
```
import cniptest
print(cniptest.bjv4())
```
# 获取北京出口ipv6地址
```
import cniptest
print(cniptest.bjv6())
```
# 获取南京出口ipv4地址
```
import cniptest
print(cniptest.njv6())
```
# 获取南京出口ipv4地址
```
import cniptest
print(cniptest.njv6())
```
# FAQ
问：为什么返回Error？
答：一般是因为没有连接网络，少数情况没有ipv6地址或者没有ipv4地址（没有ipv4的概率极少，除非是故意在路由器关闭ipv4），极少数情况是服务器故障（这种情况下一般一会儿就可以解决，不过有可能是因为API关闭，这种情况下建议更新本库，我在API关闭后会第一时间更新本库的）