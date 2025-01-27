import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparison function for priority queue to ensure the node with the lower frequency comes first
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_map(text):
    frequency = {}
    for char in text:
        frequency[char] = 1 + frequency.get(char, 0)
    return frequency

def build_huffman_tree(frequency_map):
    # Create a priority queue from the frequency map
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency_map.items()]
    heapq.heapify(priority_queue)
    
    # Combine nodes until the entire tree is built
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        # Create a new merged node and push it back into the priority queue
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_encoding_map(root, path="", encoding_map=None):
    if encoding_map is None:
        encoding_map = {}
    
    # Assign a binary code to each character
    if root.char is not None:
        encoding_map[root.char] = path
    else:
        build_encoding_map(root.left, path + "0", encoding_map)
        build_encoding_map(root.right, path + "1", encoding_map)
    
    return encoding_map

def encode_text(text, encoding_map):
    encoded_output = ""
    for char in text:
        encoded_output += encoding_map[char]
    return encoded_output

def decode_text(encoded_text, root):
    current_node = root
    decoded_output = ""
    
    # Decode the text by navigating the Huffman tree
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decoded_output += current_node.char
            current_node = root
    
    return decoded_output

def check_result(s1, s2):
    print("Test case Passed" if s1 == s2 else "Test case Failed!!!!!")

def read_file_to_string(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {filepath} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
text = "this is an example of how Huffman encoding works"

# Generate frequency map
frequency_map = build_frequency_map(text)
# Build Huffman tree
huffman_tree = build_huffman_tree(frequency_map)
# Generate encoding map
encoding_map = build_encoding_map(huffman_tree)

# Encode and decode the text
encoded_text = encode_text(text, encoding_map)
decoded_text = decode_text(encoded_text, huffman_tree)

# Output results
print("Original:", text)
print("Encoded:", encoded_text)
print("Decoded:", decoded_text)
check_result(text, decoded_text)
