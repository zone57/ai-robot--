# ROS2 Docker 小乌龟实验报告

## 📅 日期
2026-04-22

---

## 🧪 实验目的
- 学习使用 Docker 运行 ROS2 环境  
- 掌握 turtlesim 小乌龟基本操作  
- 理解 ROS2 中 Topic 通信机制  
- 使用命令控制机器人运动  

---

## 🖥️ 实验环境
- 操作系统：Windows 10  
- 工具：Docker Desktop + WSL2  
- 镜像：ghcr.io/tiryoh/ros2-desktop-vnc:humble  
- ROS版本：ROS2 Humble  

---

## 🚀 实验步骤

### 1️⃣ 启动 Docker 容器
```bash
docker run -p 6080:80 --security-opt seccomp=unconfined --shm-size=512m ghcr.io/tiryoh/ros2-desktop-vnc:humble