class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

class WarungMBG:
    def __init__(self):
        self.front = self.rear = self.top_riwayat = None

    def tambah_antrean(self, pesanan, prioritas=False):
        new = Node(pesanan)
        if not self.front:
            self.front = self.rear = new
        elif prioritas:
            new.next, self.front.prev, self.front = self.front, new, new
        else:
            new.prev, self.rear.next, self.rear = self.rear, new, new
        print(f"[{'PRIORITAS' if prioritas else 'OK'}] '{pesanan}' masuk.")

    def sajikan(self):
        if not self.front: return print("[!] Antrean kosong.")
        pesanan = self.front.data
        
        new_history = Node(pesanan)
        new_history.next, self.top_riwayat = self.top_riwayat, new_history
        
        self.front = self.front.next
        if self.front: self.front.prev = None
        else: self.rear = None
        print(f"[READY] '{pesanan}' siap!")

    def undo(self):
        if not self.top_riwayat: return print("[!] Tidak ada riwayat.")
        pesanan = self.top_riwayat.data
        self.top_riwayat = self.top_riwayat.next 
        self.tambah_antrean(pesanan, prioritas=True)
        print(f"[UNDO] '{pesanan}' dikembalikan.")

    def status(self):
        curr_q, res_q = self.front, []
        while curr_q:
            res_q.append(curr_q.data)
            curr_q = curr_q.next
        curr_h, res_h = self.top_riwayat, []
        while curr_h:
            res_h.append(curr_h.data)
            curr_h = curr_h.next
        print(f"\nAntrean: {res_q}\nRiwayat (Terbaru): {res_h}")

def main():
    app = WarungMBG()
    menu = {
        '1': lambda: app.tambah_antrean(input("Menu: ")),
        '2': lambda: app.tambah_antrean(input("Menu Prioritas: "), True),
        '3': app.sajikan, '4': app.status, '5': app.undo
    }
    while True:
        print("\n1.Reguler 2.Prioritas 3.Sajikan 4.Status 5.Undo 6.Keluar")
        pilih = input("Pilih: ")
        if pilih == '6': break
        menu.get(pilih, lambda: print("Salah input"))()

if __name__ == "__main__":
    main()