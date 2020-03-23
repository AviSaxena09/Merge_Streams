"""This File Contains Solution2 Class containing Solution to the given challenge"""
import heapq as heap  # importing  heapq library containing Heap DS methods


class Solution2:
    """This Class Contain Static function to merge InputStream"""

    @staticmethod
    def merge_two_streams(lst1, lst2):
        """
        merge two string comparing elements of the list one by one
        :param lst1:
        :param lst2:
        :return:
        """
        merged_stream = list()
        lst1.extend(lst2)  # Sorted list after merging lst1+lst2
        heap.heapify(lst1)
        for i in range(0,len(lst1)):
            merged_stream.append(heap.heappop(lst1))
        return merged_stream

    @staticmethod
    def merge(input_streams):
        """
        call merge_two_streams() by passing 2 arrays at a time and then merging passed arrays
        :return:
        """
        temp = []  # Store results temprory
        while len(input_streams) != 1:  # Runs till the 2-D list contains only 1 merged list
            temp[:] = []
            for i in range(0, len(input_streams), 2):  # Iterate two list at a time
                if i == len(input_streams) - 1:  # If only one list is present i.e. nothing to merge
                    temp.append(input_streams[i])
                else:
                    temp.append(Solution2.merge_two_streams(input_streams[i], input_streams[i + 1]))
                    # Appends merged list of the 2 lists passed
            input_streams = temp[:] # Contains 2-D list containing 1 or more lists i.e [[]] or [[],[]]
            # Iterates till only one 1 list is left [[]]
        return input_streams[0] # Returns the list of the 2-D list


if __name__ == "__main__":
    # Input Stream
    STREAM = [[1, 10, 15, 17, 20, 23, 24],
              [2, 7, 9, 11, 22, 25],
              [3, 8, 13, 18],
              [4, 6, 12, 19],
              [5, 14, 16, 21]]
    # Output Stream is returned
    O_STREAM = Solution2.merge(STREAM)
    print(O_STREAM)
