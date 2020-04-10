#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    first_airport = "NONE"
    # insert the tickets into the hashtable with source-destination as the key-value pair
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        # find and save the first airport we need to go to
        if ticket.source == "NONE":
            first_airport = ticket.destination
    
    current_airport = first_airport
    for i in range(len(route)):
        # put the current_airport in the route array
        route[i] = current_airport
        # get the next place we are going
        current_airport = hash_table_retrieve(hashtable, current_airport)
    # return all but the last element of route as that is still None
    return route[:-1]
