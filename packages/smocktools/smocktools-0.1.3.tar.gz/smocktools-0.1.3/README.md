# Tools Package

This is a package. You can use

[Github-flavored Markdown](https://github.com/smockgithub/smocktools)

MysqlRepository 是mysql工具类，为了特殊情况下的稳定性要求，进行了链接丢失的重新链接补偿。


本工具支持：
- 因各种原因中断后补偿。
- 支持ssh跳板。
- 支持批量insert（效率比较高）

使用方法：
```
pip install smocktools
```

```
from smocktools import MysqlRepository


r = MysqlRepository("localhost","user","pwd","database name")

r.get("select * from tablename")

```