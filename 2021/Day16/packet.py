import math

class PacketDecoder:
    def __init__(self):
        self.bitstream_file = 'bitstream.txt'
        self.bitstream = ''
        self.packets = []

    def getBinaryList(self):
        with open(self.bitstream_file) as f:
             for line in f:
                 if line:
                     self.bitstream = bin(int('1'+line, 16))[3:]

    def processStream(self):
        self.getBinaryList()
        total_val = self.getTransmission(self.bitstream[:])
        

    def getTransmission(self, bitstream):
        print(bitstream)
        if bitstream == '':
            return
        
        version = int(bitstream[0:3],2)
        typeID = int(bitstream[3:6],2)
        lengthTypeID = None

        if typeID != 4:
            lengthTypeID = int(bitstream[6])
            
        final_binary_number = ''
        if len(bitstream) < 29:
            return bitstream
        if typeID == 4:
            remain_string = bitstream[6:]
            
            i=1
            j=1
            while i!=1:
                i=remain_string[j*5]
                final_binary_number = final_binary_number + remain_string[j*5+1:j*5+5]
                j=j+1
            return bitstream
        else:
            if lengthTypeID == 0:
                total_length_bits = int(bitstream[7:22], 2)
                start_ind = 22
                pointer_2 = 0
                sub_packets = []
                while pointer_2 < total_length_bits:
                    sub_bin = bitstream[pointer+pointer_2:]
                    sub_pack = self.getTransmission(sub_bin)
                    sub_packets.append(sub_pack)
                    pointer_2 += len(sub_pack)
                self.sub_packets.extend(sub_packets)
                pointer += pointer_2
            elif lengthTypeID == 1:
                num_packets = int(bitstream[7:18], 2)
                sub_packets = []

                while len(sub_packets) < num_packets:
                    start_ind = 18
                    sub_pack = self.getTransmission(bitstream[start_ind:])
                    sub_packets.append(sub_pack)
                    start_ind = start_ind + len(sub_pack)
                self.sub_packets.extend(sub_packets)
                    
        print(version_sum)            
        return version_sum
        
