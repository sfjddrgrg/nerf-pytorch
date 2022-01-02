# nerf-pytorch
从train函数开始

## parser
```python
    parser = config_parser()
    args = parser.parse_args()
```
argparse 模块编写命令行接口。程序定义它需要的参数，然后 argparse 将弄清如何从 sys.argv 解析出那些参数。 argparse 模块还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息。
parser = config_parser() 将parser对象实例化，然后通过 parse_args() 方法解析参数。它将检查命令行，把每个参数转换为适当的类型然后调用相应的操作。

## load data
### llff
