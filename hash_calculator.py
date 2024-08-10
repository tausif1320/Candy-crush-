import tkinter as tk
import hashlib

def calculate_hashes():
    # Get text from entry
    text = text_entry.get().encode()

    # Calculate hashes
    md5_hash = hashlib.md5(text).hexdigest()
    sha1_hash = hashlib.sha1(text).hexdigest()
    sha256_hash = hashlib.sha256(text).hexdigest()

    # Update labels with hash results
    md5_result.config(text=md5_hash)
    sha1_result.config(text=sha1_hash)
    sha256_result.config(text=sha256_hash)

    # Start the animation
    animate_result(md5_result)
    animate_result(sha1_result)
    animate_result(sha256_result)

def animate_result(label):
    label.config(bg="yellow")  # Highlight color
    root.after(500, lambda: label.config(bg="white"))  # Revert after 500 ms

# Create the main window
root = tk.Tk()
root.title("Simple Hash Calculator")
root.geometry("400x300")
root.configure(bg="white")

# Create and place widgets
tk.Label(root, text="Enter text:", font=("Arial", 12)).pack(pady=10)

text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=10)

tk.Button(root, text="Calculate Hash", command=calculate_hashes).pack(pady=10)

# Result labels
tk.Label(root, text="MD5:").pack(anchor="w", padx=10, pady=5)
md5_result = tk.Label(root, text="", bg="white", font=("Arial", 12))
md5_result.pack(fill="x", padx=10)

tk.Label(root, text="SHA-1:").pack(anchor="w", padx=10, pady=5)
sha1_result = tk.Label(root, text="", bg="white", font=("Arial", 12))
sha1_result.pack(fill="x", padx=10)

tk.Label(root, text="SHA-256:").pack(anchor="w", padx=10, pady=5)
sha256_result = tk.Label(root, text="", bg="white", font=("Arial", 12))
sha256_result.pack(fill="x", padx=10)

# Start the Tkinter event loop
root.mainloop()
