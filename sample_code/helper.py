def process_data(text_lines):
  """
  Processes a list of strings: reverses each line and adds a prefix.

  Args:
    text_lines: A list of strings.

  Returns:
    A list of processed strings.
  """
  processed = []
  for line in text_lines:
    processed.append("processed: " + line.strip()[::-1])
  return processed
