import tkinter as tk
from tkinter import filedialog, messagebox

class CaesarCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Decryption Software of Caesar's Upgraded Version")
        
        # Mapping Table
        self.mapping_label = tk.Label(root, text="Letter mapping table:")
        self.mapping_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.mapping_table_frame = tk.Frame(root)
        self.mapping_table_frame.grid(row=0, column=1, padx=5, pady=5)
        
        self.mapping_table_text = tk.Text(self.mapping_table_frame, height=2, width=26, state='normal')
        self.mapping_table_text.pack()
        self.mapping_table_text.insert(tk.END, "abcdefghijklmnopqrstuvwxyz\n")
        self.mapping_table_text.configure(state='disabled')  # Make the first line non-editable
        
        self.mapping_entry = tk.Entry(self.mapping_table_frame, width=26)
        self.mapping_entry.pack()
        self.mapping_entry.insert(0, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
        self.mapping_warning_label = tk.Label(root, text="Please modify the second line of the mapping table", fg="red")
        self.mapping_warning_label.grid(row=0, column=2, padx=5, pady=5)
        
        # Plaintext Text Box with Scrollbar
        self.plaintext_label = tk.Label(root, text="Plaintext:")
        self.plaintext_label.grid(row=1, column=0, padx=5, pady=5)
        
        self.plaintext_frame = tk.Frame(root)
        self.plaintext_frame.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
        
        self.plaintext_text = tk.Text(self.plaintext_frame, height=10, width=50, wrap=tk.WORD)
        self.plaintext_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.plaintext_scrollbar = tk.Scrollbar(self.plaintext_frame, command=self.plaintext_text.yview)
        self.plaintext_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.plaintext_text.config(yscrollcommand=self.plaintext_scrollbar.set)
        
        # Ciphertext Text Box with Scrollbar
        self.ciphertext_label = tk.Label(root, text="Ciphertext:")
        self.ciphertext_label.grid(row=3, column=0, padx=5, pady=5)
        
        self.ciphertext_frame = tk.Frame(root)
        self.ciphertext_frame.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
        
        self.ciphertext_text = tk.Text(self.ciphertext_frame, height=10, width=50, wrap=tk.WORD)
        self.ciphertext_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.ciphertext_scrollbar = tk.Scrollbar(self.ciphertext_frame, command=self.ciphertext_text.yview)
        self.ciphertext_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.ciphertext_text.config(yscrollcommand=self.ciphertext_scrollbar.set)
        
        # Load Ciphertext Button
        self.load_button = tk.Button(root, text="Load ciphertext file", command=self.load_ciphertext)
        self.load_button.grid(row=5, column=2, padx=5, pady=5)
        
        # Decrypt Button
        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt)
        self.decrypt_button.grid(row=5, column=0, padx=5, pady=5)
        
        # Clear Ciphertext Button
        self.clear_button = tk.Button(root, text="Clear ciphertext", command=self.clear_ciphertext)
        self.clear_button.grid(row=5, column=1, padx=5, pady=5)
    
    def load_ciphertext(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                ciphertext = file.read()
                self.ciphertext_text.delete(1.0, tk.END)
                self.ciphertext_text.insert(tk.END, ciphertext)
    
    def decrypt(self):
        key_sentence = self.mapping_entry.get().strip().upper()
        ciphertext = self.ciphertext_text.get(1.0, tk.END).strip()
        if not key_sentence or not ciphertext:
            messagebox.showerror("Error", "Key sentence or ciphertext is empty.")
            return
        
        # Create mapping table
        mapping = self.create_mapping_table(key_sentence)
        
        # Decrypt the ciphertext
        plaintext = self.decrypt_ciphertext(ciphertext, mapping)
        
        self.plaintext_text.delete(1.0, tk.END)
        self.plaintext_text.insert(tk.END, plaintext)
    
    def clear_ciphertext(self):
        self.ciphertext_text.delete(1.0, tk.END)
    
    def create_mapping_table(self, key_sentence):
        key_sentence = ''.join(sorted(set(key_sentence), key=key_sentence.index))
        remaining_letters = [chr(i) for i in range(ord('A'), ord('Z')+1) if chr(i) not in key_sentence]
        mapping = {chr(i+ord('a')): key_sentence[i] if i < len(key_sentence) else remaining_letters[i-len(key_sentence)] for i in range(26)}
        return mapping
    
    def decrypt_ciphertext(self, ciphertext, mapping):
        reverse_mapping = {v: k for k, v in mapping.items()}
        plaintext = ''.join(reverse_mapping.get(char, char) for char in ciphertext)
        return plaintext

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherGUI(root)
    root.mainloop()
