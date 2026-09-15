import easyocr

def extract_text(image_path):
    reader = easyocr.Reader(['sv', 'en'])
    result = reader.readtext(image_path)
    return result

def to_sorted_items(result):
    new_three_in_row = []
    for bbox, text, conf in result:
        new_three_in_row.append((bbox[0][1], bbox[0][0], text))
    sorted_list = sorted(new_three_in_row)
    return sorted_list

def group_into_lines(sorted_list, threshold=10):
    current_line = []
    prev_y = 0
    lines = []

    for y, x, text in sorted_list:
        if y - prev_y > threshold:
            sorted_ = sorted(current_line)
            texts = [t for _, t in sorted_]
            new_line = ' '.join(texts)
            lines.append(new_line)
            current_line = []
            current_line.append((x, text))
        elif y - prev_y < threshold:
            current_line.append((x, text))
        prev_y = y

    new = sorted(current_line)
    word = [t for _, t in new]
    new_line1 = ' '.join(word)
    lines.append(new_line1)

    return lines