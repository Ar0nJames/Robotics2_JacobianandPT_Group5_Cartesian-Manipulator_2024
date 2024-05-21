<div align="center">
  <h1>Robotics2_JacobianandPT_Group5_Cartesian-Manipulator_2024</h1>
  <img src="https://github.com/Ar0nJames/Robotics2_JacobianandPT_Group5_Cartesian-Manipulator_2024/blob/main/Img%20folder/DASDADW.gif" style="height: 255px; width: 450px;">
</div>



## Table of Contents 📁
- [Abstract](#abstract)
- [Introduction](#introduction)
- [Jacobian Matrix](#jacobian-matrix)
- [Differential Equation](#differential-equation)
- [Path and Trajectory Planning](#path-and-trajectory-planning)
- [References](#references)

## Abstract 🗃️
<a name="abstract"></a>
<div align="center">
  <p>This project focuses on the development and analysis of a Cartesian Manipulator, detailing its components and operational principles. The deliverables include recorded demonstration videos, code for path and trajectory planning for two specific tasks—pick and place, and welding—and the implementation of a GUI featuring a velocity calculator and path and trajectory planning functionalities. The project portfolio, documented in the README, encompasses an abstract, an introduction, and detailed descriptions and computations related to the Jacobian Matrix and differential equations of the Cartesian Manipulator. Additionally, it provides a comprehensive guide on path and trajectory planning, complete with the associated programs and references.</p>
</div>

## Introduction ➡️

<a name="introduction"></a>
**The Cartesian Manipulator** , also known as a rectilinear or gantry robot, operates using the Cartesian coordinate system, characterized by three linear joints that move along the X, Y, and Z axes. This project delves into the development and analysis of the Cartesian Manipulator, offering an in-depth look at its components and operational principles.

Historically, Cartesian manipulators emerged in the mid-20th century as versatile tools for industrial automation, benefiting from their straightforward design and ease of control. Initially employed in applications such as material handling and machining, these robots have evolved to perform more complex tasks, including precise assembly and intricate welding operations. The simplicity and reliability of Cartesian manipulators have made them a staple in various manufacturing processes, providing a foundation for more advanced robotic systems.

In this project, we aim to provide a comprehensive understanding of the Cartesian Manipulator through recorded demonstration videos, code for path and trajectory planning for specific tasks like pick and place and welding, and the development of a GUI with a velocity calculator and path and trajectory planning functionalities. The project's portfolio, detailed in the README, includes an abstract, an introduction, and thorough descriptions and computations related to the Jacobian Matrix and differential equations of the Cartesian Manipulator. Additionally, it offers a complete guide on path and trajectory planning, accompanied by the relevant programs and references.

</div>

## Jacobian Matrix of Cartesian Manipulator <img src="https://github.com/Ar0nJames/Robotics2_JacobianandPT_Group5_Cartesian-Manipulator_2024/blob/main/Img%20folder/200w.gif" style="height: 20px; width: 100px;">
</p>

<a name="jacobian-matrix"></a>
**The Jacobian Matrix** is a fundamental tool in the analysis of small signal stability within robotic systems. It is defined as a determinant for a finite number of functions, each involving the first partial derivatives of the same function with respect to the variables. This matrix establishes a relationship between the joint variables and the end-effector velocities of a robot's manipulator. When the joints of the robot move with certain velocities, the Jacobian Matrix helps determine the corresponding velocity of the end-effector. Its primary use is in finding the transformation coordinates, making it essential for understanding the dynamics of robotic motion.





## Differential Equation of Cartesian Manipulator <img src="<img src="https://github.com/Ar0nJames/Robotics2_JacobianandPT_Group5_Cartesian-Manipulator_2024/blob/main/Img%20folder/200w%20(1).gif" style="height: 90px; width: 60px;">
</p>

<a name="differential-equation"></a>
**Differential Equation** of a Cartesian manipulator describes the relationship between the input joint velocities and the resulting end-effector velocities. It typically involves the manipulator's Jacobian matrix, which relates these velocities in a linear manner. By using the Jacobian, one can express the end-effector velocities as a function of the joint velocities. This relationship is crucial for control purposes, as it allows one to determine how changes in joint positions affect the end-effector's motion. In dynamic analyses, this equation is often used to predict the manipulator's behavior under different conditions, aiding in tasks such as trajectory planning and obstacle avoidance.
## Path and Trajectory Planning of Cartesian Manipulator













<a name="path-and-trajectory-planning"></a>
**Path Planning** and trajectory planning** are critical aspects of robotics and automation. The trend toward higher operating speeds in robotic systems aims to reduce production times, but this can impact the accuracy and repeatability of robot motions. High-speed operations demand exceptional performance from actuators and control systems, making it essential to generate smooth trajectories that minimize excessive accelerations and mechanical vibrations. Path planning algorithms create a geometric path from an initial to a final point, passing through pre-defined via-points, while trajectory planning algorithms assign time information to these paths. The careful timing of these trajectories is crucial, as it influences both the kinematic and dynamic properties of the robot's motion.

## References
<a name="references"></a>
List all the references used in the project.
