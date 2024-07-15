import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check for empty inputs
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Process each attendee and generate output files
    for i, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values, use "N/A" if data is missing
        output_content = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )
        
        # Write to output file
        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)
