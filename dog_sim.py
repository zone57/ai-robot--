#!/usr/bin/env python3

import pybullet as p
import pybullet_data
import time

# 连接GUI
p.connect(p.GUI)

# 加载资源路径
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# 加载地面
plane = p.loadURDF("plane.urdf")

# 加载“机器狗”（四足机器人）
robot = p.loadURDF("laikago/laikago_toes.urdf", [0, 0, 0.5])

# 设置重力
p.setGravity(0, 0, -9.8)

print("🐶 机器狗仿真开始！按 Ctrl+C 退出")

# 仿真循环
try:
    while True:
        p.stepSimulation()
        time.sleep(1./240.)
except KeyboardInterrupt:
    print("退出仿真")

p.disconnect()
