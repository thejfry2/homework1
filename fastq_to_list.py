
#this function Reads a FastQ file and converts sequences into lists of bases stored in a dictionary.
def read_fastq_file(file_path):

    sequences_dict = {}  # Dictionary to store sequences with sequence IDs as keys

    with open(file_path, "r") as file:
        while True:
            # Read the lines
            seq_id_line = file.readline().strip()
            sequence_line = file.readline().strip()
            plus_line = file.readline().strip()
            quality_line = file.readline().strip()

            # breaks loop at the end of the file
            if not seq_id_line:
                break
            
            # Extract sequence ID (remove '@' from the start)
            seq_id = seq_id_line[1:]

            # Convert the sequence line into a list of bases
            bases = list(sequence_line)

            # Store the sequence in the dictionary
            sequences_dict[seq_id] = bases

    return sequences_dict

# getting the specific file
file_path = "test.fq"  # Path to your FastQ file
sequences_dict = read_fastq_file(file_path)

# Print the resulting dictionary, I took this out because I made user experince cleaner
#for seq_id, bases in sequences_dict.items():
#    print(f"Sequence ID: {seq_id}")
#    print(f"Bases: {bases}\n")

#asking for the seq number
seqNum = input("please input sequence number for transcription: ")
seqNumStr = "seq"+str(seqNum)

#does the transcription base by base by making a new list and appending to it
bases = sequences_dict[seqNumStr]
print("here is " + seqNumStr + " after transcription")
transcript = []
for base in bases:
  if base == "A":
    transcript.append("U")
  elif base == "T":
    transcript.append("A")
  elif base == "G":
    transcript.append("C")
  elif base == "C":
    transcript.append("G")
  else:
    transcript.append("error")
print(transcript)

#this asks if you want the reverse and reverses if you do.
while True: 
    rev = input("would you like the reverse transcript?(Y/N)")

    if rev == "Y":
        print("ok here is the reverse")
        transcript.reverse()
        print(transcript)
        break  
    if rev == "N":
        print("Ok, have a nice day!")
        break  
    else:
        #if they put somthing else this will ask again
        print("Invalid input. Please enter Y or N. This is case sensitive")


testcaseP = ["G","A","T","C","A"] # postive test case
testcaseN = ["U", "A", 'X', "B"] # negative test case
testcase = input("would you like to see the positive and negative test cases for this code?(Y/N)")
transcript = []
if testcase == "Y": 
    for base in testcaseP: #I should have made a funtion out of this but dont want to go back and change it
        if base == "A":
            transcript.append("U")
        elif base == "T":
             transcript.append("A")
        elif base == "G":
             transcript.append("C")
        elif base == "C":
             transcript.append("G")
        else:
             transcript.append("error")
print("this is the postive test case, it should output C,U,A,G,U")
print(transcript)
transcript = []
if testcase == "Y": 
    for base in testcaseN: #I should have made a funtion out of this but dont want to go back and change it
        if base == "A":
            transcript.append("U")
        elif base == "T":
            transcript.append("A")
        elif base == "G":
            transcript.append("C")
        elif base == "C":
            transcript.append("G")
        else:
            transcript.append("error")
print("this is the negative test case, it should output error,U,error,error")
print(transcript)
#I did not make postive and negative test cases for the reverse, because its a built in funtion. 
   