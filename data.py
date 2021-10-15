class Data:
    def writefile(data):
        f = open("result.txt", "a")
        f.write(data)
        f.close
    def writeArray(data):
        for i in range(len(data)):
            Data.writefile(str(data[i]) + ", ")
        Data.writefile("\n") 