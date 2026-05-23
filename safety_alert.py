import time
import random
import sys

# Simulate getting current location
def get_current_location():
    # In a real system, this would use GPS or network location services
    # For this example, we'll return a mock location near Istanbul.
    latitude = 41.0082 + random.uniform(-0.01, 0.01) 
    longitude = 28.9784 + random.uniform(-0.01, 0.01)
    return f"Latitude: {latitude:.4f}, Longitude: {longitude:.4f}"

# Simulate sending an emergency notification
def send_emergency_notification(location, contacts):
    print("\n--- EMERGENCY ALERT ---")
    print(f"Sending alert to emergency contacts: {', '.join(contacts)}")
    print(f"Current location: {location}")
    print("Message: 'I need urgent help! My current location is attached.'")
    # In a real system, this would use an SMS API (e.g., Twilio) or email service.
    time.sleep(1) # Simulate network delay
    print("Notification sent successfully!")

# Simulate an audible alarm
def activate_audible_alarm():
    print("\n--- AUDIBLE ALARM ACTIVATED ---")
    print("Playing a loud alarm sound...")
    # In a real system, this would play an actual sound file.
    # For this example, we'll just print a message.
    time.sleep(2) # Simulate alarm duration
    print("Alarm stopped.")

def main():
    print("--- Women's Safety Smart Alert System Simulation ---")
    print("This script simulates an intelligent safety system's response to a threat.")
    print("Press 'p' and Enter to simulate a panic button press.")
    print("Press 'q' and Enter to quit.")

    emergency_contacts = ["+905XX1234567", "emergency@example.com"] # Mock contacts

    while True:
        user_input = input("\nWaiting for panic signal (p/q): ").strip().lower()

        if user_input == 'p':
            print("\nPanic signal received! Initiating smart safety response...")
            # --- Article's core concept: Intelligent, real-time response ---
            current_location = get_current_location() # Get location
            send_emergency_notification(current_location, emergency_contacts) # Notify contacts
            activate_audible_alarm() # Activate local alarm
            # --- End of core concept illustration ---
            print("\nSafety response completed. Stay safe!")
            break # For this simple example, we'll exit after one alert
        elif user_input == 'q':
            print("Exiting simulation. Stay safe!")
            break
        else:
            print("Invalid input. Please press 'p' for panic or 'q' to quit.")

if __name__ == "__main__":
    main()
