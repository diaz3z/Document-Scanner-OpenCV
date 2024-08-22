
# Document Scanner using OpenCV

This project is a simple document scanner implemented in Python using OpenCV. It can detect and scan documents from images, providing a warped and cropped view of the document.

## Features

- Document edge detection
- Perspective transformation for a top-down view
- Image preprocessing for improved edge detection
- Real-time processing of images

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Installation

1. Clone this repository:

```bash
git clone https://github.com/diaz3z/Document-Scanner-OpenCV.git

```
2. Install the required dependencies:
```bash
pip install opencv-python numpy

```
## Usage

1. Place your document image in the same directory as the script, named `paper.jpg`.

2. Run the script:
```bash
python main.py

```
3. The script will open two windows:
- 'Windows': Showing the processing steps
- 'Final': Displaying the scanned document

4. Press 'q' to exit the program.

## How It Works

1. **Image Preprocessing**: The input image is converted to grayscale, blurred, and edge-detected using Canny edge detection.

2. **Contour Detection**: The script finds the largest rectangular contour, which is assumed to be the document.

3. **Perspective Transform**: If a valid document contour is found, a bird's-eye view transform is applied.

4. **Display**: The original image, processing steps, and final scanned document are displayed.



https://github.com/user-attachments/assets/483961af-071f-4754-96ef-1a2bf1cc1e79

## Functions

- `preProcess(img)`: Prepares the image for contour detection.
- `getContours(img)`: Finds the document contours in the image.
- `reorder(myPoints)`: Reorders the corner points for proper transformation.
- `getWarp(img, biggest)`: Applies perspective transform to get the top-down view.
- `stackImages(scale, imgArray)`: Combines multiple images for display.

## Limitations

- The script assumes that the document is the largest rectangular object in the image.
- Lighting conditions and background can affect the quality of edge detection.

## Future Improvements

- Implement adaptive thresholding for better edge detection in various lighting conditions.
- Add support for multiple document detection in a single image.
- Implement a GUI for easier user interaction.

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes and commit them
4. Push to your fork and submit a pull request

## License

MIT License

## Acknowledgements

- OpenCV community for their extensive documentation and examples.
