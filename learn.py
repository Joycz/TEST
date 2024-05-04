import time
def wait():
    for i in range(60 * 1):
        time.sleep(1)
        print("Chờ : " + str(i), end='\r')
        i += 1
    return

print("Hết nhiệm vụ. Vui lòng chờ")
wait()