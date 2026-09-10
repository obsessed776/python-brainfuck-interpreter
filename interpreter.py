def read_file(filename):
    with open(filename) as file:
        return (
            "".join(file.readlines())
            .strip()
            .replace("\n", "")
            .replace(" ", "")
        )


if __name__ == "__main__":
    print(read_file("helloworld.bf"))
