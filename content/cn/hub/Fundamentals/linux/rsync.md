--- 
title: rsync命令
---

## rsync
rsync 就是远程同步的意思remote sync.
rsync 被用在UNIX / Linux执行备份操作操作.
rsync 工具包被用来从一个位置到另一个位置高效地同步文件和文件夹. rsync可以实现在同一台机器的不同文件直接备份,也可以跨服务器备份.

## 用法
从语法结构我们可以看出, 源和目标即可以在本地也可以在远端. 如果是远端的话,需要指明登录用户名, 远端服务器名, 和远端文件或目录. 同时源可以是多个, 目标位置只能是一个.

将本地的文件文件拷贝到远程主机的目录上。
```bash
rsync -avz --delete --progress /root/temp/  user@192.168.0.1:/home/user/
```

-a: 保留源文件的修改时间、文件权限等信息。
-v: verbose 
-r: recursive 
-z: compress 
--delete: 在目标文件夹删除源文件不存在的文件。
--progress 显示进度



参考：
https://www.jianshu.com/p/b862af872cbd