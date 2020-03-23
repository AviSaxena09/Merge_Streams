"""This File Contains Solution2 Class containing Solution to the given challenge"""


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
        merged_stream = []  # Sorted list after merging lst1+lst2
        p_1 = p_2 = 0
        while p_1 + p_2 < len(lst1) + len(lst2):  # check the cond in if-else and append in list merged_stream
            if p_1 != len(lst1) and (p_2 == len(lst2) or lst1[p_1] < lst2[p_2]):
                merged_stream.append(lst1[p_1])
                p_1 += 1
            else:
                merged_stream.append(lst2[p_2])
                p_2 += 1
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
