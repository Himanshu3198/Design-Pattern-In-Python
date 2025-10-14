from typing import Set,List



def basic_set():
    st : Set[int] = set()
    st.add(5)
    st.add(10)
    st.add(123)
    st.add(2323)
    st.add(5)
    st.add(5)
    st.add(10)
    st.remove(5)
    print(st)
    if 5 in st:
        print("yes")
    if 2 not in st:
        print("yes not present")
    lst = [i for i in st]
    print(lst)

def set_with_list():

    st : set[frozenset[int]] = set()

    st.add(frozenset([1,2,3,4]))
    st.add(frozenset([2,3,4,1]))
    st.add(frozenset([1,55,21]))
    st.add(frozenset([55,100]))
    st.remove(frozenset([55,100]))
    print(st)
    if frozenset([1,2,3,4]) in st:
        print(f"yes its there:{[1,2,3,4]}")
    else :
        print("no its there")

    for item in st:
        print(item)


if __name__ == "__main__":
    # basic_set()
    set_with_list()
