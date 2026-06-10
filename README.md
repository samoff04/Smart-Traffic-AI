# Smart Traffic AI

A Python + Pygame-based smart traffic simulation system that demonstrates real-time traffic flow, AI-style signal control, emergency vehicle prioritization, and animated road visualization.

---

## Features
- Realistic 3-lane road system with clear UI
- Dynamic car spawning and smooth movement
- Traffic signal system with timed switching
- Emergency vehicle priority handling
- Live statistics (cars passed, active cars)
- Smooth real-time animation (60 FPS)
- Rule-based AI behavior for traffic flow control

---

## How It Works
Cars spawn randomly in lanes and move based on traffic signal state. When the signal is GREEN, cars move; when RED, they stop. Emergency vehicles bypass signal rules. Cars are removed once they exit the screen. The system tracks active cars and total cars passed to simulate traffic flow analysis.

---

## Tech Stack
Python, Pygame, NumPy, Matplotlib

---

## Project Structure
```
Smart-Traffic-AI/
├── main.py
├── car.py
├── signal.py
├── stats.py
├── config.py
├── requirements.txt
└── .gitignore
```

---

## Installation
```
git clone https://github.com/samoff04/Smart-Traffic-AI.git
cd Smart-Traffic-AI
pip install -r requirements.txt
```
## Run Project
```
python main.py
```

---

## Future Improvements
- Congestion heatmap visualization
- Multi-intersection smart city simulation
- Real-time analytics dashboard using matplotlib
- Web-based control panel (React + FastAPI upgrade)

---

## Author

Samarth Varshney