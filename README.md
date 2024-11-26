# Thermal Imaging Drone for Search and Rescue Operations

![Cover Photo SAR Thermal Imaging Drone](/images/SAR-thermal-drone-e.png)

## Overview

This project introduces a **thermal imaging drone** designed for efficient search and rescue (SAR) operations. The system integrates a thermal camera with object detection and GPS tracking, enabling real-time location and detection of individuals in disaster zones.

---

## **Key Features**

- **Thermal Imaging:** FLIR Vue Pro R thermal camera detects heat signatures in real-time, even in low-visibility conditions.  
- **Object Detection:** Utilizes YOLOv5 for accurate and real-time identification of individuals.  
- **Live GPS Tracking:** Logs precise GPS coordinates of detected persons for easy localization.  
- **Data Logging:** Automatically saves detected locations as images and CSV files.  
- **User-Friendly:** Compatible with QGroundControl and Mission Planner for intuitive operation.  

---

## **Hardware Requirements**

| Component              | Specifications                     |
|------------------------|-------------------------------------|
| **Drone Frame**        | TAROT X6 Hexacopter frame          |
| **Flight Controller**  | Pixhawk Cube Orange Plus    |
| **Thermal Camera**     | FLIR Vue Pro R                     |
| **Gimbal**             | Custom 3D-printed two-axis gimbal  |
| **Airunit & Controller** | Herelink 1.1                     |
| **Battery**            | Tattu 22.2V 25C 6S 22000mAh Lipo  |
| **GPS Module**         | Here+ RTK GPS                      |
| **Telemetry**          | RFD 868 ux-IND                     |


---

## Software Requirements

- **Mission Planner**: Ground control station software for configuration and operation.
- **QGroundControl**: Real-time monitoring and data visualization.
- **YOLOv5**: Object detection algorithm for human identification.
- **MySQL**: Database to store GPS coordinates of detections.

---

## Installation and Setup

### 1. Hardware Configuration

- Refer the [wiring diagram](/Hardware/Wiring_Diagram.jpg) for connection
- Connect the flight controller, GPS module, and telemetry components.
- Test connections using Mission Planner and QGroundControl.
- Mount and calibrate the thermal camera and gimbal.

> #### For detailed assembly and configuration instructions, refer to the [Hardware Setup and Configuration](#) document.

### 2. Software Setup and Installation

#### **Step 1: Clone the Repository**
Clone the repository and navigate to the project folder:
```bash
git clone https://github.com/your-repository/Thermal-Imaging-Drone-SAR.git
cd Thermal-Imaging-Drone-SAR
```

#### **Step 2: Software Installation**

- Install Mission Planner ([Guide](https://github.com/sidharthmohannair/Mission-Planner-Installation-using-Mono#readme))
- Install QGroundControl ([Guide](https://docs.qgroundcontrol.com/master/en/qgc-user-guide/getting_started/download_and_install.html))
- Set up YOLOv5 ([Guide](https://github.com/ultralytics/yolov5?tab=readme-ov-file))
- Install MySQL for GPS database creation. ([Guide](/Documentation/Database_Creation_Guide.md))

    > **Note**: As part of the YOLOv5 setup, ensure all Python dependencies are installed using the `requirements.txt` file included in this repository. Run the following command after cloning the repository:
    ```bash
    pip install -r Software/requirements.txt
    ```

#### **Step 3: Organize Code Files**
Move the necessary scripts into their respective folders after installation:
- **YOLOv5 Files**:
  ```bash
  cp Software/detect.py ~/YOLOv5
  cp Software/gps_function.py ~/YOLOv5
  cp Software/plottime.py YOLOv5/
  ```
- **MAVLink Script**:
  ```bash
  cp Software/mavlink_gps_to_sql.py MAVLink/
  ```
---

## **Usage**

### **Standard Operating Procedure (SOP)**
Refer to the detailed [SOP.md](/Documentation/SOP.md) file for a comprehensive guide. Below is a quick summary:

1. **Pre-Flight Preparations**:
   - Verify hardware connections and power on all systems.
   - Use Mission Planner to check GPS signal and system readiness.

2. **Run YOLOv5 Detection**:
   - Start MAVLink GPS logging:
     ```bash
     python3 MAVLink/mavlink_gps_to_sql.py
     ```
   - Start object detection:
     ```bash
     python3 YOLOv5/detect.py --source rtsp://192.168.43.1:8554/fpv_stream --class 0
     ```

3. **Data Retrieval**:
   - Access detected locations, images, and CSV files in the `YOLOv5/detect/exp/` folder.

4. **Post-Flight Operations**:
   - Safely land the drone and back up logs, images, and CSV files.

---

## **Testing and Results**

### **Testing Summary**
- **Indoor Testing**: Verified YOLOv5 with webcam and streamed thermal feeds.
- **Outdoor Testing**: Successfully detected humans at altitudes of 20m and 50m with live GPS tracking.

### **Results**
- Successfully detected and logged human locations in low-visibility conditions.
- Thermal video streaming tested at altitudes of 20m and 40m with accurate detections.
- Stored results as images and CSV files for further analysis.

---

## Repository Structure

```plaintext
Thermal-Imaging-Drone-SAR/
├── Documentation/             # Guides for installation, hardware setup, SOP, and more
│   ├── SOP.md                 # Standard Operating Procedure
│   ├── Hardware_Setup_and_Configuration.md
│   └── Installation_Guides/
├── Hardware/                  # CAD models, components list, and wiring diagrams
│   ├── Components_List.csv
│   ├── 3D_Models/
│   │   └── Gimbal.stl
│   └── Wiring_Diagram.jpg
├── Software/                  # Python scripts and dependencies
│   ├── detect.py
│   ├── gps_function.py
│   ├── plottime.py
│   ├── mavlink_gps_to_sql.py
│   ├── requirements.txt       # Python dependencies
├── YOLOv5/                    # YOLOv5-related files and weights
├── MAVLink/                   # MAVLink-related scripts and configurations
│   └── mavlink_gps_to_sql.py
├── Results/                   # Output results, including images and CSV files
│   ├── Detected_Locations.csv
│   ├── Detected_Images/
└── README.md                  # Main project documentation

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
