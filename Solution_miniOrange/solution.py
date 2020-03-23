"""This File Contains Solution Class containing Solution to the given challenge"""
import heapq as heap  # importing  heapq library containing Heap DS methods
# pylint: disable-msg = R0903, W0702

class Solution:
    """This Class Contain Static function to merge InputStream"""
    @staticmethod
    def merge(input_streams, o_streams):
        """
        Function to merge streams
        :param input_streams: Stream containing lists of variable length
        :param o_streams: single list containing all the merged lists
        :return:
        """
        output_streams = list()  # Heap List to insert all elements
        no_lists = len(input_streams)  # Save the no.list
        size_list = list()  # Save the no. of element per list
        for i in range(0, no_lists):  # Loop to save length. in size_list
            size_list.append(len(input_streams[i]))

        max_iter = max(size_list)  # Maximum iteration required
        for i in range(0, max_iter):
            for j in range(0, no_lists):
                if i < size_list[j]:
                    try:
                        heap.heappush(output_streams, input_streams[j][i])  # insert no. in HEAP
                    except:
                        print("Error !! Cannot insert element in HEAP")
                        return
        for i in range(0, len(output_streams)): # POP() HEAP element lowest number to Output Stream
            o_streams.append(heap.heappop(output_streams))
        return

if __name__ == "__main__":
    # Input Stream
    STREAM = [[1, 10, 15, 17, 20, 23, 24],
              [2, 7, 9, 11, 22, 25],
              [3, 8, 13, 18],
              [4, 6, 12, 19],
              [5, 14, 16, 21]]

    O_STREAM = list()  # Output Stream
    Solution.merge(STREAM, O_STREAM)  # Calling of function to Merge the Streams
    print(O_STREAM)  # Print OUTPUT
