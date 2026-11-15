THRESHOLD = 5 

def count_failed(filename): 
    counts = {}
    with open(filename) as f: 
        for line in f: 
            parts = line.split()
            status = parts[2]
            ip = parts[3]
            if status == "FAILED": 
                counts[ip] = counts.get(ip, 0) + 1 
    return counts


if __name__ == "__main__": 
    counts = count_failed("sample.log") 
    print(counts)

    for ip in counts: 
        if counts[ip] > THRESHOLD: 
            print("WARNING:", ip, "has", counts[ip], "failed logins")
