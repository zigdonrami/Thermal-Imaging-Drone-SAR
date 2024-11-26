# Thermal Imaging Drone for Search and Rescue Operations

## Overview

This project introduces a **thermal imaging drone** designed for efficient search and rescue (SAR) operations. The system integrates a thermal camera with object detection and GPS tracking, enabling real-time location and detection of individuals in disaster zones.

---

## Features

- **Thermal Imaging**: Utilizes FLIR Vue Pro R thermal camera for detecting heat signatures.
- **Object Detection**: YOLOv5 algorithm for real-time identification of individuals.
- **GPS Tracking**: Logs live GPS coordinates of detected persons for easy location.
- **Data Logging**: Saves detected locations as images and CSV files for further analysis.
- **User-Friendly**: Integrated with QGroundControl and Mission Planner for ease of operation.

---

## Hardware Requirements


| Component             | Specifications                   |
| ----------------------- | ---------------------------------- |
| **Drone Frame**       | TAROT X6 Hexacopter frame        |
| **Flight Controller** | Pixhawk Cube Orange with ADS-B   |
| **Thermal Camera**    | FLIR Vue Pro R                   |
| **Gimbal**            | 3D-printed two-axis gimbal       |
| **Battery**           | Tattu 22.2V 25C 6S 22000mAh Lipo |
| **GPS Module**        | Here+ RTK GPS                    |
| **Telemetry**         | RFD 868 ux-IND                   |

---

## Software Requirements

- **Mission Planner**: Ground control station software for configuration and operation.
- **QGroundControl**: Real-time monitoring and data visualization.
- **YOLOv5**: Object detection algorithm for human identification.
- **MySQL**: Database to store GPS coordinates of detections.

---

## Installation and Setup

### 1. Software Setup

- Install Mission Planner ([Guide](https://github.com/sidharthmohannair/Mission-Planner-Installation-using-Mono#readme))
- Install QGroundControl ([Guide](https://docs.qgroundcontrol.com/))
- Set up YOLOv5 ([Guide](https://docs.ultralytics.com/quick-start/#from-pytorch-hub))
- Install MySQL for GPS database creation.

### 2. Hardware Configuration

- Mount and calibrate the thermal camera and gimbal.
- Connect the flight controller, GPS module, and telemetry components.
- Test connections using Mission Planner and QGroundControl.

---

## Usage

1. **Power On**: Ensure all hardware components are connected and powered.
2. **Live Streaming**: Use the Herelink transmitter to stream thermal video.
3. **Run YOLOv5**: Execute the modified `detect.py` to detect humans and log GPS coordinates.
4. **Data Retrieval**: Access detected locations and images in the YOLOv5 output folder.

---

## Results

- Successfully detected and logged human locations in low-visibility conditions.
- Thermal video streaming tested at altitudes of 20m and 40m with accurate detections.
- Stored results as images and CSV files for further analysis.

---

## Testing

- Indoor testing with webcams and thermal camera feeds.
- Outdoor testing at varying altitudes for accuracy and stability.
- Verified GPS logging and image extraction.

---

## Repository Structure

```plaintext
Thermal-Imaging-Drone-SAR
├── Documentation/
├── Hardware/
├── Software/
├── Testing/
├── Results/
└── References/
```

---

## Contributors

- Srinivasan Ravindran - **Project Head**
- Shafeek PM - **Progarm Coodinator**
- Sidharth Mohan Nair - **Project Lead**
- Anooja SK & Jobin J - **Software Integration**
- Sandeep S & Anwar Sherief - **Hardware Design**

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## References

- [YOLOv5 Documentation](https://docs.ultralytics.com/)
- [Mission Planner Guide](https://ardupilot.org/planner/)
- [Herelink User Guide](https://docs.cubepilot.org/)
