def read_file(filename):
    with open(filename) as file:
        return (
            "".join(file.readlines())
            .strip()
            .replace("\n", "")
            .replace(" ", "")
        )

 
def interpreter(raw_code):
    pass
    
 
if __name__ == "__main__":
    raw_code = read_file("helloworld.bf")
    