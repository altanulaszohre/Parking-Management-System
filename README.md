# 🅿️ Parking Management System

A real-time parking management system that detects and monitors parking spaces using video processing techniques.

🎥 Demo Video:  
https://user-images.githubusercontent.com/111522957/194763819-b0b0e971-6fa6-4b35-a860-02c81d1fe2ac.mp4

---

## 📌 Features

- 🧠 Detects parked vehicles using image processing
- 🟢 Detects free and occupied slots
- 🔄 Continuously updates status from video stream
- 💾 Slot coordinates customizable (editable with file)

---

## 📁 Project Structure

```
Parking-Management-System/
│
├── Park.py                  # Defines parking space and logic
├── main.py                  # Runs the video processing
├── Car_Park_Pos             # File storing parking slot coordinates
├── README.md
```

---

## 🛠️ How It Works

1. `Car_Park_Pos` contains predefined regions for each parking space
2. Each frame of the video is processed:
   - Background subtraction
   - Area detection
   - Status marking (green for free, red for occupied)
3. Results are updated in real-time on the video feed

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Parking-Management-System.git
   cd Parking-Management-System
   ```

2. Install dependencies:
   ```bash
   pip install opencv-python numpy
   ```

3. Run the system:
   ```bash
   python main.py
   ```

---

## 🎯 Example Output

- Green rectangle → Free slot  
- Red rectangle → Occupied slot

📽️ See it in action:  
https://user-images.githubusercontent.com/111522957/194763819-b0b0e971-6fa6-4b35-a860-02c81d1fe2ac.mp4

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🙌 Acknowledgments

Thanks to the creators of:
- OpenCV
- Python Image Processing Community
