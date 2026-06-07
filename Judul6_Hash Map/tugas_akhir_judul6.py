class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nIsi Hash Table (Data Kendaraan):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"(Key Angka: {self.table[i].key}, Info: {self.table[i].value})")


    def cek_nilai(self,nilai):
        hasil = self.search(nilai)
        if hasil is not None:
            print(f"Data ditemukan -> {hasil.value}")
        else:
            print("Data nilai Mahasiswa tidak ditemukan!")


def main():
    data_nilai = HashMapOpenAddressing(size=10)
    
    data_nilai.insert(2515061004, "Kirana Larasati = A+")  
    data_nilai.insert(2515061068, "Radita Pramesti Regita C.A = B+")  
    data_nilai.insert(2515061009, "Dwika Prilando = B+")
    data_nilai.insert(2515061001, "Budi Santoso = B")
    
    data_nilai.display()
    print("-" * 50)

    print("\n[Mencari nilai Mahasiswa dengan NPM]")
    data_nilai.cek_nilai(2515061004)

    print("\n[Mencari nilai Mahasiswa dengan NPM]")
    data_nilai.cek_nilai(2515061001)

    print("\n[Mencari nilai Mahasiswa dengan NPM]")
    data_nilai.cek_nilai(2515061009)



if __name__ == "__main__":
    main()