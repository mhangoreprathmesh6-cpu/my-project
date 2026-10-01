# AI-Based Health & Nutrition Tracking System

## 📌 Project Overview

The **AI-Based Health & Nutrition Tracking System** is an intelligent web-based application designed to help users monitor their daily food intake, nutrition, health metrics, and lifestyle patterns.

The system uses **Artificial Intelligence and Computer Vision** to detect food items from uploaded images using **YOLOv8**. After detecting the food, the system retrieves nutritional information and provides personalized diet recommendations based on the user's **BMI**.

The application is developed using **Python Flask**, **HTML, CSS, JavaScript**, and **MySQL**.

---

## 🎯 Objectives

* Detect food items automatically from images using YOLOv8.
* Reduce manual food entry.
* Track daily calorie and nutrition intake.
* Calculate Body Mass Index (BMI).
* Provide personalized diet recommendations.
* Track health and lifestyle progress.
* Provide secure user authentication.
* Store user and nutrition data in a MySQL database.
* Provide an admin dashboard for managing users and data.

---

## ✨ Key Features

### 👤 User Authentication

* User registration
* User login
* Secure authentication
* User-specific health data

### 🍎 Food Detection

* Upload a food image.
* Detect food items using YOLOv8.
* Display detected food labels.
* Apply confidence threshold to improve detection.

### 🥗 Nutrition Analysis

The system retrieves nutritional information for detected food items, including:

* Calories
* Protein
* Other nutritional values

The nutrition information is mapped using a structured food dataset/CSV.

### ⚖️ BMI Calculation

BMI is calculated using:

```text
BMI = Weight / (Height × Height)
```

Based on BMI, the system provides suitable diet recommendations.

### 🏃 Health Tracking

The system tracks:

* Daily calories
* Water intake
* Weekly consistency
* Health progress

### 🤖 AI Diet Recommendation

The system provides diet recommendations based on BMI:

| BMI Range  | Recommendation   |
| ---------- | ---------------- |
| Below 18.5 | Weight Gain Diet |
| 18.5 – 25  | Balanced Diet    |
| Above 25   | Weight Loss Diet |

### 👨‍💼 Admin Dashboard

The administrator can manage:

* Users
* User data
* Food-related information
* System records

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Database

* MySQL

### Artificial Intelligence

* YOLOv8
* CNN
* ResNet-based classifier

### Data

* CSV / Structured Nutrition Dataset

---

## 🏗️ System Architecture

```text
User
  ↓
Web Application
  ↓
Flask Server
  ↓
YOLOv8 AI Model
  ↓
Food Detection
  ↓
Nutrition Dataset
  ↓
MySQL Database
  ↓
Health Analysis
  ↓
Diet Recommendation
  ↓
User Dashboard
```

---

## 🔄 System Workflow

```text
1. User Login/Register
        ↓
2. Upload Food Image
        ↓
3. YOLOv8 Detects Food
        ↓
4. Food Name Identified
        ↓
5. Nutrition Data Retrieved
        ↓
6. Calories & Nutrition Calculated
        ↓
7. Data Stored in MySQL
        ↓
8. BMI Calculated
        ↓
9. Diet Recommendation Generated
        ↓
10. Results Displayed on Dashboard
```

---

## 📦 Project Modules

### 1. User Authentication Module

Handles registration, login, and user authentication.

### 2. Food Detection Module

Uses YOLOv8 to identify food items from uploaded images.

### 3. Nutrition Analysis Module

Maps detected food items with nutritional information from the dataset.

### 4. Health Tracking Module

Tracks calories, water intake, and health progress.

### 5. AI Diet Recommendation Module

Generates personalized diet recommendations using BMI-based logic.

### 6. Admin Dashboard

Allows administrators to manage users and system data.

---

## 🧠 AI Algorithms

### YOLOv8 Food Detection

**Input:** Food image

**Output:** Detected food objects with labels and bounding boxes.

A confidence threshold is used to filter low-confidence detections.

### Nutrition Calculation

Nutrition values are calculated using the detected food item and its corresponding nutritional information.

```text
Nutrition = Base Nutritional Value × Portion Size
```

### BMI Calculation

```text
BMI = Weight / Height²
```

### Health Score

The health score is based on factors such as:

* Calorie intake
* Water intake
* Weekly consistency

---

## 🗃️ Database Design

### Users

```text
Users
----------------
id
name
email
password
```

### Food History

```text
Food_History
----------------
user_id
food
calories
protein
```

### Tracking

```text
Tracking
----------------
calories
water
```

---

## 📊 Data Flow

```text
Input Food Image
       ↓
YOLOv8 Detection
       ↓
Food Identification
       ↓
Nutrition Mapping
       ↓
Database Storage
       ↓
Health Analysis
       ↓
Dashboard Display
```

---

## 📋 Requirements

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the Python dependencies required to run the project.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the Project Folder

```bash
cd finalMega_project
```

### 3. Create Virtual Environment

```bash
python -m venv myenv
```

### 4. Activate Virtual Environment

For Windows:

```bash
myenv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL

Create the required MySQL database and configure the database credentials in the project configuration.

**Do not upload database passwords or secret keys to GitHub.**

### 7. Run the Flask Application

```bash
python app.py
```

Then open the local URL displayed in the terminal.

---

## 🔐 Security

The project follows basic security practices such as:

* User authentication
* Database-based user management
* Environment variables for sensitive configuration
* `.gitignore` to prevent sensitive files from being uploaded

---

## 🚀 Future Enhancements

Future improvements can include:

* Mobile application
* Advanced AI-based diet recommendations
* Wearable device integration
* Real-time health monitoring
* Improved portion-size estimation
* More accurate nutrition prediction
* Voice-based food logging
* Personalized meal planning
* Cloud deployment

---

## 📈 Advantages

* Automated food recognition
* Reduces manual food entry
* Personalized diet recommendations
* Nutrition and calorie tracking
* Health progress monitoring
* AI-powered food detection
* Centralized data management

---

## 🎓 Project Purpose

This project demonstrates the practical integration of:

* Artificial Intelligence
* Computer Vision
* Machine Learning
* Python
* Flask
* MySQL
* Web Development

It can be used as an academic/final-year project demonstrating an AI-powered health and nutrition management system.

---

## 👨‍💻 Author

**Omkar Udale**

---

## ⭐ Conclusion

The AI-Based Health & Nutrition Tracking System combines **AI-based food detection, nutrition analysis, BMI calculation, health tracking, and personalized diet recommendations** into a single web application.

The system aims to make nutrition tracking easier, faster, and more personalized through Artificial Intelligence and web technologies.
