# Invisibility Cloak Project

## **Introduction**
The Invisibility Cloak project is a fun and engaging application of computer vision using OpenCV. Inspired by fictional cloaking devices, this project detects a specific color (e.g., blue or red) in a video feed and replaces it with a static background, creating the illusion of invisibility.

## **Technologies Used**
- **Programming Language:** Python
- **Libraries:**
  - OpenCV: For image processing and video manipulation.
  - NumPy: For efficient numerical computations.
- **Hardware Requirements:**
  - A webcam or external camera.
  - A computer with Python installed.

## **Features**
- Captures and processes live video feed.
- Detects a specific color range in the video using HSV color space.
- Replaces the detected color with a pre-captured background image.
- Real-time processing for smooth user experience.

## **How It Works**
1. **Capture Background:**
   - The program captures multiple frames of the background without the user in the frame.
   - A median of these frames is computed to create a static background.

2. **Color Detection:**
   - The program converts each video frame to the HSV color space.
   - A mask is created for the specific color range (e.g., blue).

3. **Apply Cloak Effect:**
   - The detected color is replaced with the pre-captured background.
   - The rest of the frame remains unaltered.

4. **Display Result:**
   - The processed video feed is displayed in real-time.

## **Object-Oriented Programming Concepts Used**
- **Encapsulation:**
  - Functions like `create_bg()`, `create_mask()`, and `applycloakeffect()` encapsulate specific tasks.
- **Modular Design:**
  - The project is divided into separate functions for readability and reusability.

## **Software Engineering Concepts**
- **Error Handling:**
  - The program checks for errors in camera initialization and background capture.
- **Code Modularity:**
  - The project follows a modular structure for better maintenance.
- **Scalability:**
  - The code can be extended to include additional features, such as detecting multiple colors.

## **Real-World Applications**
- **Entertainment:**
  - Used in creating special effects for videos and movies.
- **Education:**
  - Demonstrates the power of computer vision and image processing to students.
- **Gaming:**
  - Can inspire augmented reality (AR) applications in gaming.

## **Steps to Run the Project**
1. **Install Required Libraries:**
   ```bash
   pip install opencv-python numpy
   ```

2. **Run the Script:**
   ```bash
   python invisibility_cloak.py
   ```

3. **Usage Instructions:**
   - Wear a cloth of the target color (e.g., blue).
   - Ensure proper lighting for better detection.
   - Press `q` to quit the program.

## **Limitations**
- Performance may vary with lighting conditions.
- May not work well if the cloak color matches other objects in the background.
- Requires a stable camera feed for optimal results.

## **Future Enhancements**
- Add support for detecting multiple colors.
- Improve robustness in varying lighting conditions.
- Integrate with augmented reality (AR) frameworks for advanced applications.

## **Acknowledgments**
- OpenCV documentation and community for providing excellent resources.
- Inspiration from the Harry Potter series for the concept of invisibility cloaks.

---

### **Contact**
For queries or suggestions, feel free to contact the project creator.
