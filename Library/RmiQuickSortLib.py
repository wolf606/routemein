class quicksort:

    @staticmethod
    def sort(networks: list) -> list:
        return quicksort.sorting(0, len(networks)-1, networks)

    @staticmethod
    def partition(l, r, networks: list) -> int:
        # Last element will be the pivot and the first element the pointer
        pivot, ptr = networks[r].hosts, l
        for i in range(l, r):
            if networks[i].hosts >= pivot:
                # Swapping values smaller than the pivot to the front
                networks[i], networks[ptr] = networks[ptr], networks[i]
                ptr += 1
        # Finally swapping the last element with the pointer indexed number
        networks[ptr], networks[r] = networks[r], networks[ptr]
        return ptr
 
# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.
 
    @staticmethod
    def sorting(l, r, networks: list) -> list:
        if len(networks) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
            return networks
        if l < r:
            pi = quicksort.partition(l, r, networks)
            quicksort.sorting(l, pi-1, networks)  # Recursively sorting the left values
            quicksort.sorting(pi+1, r, networks)  # Recursively sorting the right values
        return networks