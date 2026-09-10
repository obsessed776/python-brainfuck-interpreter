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
            case ",":
                memory[memory_pointer] = int(input("Input: "))
            case "[":
                if memory[memory_pointer] == 0:
                    nestend_index = 1
                    while nestend_index > 0:
                        pointer += 1
                        if raw_code[pointer] == "[":
                            nestend_index += 1
                        elif raw_code[pointer] == "]":
                            nestend_index -= 1
            case "]":
                if memory[memory_pointer] != 0:
                    nestend_index = 1
                    while nestend_index > 0:
                        pointer -= 1
                        if raw_code[pointer] == "]":
                            nestend_index += 1
                        elif raw_code[pointer] == "[":
                            nestend_index -= 1
            case _:
                raise SyntaxError("Wrond command")
                            
        pointer += 1

    
if __name__ == "__main__":
    # raw_code = read_file("hi_python_cyrillic.bf")
    # raw_code = read_file("simple_hello_world.bf")
    # raw_code = read_file("sum_two_numbers.bf")
    raw_code = read_file("helloworld.bf")
    interpreter(raw_code)
