# Week 13：四足机器人入门与期末项目实施

## 一、实验基本信息

* 课程：AI Robotics
* 主题：四足机器人入门、PyBullet 仿真、期末项目整理
* 工具：Python、PyBullet、GitHub Pages

---

## 二、实验目标

本周是课程最后阶段，重点学习四足机器人的基本结构与运动控制思想，并对本学期完成的实验内容进行系统整理，完成课程项目最终检查与提交。

### 本周完成内容

* 学习四足机器人的结构组成与运动特点
* 理解四足机器人相比轮式机器人的优势
* 使用 Python 编写步态模拟程序
* 整理课程项目与 GitHub Pages 页面
* 完成期末项目检查与总结

---

## 三、理论整理

### 1. 为什么需要四足机器人？

轮式机器人在平坦路面上运行效率较高，但在楼梯、碎石路面、山地等复杂环境中运动能力有限。

四足机器人能够通过腿部运动跨越障碍物，适用于巡检、搜救、野外探索等复杂场景，因此近年来受到广泛关注。

### 2. 四足机器人的基本结构

四足机器人通常由四条腿组成：

* LF（Left Front）：左前腿
* RF（Right Front）：右前腿
* LH（Left Hind）：左后腿
* RH（Right Hind）：右后腿

每条腿通常包含多个关节：

* 髋关节（Hip Joint）
* 大腿关节（Thigh Joint）
* 小腿关节（Calf Joint）

这些关节共同完成支撑、摆动和运动控制。

### 3. 四足机器人控制思想

四足机器人控制需要综合考虑：

* 身体平衡控制
* 步态规划
* 足端接触检测
* 关节角度控制
* IMU 姿态反馈

现代四足机器人常结合以下技术：

* 模型预测控制（MPC）
* 强化学习（Reinforcement Learning）
* 仿真训练（Simulation Training）

从而实现更加稳定和灵活的运动能力。

---

## 四、课程项目整理

### 1. 项目结构整理

本学期完成并整理了以下实验内容：

* Week 1：WSL 与 ROS2 环境安装
* Week 2：ROS2 Topic 通信实验
* Week 3：机器人运动控制
* Week 4：Python 与 PyBullet
* Week 5：Linux 与机器人运动学
* Week 6：闭环控制与避障逻辑实验
* Week 7：前半学期复习与模拟练习
* Week 8：Docker ROS2 环境
* Week 9：ROS2 小乌龟与 Docker
* Week 10：Docker 镜像构建与 OpenCV、PyBullet
* Week 11：四足机器人仿真与 PPO 强化学习
* Week 12：摄像头标定与 Camera Bridge
* Week 13：四足机器人入门与期末项目整理

### 2. 核心实验内容

* ROS2 节点与 Topic 通信
* TurtleSim 控制实验
* Python 机器人运动学计算
* OpenCV 图像处理
* Docker 容器实验
* RViz 可视化
* ArUco Marker 识别
* PyBullet 仿真
* PPO 强化学习基础

### 3. 最终检查内容

* 检查 GitHub Pages 页面
* 检查 README 文件内容
* 修复图片路径问题
* 检查周目录结构
* 完成最终提交

---

## 五、仿真实验

本周使用 Python 编写简化版四足机器人步态模拟程序，用于理解 Trot 对角步态的基本原理。

### 运行命令

```bash
python3 quadruped_project_demo.py
```

### 示例代码

```python
import time

print("Week 13：四足机器人步态模拟")
print("--------------------------------")

print("四足机器人基本结构：")
print("LF：左前腿")
print("RF：右前腿")
print("LH：左后腿")
print("RH：右后腿")

print("--------------------------------")
print("开始模拟 Trot 对角步态")

for step in range(1, 7):
    print(f"Step {step}")

    if step % 2 == 1:
        print("支撑腿：LF 左前腿 + RH 右后腿")
        print("摆动腿：RF 右前腿 + LH 左后腿")
    else:
        print("支撑腿：RF 右前腿 + LH 左后腿")
        print("摆动腿：LF 左前腿 + RH 右后腿")

    print("身体保持平衡，进入下一步")
    print("--------------------------------")
    time.sleep(0.3)

print("四足机器人步态模拟完成")
print("项目核心功能测试完成")
```

---

## 六、总结

通过本周学习，我了解了四足机器人的基本结构、步态规划和控制思想，并通过 Python 模拟程序进一步理解了 Trot 对角步态的工作原理。

同时，我完成了 AI Robotics 课程项目的最终整理工作，对 ROS2、Linux、Docker、OpenCV、RViz、ArUco、PyBullet 和强化学习等内容进行了系统回顾，进一步提升了机器人软件开发与仿真实践能力。
