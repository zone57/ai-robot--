🤖 机器人学核心概念：空间与运动学在机器人控制中，我们通常在两套不同的“坐标系”下描述机器人的状态。

核心空间对比特性关节空间 （Joint Space）笛卡尔坐标空间 （Cartesian Space） 定义维度每一个关节的状态向量
q
=
[
θ
1
，
θ
2
，
.
.
.
，
θ
n
]

末端位姿向量

P
=
[
x
，
y
，
z
，
滚
转
、
俯
仰
、
偏
航
]

描述对象机器人内部：电机的转动角度或伸缩距离外部世界：末端执行器在三维世界的位置坐标单位弧度 (rad) 或 角度 (deg)米 (m) 或 毫米 (mm)直观程度抽象：人很难直观想象角度对应的空间位置直观：符合人类对前后、上下、左右的认知主要用途电机伺服控制、检查是否达到物理限位任务路径规划、目标抓取、避障2.空间转换：运动学 （Kinematics）机器人系统的核心逻辑就在于这两个空间之间的相互“翻译”： 🔄 正向运动学 （Forward Kinematics， FK）逻辑：已知 关节角度
⇒
推算 末端位置。特点：计算简单、结果唯一。只要确定了每个关节的姿态，机械手在空间的位置就是确定的。🔄 逆向运动学 （Inverse Kinematics， IK）逻辑：给定 目标坐标
⇒
求解 关节角度。特点：计算复杂、存在多解或无解。例如：你可以保持手部不动，但通过旋转肘部（手肘向上或向下）来改变姿态，这就是典型的“多解”现象。3. 实验总结关节输入模式 (FK)：通过手动调节 J0-J6 滑块，你是在控制机器人的“骨骼”旋转，观察末端坐标如何随之改变。坐标输入模式 （IK）：通过输入 X， Y， Z 指令，让计算机通过算法计算出 7 个关节该如何协同运动以到达目标点。💡 提示：在实际开发中，我们通常在坐标空间规划任务（比如“去拿杯子”），而在关节空间执行控制（向电机发送脉冲信号）


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




    import pybullet as p
import pybullet_data as pd
import time
import math

# --- 初始化 ---
p.connect(p.GUI)
p.setAdditionalSearchPath(pd.getDataPath())
p.setGravity(0, 0, -9.8)

p.configureDebugVisualizer(p.COV_ENABLE_GUI, 1)
p.resetDebugVisualizerCamera(1.5, 45, -30, [0.5, 0, 0.65])

# 加载环境
p.loadURDF("plane.urdf")
p.loadURDF("table/table.urdf", [0.5, 0, 0], useFixedBase=True)

# 加载机器人
pandaId = p.loadURDF("franka_panda/panda.urdf", [0.5, 0, 0.625], useFixedBase=True)

# ===== 控制面板 =====
mode_toggle = p.addUserDebugParameter("IK=1 / Joint=0", 1, 0, 1)

# XYZ 控制
p.addUserDebugText("=== XYZ CONTROL ===", [1.2, 0.5, 1.2], [0,0,1], 1)
ctrl_x = p.addUserDebugParameter("X", 0.3, 0.8, 0.6)
ctrl_y = p.addUserDebugParameter("Y", -0.4, 0.4, 0.0)
ctrl_z = p.addUserDebugParameter("Z", 0.65, 1.2, 0.8)

# 关节控制
joint_params = []
for i in range(7):
    joint_params.append(
        p.addUserDebugParameter(f"J{i}", -3.14, 3.14, 0)
    )

# ===== 主循环 =====
while True:
    run_ik = p.readUserDebugParameter(mode_toggle)

    if run_ik > 0.5:
        # ===== IK模式（XYZ控制）=====
        x = p.readUserDebugParameter(ctrl_x)
        y = p.readUserDebugParameter(ctrl_y)
        z = p.readUserDebugParameter(ctrl_z)

        jointPoses = p.calculateInverseKinematics(
            pandaId,
            11,
            [x, y, z],
            p.getQuaternionFromEuler([math.pi, 0, 0])
        )

        for i in range(7):
            p.setJointMotorControl2(
                pandaId, i,
                p.POSITION_CONTROL,
                jointPoses[i],
                force=500
            )

    else:
        # ===== 关节模式 =====
        for i in range(7):
            val = p.readUserDebugParameter(joint_params[i])
            p.setJointMotorControl2(
                pandaId, i,
                p.POSITION_CONTROL,
                val,
                force=500
            )

    p.stepSimulation()
    time.sleep(1./120.)