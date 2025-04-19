class Disk:
    def __init__(self, filename="disk_storage.txt"):
        self.filename = filename

    def save(self, data):
        with open(self.filename, "a", encoding="utf-8") as f:
            for entry in data:
                f.write(entry + "\n")
        print(f"Data saved to disk: {data}")

    def read_all(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            return []

    def clear(self):
        open(self.filename, "w", encoding="utf-8").close()
        print("The data on the disk has been cleared.")


class IOBuffer:
    def __init__(self, size, disk):
        self.size = size
        self.buffer = []
        self.disk = disk

    def write(self, data):
        self.buffer.append(data)
        print(f"The data is written to the buffer: {data}")
        if len(self.buffer) >= self.size:
            self.flush()

    def flush(self):
        if self.buffer:
            print("The buffer is full! Clearing...")
            self.disk.save(self.buffer)
            self.buffer.clear()

    def final_flush(self):
        if self.buffer:
            print("Final cleaning before exiting...")
            self.disk.save(self.buffer)
            self.buffer.clear()

    def print_buffer(self):
        if not self.buffer:
            print("Buffer is empty!")
        else:
            print("Current Buffer:")
            for i, item in enumerate(self.buffer, 1):
                print(f"{i}. {item}")

    def print_disk(self):
        data = self.disk.read_all()
        if not data:
            print("There is nothing on the disk yet.")
        else:
            print("Data on the disk:")
            for i, item in enumerate(data, 1):
                print(f"{i}. {item}")


def main():
    buffer_size = 3
    disk = Disk()
    buffer = IOBuffer(buffer_size, disk)

    disk.clear()

    print("\nEnter the data:")
    print("  Just enter the text to add it.")
    print("  'show' — show the buffer")
    print("  'disk' — show the disk")
    print("  'clear disk' — clear the disk")
    print("  'stop' — exit and save the remainder")
    print("  'save' - save the current buffer to disk")

    while True:
        data = input("> ")
        if data.lower() == "stop":
            break
        elif data.lower() == "show":
            buffer.print_buffer()
        elif data.lower() == "disk":
            buffer.print_disk()
        elif data.lower() == "clear disk":
            disk.clear()
        elif data.lower() == "save":
            buffer.final_flush()
        else:
            buffer.write(data)

    buffer.final_flush()
    print("All data is saved. The program is completed.")


if __name__ == "__main__":
    main()
