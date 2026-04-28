try:
    with open("file.txt", "a") as f:
        f.write("\nFile 'file.txt' created successfully.")
        
except Exception as e:
    print("Error: File not written.", e)