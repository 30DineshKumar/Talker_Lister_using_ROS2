# ROS 2 Publisher & Subscriber Node

A lightweight ROS 2 Python package demonstrating inter-node communication using custom publisher and subscriber nodes.

## Overview
This project implements a basic ROS 2 communication pipeline where a publisher node broadcasts messages over a topic and a subscriber node listens and logs the incoming data.

## Prerequisites
* **OS:** Ubuntu Linux
* **Framework:** ROS 2 (with `rclpy` and `std_msgs`)
* **Language:** Python 3

### Publisher (Talker)
The publisher node is responsible for generating and broadcasting data continuously over a designated ROS 2 topic using `rclpy`.
<br><br>
<img width="851" height="442" alt="Screenshot From 2026-11-13 15-19-10" src="https://github.com/user-attachments/assets/12885bf6-e8cc-472d-8743-5a1dc59e413a" />

### Subscriber (Listener)
The subscriber node listens to the topic established by the publisher, receiving and logging the data in real time.
<br><br>
<img width="851" height="442" alt="Screenshot From 2026-11-13 15-18-51" src="https://github.com/user-attachments/assets/ddb82caf-2fb8-40ed-bc84-af4dcbd9cd61" />


## Installation & Build
1. Clone this repository into your ROS 2 workspace `src` directory:
   git clone [https://github.com/30DineshKumar/](https://github.com/30DineshKumar/)<Talker_Listener_using_ROS2>.git

2. Click the green **Commit changes...** button in the top right corner, add a brief commit message (like `Add README.md`), and click **Commit changes** to publish it.

*(Tip: Once you make these changes on GitHub, remember to run `git pull` in your local VS Code terminal before pushing any future code updates so your local repository stays synced with the new README and repo URL).*
