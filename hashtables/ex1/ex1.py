#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # get the weights from an array to a hashtable
    # we use the weights themselves as keys
    # index serves as our index getter so we can input the index for the value
    for index, weight in enumerate(weights):
        # if the weight was already inputted once, save both indexes
        if hash_table_retrieve(ht, weight) is not None:
            # save the old index
            old_index = hash_table_retrieve(ht, weight)
            # save both the new and old indexes of the same weight
            hash_table_insert(ht, weight, [index, old_index])
        else:
            hash_table_insert(ht, weight, index)
    
    # get the correct index pair for the two wanted weights
    for weight in weights:
        # if there is a key that is the limit - weight, we have two weights that add up to the limit

        # check if the new weight is itself
        if hash_table_retrieve(ht, limit - weight) and limit - weight == weight:
            # check that we have at least two copies of that weight
            possible_weight_pair = hash_table_retrieve(ht, limit - weight)
            print(possible_weight_pair)
            if len(possible_weight_pair) > 1:
                # if we do, return the two saved indexes
                return hash_table_retrieve(ht, weight)
                # if there aren't at least two, we don't have a pair, return None

        # if the needed weight isn't itself, we just check if the needed weight is keyed
        elif hash_table_retrieve(ht, limit - weight):
            return (hash_table_retrieve(ht, limit - weight), hash_table_retrieve(ht, weight))

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
