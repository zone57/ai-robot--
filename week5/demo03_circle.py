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