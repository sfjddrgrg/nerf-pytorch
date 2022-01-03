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
llff即Local Light Field Fusion数据集，这个函数的返回值是images, poses, bds, render_poses, i_test。
```python
    poses, bds, imgs = _load_data(basedir, factor=factor) # factor=8 downsamples original imgs by 8x
    print('Loaded', basedir, bds.min(), bds.max())
    
    # Correct rotation matrix ordering and move variable dim to axis 0
    poses = np.concatenate([poses[:, 1:2, :], -poses[:, 0:1, :], poses[:, 2:, :]], 1)
    poses = np.moveaxis(poses, -1, 0).astype(np.float32)
    imgs = np.moveaxis(imgs, -1, 0).astype(np.float32)
    images = imgs
    bds = np.moveaxis(bds, -1, 0).astype(np.float32)
```
images：通过load_data函数加载的图片，形状为(h,w,3,N)，对应图片的高，宽，RGB，数量。poses、bds：相机姿态，远近边界。load_data函数中从pose_bounds.npy文件中读取。储存了姿态和最近最远处深度信息，是一个Nx17的数组。reshape为3x5xN的poses，和2xN的bds。在load_llff_data函数中修正了x、y、z轴的顺序为(y,-x,z)，并且将数量维度移至第0维。poses.shape = (N,3,5),image.shape=(N,h,w,3),bds.shape=(N,2)


render_poses：