class Textfile:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        return f"Reading text from {self.filename}"

    def close(self):
        return f"closing {self.filename}"


class PDFFile:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        return f"Extracting text from PDF {self.filename}"

    def close(self):
        return f"Closing PDF {self.filename}"


class Webpage:
    def __init__(self, url):
        self.url = url

    def read(self):
        return f"Downloading Content from {self.url}"

    def close(self):
        return f"Closing Connection {self.url}"


def readContent(reader):
    content = reader.read()
    close_message = reader.close()
    return f"{content} | {close_message}"


reader = [
    Textfile("document.txt"),
    PDFFile("presentation.pdf"),
    Webpage("https://example.com"),
]

for reade in reader:
    print(readContent(reade))
