# Rocket VTOL
An experimental research project with the objective of developing a fast, modern, and reliable VTOL system for a hybrid rocket.
Created by Jason Chen on _10 May, 2019_. **Written in Python 3.7**. Subject to change.

# Structure
## Core 
- Core functionalities for basic operation of the rocket during flight. Handles startup dictates the actions of modules.
    - `startup.py`: 
    Startup procedure. Establishes connections with the `ground_station`.
    - `main.py`: 
    Driver for the entire flight software system. Sets global variables and starts `thread_handler.py`.
    - `thread_handler.py`: 
    Class `ThreadHandler` initiates and maintains many parallel threads that run main modules throughout the entire operation of
    the rocket.
## Docs
- Contains documentation.

## Submodules
- Main modules.
    - **Control**: 
    - All software that goes directly into the devlopment and implementation of the control alogirithm (Convex Optimization).
        - *dev/ *: 
            - The `dev` directory contains development and training tools, including a simulator, to train ML models.
        - *cv/ *: 
            - Computer-vision assisted attitude determination using OpenCV.
        - *coca/ *: 
            - The Convex Optimization Control Algorithm (COCA) is a Proximal Policy Optimzation (PPO) implementation of a
            reinforcement learning algorithm that takes inputs from different sensor systems (`sensors` and `cv`) and determines
            the best course of
            action to take given that set of inputs. Outputs actuation signals to `tvc.py` and `rcs.py`. Listens for attitude
            updates from `attitude_handler.py`.
        - `rcs.py`: 
            - Controls the RCS (Reaction Control System) with accordance to COCA.
        - `tvc.py`: 
            - Controls the thrust vectoring of the propulsion system. Includes throttling.
    - **Sensors**: 
    - Passive module that constantly pulls data from `gps.py`, `imu.py`, and `cameras.py` stores it as a packet.
    - **Comms**:
    - Manages all communication systems.
        - `sdr.py`: 
        - SDR (Software-Defined Radio) for main communication medium between the ground station and the rocket.
            - `send()`: 
                - Sends telemetry packet, heartbeat signal, or mission logging information. Uses priority queue.
            - `listen()`: 
                - Listens for any signals from the ground station and stores commands in a priority queue or stack.
        - `telemetry.py`: 
        - Gathers and formats telemetry packet from `sensors`.
            - `enqueue()`: 
                - Prepares telemetry packets for transmission through the SDR. Pushes it to
        - `command_ingest.py`: 
            - Pulls the latest command from `sdr.py`'s `listen()` method and processes the command.
    - **Abort**: 
    - Handles the abort procedure if ever needed. Able to override all systems.
    - **Propulsion**: 
    - Controls the propulsion system of the rocket. Able to override COCA's commands if an abort command is issued. 
## Ground Station
- Contains software for the ground station.
    - `gui.css`
    - Graphical User Interface for ground-based mission control.
    - `main.py`
    - Manages all ground station operations.
