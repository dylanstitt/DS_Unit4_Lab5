##### Global color variables #####
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''


##################################

def TEST_privacy(Qobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Privacy{W}\n")

    try:
        Qobj._Queue__queue
        print(f"{W}Queue array is private: {G}PASSED{W}")
    except:
        print(f"{W}Queue array is private: {R}FAILED{W}")

    try:
        Qobj._Queue__size
        print(f"{W}Queue size is private: {G}PASSED{W}")
    except:
        print(f"{W}Queue size is private: {R}FAILED{W}")

    try:
        Qobj._Queue__capacity
        print(f"{W}Queue capacity is private: {G}PASSED{W}")
    except:
        print(f"{W}Queue capacity is private: {R}FAILED{W}")

    try:
        Qobj._Queue__front
        print(f"{W}Queue front is private: {G}PASSED{W}")
    except:
        print(f"{W}Queue front is private: {R}FAILED{W}")

    try:
        Qobj._Queue__is_empty()
        print(f"\n{W}is_empty() is private: {G}PASSED{W}")
    except:
        print(f"\n{W}is_empty() is private: {R}FAILED{W}")

    try:
        Qobj.resize()
        print(f"{W}resize() is private: {R}FAILED{W}")
    except:
        print(f"{W}resize() is private: {G}PASSED{W}")

    print("~" * 50, "\n\n")


def TEST_new_q(Qobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Queue Creation{W}\n")

    print(f"{B}Initial Queue: {Qobj}{W}\n")

    test = len(Qobj) == 0
    if test:
        print(f"Initial queue contains ZERO elements: {G}PASSED{W}")
    else:
        print(f"Initial queue contains ZERO elements: {R}FAILED{W}")

    test = str(Qobj) == "FRONT> <BACK"
    if test:
        print(f"Correct to-string method: {G}PASSED{W}")
    else:
        print(f"Correct to-string method: {R}FAILED{W}")

    cap = Qobj._Queue__capacity
    front = Qobj._Queue__front
    q = Qobj._Queue__queue

    test = cap == 5
    if test:
        print(f"New queue has a capacity of 5: {G}PASSED{W}")
    else:
        print(f"New queue has a capacity of 5: {R}FAILED{W}")

    test = front == 0
    if test:
        print(f"New queue's front is index 0: {G}PASSED{W}")
    else:
        print(f"New queue's front is index 0: {R}FAILED{W}")

    try:
        Qobj.first()
        print(f"first() unavailable with empty queue: {R}FAILED{W}")
    except:
        print(f"first() unavailable with empty queue: {G}PASSED{W}")

    print("~" * 50, "\n\n")


def TEST_enqueue(Qobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Enqueue{W}\n")

    Qobj.enqueue("A")
    Qobj.enqueue("B")
    Qobj.enqueue("C")
    print(f"{B}Queue of 3 elements: {Qobj}{W}\n")

    cap = Qobj._Queue__capacity
    front = Qobj._Queue__front
    q = Qobj._Queue__queue

    test = True
    for i, el in enumerate("ABC"):
        if q[i] != el:
            test = False

    if test:
        print(f"Elements added to back: {G}PASSED{W}")
    else:
        print(f"Elements added to back: {R}FAILED{W}")

    test = len(Qobj) == 3
    if test:
        print(f"Enqueue affects size: {G}PASSED{W}")
    else:
        print(f"Enqueue affects size: {R}FAILED{W}")

    for el in "WXYZ":
        Qobj.enqueue(el)

    print(f"\n{B}Queue of 7 elements: {Qobj}{W}\n")

    cap = Qobj._Queue__capacity
    front = Qobj._Queue__front
    q = Qobj._Queue__queue

    test = cap == 10
    if test:
        print(f"Capacity doubles when queue is full: {G}PASSED{W}")
    else:
        print(f"Capacity doubles when queue is full: {R}FAILED{W}")

    test = front == 0
    if test:
        print(f"Queue's front not affected by enqueue: {G}PASSED{W}")
    else:
        print(f"Queue's front not affected by enqueue: {R}FAILED{W}")

    print("~" * 50, "\n\n")


def TEST_dequeue(Qobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Dequeue{W}\n")

    print(f"{B}Initial Queue: {Qobj}    {len(Qobj)} elements{W}\n")

    ele = Qobj.dequeue()
    cap = Qobj._Queue__capacity
    front = Qobj._Queue__front
    q = Qobj._Queue__queue

    test = ele == "A"
    if test:
        print(f"Dequeue returns a value: {G}PASSED{W}")
    else:
        print(f"Dequeue returns a value: {R}FAILED{W}")

    test = front == 1 and Qobj.first() == "B"
    if test:
        print(f"Front is affected by dequeue: {G}PASSED{W}")
    else:
        print(f"Front is affected by dequeue: {R}FAILED{W}")

    test = len(Qobj) == 6
    if test:
        print(f"Dequeue affects size: {G}PASSED{W}")
    else:
        print(f"Dequeue affects size: {R}FAILED{W}")

    test = cap == 10
    if test:
        print(f"Dequeue does not affect capacity: {G}PASSED{W}")
    else:
        print(f"Dequeue does not affect capacity: {R}FAILED{W}")

    print(f"\n{B}Updated Queue: {Qobj}    {len(Qobj)} elements{W}\n")

    for i in range(len(Qobj)):
        Qobj.dequeue()
        print(f"{B}Edited Queue: {Qobj}    {len(Qobj)} elements{W}")

    print(f"\n{B}Queue was emptied{W}\n")
    cap = Qobj._Queue__capacity
    front = Qobj._Queue__front
    q = Qobj._Queue__queue

    test1 = front == 7
    test2 = cap == 10
    test3 = len(Qobj) == 0

    test = test1 and test2 and test3
    if test:
        print(f"Queue can be emptied successfully: {G}PASSED{W}")
    else:
        print(f"Queue can be emptied successfully: {R}FAILED{W}")

    try:
        Qobj.dequeue()
        print(f"Dequeue from empty queue raises exception: {R}FAILED{W}")
    except:
        print(f"Dequeue from empty queue raises exception: {G}PASSED{W}")

    test = True
    for el in q:
        if el != None:
            test = False
    if test:
        print(f"Elements removed from queue are replaced with None: {G}PASSED{W}")
    else:
        print(f"Elements removed from queue are replaced with None: {R}FAILED{W}")

    print("~" * 50, "\n\n")


def TEST_enqueue2(Qobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Enqueue Again{W}\n")

    Qobj.enqueue("L")
    cap = Qobj._Queue__capacity
    front = Qobj._Queue__front
    q = Qobj._Queue__queue

    print(f"{B}Updated Queue: {Qobj}    {len(Qobj)} elements{W}\n")

    test = len(Qobj) == 1 and Qobj.first() == "L" and front == 7
    if test:
        print(f"Dequeue does not hinder enqueue process: {G}PASSED{W}\n")
    else:
        print(f"Dequeue does not hinder enqueue process: {R}FAILED{W}\n")

    for el in "MNOPQRSTU":
        Qobj.enqueue(el)
        print(f"{B}Edited Queue: {Qobj}    {len(Qobj)} elements{W}")

    print(f"\n{B}Queue filled to capacity{W}\n")

    cap = Qobj._Queue__capacity
    front = Qobj._Queue__front
    q = Qobj._Queue__queue

    test = len(Qobj) == cap == 10
    if test:
        print(f"Queue was not resized: {G}PASSED{W}")
    else:
        print(f"Queue was not resized: {R}FAILED{W}")

    test = q[front - 1] == "U" and q[front] == "L"
    if test:
        print(f"Queue was populated circularly: {G}PASSED{W}")
    else:
        print(f"Queue was populated circularly: {R}FAILED{W}")

    print("~" * 50, "\n\n")


def TEST_resize(Qobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Resize{W}\n")

    cap = Qobj._Queue__capacity
    front = Qobj._Queue__front
    q = Qobj._Queue__queue

    print(f"{B}Initial Queue: {Qobj}\nQueue Array: {q}")
    print(f"First: {Qobj.first()}\nFront Pointer: {front}")
    print(f"Size: {len(Qobj)}\nCapacity: {cap}{W}\n")

    Qobj.enqueue("V")
    cap = Qobj._Queue__capacity
    front = Qobj._Queue__front
    q = Qobj._Queue__queue

    test = cap == 20
    if test:
        print(f"Capacity was doubled: {G}PASSED{W}")
    else:
        print(f"Capacity was doubled: {R}FAILED{W}")

    test = front == 0
    if test:
        print(f"Front pointer returns to index 0: {G}PASSED{W}")
    else:
        print(f"Front pointer returns to index 0: {R}FAILED{W}")

    test = Qobj.first() == "L"
    if test:
        print(f"The queue's first element is preserved: {G}PASSED{W}")
    else:
        print(f"The queue's first element is preserved: {R}FAILED{W}")

    test = True
    for i, el in enumerate("LMNOPQRSTUV"):
        if q[i] != el:
            test = False
    if test:
        print(f"Queue elements were reordered during resize: {G}PASSED{W}")
    else:
        print(f"Queue elements were reordered during resize: {R}FAILED{W}")

    print(f"\n{B}Final Queue: {Qobj}\nQueue Array: {q}")
    print(f"First: {Qobj.first()}\nFront Pointer: {front}")
    print(f"Size: {len(Qobj)}\nCapacity: {cap}{W}\n")

    print("~" * 50, "\n\n")


def TEST_docs(Qobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")

    doc = Qobj.enqueue.__doc__
    if doc != None:
        print(f"{B}Enqueue Documentation:{W} {doc}\n")
    else:
        print(f"{R}Enqueue Documentation Missing{W}\n")

    doc = Qobj.dequeue.__doc__
    if doc != None:
        print(f"{B}Dequeue Documentation:{W} {doc}\n")
    else:
        print(f"{R}Dequeue Documentation Missing{W}\n")

    doc = Qobj.first.__doc__
    if doc != None:
        print(f"{B}First Documentation:{W} {doc}\n")
    else:
        print(f"{R}First Documentation Missing{W}\n")

    doc = Qobj._Queue__resize.__doc__
    if doc != None:
        print(f"{B}Resize Documentation:{W} {doc}\n")
    else:
        print(f"{R}Resize Documentation Missing{W}\n")

    doc = Qobj._Queue__is_empty.__doc__
    if doc != None:
        print(f"{B}Is Empty Documentation:{W} {doc}\n")
    else:
        print(f"{R}Is Empty Documentation Missing{W}\n")

    doc = Qobj.__len__.__doc__
    if doc != None:
        print(f"{B}Len Documentation:{W} {doc}\n")
    else:
        print(f"{R}Len Documentation Missing{W}\n")

    doc = Qobj.__str__.__doc__
    if doc != None:
        print(f"{B}Str Documentation:{W} {doc}\n")
    else:
        print(f"{R}Str Documentation Missing{W}\n")

    print("~" * 50, "\n\n")