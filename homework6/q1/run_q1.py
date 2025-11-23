from merge_sort import merge_sort
from quick_sort import quick_sort
from insertion_sort import insertion_sort

def load_file(path):
    with open(path, "r") as f:
        nums = [int(x) for x in f.read().split()]
    return nums

def demo(path):
    nums = load_file(path)
    print(f"\n==== Input from {path} ====")
    print(nums)

    print("Merge Sort:      ", merge_sort(nums))
    print("Quick Sort:      ", quick_sort(nums))
    print("Insertion Sort:  ", insertion_sort(nums))

if __name__ == "__main__":
    demo("inputs_small.txt")
    demo("inputs_medium.txt")
    demo("inputs_large.txt")
