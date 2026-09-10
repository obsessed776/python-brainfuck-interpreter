def read_file(filename):
    with open(filename) as file:
        return (
            "".join(file.readlines())
            .strip()
            .replace("\n", "")
            .replace(" ", "")
        )

 
def interpreter(raw_code):
    memory = [0] * 30_000
    memory_pointer = 0
    pointer = 0
    
    while pointer < len(raw_code):
        instruction = raw_code[pointer]

        match instruction:
            case ">":
                memory_pointer += 1
            case "<":
                memory_pointer -= 1
            case "+":
                memory[memory_pointer] += 1
            case "-":
                memory[memory_pointer] -= 1
            case ".":
                print(chr(memory[memory_pointer]), end="")
            
        pointer += 1

    
if __name__ == "__main__":
    raw_code = read_file("helloworld.bf")
    interpreter(raw_code)
