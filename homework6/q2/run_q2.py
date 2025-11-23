from radix_sort import radix_sort


def load_file(path):
    with open(path, "r") as f:
        nums = [int(x) for x in f.read().split()]
    return nums


def demo(path):
    nums = load_file(path)
    print(f"\n==== Input from {path} ====")
    print(nums)

    sorted_nums = radix_sort(nums)
    print("Radix Sort result:")
    print(sorted_nums)


if __name__ == "__main__":
    demo("inputs_small.txt")
    demo("inputs_medium.txt")
    demo("inputs_large.txt")
