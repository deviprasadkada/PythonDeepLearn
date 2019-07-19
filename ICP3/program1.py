# Dictionaries & Sets practice

sequence = "CCATGCTTGATCA"
sequence_list = list(sequence)
codon_list = ["ATG", "TAA", "TAG", "TGA"]
position_list = []

length_sequence = len(sequence)
length_codon = len(codon_list)
length_position = len(position_list)

n = length_sequence-1
while n >= 0:

    for i in range(0, len(codon_list)):
        codon_sub_list = list(codon_list[i])

        if sequence_list[n] == codon_sub_list[2] and sequence_list[n-1] == codon_sub_list[1] and sequence_list[n-2] == codon_sub_list[0]:
            position_list.append(n-2)
            print(sequence_list[n], "@", n)
            print(sequence_list[n-1], "@", n-1)
            print(sequence_list[n-2], "@", n-2)

    n-=1

print(len(position_list))
print(sequence[position_list[length_position-1]:(position_list[0]+3)])