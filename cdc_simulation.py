import json
import time
import random
from datetime import datetime

def generate_cdc_event():
    """Generate a simulated CDC event with random data."""
    event_types = ['INSERT', 'UPDATE', 'DELETE']
    tables = ['users', 'orders', 'products', 'inventory']
    
    event = {
        'timestamp': datetime.utcnow().isoformat(),
        'event_type': random.choice(event_types),
        'table': random.choice(tables),
        'data': {
            'id': random.randint(1000, 9999),
            'value': random.randint(1, 100),
            'status': random.choice(['active', 'pending', 'completed'])
        }
    }
    return event

def main():
    """Main function to generate and print CDC events."""
    print("Starting CDC simulation...")
    try:
        while True:
            event = generate_cdc_event()
            print(json.dumps(event))
            time.sleep(0.1)  # Generate events every 100ms
    except KeyboardInterrupt:
        print("\nCDC simulation stopped.")

if __name__ == "__main__":
    main() 