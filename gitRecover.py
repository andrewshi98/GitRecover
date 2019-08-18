import subprocess

deletedHashList = "./hash.temp"

outHash = open(deletedHashList, "w")
subprocess.run(['git', 'prune', '-n'], stdout=outHash)
outHash.close()

contains = input("file contains:")

with open(deletedHashList, mode='r') as f:
    for line in f:
        # Remove last 5 character, aka ' blob'
        hash = line[:-6] 
        process = subprocess.run(['git', 'cat-file', '-p', hash], stdout=subprocess.PIPE)
        try:
            output = process.stdout.decode("utf-8")
            if contains in output :
                print(output)
                input("Press Enter to continue...")
        except:
            continue
