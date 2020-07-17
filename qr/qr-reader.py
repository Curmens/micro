import cv2, png, pyqrcode, argparse, datetime, imutils, time
import os, sys
from pyzbar import pyzbar
from imutils.video import VideoStream


def generate_qr():
    gen_data = input('Enter text to generate qr-code: ')
    generate = pyqrcode.create(gen_data)
    generate.png('code.png', scale=6, module_color=[
                 0, 0, 0, 128], background=[0xff, 0xff, 0xcc])


# generate_qr()

def extract_data():
    image_path = input("Enter the path of your file: ")
    assert os.path.exists(
        image_path), "Could not find the file at location, "+str(image_path)

    img = cv2.imread(image_path)
    barcodes = pyzbar.decode(img)

    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{} ({})".format(barcodeData, barcodeType)
        print(text)
        cv2.putText(img, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        print("[INFO] found {} barcode {}".format(barcodeType, barcodeData))

        cv2.imwrite("generated.jpg", img)

def realtime():
    # initialize the video stream and allow the camera sensor to warm up
    print("[INFO] starting video stream...")
    # vs = VideoStream(src=0).start()
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)
    while True:
        # grab the frame from the threaded video stream and resize it to
        # have a maximum width of 400 pixels
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        # find the barcodes in the frame and decode each of the barcodes
        barcodes = pyzbar.decode(frame)
    pass

print(f"""
[1] Generate QR Code
[2] Scan QR Code
[3] Help
[4] Exit
""")
def home():
    try:
        choices = input('Select an option: ')
        if choices == '1' or choices == 'Generate QR Code':
            generate_qr()
        elif choices == '2' or choices == 'Scan QR Code':
            try:
                extract_data()
            except Exception as e:
                print('An error occured at 0x0100')
                print('Consider checking your file path')
        elif choices == '3' or choices == 'Help':
            print(f"""
            ======================================================================
            To generate QR Code select option 1 and follow the commands associated
            ======================================================================
            To scan QR Code select option 2 and input your absolute file path of the
            QR image
            ======================================================================
            If you are receiving some kind of technical error please restart the 
            application and make sure you have installed all dependencies on the
            requirement.txt file
            Run command: pip install -r requirements.txt
            """)
            home()
        elif choices == '4' or choices == 'Exit':
            print('Closing the application.....')
            time.sleep(2)
            sys.exit()
        else:
            try:
                print("""Something just happend try restarting the application.
                if the problem still persists please visit the help page.
                """)
            except Exception as e:
                print(e)
    except KeyboardInterrupt:
        print('\nClosing the application...')
        time.sleep(3)

home()
