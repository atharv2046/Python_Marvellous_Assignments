import sys 

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python script.py <source_file>")
    else:
        source_file = sys.argv[1]  
        new_file = "Demo.txt"    

    try:
       
        with open(source_file, 'r') as src, open(new_file, 'w') as new:
            content = src.read()     
            new.write(content)     
        print("Contents of " + source_file + " copied to " + new_file)
    except FileNotFoundError:
        print(source_file + " not found.")



if __name__ == "__main__":
    main()