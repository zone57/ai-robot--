# Week14 ROS2 Turtlesim Remote Control Project

## 项目名称
ROS2 Turtlesim 远程控制与自动运行项目

---

## 项目目标

本项目基于 ROS2 Jazzy 和 Turtlesim，实现：

- 手机网页远程控制乌龟移动
- Python 作为 ROS2 与网页之间的桥接程序
- Tailscale 实现手机与电脑跨设备通信
- 自动运行模式（AUTO）
- 乌龟轨迹展示

---

## 开发环境

| 项目 | 版本 |
|--------|--------|
| Ubuntu | 24.04 |
| ROS2 | Jazzy |
| Python | 3 |
| Turtlesim | ROS2 Package |
| Tailscale | Latest |
| Browser | Mobile Browser |

---

## 系统结构

```text
手机浏览器
      ↓
controller.html
      ↓
HTTP POST
      ↓
bridge_turtle.py
      ↓
ROS2 Topic
      ↓
/turtle1/cmd_vel
      ↓
turtlesim
```

---

## 功能实现

### 1. 手动控制

手机访问控制网页：

```text
http://100.xxx.xxx.xxx:8080
```

提供：

- 前进
- 后退
- 左转
- 右转
- 停止

按钮控制。

---

### 2. 自动运行模式

新增 AUTO 按钮。

点击后：

- 乌龟自动前进
- 自动转向
- 持续循环运动
- 无需人工干预

---

## 运行方法

### 启动 Turtlesim

```bash
source /opt/ros/jazzy/setup.bash

ros2 run turtlesim turtlesim_node
```

### 启动桥接程序

```bash
cd ~/robot_bridge

source /opt/ros/jazzy/setup.bash

python3 bridge_turtle.py
```

### 手机连接

浏览器访问：

```text
http://100.xxx.xxx.xxx:8080
```

---

## 项目成果

### 手动控制演示

文件：

```text
手动.mp4
```

内容：

- 手机控制乌龟移动
- 验证远程控制成功

---

### 自动运行演示

文件：

```text
自动视频.mp4
```

内容：

- 点击 AUTO
- 乌龟自动运动
- 自动绘制轨迹

---

### 自动运行截图

文件：

```text
自动动.png
```

内容：

- 自动运行状态截图
- 展示乌龟运动轨迹

---

## 项目总结

通过本项目学习并实践了：

- ROS2 Topic 通信
- Python ROS2 编程
- HTTP 服务开发
- 网页前后端交互
- Tailscale 网络通信
- Turtlesim 机器人控制

成功实现了手机远程控制和自动运行功能。