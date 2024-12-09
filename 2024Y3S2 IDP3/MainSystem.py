from systemvars import *

def handle_states(distance, threshold_distance):

    hand_detected = distance < threshold_distance

    # State Logic
    if state == 1:
        if hand_detected:
            print("Hand detected. Preparing to open door.")
            time.sleep(0.5)  # Simulate delay for hand detection
            state = 2  # Move to State 2
            print("Door opening...")  # Placeholder for door opening logic
            m2f(2)
    elif state == 2:
        if hand_detected:
            print("Door closing...")
            m2r(2)
            state = 3  # Move to State 3
    elif state == 3:
        conveyor()
    elif state == 4:
        print("Door opening...")  # Placeholder for door opening logic
        m2f(2)
        m1r(4)
        state = 5
    elif state == 5:
        if hand_detected:
            print("Door closing...")
            m2r(2)
            state = 1

handle_states(ultrasonicbutton, 5)
