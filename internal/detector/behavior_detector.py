from internal.response.alert_manager import raise_alert

def detect_behavior(event):

    if "tmp" in event:
        raise_alert("Suspicious file activity detected")
