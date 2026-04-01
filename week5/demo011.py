import pybullet as p
import pybullet_data
import time
import math

# ===== 初始化 =====
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

p.resetDebugVisualizerCamera(1.5, 45, -30, [0.5, 0, 0.65])

# 加载环境
p.loadURDF("plane.urdf")
p.loadURDF("table/table.urdf", [0.5, 0, 0], useFixedBase=True)

# 加载机械臂
pandaId = p.loadURDF("franka_panda/panda.urdf", [0.5, 0, 0.625], useFixedBase=True)

# 末端执行器
ee_index = 11
orientation = p.getQuaternionFromEuler([math.pi, 0, 0])

print("开始画圆...")

# ===== 圆参数 =====
center = [0.6, 0.0, 0.8]   # 圆心
radius = 0.1               # 半径

# ===== 画圆（IK）=====
for t in range(360):
    angle = math.radians(t)

    x = center[0] + radius * math.cos(angle)
    y = center[1] + radius * math.sin(angle)
    z = center[2]

    jointPoses = p.calculateInverseKinematics(
        pandaId,
        ee_index,
        [x, y, z],
        orientation
    )

    for i in range(7):
        p.setJointMotorControl2(
            pandaId,
            i,
            p.POSITION_CONTROL,
            jointPoses[i],
            force=500
        )

    p.stepSimulation()
    time.sleep(1./240.)

print("画圆完成！")

# 保持窗口
while True:
    p.stepSimulation()
    time.sleep(1./240.)