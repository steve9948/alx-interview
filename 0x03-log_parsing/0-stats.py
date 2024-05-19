#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Print the collected statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def handle_interrupt(signum, frame):
    """Handle keyboard interrupt and print statistics."""
    print_stats()
    sys.exit(0)


# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) < 9:
            continue

        try:
            # Extract and validate the required parts
            ip_address = parts[0]
            date = parts[3] + " " + parts[4]
            request = parts[5] + " " + parts[6] + " " + parts[7]
            status_code = int(parts[8])
            file_size = int(parts[9])

            if request != "\"GET /projects/260 HTTP/1.1\"":
                continue

            # Update metrics
            global total_file_size
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        except (ValueError, IndexError):
            continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    handle_interrupt(None, None)

# Print the final stats after exiting the loop
print_stats()
