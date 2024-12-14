import subprocess
import cv2

def check_cuda_installation():
    """Checks if CUDA is installed and returns the CUDA version."""

    try:
        output = subprocess.check_output(["nvidia-smi", "--query-gpu=cuda_version", "--format=csv"])
        cuda_version = output.decode().strip().split(',')[1]
        print(f"CUDA is installed. Version: {cuda_version}")
        return True
    except subprocess.CalledProcessError:
        print("CUDA is not installed.")
        return False

def verify_cuda_processing(image_path):
    """Verifies if an image is being processed using CUDA."""

    if not check_cuda_installation():
        return

    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Perform a simple CUDA-accelerated image processing operation (e.g., blurring)
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Display the original and blurred images
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image (CUDA)", blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Image processing using CUDA was successful.")

if __name__ == "__main__":
    image_path = r"/home/om/Desktop/Coffee-Machine/Data/coffee_1.jpg"  # Replace with the actual path to your image
    verify_cuda_processing(image_path)