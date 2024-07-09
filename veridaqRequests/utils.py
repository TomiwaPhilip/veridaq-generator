def split_text_to_lines(text, min_length=20, max_length=50):
    lines = []
    while text:
        # Determine the length of the next chunk
        chunk_length = min(max_length, len(text))
        
        if chunk_length < min_length:
            chunk_length = min_length
        
        # Extract the chunk but ensure we don't break a word
        line = text[:chunk_length]
        
        if len(text) > chunk_length and text[chunk_length] != ' ':
            last_space = line.rfind(' ')
            if last_space != -1:
                line = line[:last_space]
                chunk_length = last_space

        lines.append(line)
        
        # Remove the chunk from the original text
        text = text[chunk_length:].lstrip()
    
    return lines


# Function definition
def drawLines(lines, x, y, c):
    for i, line in enumerate(lines):
        c.drawString(x, y - i * 17, line)
    