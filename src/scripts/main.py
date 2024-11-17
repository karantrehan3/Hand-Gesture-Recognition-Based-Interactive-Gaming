import cv2
import numpy as np
from camera import Camera
from trackbars import Trackbars
from processing import FrameProcessor, ContourProcessor
from control import Control


class MainApp:
    def __init__(self):
        self.camera = Camera()
        self.control = Control()
        self.contour_processor = ContourProcessor(self.control)
        self.top, self.right, self.bottom, self.left = 0, 700, 525, 240
        self.frame_processor = FrameProcessor(
            self.top, self.right, self.bottom, self.left
        )
        self.trackbars = Trackbars()

    def run(self):
        cap = self.camera.initialize_camera()
        self.trackbars.create_trackbars()

        while True:
            try:
                ret, frame = cap.read()
                if not ret:
                    break

                frame, roi, hsv = self.frame_processor.process_frame(frame)
                h, s, v, start = self.trackbars.get_trackbar_values()

                lower_skin = np.array([h, s, v])
                upper_skin = np.array([255, 255, 255])
                mask = cv2.inRange(hsv, lower_skin, upper_skin)
                result = cv2.bitwise_and(roi, roi, mask=mask)
                cv2.imshow("Result", result)

                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
                contours, _ = cv2.findContours(
                    mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
                )
                if contours:
                    self.contour_processor.process_contours(contours, roi, start)

            except Exception as e:
                print(f"An error occurred: {e}")

            if cv2.waitKey(5) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = MainApp()
    app.run()
