from internal.detector.behavior_detector import detect_behavior

def collect_event(event):

    print("[EVENT]", event)
    detect_behavior(event)
