import cv2
import os
import time

# creates folder for image class i
# the app opens up
# saves a frame every 2 seconds, it'll save a total of 100 
# it'll countdown from 1 - 10 when it's time to take shots for class i + 1
# after number of classes is complete. it'll destroy the app

def main():
    image_capture()
   


def image_capture():
    # make sure you're in the folder you want to store the images
    main_cwd = os.getcwd()
    os.chdir(main_cwd) #change directory to current working directory

    # collect user input for what to name folder
    folder_name = input("folder name: ")
    os.mkdir(folder_name)
    folder_path = os.path.join(main_cwd,folder_name)
    os.chdir(folder_path)
    # collect number of classes from user
    num_classes = int(input("How many classes are there? "))

    for i in range(num_classes):
        class_name = input(f"Name class {i}: ") # class i in range num_class
        os.mkdir(class_name) # make class folder
        os.chdir(os.path.join(folder_path,class_name)) #change to current class directory

        print(f"Staring Class {i}...")
        time.sleep(5)

        # start up camera
        capture = cv2.VideoCapture(0)
        image_count = int(input("How many Images: ")) # to name the files
        last_captured = time.time()
        capture_freq = 1
        
        
        while True:
            ret, frame = capture.read()

            recent_captured = time.time()
            cv2.imshow("Video", frame)

            if (recent_captured - last_captured >= capture_freq and image_count >= 0):
                cv2.imwrite(f"{class_name}_{image_count - 1}.png", frame)
                last_captured = recent_captured
                image_count -= 1

            # to quit
            if cv2.waitKey(1) == ord("q") or image_count <= 1:
                break

        print(f"...Stoppig Class {i}")

        capture.release()
        cv2.destroyAllWindows()

        

        # go to root directory
        os.chdir(folder_path)
    
    

if __name__ == "__main__":
    main()

