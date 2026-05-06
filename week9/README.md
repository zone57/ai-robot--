
# 🐢 ROS2 Docker 小乌龟实验报告

## 📅 日期

2026-05-26

---

## 🧪 实验目的

* 学习使用 Docker 运行 ROS2 环境
* 掌握 turtlesim 小乌龟基本操作
* 理解 ROS2 中 Topic 通信机制
* 使用命令控制机器人运动

---

## 🖥️ 实验环境

* 操作系统：Windows 10
* 工具：Docker Desktop + WSL2
* 镜像：ghcr.io/tiryoh/ros2-desktop-vnc:humble
* ROS版本：ROS2 Humble

---

## 🚀 实验步骤

### 1️⃣ 启动 Docker 容器

在 Windows PowerShell 中输入：

```bash
docker run -p 6080:80 --security-opt seccomp=unconfined --shm-size=512m -v ${PWD}:/home/ws ghcr.io/tiryoh/ros2-desktop-vnc:humble
```

启动后，在浏览器访问：

```text
http://127.0.0.1:6080/
```

进入 Ubuntu 桌面环境。

---

### 2️⃣ 打开终端

在网页桌面中打开 Terminal（终端），进入工作目录：

```bash
cd /home/ws
```

---

### 3️⃣ 启动小乌龟节点（turtlesim）

```bash
ros2 run turtlesim turtlesim_node
```

运行后会弹出一个窗口，显示蓝色背景的小乌龟。

---

### 4️⃣ 启动键盘控制节点

新开一个终端，输入：

```bash
ros2 run turtlesim turtle_teleop_key
```

---

### 5️⃣ 控制小乌龟运动

点击控制终端窗口，使用键盘操作：

* ↑ 前进
* ↓ 后退
* ← 左转
* → 右转

小乌龟会根据按键进行移动。

---

### 6️⃣ 查看 ROS2 通信机制

#### 查看当前节点

```bash
ros2 node list
```

输出示例：

```text
/turtlesim
/teleop_turtle
```

---

#### 查看话题（Topic）

```bash
ros2 topic list
```

输出示例：

```text
/turtle1/cmd_vel
/turtle1/pose
```

---

#### 查看话题数据

```bash
ros2 topic echo /turtle1/pose
```

可以实时看到小乌龟的位置和姿态信息。

---

## 🧠 实验原理

ROS2 使用“节点（Node）+ 话题（Topic）”进行通信：

* `turtlesim_node`：发布乌龟的位置（Publisher）
* `turtle_teleop_key`：发布控制指令（Publisher）
* 系统通过 Topic 实现数据传输

👉 核心机制：

**发布（Publish） → 话题（Topic） → 订阅（Subscribe）**

---

## 🎯 实验结果

* 成功启动 ROS2 Docker 环境
* 成功运行 turtlesim 小乌龟模拟器
* 实现键盘控制乌龟运动
* 成功查看 ROS2 节点和话题
* 理解 ROS2 基本通信机制

---

## ❗ 遇到的问题与解决方法

### 问题 1：无法连接 Docker

**原因**：Docker 未启动
**解决**：启动 Docker Desktop

---

### 问题 2：无法访问网页

**原因**：端口未映射
**解决**：确认使用 `-p 6080:80`

---

### 问题 3：路径错误（C:\ 无法访问）

**原因**：Linux 与 Windows 路径不同
**解决**：使用 `/home/ws` 挂载目录

---

### 问题 4：命令找不到

**解决：**

```bash
source /opt/ros/humble/setup.bash
```

---

## 🧾 实验总结

通过本次实验，我掌握了在 Docker 环境下运行 ROS2 的基本方法，并成功使用 turtlesim 小乌龟进行控制实验。理解了 ROS2 中节点与话题的通信机制，以及如何通过命令行进行系统交互。这为后续学习机器人开发和 ROS2 编程打下了基础。
