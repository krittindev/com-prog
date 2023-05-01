
def count_in_list(w, l):
    count = 0
    for e in l:
        if w == e:
            count += 1
    return count


def cal_search(w, t):
    l, s = t
    return count_in_list(w, l) / len(l) * 1 / len(s)


def top_search(w, pages):
    top_page = {"page": "NOT FOUND", "score": 0.0}
    for page_name, t in pages.items():
        cal = cal_search(w, t)
        if cal > top_page["score"]:
            top_page = {"page": page_name, "score": cal}
    return top_page["page"]


def main():
    pages = {}
    n_pages = int(input().strip())

    for _ in range(n_pages):
        page_name = input().strip()
        page_words = input().strip().split()
        pages[page_name] = (tuple(page_words), set(page_words))

    while True:
        search = input().strip()
        if search == "-1":
            break
        print(top_search(search, pages))


main()
