__author__ = 'liufule12'

ALPHABET = 'ACGT'


def extend_phyche_index(original_index, extend_index):
    """Extend {phyche:[value, ... ]}"""
    if 0 == len(extend_index):
        return original_index
    for key in original_index.keys():
        original_index[key].extend(extend_index[key])
    return original_index


def make_ac_vector(sequence_list, lag, phyche_value, k):
    phyche_values = phyche_value.values()
    len_phyche_value = len(phyche_values[0])

    vec_ac = []
    for sequence in sequence_list:
        len_seq = len(sequence)
        each_vec = []

        for temp_lag in range(1, lag + 1):
            for j in range(len_phyche_value):

                # Calculate average phyche_value for a nucleotide.
                ave_phyche_value = 0.0
                for i in range(len_seq - temp_lag - k + 1):
                    nucleotide = sequence[i: i+k]
                    ave_phyche_value += phyche_value[nucleotide][j]
                ave_phyche_value /= len_seq

                # Calculate the vector.
                temp_sum = 0.0
                for i in range(len_seq - temp_lag - k + 1):
                    nucleotide1 = sequence[i: i+k]
                    nucleotide2 = sequence[i+temp_lag: i+temp_lag+k]
                    temp_sum += (phyche_value[nucleotide1][j] - ave_phyche_value) * (phyche_value[nucleotide2][j])

                each_vec.append(temp_sum / (len_seq - temp_lag))
        vec_ac.append(each_vec)

    return vec_ac


def make_cc_vector(sequence_list, lag, phyche_value, k):
    phyche_values = phyche_value.values()
    len_phyche_value = len(phyche_values[0])
    print len_phyche_value

    vec_cc = []
    for sequence in sequence_list:
        len_seq = len(sequence)
        each_vec = []

        for temp_lag in range(1, lag + 1):
            for i1 in range(len_phyche_value):
                # print 'i1', i1
                for i2 in range(len_phyche_value):
                    if i1 != i2:
                        # Calculate average phyche_value for a nucleotide.
                        ave_phyche_value1 = 0.0
                        ave_phyche_value2 = 0.0
                        for j in range(len_seq - temp_lag - k + 1):
                            nucleotide = sequence[j: j+k]
                            ave_phyche_value1 += phyche_value[nucleotide][i1]
                            ave_phyche_value2 += phyche_value[nucleotide][i2]
                        ave_phyche_value1 /= len_seq
                        ave_phyche_value2 /= len_seq

                        # Calculate the vector.
                        temp_sum = 0.0
                        for j in range(len_seq - temp_lag - k + 1):
                            nucleotide1 = sequence[j: j+k]
                            nucleotide2 = sequence[j+temp_lag: j+temp_lag+k]
                            temp_sum += (phyche_value[nucleotide1][i1] - ave_phyche_value1) * \
                                        (phyche_value[nucleotide2][i2] - ave_phyche_value2)
                        each_vec.append(temp_sum / (len_seq - temp_lag))
                        # print temp_lag, i1, i2, each_vec
                        # print len(each_vec)

        vec_cc.append(each_vec)

    return vec_cc


if __name__ == '__main__':
    pass