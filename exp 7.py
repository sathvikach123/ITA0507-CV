import cv2

video_path = r"C:\Users\SATHVIKA\Downloads\car video.mp4"

cap_slow = cv2.VideoCapture(video_path)
cap_fast = cv2.VideoCapture(video_path)

slow_frame = None
frame_count = 0

while True:
    # Slow motion: only grab a new frame every 3rd loop (repeats same frame in between)
    if frame_count % 3 == 0:
        ret_slow, new_slow_frame = cap_slow.read()
        if not ret_slow:
            break
        slow_frame = new_slow_frame

    # Fast motion: skip frames to speed it up
    ret_fast, fast_frame = cap_fast.read()
    if not ret_fast:
        break
    ret_fast, fast_frame = cap_fast.read()   # skip an extra frame
    if not ret_fast:
        break

    cv2.imshow("Slow Motion", slow_frame)
    cv2.imshow("Fast Motion", fast_frame)

    frame_count += 1

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap_slow.release()
cap_fast.release()
cv2.destroyAllWindows()
