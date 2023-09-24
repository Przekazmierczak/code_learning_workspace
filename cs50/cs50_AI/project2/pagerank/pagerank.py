import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # get all possible page's links
    linked_pages_dict = corpus[page]

    # prepare a dictionary
    all_pages_dict = corpus.copy()

    if len(linked_pages_dict) > 0:
        # add chance, to every possible page, to be picked randomly in 1 - damping_factor situation
        random_choose_chance = (1 - damping_factor) / len(all_pages_dict)
        for key in all_pages_dict:
            all_pages_dict[key] = random_choose_chance
        # add chance, to linked pages, to be picked in damping_factor situation
        linked_choose_chance = damping_factor / len(linked_pages_dict)
        for key in linked_pages_dict:
            all_pages_dict[key] += linked_choose_chance
    else: 
        # add chance, to every possible page, to be picked randomly if current page links not other page situation
        random_choose_chance = 1 / len(all_pages_dict)
        for key in all_pages_dict:
            all_pages_dict[key] = random_choose_chance

    return all_pages_dict


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # prepare empty dict
    all_pages_dict = corpus.copy()
    for key in all_pages_dict:
        all_pages_dict[key] = 0

    # get random page from corpus
    page = random.choice(list(corpus.keys()))

    # get page n times and add it to dictionary
    for _ in range(n):
        model = transition_model(corpus, page, damping_factor)
        page = random.choices(list(model.keys()), list(model.values()))[0]
        all_pages_dict[page] += 1 / n

    return all_pages_dict



def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # get new dictionaries
    all_pages_dict = corpus.copy()
    new_ranking = corpus.copy()

    # N - number of all pages
    N = len(all_pages_dict)

    # start by assuming the PageRank of every page is 1 / N
    for key in all_pages_dict:
        all_pages_dict[key] = 1 / N


    while True:
        # loop over all pages
        for key_p in all_pages_dict:
            # list with all pages_i that link to page_p
            key_p_list = []
            for key_i, value_i in corpus.items():
                number_of_links = len(value_i)
                # page that has no links interpreted as having one link for every page in the corpus
                if number_of_links == 0:
                    value = set()
                    for page in all_pages_dict:
                        value.add(page)
                    key_p_list.append([key_i, value])
                # page that has links
                else:
                    if key_p in corpus[key_i]:
                        key_p_list.append([key_i, value_i])
            # update ranking for page_p
            new_ranking[key_p] = (1 - damping_factor) / N
            for item in key_p_list:
                new_ranking[key_p] += damping_factor * (all_pages_dict[item[0]] / len(item[1]))
        
        # check if PageRank value changes by more than 0.001
        check_list = []
        for page in all_pages_dict:
            check = all_pages_dict[page] - new_ranking[page]
            check_list.append(abs(check))
        if max(check_list) <= 0.001:
            return new_ranking

        # update ranking after actual reiteration
        all_pages_dict = new_ranking.copy()



if __name__ == "__main__":
    main()
