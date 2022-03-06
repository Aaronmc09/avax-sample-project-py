import json
import itertools
import threading
import time
import sys
from objects import AvaxEl33t

done = False


# Command line loading animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')


def write_trait_counts_file(trait_counts: dict):
    with open('files/trait_counts.json', 'w') as fp:
        json.dump(trait_counts, fp, indent=4)


# Sorts trait_counts dictionary
def sort_counts(trait_counts: dict, idx: int = 1, asc: bool = True):
    """
    :param trait_counts: Count dictionary
    :param idx: Sort by name = 0, Sort by value = 1
    :param asc: Ascending order = True, Descending order = False
    :return None;
    """
    for k in trait_counts.keys():
        trait_counts[k] = {i: j for i, j in sorted(trait_counts[k].items(), key=lambda att: att[idx], reverse=not asc)}


def update_count(count_dict: dict, clean_attr: dict):
    for key in clean_attr.keys():
        current_count = 1

        if key not in count_dict.keys():
            count_dict[key] = {
                clean_attr[key]: current_count
            }
            continue

        if clean_attr[key] not in count_dict.get(key).keys():
            count_dict[key].update({
                clean_attr[key]: 1
            })
            continue

        current_count = count_dict[key][clean_attr[key]]
        count_dict[key][clean_attr[key]] = current_count + 1


def avax_script():
    with open('files/metadata_e.json') as f:
        metadata = json.load(f)
        trait_counts: dict = {}

        for nft_data in metadata:
            el33t_nft = AvaxEl33t(**nft_data)
            cleaned_attributes = el33t_nft.clean_attributes()
            update_count(trait_counts, cleaned_attributes)

        sort_counts(trait_counts)  # Optional sorting of attribute counts
        write_trait_counts_file(trait_counts)  # Create or overwrite trait_counts file


if __name__ == '__main__':
    t = threading.Thread(target=animate)
    t.start()

    avax_script()

    done = True
